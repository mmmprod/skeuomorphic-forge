---
name: skeuomorphic-forge
description: "Create production-grade skeuomorphic UI with Tailwind CSS. Use when building physically-realistic elements: buttons with mechanical depth, gauges, meters, LED/nixie indicators, toggle switches, sliders, progress bars, cards with material textures (metal, glass, leather, wood, paper, fabric, concrete, plastic), industrial panels, CRT/VFD displays, neumorphic components, particle effects, or any UI mimicking real-world objects. Covers dark (industrial, military) and light (classic, iOS-era, neumorphic) themes. Triggers: skeuomorphic, realistic, 3D button, industrial UI, gauge, meter, LED, nixie, analog, physical, tactile, metal texture, glass effect, depth effect, neumorphic, soft UI, leather, wood grain, rim light, chrome, gold, brushed metal, particles, starfield, space dust, vortex, particle system, disintegration, GPGPU, material with depth, retro-industrial, aerospace, vintage instrument, warm industrial, CRT terminal, mechanical counter, bezel assembly, phosphor glow, DSP panel, cockpit UI. Do NOT trigger for flat/minimal UI, standard Material/Shadcn components, or conventional Tailwind layouts without physical realism."
---

# Skeuomorphic Forge

Build physically-realistic UI components using Tailwind CSS. Every component MUST look like a real physical object — with correct lighting, shadow depth, material textures, and mechanical behavior.

---

## MANDATORY RULES — READ BEFORE ANY ACTION

**Rule 1 — Physical realism over decoration.** Every shadow, gradient, and highlight MUST serve a physical purpose. Shadows = depth. Gradients = curvature. Highlights = specular reflection. Animations = mechanical behavior (springs, inertia, depression). Decorative-only effects are FORBIDDEN.

**Rule 2 — The 4-layer construction rule.** Every component has AT MINIMUM:
1. **Chassis/body** — the physical material (metal, glass, plastic, leather, wood, paper, fabric)
2. **Depth** — inset or raised shadows establishing spatial position
3. **Lighting** — specular highlights and rim light consistent with a single light source
4. **Detail** — texture overlays, screws, mesh, stitching, grain, wear marks

**Rule 3 — Shadow depth standard.** Flat, lazy shadows destroy realism. Minimum layer counts:
- **Standard components** (buttons, cards, toggles): minimum 5 `box-shadow` layers
- **Advanced components** (knobs, dials, meters, CRT screens): minimum 8 `box-shadow` layers
- **Hero components** (faceplates, full panel assemblies): 11-15 `box-shadow` layers
- 2-3 shadow layers is FLAT DESIGN. NEVER acceptable.

**Rule 4 — Hardware placement.** Decorative fasteners follow real-world structural logic:
- Rectangle/square panel → 4 screws (one per corner, inset 8-16px)
- Narrow strip → 2 screws (centered at each end)
- Circle/dial → 0 screws (bezel ring suffices) or 4+ evenly spaced
- **NEVER place a single screw** — one fastener cannot prevent rotation

**Rule 5 — Single light source.** Default: top-left (135deg). ALL shadows, highlights, bevels, and gradients MUST be consistent with this direction.

---

## MANDATORY PRE-BUILD PROTOCOL

**BEFORE writing ANY component code, complete ALL of these steps. Skipping steps produces flat, unrealistic output.**

### Step 1 — Identify the physical analog
What real-world object does this represent? A machined metal button? A CRT screen? A leather panel? Name it explicitly.

### Step 2 — Choose the aesthetic family

| Family | Background | Materials | Accents |
|--------|-----------|-----------|---------|
| **Industrial / Dark** | `#050505`–`#1a1a1a` | Brushed metal, gunmetal, cast iron | Amber/green/red glows |
| **Retro-Industrial / Aerospace** | `hsl(30 12% 6%)`–`hsl(35 10% 12%)` | Machined aluminum, anodized metal | Warm amber `hsl(35-45)` |
| **Classic / Light** | `#d0d0d0`–`#f0f0f0` | Leather, wood, paper, glossy plastic | Warm or cool tones |
| **Neumorphic / Soft UI** | `#e0e0e0` or tinted | Extruded/pressed into background | Minimal color, max shape |

### Step 3 — MANDATORY: Load reference files from the lookup table below

Look up the component type in the **Component Lookup Table**. Read the listed reference files. This is NOT optional — the reference files contain the shadow stacks, gradient recipes, and construction blueprints that make components realistic.

### Step 4 — Build following assembly order
Backplate → sub-panels → wells → hardware → instruments → displays → labels → overlays. Apply shadow stacks from reference files. Set `will-change` on animated elements, `pointer-events-none` on textures.

### Step 5 — Apply typography
Match text rendering to material surface (see Typography section below).

### Step 6 — Add state transitions
Hover, active/pressed, disabled, focus for EVERY interactive element.

### Step 7 — MANDATORY: Verify against Quality Checklist (bottom of this file)

---

## Component Lookup Table

**MANDATORY: Find the component type below. Read the listed files BEFORE writing code.**

### Buttons & Toggles
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Industrial push button | 14.16 | `04-community-techniques.md` (search "14.16") + `01` |
| iOS 6 glass button | 14.3 | `04` (search "14.3") + `07-glass-effects.md` |
| Bevel button (3-layer) | 14.95 | `04` (search "14.95") |
| Shape-shifted bevel button | 14.97 | `04` (search "14.97") |
| Brushed metal button | 24.2 | `08-metal-effects.md` |
| Metallic conic button | 24.3 | `08-metal-effects.md` |
| Power button (on/off glow) | 14.101 | `04` (search "14.101") |
| Membrane/jelly button | 14.3 | `04` + `01` |
| Toggle switch (spring) | — | `02-hardware-animation-neumorphism.md` |
| Rocker switch | — | `02` + `01` |
| Engraved glow button | 14.38 | `04` (search "14.38") |
| Circuit relay button | 14.53 | `04` (search "14.53") |

### Cards & Panels
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Metal panel/faceplate | 9.1-9.6 | `03-blueprints-performance-palettes.md` + `01` |
| Rim light card | 14.98 / 25 | `04` (search "14.98") + `09-rim-light-effects.md` |
| Dark glass card | 23.4 | `07-glass-effects.md` |
| Frosted glass card | 23.3 | `07-glass-effects.md` |
| Leather panel | 14.4 | `04` (search "14.4") + `01` |
| Wood panel | 14.5 | `04` (search "14.5") + `01` |
| Paper/torn paper card | 14.87 | `04` (search "14.87") + `01` |
| Rubber overmold | — | `01` (search "rubber") |
| Area light card | 14.99 | `04` (search "14.99") |
| Layered depth shadow card | 14.100 | `04` (search "14.100") |

### Gauges, Meters & Displays
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| VU meter | 9.12 | `03` + `05-physics-composition-interaction-typography.md` |
| Oscilloscope | 14.60 | `04` (search "14.60") + `11-retro-industrial-patterns.md` |
| CRT display (full) | 28 | `11-retro-industrial-patterns.md` |
| 7-segment display | 14.12 | `04` (search "14.12") |
| Nixie tube | 14.14 | `04` (search "14.14") |
| VFD readout | — | `11` (search "CRT") + `01` |
| LED indicator | 29 | `11-retro-industrial-patterns.md` |
| Bargraph meter | — | `03` + `01` |
| Mechanical counter | 33 | `11-retro-industrial-patterns.md` |

### Knobs, Dials & Sliders
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Machined knob | 14.10 | `04` (search "14.10") + `01` |
| Arturia multi-layer knob | 14.11 | `04` (search "14.11") |
| Chickenhead selector | 14.15 | `04` (search "14.15") |
| Rotary radial menu | 14.61 | `04` (search "14.61") |
| Slider/range | — | `02` + `01` |
| Glass thermostat knob | 14.93 | `04` (search "14.93") |
| Glass slider/equalizer | 14.94 | `04` (search "14.94") |

### Industrial Hardware
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Bezel assembly (3-ring) | 27 | `11-retro-industrial-patterns.md` |
| Torx/Phillips screw | 30 | `11-retro-industrial-patterns.md` |
| Eurorack jack | 14.7 | `04` (search "14.7") |
| Patch cable | 14.8 | `04` (search "14.8") |
| Footswitch (stomp) | 14.9 | `04` (search "14.9") |
| Compressor faceplate | 14.16 | `04` (search "14.16") + `03` |
| Vent slat / rivet | — | `02-hardware-animation-neumorphism.md` |

### Glass & Metal Effects
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Glass sphere/bead | 23.6-23.7 | `07-glass-effects.md` |
| Glass icon/tile | 23.5 | `07-glass-effects.md` |
| SVG filter glass (warp) | 23.8 | `07-glass-effects.md` |
| Chrome text | 24.4 | `08-metal-effects.md` |
| Gold text | 24.5 | `08-metal-effects.md` |
| Metallic border | 24.6 | `08-metal-effects.md` |
| Brushed metal texture | 24.7 | `08-metal-effects.md` |

### Text & Light Effects
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Neon sign flicker | 14.102 | `04` (search "14.102") |
| Neon text (triple blend) | 14.74 | `04` (search "14.74") |
| Bevelled text/icons | 14.96 | `04` (search "14.96") |
| 3D extruded text | 14.90 | `04` (search "14.90") |
| 3D chrome text | 14.86 | `04` (search "14.86") |
| Slit light system | 14.56 | `04` (search "14.56") |
| Pendant light | 14.77 | `04` (search "14.77") |
| Ambient glow orb | 14.78 | `04` (search "14.78") |

### Particle Effects
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| CSS starfield | 26.2 | `10-particle-effects.md` |
| Canvas particle engine | 26.3 | `10-particle-effects.md` |
| Click-burst dust | 26.4 | `10-particle-effects.md` |
| Fire particles | 26.5 | `10-particle-effects.md` |
| Orbital starfield | 26.6 | `10-particle-effects.md` |
| Black hole vortex | 26.7 | `10-particle-effects.md` |
| WebGL GPGPU particles | 26.8 | `10-particle-effects.md` |
| Text disintegration | 26.9 | `10-particle-effects.md` |

### Aging, Patina & Safety
| Component | Pattern # | Reference File(s) |
|-----------|-----------|-------------------|
| Vintage/weathered look | 19 | `06-aging-safety-tokens-palettes.md` |
| Industrial safety colors | 20 | `06-aging-safety-tokens-palettes.md` |
| Design tokens setup | 21 | `06-aging-safety-tokens-palettes.md` |

**Component not in the table?** Search across all reference files:
```bash
grep -ri "keyword" references/
```

---

## Quick-Reference Recipes (Inline)

These 5 recipes cover the most common patterns. Use them directly WITHOUT loading reference files. For advanced variants, load the referenced file.

### Recipe 1 — Dark Card Shadow Stack (5-layer minimum)
```css
box-shadow:
  inset 0 1px 0 rgba(255,255,255,0.05),   /* top edge catch */
  inset 0 -1px 0 rgba(0,0,0,0.3),          /* bottom edge */
  0 2px 4px rgba(0,0,0,0.4),               /* close cast shadow */
  0 8px 16px rgba(0,0,0,0.3),              /* mid depth */
  0 16px 32px rgba(0,0,0,0.2);             /* ambient occlusion */
background: linear-gradient(145deg, #1a1a1a 0%, #0d0d0d 100%);
```

### Recipe 2 — Bevel Button (3-layer, active depression)
```css
/* Normal state */
box-shadow:
  inset 0 1px 1px rgba(255,255,255,0.15),  /* top bevel highlight */
  inset 0 -1px 1px rgba(0,0,0,0.3),        /* bottom bevel shadow */
  0 2px 8px rgba(0,0,0,0.5),               /* cast shadow */
  0 4px 16px rgba(0,0,0,0.3),              /* ambient */
  0 0 20px rgba(255,180,0,0.1);            /* ambient glow */
/* Active state — depress into surface */
box-shadow:
  inset 0 2px 4px rgba(0,0,0,0.5),         /* pressed inset */
  inset 0 1px 1px rgba(0,0,0,0.3),         /* inner depth */
  0 1px 2px rgba(0,0,0,0.3);               /* minimal cast */
transform: translateY(1px);
```

### Recipe 3 — Rim Light (edge glow on dark card)
```css
/* On the card element */
box-shadow:
  inset 0 1px 0 rgba(255,255,255,0.06),
  inset 0 -1px 0 rgba(0,0,0,0.4),
  0 4px 12px rgba(0,0,0,0.5),
  0 0 1px rgba(255,255,255,0.1);
/* ::before — top edge glow */
position: absolute; top: 0; left: 10%; right: 10%; height: 1px;
background: radial-gradient(ellipse at center, rgba(255,255,255,0.25), transparent 70%);
/* ::after — bottom subtle glow */
position: absolute; bottom: 0; left: 20%; right: 20%; height: 1px;
background: radial-gradient(ellipse at center, rgba(255,255,255,0.08), transparent 70%);
```

### Recipe 4 — Phosphor Glow Text (CRT/LED)
```css
font-family: 'Orbitron', sans-serif;
font-weight: 700;
letter-spacing: 0.05em;
text-transform: uppercase;
color: hsl(35 100% 65%);
text-shadow:
  0 0 4px currentColor,
  0 0 10px currentColor,
  0 0 20px rgba(255,180,0,0.3);
```

### Recipe 5 — Silkscreen Label (panel text)
```css
font-family: ui-monospace, monospace;
font-weight: 600;
letter-spacing: 0.08em;
text-transform: uppercase;
color: rgba(255,255,255,0.06);
text-shadow: 0 1px 0 rgba(0,0,0,0.9), 0 0 6px rgba(255,255,255,0.05);
```

---

## Warm Industrial Palette

Color tokens for the Retro-Industrial / Aerospace family. All hues 25-40 (warm amber/brown).

| Token | Value | Usage |
|---|---|---|
| `--ri-chassis-dark` | `hsl(30 14% 5%)` | Deepest panel background |
| `--ri-chassis-base` | `hsl(30 12% 8%)` | Standard panel/card background |
| `--ri-chassis-mid` | `hsl(35 10% 12%)` | Elevated surface |
| `--ri-chassis-light` | `hsl(35 8% 18%)` | Bezel outer ring |
| `--ri-bevel` | `hsl(40 8% 26%)` | Chamfered edges |
| `--ri-highlight` | `hsl(40 12% 38%)` | Specular spots |
| `--ri-amber` | `hsl(35 100% 60%)` | CRT text, active state |
| `--ri-amber-dim` | `hsl(35 60% 40%)` | Muted accent, borders |
| `--ri-amber-glow` | `rgba(255,180,0,0.4)` | Text-shadow halo |
| `--ri-cream` | `hsl(40 60% 72%)` | Counter digits |
| `--ri-green` | `hsl(120 80% 55%)` | LED green |
| `--ri-red` | `hsl(0 80% 55%)` | LED red, critical |
| `--ri-silk` | `rgba(255,255,255,0.06)` | Silkscreen text |
| `--ri-silk-active` | `rgba(245,158,11,0.8)` | Backlit label |

## Instrumental Typography

| Context | Font | Weight | Tracking | Case |
|---|---|---|---|---|
| CRT/VFD readout | `'Orbitron', sans-serif` | 700 | `0.05em` | uppercase |
| Terminal/status | `'Share Tech Mono', monospace` | 400 | `0.02em` | mixed |
| Counter digits | `'Orbitron', sans-serif` | 700 | `0.1em` | numeric |
| Silkscreen labels | `font-mono` (system) | 600 | `0.08-0.15em` | uppercase |
| Engraved text | `font-mono` (system) | 700 | `0.05em` | uppercase |

---

## MANDATORY Quality Checklist — Verify BEFORE Delivering

**Every component MUST pass ALL items. Do NOT deliver code that fails any check.**

- [ ] **Shadow depth**: Standard ≥ 5 layers, Advanced ≥ 8, Hero ≥ 11. Count them.
- [ ] **Light consistency**: Single direction (default 135deg) for ALL shadows and highlights
- [ ] **4-layer construction**: Chassis + Depth + Lighting + Detail all present
- [ ] **Hardware placement**: Screws match geometry. NEVER a single screw.
- [ ] **State coverage**: hover, active, disabled, focus all implemented
- [ ] **Physical realism**: Every effect represents something physical (no decorative-only)
- [ ] **Typography method**: Text rendering matches surface (silkscreen/engraved/embossed)
- [ ] **Assembly order**: Backplate → panels → wells → hardware → instruments → labels
- [ ] **Accessibility**: Contrast ratios, focus-visible, touch targets ≥ 44px, `prefers-reduced-motion`
- [ ] **Performance**: `will-change` on animated elements, `pointer-events-none` on textures, no animated blur
- [ ] **Tailwind-first**: Inline style only for complex multi-shadow stacks
- [ ] **Reference files consulted**: At least one reference file was read for the component type

---

## Anti-Patterns — NEVER Do These

- **2-3 layer shadows on 3D objects** — use 5-15 layers. If it looks flat, add more layers.
- **Single screw on a panel** — minimum 2 for a strip, 4 for a rectangle.
- **`conic-gradient` for point-source lighting** — use `radial-gradient` + `mask-composite: exclude`
- Uniform glow without multi-distance layers (core + mid + halo)
- Symmetric lighting from multiple directions
- `filter: blur()` in animations (use `opacity` and `transform` only)
- Neumorphism on dark or light backgrounds (MUST be mid-tone ~`#e0e0e0`)
- Missing focus indicators on interactive elements
- Decorative effects with no physical explanation

---

## Reference Files (11 files — load via lookup table above)

All files live in `references/`. Load ONLY the files indicated by the Component Lookup Table.

| File | Content | When to Load |
|------|---------|-------------|
| `01-shadows-materials-textures.md` | Shadows, 16 materials, lighting, glow, textures | Core file — any component |
| `02-hardware-animation-neumorphism.md` | Screws, vents, rivets, 8 animations, neumorphism | Panels with hardware, animated elements |
| `03-blueprints-performance-palettes.md` | 14 blueprints, performance rules, 6 palettes | New component from scratch |
| `04-community-techniques.md` | 102 community patterns (14.1–14.102) | Pattern number from lookup table |
| `05-physics-composition-interaction-typography.md` | Light physics, assembly rules, interaction, typography | Multi-element panels, faceplates |
| `06-aging-safety-tokens-palettes.md` | Aging/patina, safety colors, design tokens | Vintage, weathered, industrial safety |
| `07-glass-effects.md` | 10 glass techniques | Any glass effect |
| `08-metal-effects.md` | 8 metal techniques | Any metal surface/text |
| `09-rim-light-effects.md` | 5 rim light techniques | Edge-lit dark cards/panels |
| `10-particle-effects.md` | 10 particle systems (CSS/Canvas/WebGL) | Any particle effect |
| `11-retro-industrial-patterns.md` | Bezel, CRT, LED, screw, texture, counter | Warm industrial / aerospace |

### Searching across all files
```bash
grep -ri "keyword" references/
```

### HTML asset
`assets/agile-tech-skeuomorphic-site.html` — Full 8000-line skeuomorphic website. Too large to load fully. Search with `grep -i "keyword"` for specific techniques.
