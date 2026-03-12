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
| 0 | **Context Scan & Decision** | **BLOCKING** | Random style choices, wrong button tier, no page coherence |
| 1 | Shadow Depth | CRITICAL | Flat design disguised as skeuomorphic |
| 2 | Drop Shadows = BLACK ONLY | CRITICAL | Bizarre colored shadows underneath elements |
| 3 | Contrast Separation | CRITICAL | Dark-on-dark: containers and cards melting together |
| 4 | Light/Shadow Separation | CRITICAL | Confused, muddy, unrealistic surfaces |
| 5 | Warm Highlights | CRITICAL | Blafard/washed-out industrial components |
| 6 | Typography & Readability | HIGH | Illegible tiny text, unreadable labels |
| 7 | Assembly Order | HIGH | Decorative screws on flat surfaces |
| 8 | Interaction States | HIGH | Dead buttons with no physical feedback |
| 9 | Physical Naming | HIGH | Generic components without identity |
| 10 | Creative Variety | HIGH | Always the same style, no personality |
| 11 | Accessibility | MEDIUM | Unusable components despite visual quality |
| 12 | Performance | MEDIUM | Janky animations, layout thrash |

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

Determine WHAT the component is and its ROLE on the page:

#### Button Decision Matrix

| Role | Visual weight | Shadow tier | Gradient | Size | When to use |
|------|--------------|-------------|----------|------|-------------|
| **CTA / Hero** | Maximum — eye-catching, unique color | Advanced (8+) | Bold themed gradient + shimmer/LED | Large (48-56px height, 16px+ padding) | 1 per page max. Primary conversion action |
| **Primary action** | High — solid, visible | Standard (5+) | Surface gradient matching page accent | Medium (40-44px height) | Main actions: Save, Submit, Confirm |
| **Secondary action** | Medium — understated solid | Standard (5) | Subtle surface gradient | Medium (36-40px) | Alternative actions: Cancel, Back, Edit |
| **Tertiary / Ghost** | Low — border only, no fill | Minimal (2-3 inset) | None — transparent with border | Small-Medium (32-40px) | Minor actions: filters, toggles, options |
| **Destructive** | High — danger color | Standard (5+) | Red gradient `#4a1010 → #2a0808` | Medium (40-44px) | Delete, Remove, Reset |
| **Navigation** | Low — text-like | None or minimal | None | Inline | Links, breadcrumbs, pagination |

#### Container Decision Matrix

| Role | Background | Shadow type | Borders | When to use |
|------|-----------|-------------|---------|-------------|
| **Page section well** | `#08-#0e` (darkest) | Inset 4-6 layers | Subtle top border `rgba(255,255,255,0.04)` | Grouping related content |
| **Card (floating)** | `#1c-#28` (lighter than well) | Drop shadow Standard 5+ | Top/left bevel, bottom/right dark | Individual items inside wells |
| **Nested card** | `#14-#1c` (between well and card) | Drop shadow 3-5 layers | Subtle border | Sub-items inside cards |
| **Modal / overlay** | `#1a-#22` | Hero 11+ (max drama) | Strong bevel all sides | Overlays, dialogs, important panels |
| **Header / toolbar** | Match page bg or slightly lighter | Standard 5 bottom shadow | Bottom border only | Navigation, controls |

#### Special Elements

| Type | Shadow tier | Reference file | Notes |
|------|------------|---------------|-------|
| Gauge / meter | Advanced 8+ | `01-shadows-materials` | Circular gradient, rim light |
| CRT display | Hero 11+ or Ultra 31 | `11-retro-industrial` | Phosphor glow, scanlines |
| Toggle / switch | Standard 5 | `02-hardware-animation` | Track recess + thumb raised |
| Knob / dial | Advanced 8+ | `08-metal-effects` | Conic gradient, pointer |
| LED indicator | Standard 5 | `11-retro-industrial` | Radial gradient, pulse animation |

### Phase 3 — ASK before choosing (MANDATORY)

**If the style choice is not obvious from context, ASK the user.** Present options based on the scan.

**When to ask:**

| Situation | Question format |
|-----------|----------------|
| New button, no clear role | "This button could be: (A) Primary action [amber gradient], (B) CTA hero [themed, with effects], (C) Ghost/subtle. Which fits?" |
| New section, ambiguous hierarchy | "This section should be: (A) A well/recess [dark, cards float inside], (B) A card panel [raised, lighter]. Which one?" |
| Page has no established theme | "No theme detected. I propose: (A) Warm industrial [amber], (B) Cool steel [blue-grey], (C) [other based on context]. Which direction?" |
| Multiple button styles already exist | "The page already has [X] and [Y] button styles. This new button should: (A) Match the primary style, (B) Be a different tier [explain why], (C) Something new [propose]" |
| Building something that will be prominent | "This [component] will be visually prominent. I suggest [specific style + reasoning]. OK, or do you prefer something else?" |

**When NOT to ask (just adapt):**

- Page has a clear established theme → match it
- Component role is unambiguous (e.g., "add a save button" → primary action, match existing accent)
- User explicitly stated the style they want
- It's a standard card inside an existing well → match sibling cards

### Phase 3b — CONSISTENCY CHECK

After deciding on a style, verify it doesn't clash:

1. **Same role = same style** — If 3 primary buttons exist with amber gradient, the 4th must match
2. **Hierarchy must be readable** — A new element can't be brighter than the element above it in the hierarchy
3. **Accent colors limited** — Max 2 accent colors per page. A third needs explicit user approval
4. **New theme on existing page = ASK** — Never introduce a new theme family without confirmation

---

## STEP 1 — FIND THE RIGHT PATTERN

### Using the Search Engine (for files 04, 11, and cross-file searches)

```bash
# Search all 13 reference files + 13 HTML assets
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

The search engine indexes 2400+ sections across all 26 source files (13 references + 13 HTML assets) using BM25 ranking. Use it instead of reading large files (04 = 8671 lines, 11 = 5392 lines).

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

| Element | Brightness range | Example |
|---------|-----------------|---------|
| **Well/recess container** | Very dark: `#08-#10` | `#0e0e0e`, `#0a0a0a` |
| **Card floating inside** | Lighter: `#1c-#28` | `#242424`, `#252525` |
| **Minimum delta** | >= `#12` hex difference | Container `#0e` → Card `#22` = `#14` delta |

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
  inset 0 3px 8px rgba(0,0,0,0.6),     /* gorge top — light blocked */
  inset 0 -3px 5px rgba(0,0,0,0.5),    /* gorge bottom — ambient occlusion */
  inset 3px 0 6px rgba(0,0,0,0.55),    /* gorge left wall */
  inset -3px 0 6px rgba(0,0,0,0.55),   /* gorge right wall */
  0 2px 4px rgba(0,0,0,0.4),           /* close drop shadow — BLACK */
  0 4px 8px rgba(0,0,0,0.3),           /* mid depth — BLACK */
  0 8px 16px rgba(0,0,0,0.25),         /* far depth — BLACK */
  0 16px 32px rgba(0,0,0,0.15);        /* ambient floor shadow — BLACK */
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
Detailed versions with L/S annotations: `references/00-golden-examples.md` section 1.

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
  0 16px 32px rgba(0,0,0,0.15)
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

## STEP 6b — TYPOGRAPHY & READABILITY (Priority 6)

Skeuomorphic does NOT mean tiny. Text must be readable. Apply these MINIMUM font sizes:

| Element | Minimum | Recommended | Font |
|---------|---------|-------------|------|
| **Body text / descriptions** | 13px | 14-16px | mono or sans-serif |
| **Card titles / zone names** | 14px | 14-16px | Orbitron or mono, 700 weight |
| **Section headers** | 13px | 14px | Orbitron uppercase, letter-spacing 0.08-0.1em |
| **Sub-labels / captions** | 11px | 12px | mono, lighter opacity |
| **Badges / tags** | 10px | 11px | mono, uppercase |
| **CRT readout values** | 13px | 14px | mono, amber/accent color |
| **Button labels** | 13px | 14px | Orbitron, 700, uppercase |

**NEVER go below 10px for ANY text.** If text needs to be de-emphasized, reduce opacity (0.4-0.6) instead of shrinking font size.

**Text opacity for readability:**

| Purpose | Minimum opacity | Why |
|---------|----------------|-----|
| Primary text (titles, labels) | 0.85 | Must be immediately readable |
| Secondary text (descriptions) | 0.5 | Readable on inspection |
| Tertiary text (captions, meta) | 0.35 | Visible but not competing |

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

| Theme | Surface gradient | Accent | Inset highlight | Text |
|-------|-----------------|--------|-----------------|------|
| Warm industrial | `#1e1e1e → #141414` | `hsl(35 100% 60%)` amber | `rgba(255,240,220,0.12)` | `rgba(255,240,220,0.9)` |
| Cool steel | `#1a1c20 → #12141a` | `hsl(210 70% 60%)` blue | `rgba(180,200,255,0.10)` | `rgba(200,220,255,0.9)` |
| Deep purple | `#2d1854 → #150b28` | `hsl(270 100% 70%)` violet | `rgba(200,160,255,0.12)` | `rgba(220,200,255,0.95)` |
| Military | `#1a1e14 → #10140c` | `hsl(0 70% 55%)` red | `rgba(180,200,150,0.08)` | `rgba(180,200,150,0.85)` |
| Vintage audio | `#2a2218 → #1a1610` | `hsl(30 80% 55%)` copper | `rgba(255,220,180,0.10)` | `rgba(240,220,190,0.9)` |
| CRT terminal | `#0a0f0a → #050805` | `hsl(120 100% 50%)` green | `rgba(0,255,60,0.06)` | `rgba(0,255,60,0.85)` |

**IMPORTANT**: Regardless of theme, drop shadows remain BLACK `rgba(0,0,0,...)`. Only `inset` highlights and text/accent colors change with theme.

### When to propose variety:

- User asks for a "button" or "card" without specifying style → propose 2-3 theme options
- Building a new page section → ask if it should match existing theme or contrast
- User says "something different" or "more personality" → explore non-default themes
- Same component requested multiple times → vary the approach each time

---

## STEP 7 — VERIFY (Pre-Delivery Gate)

### Context Scan (BLOCKING — must be done FIRST)

- [ ] Page was READ before any styling began (Step 0.5 Phase 1)
- [ ] Existing palette, button styles, and container hierarchy were identified
- [ ] Component role was classified using Decision Matrix (Step 0.5 Phase 2)
- [ ] User was ASKED before choosing style (if ambiguous) or choice was justified by existing siblings
- [ ] Max 2 accent colors on the page — no 3rd accent introduced without approval
- [ ] New component matches sibling components of same role

### Depth Quality (CRITICAL)

- [ ] Shadow layer count: Standard >= 5, Advanced >= 8, Hero >= 11. COUNT them.
- [ ] Shadow uses ONLY dark `rgba(0,0,0,...)` for ALL drop shadows (non-inset)
- [ ] NO colored drop shadows: no purple, amber, blue `0 Xpx Ypx rgba(color)` underneath elements
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

### Contrast Separation (CRITICAL)

- [ ] Container/well backgrounds are DARKER than card backgrounds (>= #12 hex delta)
- [ ] Cards inside dark wells have reinforced top/left borders (opacity >= 0.09)
- [ ] No two nested elements share the same brightness level

### Typography & Readability (HIGH)

- [ ] Body text >= 13px, titles >= 14px, labels >= 12px, NOTHING below 10px
- [ ] Primary text opacity >= 0.85, secondary >= 0.5
- [ ] Labels use silkscreen (`text-shadow`) or engraved (clip + gradient)
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
| Colored drop shadows `rgba(140,80,255,0.2)` | Shadows are absence of light — always black in reality | `rgba(0,0,0,...)` for ALL drop shadows. Color only in `inset` highlights |
| Body text < 13px / titles < 14px | Unreadable on most screens, looks like fine print | Body >= 13px, titles >= 14px, labels >= 11px (see Step 6b) |
| Container and card same brightness (#18 vs #1c) | Everything melts together, no visual hierarchy | Container #08-#10, card #1c-#28, minimum #12 hex delta |
| Always amber-on-dark industrial | Monotonous, every page looks identical | Propose 2-3 themes from the 6 palettes (see Step 6c) |
| Styling without reading the page first | Random choices that clash with existing patterns | STEP 0.5: scan page, extract palette, match hierarchy |
| Choosing button style without asking | Wrong tier: CTA where secondary needed, ghost where primary needed | Use Button Decision Matrix, ask if ambiguous |
| Adding a 3rd accent color silently | Visual chaos, page loses coherence | Max 2 accents per page. Ask before introducing a new one |
| Ignoring existing sibling components | New card looks nothing like the 5 existing cards | Same role = same style. Match siblings first |

---

## Reference Files (13 references + 13 HTML assets)

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
| `12-production-components.md` | 11 production patterns: button, dashboard, VU, switch, LCD, lever, gauge, alert, CRT, accordion, thermometer | ~500 | Read or search |

### HTML Assets — Quick Lookup

| Need | File | Search key | Key patterns |
|------|------|-----------|--------------|
| Push button with LED | `power-button.html` | `power-button` | 17-layer button, glow slot, Phillips screws |
| Dashboard / analytics | `synthscore-analytics.html` | `synthscore` | Gradient bar, metallic border, tech brackets |
| VU meter / gauge | `tube-compressor-vu.html` | `vu-meter` | 16-layer well, 5-layer glass, animated needle |
| Toggle switch | `skeuomorphic-switch.html` | `switch` | Recessed track, grip handle, LED indicators |
| LCD numeric display | `lcd-db-display.html` | `lcd` | Olive screen, scanlines, Digital-7 font |
| Rotary lever / knob | `industrial-lever.html` | `lever` | 11-layer knob, SVG screws, CSS-only checkbox |
| Score gauge / radial | `credit-score-gauge.html` | `gauge` | SVG arc, 16-layer chassis, brushed metal |
| Alert / warning panel | `autochord-alert-panel.html` | `alert` | Dome icon, red glow, perforated backplate |
| CRT danger screen | `deep-screen-phosphor.html` | `phosphor` | Red phosphor, 31-layer chassis hole, breathing anim |
| Folding / accordion | `folding-header.html` | `folding` | Collapsible, glowing icon, neomorphic well |
| Horizontal bar meter | `horizontal-thermometer.html` | `thermometer` | Glass bulb, recessed tube, color-reactive fill |
| Deep CRT (31 layers) | `codepen-deep-screen.html` | `deep-screen` | Ultra shadow stack gold standard |
| Full page (15+ buttons) | `agile-tech-skeuomorphic-site.html` | `site` | Multiple button tiers, full layout |

All files in `assets/`. Detailed breakdowns: `references/12-production-components.md`

### Searching References

Use the BM25 search engine for efficient pattern discovery:

```bash
# Cross-file search (all 26 sources)
python3 scripts/search.py "button shadow"

# Targeted file search (for 04 or 11)
python3 scripts/search.py "CRT bezel" --file 11

# Code blocks only (skip prose)
python3 scripts/search.py "knob gradient" --code-only -n 5

# Limited preview
python3 scripts/search.py "rim light" --context 5
```

Common search terms: `button`, `shadow`, `CRT`, `knob`, `glass`, `metal`, `rim light`, `LED`, `bezel`, `screw`, `gauge`, `meter`, `panel`, `switch`, `dial`, `lever`, `LCD`, `VU`, `dashboard`, `toggle`, `alert`, `phosphor`, `thermometer`, `folding`, `accordion`, `dome`, `bulb`, `arc`, `score`
