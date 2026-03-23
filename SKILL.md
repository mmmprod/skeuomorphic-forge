---
name: skeuomorphic-forge
description: "Build physically-realistic skeuomorphic UI with Tailwind CSS. Covers buttons, panels, gauges, knobs, CRT/LED displays, glass/metal effects, particle systems, and industrial hardware. Provides shadow stacks, material textures, lighting rules, and construction blueprints. Triggers on: skeuomorphic, realistic depth, industrial UI, 3D button, gauge, meter, analog, tactile, material texture, retro-industrial, aerospace panel, DSP cockpit. Do NOT trigger for flat/minimal UI or standard Material/Shadcn components."
---

# Skeuomorphic Forge

Build physically-realistic UI components using Tailwind CSS + inline styles. Every component MUST look like a real physical object — machined metal, CRT glass, brushed aluminum — not a flat div with a drop shadow.

---

## Rule Categories by Priority

| Priority | Category                    | Impact       | What it prevents                                           |
| -------- | --------------------------- | ------------ | ---------------------------------------------------------- |
| 0        | **Context Scan & Decision** | **BLOCKING** | Random style choices, wrong button tier, no page coherence |
| 1        | Shadow Depth                | CRITICAL     | Flat design disguised as skeuomorphic                      |
| 2        | Drop Shadows = BLACK ONLY   | CRITICAL     | Bizarre colored shadows underneath elements                |
| 3        | Contrast Separation         | CRITICAL     | Dark-on-dark: containers and cards melting together        |
| 4        | Light/Shadow Separation     | CRITICAL     | Confused, muddy, unrealistic surfaces                      |
| 5        | Warm Highlights             | CRITICAL     | Blafard/washed-out industrial components                   |
| 6        | Typography & Readability    | HIGH         | Illegible tiny text, unreadable labels                     |
| 7        | Assembly Order              | HIGH         | Decorative screws on flat surfaces                         |
| 8        | Interaction States          | HIGH         | Dead buttons with no physical feedback                     |
| 9        | Physical Naming             | HIGH         | Generic components without identity                        |
| 10       | Creative Variety            | HIGH         | Always the same style, no personality                      |
| 11       | Accessibility               | MEDIUM       | Unusable components despite visual quality                 |
| 12       | Performance                 | MEDIUM       | Janky animations, layout thrash                            |

---

## Quick Reference — Shadow Tiers

| Tier         | Use for                        | Min layers | Source                            |
| ------------ | ------------------------------ | ---------- | --------------------------------- |
| **Standard** | buttons, cards, toggles        | 5          | Section 4a below                  |
| **Advanced** | knobs, dials, meters, displays | 8          | Section 4b below                  |
| **Hero**     | panels, chassis, backplates    | 11         | Section 4c below                  |
| **Ultra**    | showcase CRT, deep chassis     | 31         | `assets/codepen-deep-screen.html` |

---

## STEP 0 — READ BEFORE BUILDING (MANDATORY)

**Always read `references/00-golden-examples.md` FIRST.** It contains:

- Production shadow stacks (5/8/13/31 layers) extracted from working code
- Complete button implementation (rest/hover/active) — COPY AND ADAPT, do not invent
- Complete card implementation with rim light
- CRT display construction with phosphor glow
- The warm industrial palette
- Component Lookup Table mapping component types to reference files

**NEVER invent shadow stacks from scratch.** Always start from a proven pattern.

---

## STEP 0.5 — CONTEXT SCAN & DECISION (MANDATORY BEFORE ANY STYLING)

**NEVER style a component without analyzing the page first. NEVER choose a pattern without asking.**

This step prevents random style choices. Before touching CSS/JSX, perform a 3-phase analysis:

### Phase 1 — SCAN the existing page

Read the target file and its parent page. Extract:

1. **Existing color palette** — What surface colors, accents, and text colors are already in use?
2. **Existing button styles** — What button patterns exist on this page? (gradients, shadows, sizes)
3. **Container hierarchy** — What is the nesting structure? (page bg → section well → card → element)
4. **Typography in use** — What font sizes, weights, families are already established?
5. **Theme identity** — Which aesthetic family does this page use? (warm industrial, cool steel, purple, etc.)

```
Example scan output:
  Page: AnalysisPage.tsx
  Background: #0a0a0a (very dark)
  Section wells: #0e0e0e with inset shadows
  Cards: #242424 with 5-layer shadows
  Accent: amber hsl(35 100% 60%)
  Buttons: 2 existing — primary (amber gradient), secondary (outline ghost)
  Typography: Orbitron 14px titles, mono 13px body
  Theme: Warm industrial
```

### Phase 2 — CLASSIFY the requested component

**Read `references/17-context-scan-matrices.md`** for the full decision matrices:
- **Button Decision Matrix** — 6 tiers from CTA/Hero to Navigation
- **Container Decision Matrix** — 5 roles from Page well to Header
- **Physical Size Rule** — device cards have FIXED dimensions
- **Special Elements** — gauge, CRT, toggle, knob, LED shadow tiers

### Phase 3 — ASK before choosing (MANDATORY)

If the style choice is not obvious from context, ASK the user. See `references/17-context-scan-matrices.md` for the "When to ask" vs "When NOT to ask" decision table.

### Phase 3b — CONSISTENCY CHECK

After deciding on a style, verify it doesn't clash:

1. **Same role = same style** — If 3 primary buttons exist with amber gradient, the 4th must match
2. **Hierarchy must be readable** — A new element can't be brighter than the element above it in the hierarchy
3. **Accent colors limited** — Max 2 accent colors per page. A third needs explicit user approval
4. **New theme on existing page = ASK** — Never introduce a new theme family without confirmation

---

## 3D Vocabulary — What Users Mean

When a user asks for "3D", "depth", "relief", or "effet 3D", map their words to techniques:

| User says                 | Technique                                            | Reference                              |
| ------------------------- | ---------------------------------------------------- | -------------------------------------- |
| "3D effect" / "effet 3D"  | Multi-layer shadow stack + optional perspective tilt | `13-3d-depth-techniques.md` §13.3-13.4 |
| "3D button"               | Press effect: shadow compression on :active          | §13.5                                  |
| "depth" / "profondeur"    | Graduated shadow layers OR translateZ                | §13.3, §13.10                          |
| "relief" / "embossed"     | Text/shape raised via gradient clip + text-shadow    | §13.8                                  |
| "recessed" / "inset"      | Inset shadow stack (gorge effect)                    | §13.3                                  |
| "floating" / "levitating" | Extra-wide drop shadows + translateY lift            | §13.3                                  |
| "parallax"                | Layers at different translateZ or scroll speeds      | §13.11                                 |
| "glass dome" / "bubble"   | Radial gradient pseudo-element over content          | §13.9, `07-glass-effects.md`           |
| "flip card"               | rotateY(180deg) + preserve-3d + backface-visibility  | §13.6                                  |
| "isometric"               | rotateX + rotateY small angles + edge faces          | §13.7                                  |
| "tilted" / "angled"       | perspective parent + rotateX/Y on hover              | §13.4                                  |

**Always read `references/13-3d-depth-techniques.md`** when the request involves any of these terms.

---

## STEP 1 — FIND THE RIGHT PATTERN

### Using the Search Engine (for files 04, 11, and cross-file searches)

```bash
# Search all 19 reference files + 21 HTML assets
python3 scripts/search.py "button shadow"

# Top 5 results
python3 scripts/search.py "CRT display" -n 5

# Search specific file only
python3 scripts/search.py "box-shadow" --file 04

# Only show code blocks from matching sections
python3 scripts/search.py "knob gradient" --code-only

# Show limited context preview
python3 scripts/search.py "rim light" --context 5
```

The search engine indexes all sections across 40 source files (19 references + 21 HTML assets) using BM25 ranking. Use it instead of reading large files (04 = 10046 lines, 11 = 5489 lines).

### Using the Lookup Table

Find the component type in the Lookup Table (inside `00-golden-examples.md`), load the indicated reference file(s), find the matching pattern, and ADAPT it.

---

## STEP 2 — CRITICAL: SHADOWS, LIGHT & CONTRAST (Priority 1-5)

These are SEPARATE systems. NEVER confuse them. NEVER combine them into one property.

### ABSOLUTE RULE: DROP SHADOWS = BLACK ONLY (Priority 2)

**ALL drop shadows (non-inset, underneath the element) MUST use `rgba(0,0,0,...)` ONLY.**

A shadow is the absence of light. In reality, shadows are ALWAYS dark/black. A purple, blue, or amber shadow underneath a div is physically wrong and visually bizarre.

**FORBIDDEN** (unless user explicitly requests colored shadows):

```css
/* NEVER — colored drop shadows */
0 4px 8px rgba(80,30,160,0.25)    /* purple shadow = WRONG */
0 8px 16px rgba(60,20,120,0.2)    /* purple shadow = WRONG */
0 0 40px rgba(255,180,0,0.06)     /* amber glow underneath = WRONG */
0 0 60px rgba(140,80,255,0.08)    /* purple glow underneath = WRONG */
```

**CORRECT:**

```css
/* ALWAYS — black drop shadows */
0 4px 8px rgba(0,0,0,0.3)         /* black shadow = correct */
0 8px 16px rgba(0,0,0,0.25)       /* black shadow = correct */
0 16px 32px rgba(0,0,0,0.15)      /* black shadow = correct */
```

**Exception**: `inset` highlights using light/colored rgba are fine — they represent light hitting the INSIDE edge of the element, not a shadow underneath. Colored `inset` at low opacity (0.05-0.15) is acceptable for themed surfaces (purple buttons, amber panels).

### CONTRAST SEPARATION (Priority 3)

**Container backgrounds and card backgrounds MUST have visible brightness difference.**

When placing cards inside a container panel (wells, recessed panels, sections):

| Element                   | Brightness range        | Example                                    |
| ------------------------- | ----------------------- | ------------------------------------------ |
| **Well/recess container** | Very dark: `#08-#10`    | `#0e0e0e`, `#0a0a0a`                       |
| **Card floating inside**  | Lighter: `#1c-#28`      | `#242424`, `#252525`                       |
| **Minimum delta**         | >= `#12` hex difference | Container `#0e` → Card `#22` = `#14` delta |

**WRONG** (everything melts together):

```css
container: "#181818"  /* dark */
card:      "#1c1c1c"  /* almost the same dark = INVISIBLE */
```

**CORRECT** (cards pop out of the well):

```css
container: "#0a0a0a"  /* very dark recess */
card:      "#242424"  /* noticeably lighter = VISIBLE separation */
```

Also reinforce card edges with:

- `borderTop: "1px solid rgba(255,255,255,0.09)"` — visible top bevel
- `borderLeft: "1px solid rgba(255,255,255,0.06)"` — subtle left catch
- Stronger drop shadows on cards since they sit on dark wells

### SHADOW = where light DOES NOT reach

Shadow creates **depth, recession, and spatial positioning**. Implemented via `box-shadow` with **dark colors only** (`rgba(0,0,0,...)`).

```css
/* SHADOW — depth layers (BLACK ONLY — no colored shadows) */
box-shadow:
  inset 0 3px 8px rgba(0, 0, 0, 0.6),
  /* gorge top — light blocked */ inset 0 -3px 5px rgba(0, 0, 0, 0.5),
  /* gorge bottom — ambient occlusion */ inset 3px 0 6px rgba(0, 0, 0, 0.55),
  /* gorge left wall */ inset -3px 0 6px rgba(0, 0, 0, 0.55),
  /* gorge right wall */ 0 2px 4px rgba(0, 0, 0, 0.4),
  /* close drop shadow — BLACK */ 0 4px 8px rgba(0, 0, 0, 0.3),
  /* mid depth — BLACK */ 0 8px 16px rgba(0, 0, 0, 0.25),
  /* far depth — BLACK */ 0 16px 32px rgba(0, 0, 0, 0.15); /* ambient floor shadow — BLACK */
```

### LIGHT = where light HITS the surface

Light creates **specular highlights, edge catches, and warm reflections**. Implemented via:

- `box-shadow` with **light colors** (`rgba(255,255,255,...)`) — edge catches only, max opacity 0.15
- `background: linear-gradient(...)` — surface curvature and specular bands
- `border-top/left` with light rgba — bevel highlight edges
- `::before/::after` pseudo-elements — specular hotspots and rim glow

```css
/* LIGHT — edge catches (go in SAME box-shadow, DIFFERENT purpose) */
box-shadow:
  /* ... dark shadow layers above ... */
  inset 0 1px 0 rgba(255, 255, 255, 0.15),
  /* top edge catch */ 0 1px 0 rgba(255, 255, 255, 0.03); /* bottom reflected light */

/* LIGHT — surface curvature */
background: linear-gradient(145deg, #1e1e1e 0%, #121212 100%);

/* LIGHT — bevel edges */
border-top: 1px solid rgba(255, 255, 255, 0.08);
border-left: 1px solid rgba(255, 255, 255, 0.04);
border-bottom: 1px solid rgba(0, 0, 0, 0.3);
border-right: 1px solid rgba(0, 0, 0, 0.2);
```

### WARM light, not blafard white

**NEVER** use pure `rgba(255,255,255,...)` for specular highlights at opacity > 0.1.

| Purpose             | Color                                         | Opacity         | When                            |
| ------------------- | --------------------------------------------- | --------------- | ------------------------------- |
| Edge catch (subtle) | `rgba(255,255,255,...)`                       | 0.03-0.08       | Always, on every raised surface |
| Top bevel highlight | `rgba(255,255,255,...)`                       | 0.08-0.15       | Top/left edges facing light     |
| Specular hotspot    | `rgba(255,240,220,...)`                       | 0.15-0.30       | `::before` on curved surfaces   |
| Active glow         | `rgba(255,180,60,...)`                        | 0.10-0.40       | Active/on states, LEDs          |
| CRT/LED emission    | `hsl(35 100% 60%)`                            | Full color      | Display elements                |
| Rim light (pseudo)  | `rgba(255,255,255,0.25)` center → transparent | radial-gradient | Top edge of raised panels       |

---

## STEP 3 — CONSTRUCTION PROTOCOL (Priority 4, 6)

### 3a. Name the physical object

State explicitly: "This is a machined aluminum faceplate" or "This is a Bakelite rocker switch." If the analog is unclear, the component will look generic.

### 3b. Choose aesthetic family

- **Retro-Industrial** (default): `hsl(30 12% 8%)` base, amber accents `hsl(35 100% 60%)`
- **Industrial/Dark**: `#050505`-`#1a1a1a`, cool steel
- **Classic/Light**: `#d0d0d0`-`#f0f0f0`, chrome
- **Neumorphic**: mid-tone `#e0e0e0` ONLY (never dark, never light)

### 3c. Build in assembly order (back to front)

```
Backplate (deepest, largest shadow stack)
  +-- Sub-panels / bezels (medium shadow stack)
       +-- Wells / recesses (inset shadows)
            +-- Instruments / displays (content + glow)
                 +-- Hardware (screws, rivets — AFTER depth exists)
                      +-- Labels / overlays (silkscreen, engraved text)
                           +-- Glass / reflection (::before/::after)
```

**CRITICAL**: Hardware (screws, vents) goes AFTER the depth layers exist. Screws on a flat surface = contradiction. Build depth FIRST, then add hardware.

---

## STEP 4 — APPLY SHADOW STACK (Priority 1)

Copy the appropriate tier from below. COUNT the layers after pasting.
Detailed versions with L/S annotations: `references/00-golden-examples.md` section 1.

### 4a. Standard (buttons, cards, toggles) — minimum 5 layers

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,255,255,0.05),
  inset 0 -1px 0 rgba(0,0,0,0.3),
  0 2px 4px rgba(0,0,0,0.4),
  0 8px 16px rgba(0,0,0,0.3),
  0 16px 32px rgba(0,0,0,0.2)
`;
```

### 4b. Advanced (knobs, dials, meters) — minimum 8 layers

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,255,255,0.12),
  inset 0 -2px 4px rgba(0,0,0,0.6),
  inset 3px 0 6px rgba(0,0,0,0.4),
  inset -3px 0 6px rgba(0,0,0,0.4),
  0 2px 4px rgba(0,0,0,0.4),
  0 4px 8px rgba(0,0,0,0.3),
  0 8px 16px rgba(0,0,0,0.25),
  0 16px 32px rgba(0,0,0,0.15)
`;
```

### 4c. Hero (panels, chassis) — minimum 11 layers

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,255,255,0.25),
  inset 0 -1px 0 rgba(0,0,0,0.8),
  inset 1px 0 1px rgba(255,255,255,0.1),
  inset -1px 0 1px rgba(0,0,0,0.5),
  0 2px 4px rgba(0,0,0,0.4),
  0 4px 8px rgba(0,0,0,0.3),
  0 6px 12px rgba(0,0,0,0.25),
  0 8px 16px rgba(0,0,0,0.2),
  0 12px 24px rgba(0,0,0,0.15),
  0 16px 32px rgba(0,0,0,0.1),
  0 20px 40px rgba(0,0,0,0.08),
  0 40px 60px -20px rgba(0,0,0,0.5)
`;
```

### 4d. Ultra (showcase CRT, deep chassis) — 31 layers

Read `assets/codepen-deep-screen.html` for the complete 31-layer stack. Gold standard for maximum depth realism.

---

## STEP 5 — ADD LIGHTING SEPARATELY (Priority 2-3)

After shadows are in place, add light on TOP:

1. **Surface gradient** (curvature): `background: linear-gradient(145deg, lighter 0%, darker 100%)`
2. **Bevel edges**: `border-top: 1px solid rgba(255,255,255,0.08)`
3. **Specular hotspot**: `::before` with `radial-gradient(circle at 35% 30%, rgba(255,240,220,0.2), transparent 60%)`
4. **Rim glow**: `::before` with `radial-gradient(ellipse at center, rgba(255,255,255,0.25), transparent 70%)` at top edge

**Light direction**: Single source at 135deg, consistent across ALL components on the page.

---

## STEP 6 — ADD INTERACTION STATES (Priority 5)

EVERY interactive element needs ALL of these:

```javascript
// Hover — lift + expand shadow
':hover': {
  transform: 'translateY(-1px)',
  boxShadow: '/* same stack but blur +2px per layer, opacity +0.05 on highlights */'
}
// Active — depress into surface
':active': {
  transform: 'translateY(1px)',
  boxShadow: `
    inset 0 2px 4px rgba(0,0,0,0.5),
    inset 0 1px 1px rgba(0,0,0,0.3),
    0 1px 2px rgba(0,0,0,0.3)
  `
}
// Disabled — desaturate + reduce opacity
':disabled': {
  opacity: 0.5,
  filter: 'saturate(0.3)',
  pointerEvents: 'none'
}
// Focus — visible ring
':focus-visible': {
  outline: '2px solid hsl(35 100% 60%)',
  outlineOffset: '2px'
}
```

---

## STEP 6b — TYPOGRAPHY & READABILITY (Priority 6)

Skeuomorphic does NOT mean tiny. Text must be readable. Apply these MINIMUM font sizes:

| Element                      | Minimum | Recommended | Font                                          |
| ---------------------------- | ------- | ----------- | --------------------------------------------- |
| **Body text / descriptions** | 13px    | 14-16px     | mono or sans-serif                            |
| **Card titles / zone names** | 14px    | 14-16px     | Orbitron or mono, 700 weight                  |
| **Section headers**          | 13px    | 14px        | Orbitron uppercase, letter-spacing 0.08-0.1em |
| **Sub-labels / captions**    | 11px    | 12px        | mono, lighter opacity                         |
| **Badges / tags**            | 10px    | 11px        | mono, uppercase                               |
| **CRT readout values**       | 13px    | 14px        | mono, amber/accent color                      |
| **Button labels**            | 13px    | 14px        | Orbitron, 700, uppercase                      |

**NEVER go below 10px for ANY text.** If text needs to be de-emphasized, reduce opacity (0.4-0.6) instead of shrinking font size.

**Text opacity for readability:**

| Purpose                        | Minimum opacity | Why                          |
| ------------------------------ | --------------- | ---------------------------- |
| Primary text (titles, labels)  | 0.85            | Must be immediately readable |
| Secondary text (descriptions)  | 0.5             | Readable on inspection       |
| Tertiary text (captions, meta) | 0.35            | Visible but not competing    |

---

## STEP 6c — CREATIVE VARIETY (Priority 10)

**Do NOT always produce the same amber-on-dark industrial look.** Skeuomorphic design has many personalities. PROPOSE options to the user before building.

### When starting a new component or section, PROPOSE 2-3 visual approaches:

Example proposals:

- **"Warm industrial" (default)**: Amber accents, dark chassis, warm specular highlights
- **"Cool steel"**: Blue-grey tones, chrome highlights, cold steel feel
- **"Deep purple"**: Violet gradient surface, purple-tinted inset highlights, elegant
- **"Military/aerospace"**: OD green, red safety indicators, stencil typography
- **"Vintage audio"**: Brown/cream Bakelite, warm tube glow, VU meter aesthetic
- **"CRT terminal"**: Green phosphor on black, scanlines, retro computing

### Color themes — surface + accent pairs:

| Theme           | Surface gradient    | Accent                     | Inset highlight          | Text                     |
| --------------- | ------------------- | -------------------------- | ------------------------ | ------------------------ |
| Warm industrial | `#1e1e1e → #141414` | `hsl(35 100% 60%)` amber   | `rgba(255,240,220,0.12)` | `rgba(255,240,220,0.9)`  |
| Cool steel      | `#1a1c20 → #12141a` | `hsl(210 70% 60%)` blue    | `rgba(180,200,255,0.10)` | `rgba(200,220,255,0.9)`  |
| Deep purple     | `#2d1854 → #150b28` | `hsl(270 100% 70%)` violet | `rgba(200,160,255,0.12)` | `rgba(220,200,255,0.95)` |
| Military        | `#1a1e14 → #10140c` | `hsl(0 70% 55%)` red       | `rgba(180,200,150,0.08)` | `rgba(180,200,150,0.85)` |
| Vintage audio   | `#2a2218 → #1a1610` | `hsl(30 80% 55%)` copper   | `rgba(255,220,180,0.10)` | `rgba(240,220,190,0.9)`  |
| CRT terminal    | `#0a0f0a → #050805` | `hsl(120 100% 50%)` green  | `rgba(0,255,60,0.06)`    | `rgba(0,255,60,0.85)`    |

**IMPORTANT**: Regardless of theme, drop shadows remain BLACK `rgba(0,0,0,...)`. Only `inset` highlights and text/accent colors change with theme.

### When to propose variety:

- User asks for a "button" or "card" without specifying style → propose 2-3 theme options
- Building a new page section → ask if it should match existing theme or contrast
- User says "something different" or "more personality" → explore non-default themes
- Same component requested multiple times → vary the approach each time

---

## STEP 7 — VERIFY (Pre-Delivery Gate)

**Read and apply `references/18-verification-checklist.md`** — the full U0-U9 pre-delivery verification gate.

Key gates: U0 Context Scan (BLOCKING), U1 Shadow Depth (CRITICAL), U2 Light Source (CRITICAL), U3-U4 Construction + Hardware (HIGH), U5 Interaction States (HIGH), U6 Physical Purpose (HIGH), U7 Typography (HIGH), U8 Accessibility (MEDIUM), U9 Benchmark Lessons.

A component that fails this gate MUST NOT be delivered.

---

## Anti-Patterns (Do / Don't)

**Full table in `references/00-golden-examples.md`** (section 10 — Anti-Patterns).

Key rules: shadows BLACK only, min 5 layers, hardware AFTER depth, warm light (not pure white above 0.10), same dimensions for all states, copy shadow stacks from golden examples (never invent), max 2 accent colors per page.

---

## CRITICAL — Mandatory Minimums for 3 Problem Areas

> These 3 areas ALWAYS fail without enforcement. Read the dedicated reference BEFORE building.

### Metal Recesses / Wells / Inset Effects

**Read `references/14-metal-recess-wells.md` FIRST** when building ANY recessed element (wells, input fields, display recesses, gauge pits, slider channels, LED holes).

| Component                  | Minimum inset layers | Background                   | Reference |
| -------------------------- | -------------------- | ---------------------------- | --------- |
| Input field / small status | 6                    | `#080808 → #0c0c0c`          | §14.3     |
| Gauge/meter well           | 9                    | `#050505 → #080808`          | §14.4     |
| CRT/deep display           | 12                   | `#030303`                    | §14.5     |
| Slider channel             | 5                    | gradient `#050505 → #0f0f0f` | §14.6     |
| LED hole                   | 4                    | radial `#1a1a1a → #000`      | §14.7     |

**FORBIDDEN**: `inset 0 2px 4px rgba(0,0,0,0.3)` alone (1-3 layers). This is a CSS input field, not a metal recess. Every recess needs ALL 4 zones: top attack, lateral walls, bottom catch, outer lip.

### Rim Light Effects

**Read `references/09-rim-light-effects.md` §25.0 FIRST** when building ANY rim light.

**Mandatory checklist:**

- Shadow stack built FIRST (5+ depth layers), THEN rim light on top
- Top edge 2-4x brighter than bottom (directional light, not uniform)
- At least ONE `::before` or `::after` with `radial-gradient` for concentrated hotspot
- No highlight opacity > 0.25 — rim light is SUBTLE
- `pointer-events: none` on pseudo-element overlays

**FORBIDDEN**: `border: 1px solid rgba(255,255,255,0.1)` as "rim light" (uniform border = picture frame). `box-shadow: 0 0 20px rgba(255,255,255,0.1)` alone (uniform glow = neon sign).

### Metal Chassis / Panels

**Read `references/15-detailed-chassis.md` FIRST** when building ANY chassis, panel, backplate, or enclosure.

**Mandatory: 3+ zones from the 6-zone anatomy:**

1. Bezel frame (outer rim with multi-layer shadow + bevel borders)
2. Main surface (brushed/textured metal, NOT flat gray)
3. Wells/recesses (inset shadows per §14 above)
4. Display areas (screens, gauges — recessed with color bleed)
5. Grille/ventilation (perforated hex or slot pattern)
6. Labels (stamped/embossed/engraved — NOT plain text)

**FORBIDDEN**: Flat `#333` rectangle with a basic CSS grid of dots. Every chassis needs surface texture (brushed metal gradient or noise), at least one recess, and at least one hardware detail (screws, seams, or labels). See §15.11 for the mandatory chassis checklist.

---

## Reference Files (19 references + 21 HTML assets)

**ALWAYS start with `00-golden-examples.md`** — it has the Lookup Table to find component patterns.

| File                                               | Content                                                                                                                                       | Lines    | Search?         |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- |
| `00-golden-examples.md`                            | **START HERE** — Shadow stacks, button/card/CRT, Lookup Table, Palette                                                                        | ~540     | Read full       |
| `01-shadows-materials-textures.md`                 | 16 material gradients (chrome, leather, wood, rubber...)                                                                                      | 321      | Read full       |
| `02-hardware-animation-neumorphism.md`             | Screws, vents, rivets, 8 animations, neumorphism                                                                                              | 166      | Read full       |
| `03-blueprints-performance-palettes.md`            | 14 component blueprints, performance rules, 6 palettes                                                                                        | 130      | Read full       |
| `04-community-techniques.md`                       | 102 community patterns (14.1-14.102)                                                                                                          | **10046** | **SEARCH ONLY** |
| `05-physics-composition-interaction-typography.md` | Light physics, sphere/cylinder/flat lighting                                                                                                  | 258      | Read full       |
| `06-aging-safety-tokens-palettes.md`               | Aging/patina, safety colors, design tokens                                                                                                    | 160      | Read full       |
| `07-glass-effects.md`                              | 10 glass techniques (frosted, dark glass, sphere)                                                                                             | 1163     | Read or search  |
| `08-metal-effects.md`                              | 8 metal techniques (brushed, chrome, gold, conic)                                                                                             | 690      | Read or search  |
| `09-rim-light-effects.md`                          | 7 common mistakes + 5 rim light techniques with 4-layer system                                                                                | ~530     | Read or search  |
| `10-particle-effects.md`                           | 10 particle systems (CSS, Canvas, WebGL, fire)                                                                                                | 877      | Read or search  |
| `11-retro-industrial-patterns.md`                  | Bezel, CRT, LED, screw, texture, counter                                                                                                      | **5489** | **SEARCH ONLY** |
| `12-production-components.md`                      | 11 production patterns: button, dashboard, VU, switch, LCD, lever, gauge, alert, CRT, accordion, thermometer                                  | ~500     | Read or search  |
| `13-3d-depth-techniques.md`                        | **3D glossary**, shadow depth, perspective/transforms, button press, flip card, isometric, emboss, glass dome, parallax, @property animations | ~880     | Read or search  |
| `14-metal-recess-wells.md`                         | **Metal recesses/wells** — 4-zone anatomy, 6/9/12-layer inset stacks, gorges, punched holes, LCD wells, color bleed                           | ~360     | Read or search  |
| `15-detailed-chassis.md`                           | **Detailed chassis** — 6-zone anatomy, bezel frame, brushed texture, hex perf, panel joints, torx screws, stamped labels                      | ~570     | Read or search  |
| `16-benchmark-lessons.md`                          | **Benchmark failures** — 17 lessons from testing: display wells, color bleed, rim light, device sizing, emboss opacity                        | ~460     | Read or search  |
| `17-context-scan-matrices.md`                      | **Decision matrices** — Button/container tiers, physical size rule, special elements, when-to-ask tables                                      | ~100     | Read full       |
| `18-verification-checklist.md`                     | **Pre-delivery gate** — U0-U9 pre-delivery verification gate                                                                                  | ~100     | Read full       |

### HTML Assets — Quick Lookup

| Need                    | File                                | Search key     |
| ----------------------- | ----------------------------------- | -------------- |
| Push button with LED    | `power-button.html`                 | `power-button` |
| Dashboard / analytics   | `synthscore-analytics.html`         | `synthscore`   |
| VU meter / gauge        | `tube-compressor-vu.html`           | `vu-meter`     |
| Toggle switch           | `skeuomorphic-switch.html`          | `switch`       |
| LCD numeric display     | `lcd-db-display.html`               | `lcd`          |
| Rotary lever / knob     | `industrial-lever.html`             | `lever`        |
| Score gauge / radial    | `credit-score-gauge.html`           | `gauge`        |
| Alert / warning panel   | `autochord-alert-panel.html`        | `alert`        |
| CRT danger screen       | `deep-screen-phosphor.html`         | `phosphor`     |
| Folding / accordion     | `folding-header.html`               | `folding`      |
| Horizontal bar meter    | `horizontal-thermometer.html`       | `thermometer`  |
| Deep CRT (31 layers)    | `codepen-deep-screen.html`          | `deep-screen`  |
| Full page (15+ buttons) | `agile-tech-skeuomorphic-site.html` | `site`         |
| Rimlight toggle switch  | `rimlight-toggle-switch.html`       | `rimlight`     |
| Color-mix buttons       | `color-mix-buttons.html`            | `color-mix`    |
| Rocker 3D switch        | `rocker-3d-switch.html`             | `rocker`       |
| Tile up/down/button     | `tile-buttons-divs.html`            | `tiles`        |
| Neumorphic loader       | `neumorphic-loading-circle.html`    | `loading`      |
| Progress loader (light) | `neumorphic-progress-loader.html`   | `progress`     |
| Pressed buttons (light) | `neumorphic-pressed-buttons.html`   | `pressed`      |
| Fingerprint SVG button  | `fingerprint-button.html`           | `fingerprint`  |

All files in `assets/`. Detailed breakdowns: `references/12-production-components.md`

### Searching References

Use the BM25 search engine for efficient pattern discovery:

```bash
# Cross-file search (all 40 sources)
python3 scripts/search.py "button shadow"

# Targeted file search (for 04 or 11)
python3 scripts/search.py "CRT bezel" --file 11

# Code blocks only (skip prose)
python3 scripts/search.py "knob gradient" --code-only -n 5

# Limited preview
python3 scripts/search.py "rim light" --context 5
```

Common search terms: `button`, `shadow`, `CRT`, `knob`, `glass`, `metal`, `rim light`, `LED`, `bezel`, `screw`, `gauge`, `meter`, `panel`, `switch`, `dial`, `lever`, `LCD`, `VU`, `dashboard`, `toggle`, `alert`, `phosphor`, `thermometer`, `folding`, `accordion`, `dome`, `bulb`, `arc`, `score`, `3D`, `depth`, `perspective`, `emboss`, `parallax`, `isometric`, `flip`, `floating`, `recess`, `well`, `inset`, `gorge`, `chassis`, `brushed`, `perforation`, `seam`, `torx`, `stamped`, `label`, `channel`
