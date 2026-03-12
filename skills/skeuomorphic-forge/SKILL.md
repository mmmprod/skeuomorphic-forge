---
name: skeuomorphic-forge
description: "Build physically-realistic skeuomorphic UI with Tailwind CSS. Covers buttons, panels, gauges, knobs, CRT/LED displays, glass/metal effects, particle systems, and industrial hardware. Provides shadow stacks, material textures, lighting rules, and construction blueprints. Triggers on: skeuomorphic, realistic depth, industrial UI, 3D button, gauge, meter, analog, tactile, material texture, retro-industrial, aerospace panel, DSP cockpit. Do NOT trigger for flat/minimal UI or standard Material/Shadcn components."
---

# Skeuomorphic Forge

Build physically-realistic UI components using Tailwind CSS + inline styles. Every component MUST look like a real physical object — machined metal, CRT glass, brushed aluminum — not a flat div with a drop shadow.

---

## Rule Categories by Priority

| Priority | Category | Impact | What it prevents |
|----------|----------|--------|------------------|
| 1 | Shadow Depth | CRITICAL | Flat design disguised as skeuomorphic |
| 2 | Light/Shadow Separation | CRITICAL | Confused, muddy, unrealistic surfaces |
| 3 | Warm Highlights | CRITICAL | Blafard/washed-out industrial components |
| 4 | Assembly Order | HIGH | Decorative screws on flat surfaces |
| 5 | Interaction States | HIGH | Dead buttons with no physical feedback |
| 6 | Physical Naming | HIGH | Generic components without identity |
| 7 | Typography | MEDIUM | Flat text on 3D surfaces |
| 8 | Accessibility | MEDIUM | Unusable components despite visual quality |
| 9 | Performance | MEDIUM | Janky animations, layout thrash |

---

## Quick Reference — Shadow Tiers

| Tier | Use for | Min layers | Source |
|------|---------|------------|--------|
| **Standard** | buttons, cards, toggles | 5 | Section 4a below |
| **Advanced** | knobs, dials, meters, displays | 8 | Section 4b below |
| **Hero** | panels, chassis, backplates | 11 | Section 4c below |
| **Ultra** | showcase CRT, deep chassis | 31 | `assets/codepen-deep-screen.html` |

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

## STEP 1 — FIND THE RIGHT PATTERN

### Using the Search Engine (for files 04, 11, and cross-file searches)

```bash
# Search all 12 reference files + 2 HTML assets
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

The search engine indexes 2400+ sections across all reference files using BM25 ranking. Use it instead of reading large files (04 = 8671 lines, 11 = 5392 lines).

### Using the Lookup Table

Find the component type in the Lookup Table (inside `00-golden-examples.md`), load the indicated reference file(s), find the matching pattern, and ADAPT it.

---

## STEP 2 — CRITICAL: SHADOW vs LIGHT (Priority 1-3)

These are SEPARATE systems. NEVER confuse them. NEVER combine them into one property.

### SHADOW = where light DOES NOT reach

Shadow creates **depth, recession, and spatial positioning**. Implemented via `box-shadow` with **dark colors only** (`rgba(0,0,0,...)`).

```css
/* SHADOW — depth layers (dark only) */
box-shadow:
  inset 0 3px 8px rgba(0,0,0,0.6),     /* gorge top — light blocked */
  inset 0 -3px 5px rgba(0,0,0,0.5),    /* gorge bottom — ambient occlusion */
  inset 3px 0 6px rgba(0,0,0,0.55),    /* gorge left wall */
  inset -3px 0 6px rgba(0,0,0,0.55),   /* gorge right wall */
  0 2px 4px rgba(0,0,0,0.4),           /* close drop shadow */
  0 4px 8px rgba(0,0,0,0.3),           /* mid depth */
  0 8px 16px rgba(0,0,0,0.25),         /* far depth */
  0 16px 32px rgba(0,0,0,0.15);        /* ambient floor shadow */
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
  inset 0 1px 0 rgba(255,255,255,0.15),   /* top edge catch */
  0 1px 0 rgba(255,255,255,0.03);          /* bottom reflected light */

/* LIGHT — surface curvature */
background: linear-gradient(145deg, #1e1e1e 0%, #121212 100%);

/* LIGHT — bevel edges */
border-top: 1px solid rgba(255,255,255,0.08);
border-left: 1px solid rgba(255,255,255,0.04);
border-bottom: 1px solid rgba(0,0,0,0.3);
border-right: 1px solid rgba(0,0,0,0.2);
```

### WARM light, not blafard white

**NEVER** use pure `rgba(255,255,255,...)` for specular highlights at opacity > 0.1.

| Purpose | Color | Opacity | When |
|---------|-------|---------|------|
| Edge catch (subtle) | `rgba(255,255,255,...)` | 0.03-0.08 | Always, on every raised surface |
| Top bevel highlight | `rgba(255,255,255,...)` | 0.08-0.15 | Top/left edges facing light |
| Specular hotspot | `rgba(255,240,220,...)` | 0.15-0.30 | `::before` on curved surfaces |
| Active glow | `rgba(255,180,60,...)` | 0.10-0.40 | Active/on states, LEDs |
| CRT/LED emission | `hsl(35 100% 60%)` | Full color | Display elements |
| Rim light (pseudo) | `rgba(255,255,255,0.25)` center → transparent | radial-gradient | Top edge of raised panels |

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

### 4a. Standard (buttons, cards, toggles) — minimum 5 layers

```javascript
boxShadow: `
  inset 0 1px 0 rgba(255,255,255,0.05),
  inset 0 -1px 0 rgba(0,0,0,0.3),
  0 2px 4px rgba(0,0,0,0.4),
  0 8px 16px rgba(0,0,0,0.3),
  0 16px 32px rgba(0,0,0,0.2)
`
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
  0 16px 32px rgba(0,0,0,0.15),
  0 0 40px rgba(255,180,0,0.06)
`
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
  0 0 60px rgba(255,176,0,0.06),
  0 40px 60px -20px rgba(0,0,0,0.5)
`
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

## STEP 7 — VERIFY (Pre-Delivery Gate)

### Depth Quality (CRITICAL)

- [ ] Shadow layer count: Standard >= 5, Advanced >= 8, Hero >= 11. COUNT them.
- [ ] Shadow uses ONLY dark `rgba(0,0,0,...)` for depth layers
- [ ] Graduated blur progression: near shadows tight (2-4px), far shadows wide (16-32px)
- [ ] Started from golden-example or reference pattern, NOT invented

### Lighting Quality (CRITICAL)

- [ ] Light and shadow are SEPARATE systems (not mixed in one confused stack)
- [ ] No blafard white: specular uses `rgba(255,240,220,...)` or amber tones
- [ ] Edge catches at opacity 0.03-0.15 only (not 0.3+)
- [ ] Single light direction (135deg) consistent across ALL components
- [ ] Surface gradient present for curvature (`linear-gradient(145deg, ...)`)

### Construction Quality (HIGH)

- [ ] Physical object named explicitly ("machined aluminum", "Bakelite switch")
- [ ] 4-layer construction: Chassis + Depth + Lighting + Detail all present
- [ ] Assembly order respected: depth BEFORE hardware
- [ ] Screws/rivets sit ON a surface with depth, not on flat div

### Interaction Quality (HIGH)

- [ ] hover, active, disabled, focus-visible all implemented
- [ ] Hover lifts (`translateY(-1px)`) with expanded shadow
- [ ] Active depresses (`translateY(1px)`) with compressed shadow
- [ ] Shadow stack CHANGES between states (not same for all)

### Typography (MEDIUM)

- [ ] Labels use silkscreen (`rgba(255,255,255,0.06)` + `text-shadow`) or engraved (clip + gradient)
- [ ] Every CSS effect maps to a physical phenomenon (shadow=depth, gradient=curvature, highlight=reflection)

### Accessibility & Performance (MEDIUM)

- [ ] Contrast ratio OK for all text
- [ ] `focus-visible` present on all interactive elements
- [ ] Touch targets >= 44px
- [ ] `prefers-reduced-motion` respected
- [ ] `will-change` on animated elements
- [ ] `pointer-events-none` on texture overlays
- [ ] No `filter: blur()` in animations (use `opacity` + `transform` only)

---

## Anti-Patterns (Do / Don't)

| BAD | WHY | GOOD |
|-----|-----|------|
| 2-3 layer box-shadow | = flat design, no physical depth | 5-15 layers, graduated blur |
| Screws on a flat surface | Screws without depth = decorative contradiction | Build depth FIRST, add screws on top |
| Pure white highlights `rgba(255,255,255,0.3)` | Looks blafard/washed-out, unnatural | Warm `rgba(255,240,220,0.2)` or amber |
| Same box-shadow for rest/hover/active | No physical feedback, button feels dead | Different stacks per state (Step 6) |
| `filter: blur()` in animation | Performance killer, causes repaint | `opacity` + `transform` only |
| Multiple light directions | Physically impossible, breaks realism | Single source 135deg everywhere |
| Inventing a shadow stack | Inconsistent, likely too shallow | Copy-adapt from golden-examples |
| Hardware BEFORE depth | Cosmetic, not structural | Assembly order: depth layers first |
| Light mixed with shadow in one confused stack | Muddy, unrealistic surfaces | Dark for depth, warm for specular — separate |
| `rgba(255,255,255,0.5)` edge catch | Glowing white line, not realistic | `rgba(255,255,255,0.08)` max for edges |

---

## Reference Files (12 + 2 HTML assets)

**ALWAYS start with `00-golden-examples.md`** — it has the Lookup Table to find component patterns.

| File | Content | Lines | Search? |
|------|---------|-------|---------|
| `00-golden-examples.md` | **START HERE** — Shadow stacks, button/card/CRT, Lookup Table, Palette | ~540 | Read full |
| `01-shadows-materials-textures.md` | 16 material gradients (chrome, leather, wood, rubber...) | 321 | Read full |
| `02-hardware-animation-neumorphism.md` | Screws, vents, rivets, 8 animations, neumorphism | 166 | Read full |
| `03-blueprints-performance-palettes.md` | 14 component blueprints, performance rules, 6 palettes | 130 | Read full |
| `04-community-techniques.md` | 102 community patterns (14.1-14.102) | **8671** | **SEARCH ONLY** |
| `05-physics-composition-interaction-typography.md` | Light physics, sphere/cylinder/flat lighting | 258 | Read full |
| `06-aging-safety-tokens-palettes.md` | Aging/patina, safety colors, design tokens | 160 | Read full |
| `07-glass-effects.md` | 10 glass techniques (frosted, dark glass, sphere) | 1163 | Read or search |
| `08-metal-effects.md` | 8 metal techniques (brushed, chrome, gold, conic) | 690 | Read or search |
| `09-rim-light-effects.md` | 5 rim light techniques with 4-layer system | 459 | Read or search |
| `10-particle-effects.md` | 10 particle systems (CSS, Canvas, WebGL, fire) | 877 | Read or search |
| `11-retro-industrial-patterns.md` | Bezel, CRT, LED, screw, texture, counter | **5392** | **SEARCH ONLY** |

### HTML Assets

| File | Content | Use |
|------|---------|-----|
| `assets/agile-tech-skeuomorphic-site.html` | 8000-line production site, 15+ button variants | Search for patterns |
| `assets/codepen-deep-screen.html` | 31-layer ultra shadow stack | Gold standard for depth |

### Searching References

Use the BM25 search engine for efficient pattern discovery:

```bash
# Cross-file search (all 14 sources)
python3 scripts/search.py "button shadow"

# Targeted file search (for 04 or 11)
python3 scripts/search.py "CRT bezel" --file 11

# Code blocks only (skip prose)
python3 scripts/search.py "knob gradient" --code-only -n 5

# Limited preview
python3 scripts/search.py "rim light" --context 5
```

Common search terms: `button`, `shadow`, `CRT`, `knob`, `glass`, `metal`, `rim light`, `LED`, `bezel`, `screw`, `gauge`, `meter`, `panel`, `switch`, `dial`
