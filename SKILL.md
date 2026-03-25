---
name: skeuomorphic-forge
description: "Build physically-realistic skeuomorphic UI with Tailwind CSS. Covers buttons, panels, gauges, knobs, CRT/LED displays, glass/metal effects, particle systems, and industrial hardware. Provides shadow stacks, material textures, lighting rules, and construction blueprints. Triggers on: skeuomorphic, realistic depth, industrial UI, 3D button, gauge, meter, analog, tactile, material texture, retro-industrial, aerospace panel, DSP cockpit. Do NOT trigger for flat/minimal UI or standard Material/Shadcn components."
---

# SKEUOMORPHIC FORGE — Instructions de generation UI

Tu es un expert en UI skeuomorphique physiquement realiste. Chaque composant que tu produis DOIT ressembler a un objet physique reel (metal usine, verre CRT, aluminium brosse, Bakelite), pas un div plat avec une ombre CSS.

Tu generes du code React/JSX avec Tailwind CSS + inline styles (`style={{}}`). Pas de classes CSS custom sauf indication contraire.

---

## CONTRAINTES PHYSIQUES ABSOLUES (s'appliquent a CHAQUE composant)

Violer une seule de ces regles produit un composant visuellement casse.

**C1 Ombres portees = NOIR UNIQUEMENT.** Tous les `box-shadow` non-inset utilisent exclusivement `rgba(0,0,0,...)`. Une ombre est l'absence de lumiere. Jamais d'ombre portee violette, ambree, bleue. Exception : les `inset` highlights avec rgba clair/colore sont OK (lumiere frappant les bords internes).

**C2 Source lumineuse unique a 135deg**, coherente sur TOUS les composants de la page. Plusieurs directions = physiquement impossible.

**C3 Highlights chauds au-dessus de 0.10 d'opacite.** Tout `rgba(255,255,255,X)` avec X > 0.10 doit devenir `rgba(255,240,220,X)` ou plus chaud. Blanc pur au-dessus de 0.10 = blafard/clinique. Les edge catches a 0.03-0.08 peuvent rester en blanc pur.

**C4 Separation de contraste.** Les fonds de conteneurs/wells (#08-#10) DOIVENT etre plus sombres que les fonds de cartes (#1c-#28). Delta minimum #12 hex. Renforcer les bords de carte : `borderTop: "1px solid rgba(255,255,255,0.09)"`, `borderLeft: "1px solid rgba(255,255,255,0.06)"`.

**C5 Ombre et lumiere sont des systemes SEPARES.** L'ombre (rgba sombre) cree profondeur/recession via `box-shadow`. La lumiere (rgba chaud, gradients, pseudo-elements) cree reflets speculaires/edge catches. Ne jamais les confondre dans un stack brouille.

**C6 Minimum de couches d'ombre.** Standard (boutons/cartes/toggles) >= 5. Advanced (knobs/dials/meters) >= 8. Hero (panneaux/chassis) >= 11. Ultra (CRT vitrine) = 31. LES COMPTER apres collage.

**C7 Ne jamais inventer de shadow stacks.** Toujours copier-adapter depuis les stacks canoniques ci-dessous.

**C8 Ordre d'assemblage : arriere vers avant.** Backplate -> sous-panneaux/bezels -> wells/recesses -> instruments/displays -> hardware (vis/rivets) -> labels -> verre/reflet. Du hardware sur une surface plate = contradiction. Construire la profondeur D'ABORD.

**C9 Taille physique fixe.** Les cartes-appareils (CRT, gauge, instrument) ont des dimensions FIXES. Toutes les instances du meme composant = meme width+height. Etat disabled = memes dimensions que actif. Le contenu se centre dans le chassis. Utiliser `width` + `height` explicites.

**C10 Max 2 couleurs d'accent par page.** Un 3e accent necessite approbation explicite.

---

## VERIFICATION PRE-LIVRAISON (checker AVANT de livrer)

Un composant qui echoue un gate CRITICAL ne doit PAS etre livre.

**U0 Context Scan (BLOCKING):** La page existante a ete analysee avant de styler. Palette, boutons existants, hierarchie des conteneurs identifies. Meme role = meme style que les siblings. Shadow stack source depuis les canoniques, pas invente.

**U1 Shadow Depth (CRITICAL):** Nombre de couches respecte le minimum du tier (C6). Ombres portees NOIR uniquement (C1). Progression graduee du blur.

**U2 Light Source (CRITICAL):** Direction unique 135deg partout (C2). Lumiere/ombre separees (C5). Pas de blanc pur au-dessus de 0.10 (C3). Gradient de surface present.

**U3 Construction (HIGH):** Objet physique nomme explicitement. 4 couches : chassis + profondeur + eclairage + detail. Ordre d'assemblage respecte (C8).

**U4 Hardware (HIGH):** Vis aux coins avec radial-gradient sphere + 5 couches d'ombre + slot torx/phillips. Vis sur METAL uniquement, jamais sur verre/ecran.

**U5 Interaction States (HIGH):** hover (lift + expand shadow), active (depress + compress), disabled (opacity 0.5 + desaturate), focus-visible (outline 2px). Le shadow stack CHANGE entre les etats.

**U6 Typography (HIGH):** Body >= 13px, titres >= 14px, labels >= 11px, rien sous 10px. Texte primaire opacity >= 0.85, secondaire >= 0.5, tertiaire >= 0.35. Labels en silkscreen (text-shadow) ou grave (clip + gradient), pas en texte brut.

**U7 Accessibility (MEDIUM):** Contraste WCAG OK. `focus-visible` sur tous les interactifs. Touch targets >= 44px. `prefers-reduced-motion`. `pointer-events: none` sur les overlays de texture. Pas de `filter: blur()` dans les animations.

---

## SHADOW STACKS CANONIQUES (copier-adapter, ne jamais inventer)

### Standard (5+ couches) — boutons, cartes, toggles

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,255,255,0.05),   /* L: top edge catch */
  inset 0 -1px 0 rgba(0,0,0,0.3),          /* S: bottom edge */
  0 2px 4px rgba(0,0,0,0.4),               /* S: close cast */
  0 8px 16px rgba(0,0,0,0.3),              /* S: mid depth */
  0 16px 32px rgba(0,0,0,0.2)              /* S: ambient floor */
`
```

### Advanced (8-9 couches) — knobs, dials, meters, rails de switch

Gorge/channel :

```javascript
boxShadow: `
  inset 0 6px 14px rgba(0,0,0,0.98),       /* S: top gorge */
  inset 0 3px 5px rgba(0,0,0,0.85),        /* S: mid gorge */
  inset 0 -3px 5px rgba(0,0,0,0.5),        /* S: bottom step */
  inset 3px 0 6px rgba(0,0,0,0.55),        /* S: left wall */
  inset -3px 0 6px rgba(0,0,0,0.55)        /* S: right wall */
`
```

Display well (9 couches) :

```javascript
boxShadow: `
  inset 0 12px 30px rgba(0,0,0,0.95),
  inset 0 6px 14px rgba(0,0,0,0.85),
  inset 0 -12px 30px rgba(0,0,0,0.8),
  inset 4px 0 12px rgba(0,0,0,0.6),
  inset -4px 0 12px rgba(0,0,0,0.6),
  inset 0 0 40px rgba(0,5,15,0.3),
  inset 0 0 30px rgba(255,180,60,0.02),    /* L: warm glow in well */
  0 0 0 1px rgba(0,0,0,0.95),
  0 1px 0 rgba(255,255,255,0.03)
`
```

### Hero (11+ couches) — panneaux, chassis, faceplates

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,240,220,0.25),    /* L: top bevel (warm per C3) */
  inset 0 -1px 0 rgba(0,0,0,0.8),          /* S: bottom bevel */
  inset 1px 0 1px rgba(255,255,255,0.1),    /* L: left bevel */
  inset -1px 0 1px rgba(0,0,0,0.5),         /* S: right bevel */
  0 2px 4px rgba(0,0,0,0.4),
  0 4px 8px rgba(0,0,0,0.3),
  0 6px 12px rgba(0,0,0,0.25),
  0 8px 16px rgba(0,0,0,0.2),
  0 12px 24px rgba(0,0,0,0.15),
  0 16px 32px rgba(0,0,0,0.1),
  0 20px 40px rgba(0,0,0,0.08),
  0 0 60px rgba(255,176,0,0.06),            /* L: amber backlight */
  0 40px 60px -20px rgba(0,0,0,0.5)
`
```

### Ultra (31 couches) — deep CRT recess

Structure : 7 micro-borders (crisp edge) + 5 vertical depth + 5 horizontal walls + 5 bottom depth + 4 corner occlusion + 5 external rim/base.

```javascript
boxShadow: `
  inset 0 1px 0 #000, inset 0 2px 0 #000, inset 0 3px 1px #000,
  inset 1px 0 0 #000, inset 2px 0 0 #000, inset -1px 0 0 #000, inset -2px 0 0 #000,
  inset 0 4px 4px rgba(0,0,0,1), inset 0 8px 10px rgba(0,0,0,1),
  inset 0 14px 18px rgba(0,0,0,0.95), inset 0 22px 30px rgba(0,0,0,0.85),
  inset 0 32px 50px rgba(0,0,0,0.6),
  inset 6px 0 8px rgba(0,0,0,1), inset 12px 0 16px rgba(0,0,0,0.9),
  inset 20px 0 24px rgba(0,0,0,0.6),
  inset -6px 0 8px rgba(0,0,0,1), inset -12px 0 16px rgba(0,0,0,0.9),
  inset -20px 0 24px rgba(0,0,0,0.6),
  inset 0 -4px 4px rgba(0,0,0,1), inset 0 -8px 10px rgba(0,0,0,1),
  inset 0 -14px 18px rgba(0,0,0,0.95), inset 0 -22px 30px rgba(0,0,0,0.85),
  inset 0 -32px 50px rgba(0,0,0,0.6),
  inset 10px 10px 18px rgba(0,0,0,0.9), inset -10px 10px 18px rgba(0,0,0,0.9),
  inset 10px -10px 18px rgba(0,0,0,0.9), inset -10px -10px 18px rgba(0,0,0,0.9),
  0 1px 0 rgba(255,255,255,0.05), 0 2px 0 rgba(255,255,255,0.02),
  0 -1px 0 rgba(0,0,0,0.9), 0 -2px 4px rgba(0,0,0,0.6),
  0 6px 24px rgba(0,0,0,0.6), 0 12px 48px rgba(0,0,0,0.4)
`
```

---

## CLASSIFICATION DU COMPOSANT

### Boutons

| Role | Tier shadow | Gradient | Taille |
|---|---|---|---|
| CTA/Hero | Advanced 8+ | Bold thematique + shimmer/LED | 48-56px height, 1 par page max |
| Primary | Standard 5+ | Surface gradient accent | 40-44px |
| Secondary | Standard 5 | Subtle surface gradient | 36-40px |
| Tertiary/Ghost | Minimal 2-3 inset | Aucun, transparent + border | 32-40px |
| Destructive | Standard 5+ | Red `#4a1010->#2a0808` | 40-44px |

### Conteneurs

| Role | Background | Shadow |
|---|---|---|
| Section well | #08-#0e (le plus sombre) | Inset 4-6 couches |
| Card (flottante) | #1c-#28 (plus clair) | Drop Standard 5+ |
| Card imbriquee | #14-#1c (intermediaire) | Drop 3-5 |
| Modal/overlay | #1a-#22 | Hero 11+ |

### Elements speciaux

| Type | Tier shadow |
|---|---|
| Gauge/meter | Advanced 8+ |
| CRT display | Hero 11+ ou Ultra 31 |
| Toggle/switch | Standard 5 |
| Knob/dial | Advanced 8+ |
| LED indicator | Standard 5 |

---

## PROTOCOLE DE CONSTRUCTION

### 1. Nommer l'objet physique

Dire explicitement : "Ceci est une faceplate en aluminium usine" ou "Ceci est un interrupteur a bascule en Bakelite". Si l'analogie physique est floue, le composant sera generique.

### 2. Choisir la famille esthetique

| Theme | Surface gradient | Accent | Inset highlight | Texte |
|---|---|---|---|---|
| Warm industrial (defaut) | `#1e1e1e->#141414` | `hsl(35 100% 60%)` amber | `rgba(255,240,220,0.12)` | `rgba(255,240,220,0.9)` |
| Cool steel | `#1a1c20->#12141a` | `hsl(210 70% 60%)` blue | `rgba(180,200,255,0.10)` | `rgba(200,220,255,0.9)` |
| Deep purple | `#2d1854->#150b28` | `hsl(270 100% 70%)` violet | `rgba(200,160,255,0.12)` | `rgba(220,200,255,0.95)` |
| Military | `#1a1e14->#10140c` | `hsl(0 70% 55%)` red | `rgba(180,200,150,0.08)` | `rgba(180,200,150,0.85)` |
| Vintage audio | `#2a2218->#1a1610` | `hsl(30 80% 55%)` copper | `rgba(255,220,180,0.10)` | `rgba(240,220,190,0.9)` |
| CRT terminal | `#0a0f0a->#050805` | `hsl(120 100% 50%)` green | `rgba(0,255,60,0.06)` | `rgba(0,255,60,0.85)` |

Les ombres portees restent NOIRES `rgba(0,0,0,...)` quel que soit le theme.

### 3. Eclairage (applique APRES les ombres)

1. **Gradient de surface** (courbure) : `background: linear-gradient(145deg, plus-clair 0%, plus-sombre 100%)`
2. **Bords biseautes** : `borderTop: "1px solid rgba(255,255,255,0.08)"`, `borderBottom: "1px solid rgba(0,0,0,0.3)"`
3. **Point speculaire** : `::before` avec `radial-gradient(circle at 35% 30%, rgba(255,240,220,0.2), transparent 60%)`
4. **Rim glow** : `::before` avec `radial-gradient(ellipse at center, rgba(255,255,255,0.25), transparent 70%)` au bord superieur, `pointerEvents: "none"`

| But | Couleur | Opacite |
|---|---|---|
| Edge catch | `rgba(255,255,255,...)` | 0.03-0.08 |
| Top bevel | `rgba(255,255,255,...)` | 0.08-0.15 |
| Specular hotspot | `rgba(255,240,220,...)` | 0.15-0.30 |
| Active glow | `rgba(255,180,60,...)` | 0.10-0.40 |
| CRT/LED emission | `hsl(35 100% 60%)` | Full |
| Rim light (pseudo) | `rgba(255,255,255,0.25)` center->transparent | radial-gradient |

### 4. Etats d'interaction (CHAQUE element interactif)

```javascript
// Hover — lift + expand shadow
onHover: { transform: 'translateY(-1px)', boxShadow: '/* meme stack, blur +2px/couche, highlight opacity +0.05 */' }
// Active — depress
onActive: { transform: 'translateY(1px)', boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.5), inset 0 1px 1px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.3)' }
// Disabled
onDisabled: { opacity: 0.5, filter: 'saturate(0.3)', pointerEvents: 'none' }
// Focus
focusVisible: { outline: '2px solid hsl(35 100% 60%)', outlineOffset: '2px' }
```

---

## REGLES COMPOSANTS SPECIFIQUES

### Metal Recesses / Wells

Chaque recess necessite les 4 zones : top attack, murs lateraux, bottom catch, levre exterieure.

| Composant | Min couches inset | Background |
|---|---|---|
| Input / petit statut | 6 | `#080808->#0c0c0c` |
| Well de gauge/meter | 9 | `#050505->#080808` |
| CRT/deep display | 12 | `#030303` |
| Canal slider | 5 | gradient `#050505->#0f0f0f` |
| Trou LED | 4 | radial `#1a1a1a->#000` |

**INTERDIT** : `inset 0 2px 4px rgba(0,0,0,0.3)` seul (1-3 couches). C'est un input CSS, pas un recess metal.

### Rim Light

Shadow stack construit D'ABORD (5+ couches), PUIS rim light par-dessus. Bord superieur 2-4x plus lumineux que le bas. Au moins UN `::before` ou `::after` avec `radial-gradient` pour hotspot concentre. Pas d'opacite highlight > 0.25. `pointerEvents: "none"` sur les overlays.

**INTERDIT** : `border: 1px solid rgba(255,255,255,0.1)` comme "rim light" (border uniforme = cadre photo). `box-shadow: 0 0 20px rgba(255,255,255,0.1)` seul (glow uniforme = neon).

### Chassis Metal / Panneaux

3+ zones obligatoires parmi : (1) Cadre bezel (rim multi-couches + bevel borders), (2) Surface principale (metal brosse/texture, PAS gris plat), (3) Wells/recesses, (4) Zones d'affichage (recessed + color bleed), (5) Grille/ventilation (hex perf ou fentes), (6) Labels (estampes/graves, PAS texte brut).

**INTERDIT** : Rectangle plat `#333` avec grille CSS de points. Tout chassis a besoin de texture de surface, au moins un recess, au moins un detail hardware.

---

## PATTERNS DE PRODUCTION CANONIQUES

### Bouton complet — Rest / Hover / Active

```css
.button {
  --bg: #080808; border: 0; border-radius: 100px;
  background-color: var(--bg); cursor: pointer; transition: all 0.2s ease;
  box-shadow:
    inset 0 0.3rem 0.9rem rgba(255,255,255,0.3),
    inset 0 -0.1rem 0.3rem rgba(0,0,0,0.7),
    inset 0 -0.4rem 0.9rem rgba(255,255,255,0.5),
    0 3rem 3rem rgba(0,0,0,0.3),
    0 1rem 1rem -0.6rem rgba(0,0,0,0.8);
}
.button:hover {
  box-shadow:
    inset 0 0.3rem 0.5rem rgba(255,255,255,0.4),
    inset 0 -0.1rem 0.3rem rgba(0,0,0,0.7),
    inset 0 -0.4rem 0.9rem rgba(255,255,255,0.7),
    0 3rem 3rem rgba(0,0,0,0.3),
    0 1rem 1rem -0.6rem rgba(0,0,0,0.8);
}
.button:active {
  transform: translateY(4px);
  box-shadow:
    inset 0 0.3rem 0.5rem rgba(255,255,255,0.5),
    inset 0 -0.1rem 0.3rem rgba(0,0,0,0.8),
    inset 0 -0.4rem 0.9rem rgba(255,255,255,0.4),
    0 3rem 3rem rgba(0,0,0,0.3),
    0 1rem 1rem -0.6rem rgba(0,0,0,0.8);
}
```

Pattern : Hover AUGMENTE les highlights (opacity +0.1 a +0.2). Active ENFONCE (translateY + redistribution lumiere). Les couches de shadow restent constantes, seules les opacites changent.

### Card avec Rim Light

```javascript
const cardStyle = {
  position: 'relative', borderRadius: 12,
  background: 'linear-gradient(145deg, hsl(30 12% 10%) 0%, hsl(30 14% 6%) 100%)',
  padding: '24px', overflow: 'hidden',
  boxShadow: `
    inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(0,0,0,0.4),
    0 4px 12px rgba(0,0,0,0.5), 0 8px 24px rgba(0,0,0,0.3),
    0 0 1px rgba(255,255,255,0.1)
  `,
};
// ::before rim light — top edge
{ position: 'absolute', top: 0, left: '10%', right: '10%', height: 1,
  background: 'radial-gradient(ellipse at center, rgba(255,255,255,0.25), transparent 70%)',
  pointerEvents: 'none' }
// ::after bottom rim
{ position: 'absolute', bottom: 0, left: '20%', right: '20%', height: 1,
  background: 'radial-gradient(ellipse at center, rgba(255,255,255,0.08), transparent 70%)',
  pointerEvents: 'none' }
```

### Tete de vis (5 couches + radial gradient)

```javascript
{ position: 'absolute', width: 7, height: 7, borderRadius: '50%',
  background: 'radial-gradient(circle at 32% 26%, hsl(40 15% 50%) 0%, hsl(35 18% 38%) 15%, hsl(30 20% 25%) 40%, hsl(25 22% 15%) 70%, hsl(20 20% 8%) 100%)',
  boxShadow: `
    inset 0 2px 4px rgba(0,0,0,0.95), inset 0 -0.5px 0 rgba(255,255,255,0.2),
    0 1px 1px rgba(0,0,0,0.9), 0 2px 3px rgba(0,0,0,0.6),
    0 0 0 0.5px rgba(0,0,0,0.8)
  `,
  zIndex: 20 }
// Slot torx : ::before avec linear-gradient(angle, transparent 38%, rgba(0,0,0,0.7) 42%, ... 58%, transparent 62%)
```

### Phosphor / CRT Text Glow

```javascript
// Amber (palette par defaut)
{ fontFamily: "'Orbitron', sans-serif", fontWeight: 700,
  letterSpacing: '0.05em', textTransform: 'uppercase',
  color: 'hsl(35 100% 65%)',
  textShadow: '0 0 4px currentColor, 0 0 10px currentColor, 0 0 20px rgba(255,180,0,0.3)' }
// Rouge : color #ff6b5a, textShadow: 0 0 1px rgba(255,107,90,1), 0 0 6px rgba(255,80,60,0.7), 0 0 12px rgba(255,40,20,0.3)
// Animation optionnelle : opacity 0.95->1->0.95 sur 4s
```

### Silkscreen Label

```javascript
{ fontFamily: 'ui-monospace, monospace', fontWeight: 600,
  letterSpacing: '0.08em', textTransform: 'uppercase', fontSize: '0.65rem',
  color: 'rgba(255,255,255,0.06)',
  textShadow: '0 1px 0 rgba(0,0,0,0.9), 0 0 6px rgba(255,255,255,0.05)' }
```

### Gradients de materiaux

```javascript
// Metal brosse (sombre, chaud)
background: `url("data:image/svg+xml,%3Csvg viewBox='0 0 128 128' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='r'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='2.5' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23r)' opacity='0.04'/%3E%3C/svg%3E"), linear-gradient(142deg, hsl(40 10% 16%) 0%, hsl(35 12% 11%) 25%, hsl(30 14% 7%) 50%, hsl(35 10% 9%) 75%, hsl(40 8% 13%) 100%)`,
backgroundBlendMode: 'overlay, normal',
// Sphere/knob : radial-gradient(circle at 35% 30%, hsl(40 15% 50%) 0%, hsl(35 12% 30%) 45%, hsl(30 14% 10%) 100%)
// Chrome : linear-gradient(135deg, #e8e8ec 0%, #a0a0a8 30%, #d0d0d4 50%, #909098 70%, #c8c8cc 100%)
// Cuir : linear-gradient(160deg, #6b4226 0%, #4a2d18 100%) + SVG feTurbulence grain 8-12% opacity
// Bois : repeating-linear-gradient(95deg, rgba(139,90,43,0.15) 0px, transparent 3px, transparent 8px), linear-gradient(180deg, #8b5a2b 0%, #6b3a1b 100%)
```

---

## PALETTE WARM INDUSTRIAL (defaut)

| Token | Valeur | Usage |
|---|---|---|
| chassis-dark | `hsl(30 14% 5%)` | Fond panneau profond |
| chassis-base | `hsl(30 12% 8%)` | Fond panneau/carte standard |
| chassis-mid | `hsl(35 10% 12%)` | Surface elevee |
| chassis-light | `hsl(35 8% 18%)` | Anneau externe bezel |
| bevel | `hsl(40 8% 26%)` | Chanfreins |
| highlight | `hsl(40 12% 38%)` | Points speculaires |
| amber | `hsl(35 100% 60%)` | Texte CRT, etat actif |
| amber-dim | `hsl(35 60% 40%)` | Accent muted, bordures |
| amber-glow | `rgba(255,180,0,0.4)` | Halo text-shadow |
| cream | `hsl(40 60% 72%)` | Digits compteur |
| green | `hsl(120 80% 55%)` | LED vert |
| red | `hsl(0 80% 55%)` | LED rouge, critique |
| silk | `rgba(255,255,255,0.06)` | Texte silkscreen |

### Typographie

| Contexte | Font | Weight | Tracking | Case |
|---|---|---|---|---|
| CRT/VFD readout | `'Orbitron', sans-serif` | 700 | 0.05em | uppercase |
| Terminal/status | `'Share Tech Mono', monospace` | 400 | 0.02em | mixed |
| Counter digits | `'Orbitron', sans-serif` | 700 | 0.1em | numeric |
| Silkscreen labels | `font-mono` (system) | 600 | 0.08-0.15em | uppercase |
| Gravure | `font-mono` (system) | 700 | 0.05em | uppercase |

---

## VOCABULAIRE 3D

| L'utilisateur dit | Technique |
|---|---|
| "3D effect" / "effet 3D" | Multi-layer shadow stack + perspective tilt optionnel |
| "3D button" | Press effect : compression shadow sur :active |
| "depth" / "profondeur" | Couches d'ombre graduees OU translateZ |
| "relief" / "embossed" | Texte/forme sureleve via gradient clip + text-shadow |
| "recessed" / "inset" | Inset shadow stack (effet gorge) |
| "floating" / "levitating" | Drop shadows extra-larges + translateY lift |
| "parallax" | Couches a differents translateZ ou vitesses de scroll |
| "glass dome" / "bubble" | Pseudo-element radial-gradient sur le contenu |
| "flip card" | rotateY(180deg) + preserve-3d + backface-visibility |
| "isometric" | rotateX + rotateY petits angles + faces d'arete |

---

## ANTI-PATTERNS

| MAUVAIS | BON |
|---|---|
| 2-3 couches box-shadow | 5-15 couches, blur gradue |
| Vis sur surface plate | Profondeur D'ABORD, vis par-dessus |
| Vis sur verre/ecran | Vis sur METAL uniquement |
| Vis cercle plat 1 inset | Radial gradient sphere + 5 couches + slot torx |
| Carte qui resize avec contenu | width+height explicites, frame fixe |
| Recess sans inner rim light | 1px warm border au bord, top plus lumineux |
| 1-3 inset pour ecran | 12+ couches inset + inner rim light |
| Rim light avec glow/blur | Border clean 1px, PAS de bloom |
| Pas de color bleed depuis display | Inner rim capte la couleur display a 0.06-0.10 |
| Texte embosse opacity < 0.25 | Min 0.35 tertiaire, 0.50 secondaire |
| Taille differente pour etat disabled | Memes width+height pour tous les etats |
| Rim light decoratif sans source physique | Chaque effet lumineux a une source physique |
| Blanc pur rgba(255,255,255,X) X>0.10 | rgba(255,240,220,X) tint chaud |
| Meme box-shadow rest/hover/active | Stacks differents par etat |
| `filter: blur()` en animation | opacity + transform uniquement |
| Plusieurs directions lumineuses | 135deg unique partout |
| Inventer des shadow stacks | Copier-adapter depuis les canoniques |
| Hardware avant profondeur | Ordre d'assemblage : profondeur d'abord |
| Lumiere + ombre melangees | Systemes separes |
| Edge catch rgba(255,255,255,0.5) | Max 0.08 pour les edges |
| Ombres portees colorees | rgba(0,0,0,...) pour TOUTES les drops |
| Body text < 13px | Body >= 13px, titres >= 14px, labels >= 11px |
| Conteneur/carte meme luminosite | Delta minimum #12 hex |
| Toujours amber-on-dark | Proposer 2-3 themes si nouvelle UI |
| Styler sans lire la page | Scanner la page, extraire palette, matcher hierarchie |
| Choisir style bouton sans classifier | Utiliser la matrice de decision |
| Ajouter un 3e accent silencieusement | Max 2 par page, demander avant le 3e |
| Ignorer les siblings | Meme role = meme style |

---

## VARIETE CREATIVE (nouvelles UIs uniquement)

Si modification d'une page existante : coherence, matcher le theme existant. Ne pas proposer de variete.

Si creation d'un composant net-new sans theme etabli : proposer 2 options maximum depuis les 6 themes ci-dessus. L'utilisateur choisit.

Ne jamais proposer de variete quand la page environnante etablit deja le role, la palette et la hierarchie.
