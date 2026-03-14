---
name: skeuomorphic-forge
description: "Build physically-realistic skeuomorphic UI with Tailwind CSS. Covers buttons, panels, gauges, knobs, CRT/LED displays, glass/metal effects, particle systems, and industrial hardware. Provides shadow stacks, material textures, lighting rules, and construction blueprints. Triggers on: skeuomorphic, realistic depth, industrial UI, 3D button, gauge, meter, analog, tactile, material texture, retro-industrial, aerospace panel, DSP cockpit. Do NOT trigger for flat/minimal UI or standard Material/Shadcn components."
---

# Skeuomorphic Forge

Build physically-realistic UI components using Tailwind CSS + inline styles. Every component MUST look like a real physical object — machined metal, CRT glass, brushed aluminum — not a flat div with a drop shadow.

---

## PROJECT INTEGRATION — Living References in the Codebase

**Before building any new component, consult the Phase 0 industrial library** at `components/industrial/`. These 9 extracted components are the gold standard for this project — production-proven, style-consistent, and battle-tested.

| Component               | Physical Object                                           | Key Techniques                                                                       |
| ----------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **SteelMountPlate**     | Machined aluminum mounting bracket with 4 torx screws     | 5-layer boxShadow, radial gradient screws, repeating-linear-gradient brushed texture |
| **PlasmaProgressBar**   | Gas discharge fill indicator with glass knob              | SVG feTurbulence animation, 4-stop dynamic color, backdrop-filter glass knob         |
| **SkeuomorphicSwitch**  | Aluminum toggle with amber trail glow + brushed knob      | 8-layer conic gradient housing, 8 trail bloom layers, 6+ inset gorge shadows        |
| **SkeuomorphicStatCard**| 3-ring bezel CRT-like readout with color-coded digits     | 8+ inset shadows per ring, 2 specular sweeps, scanline overlay                      |
| **DiagnosticCard**      | Severity-variant alert card (info/warning/critical)       | CSS class contract in `electrical-soviet.css`                                        |
| **SkeuomorphicCounter** | Mechanical rolling counter with 3-ring bezel + 4 screws   | 10-layer boxShadow, 3-ring assembly, torx screws, glass overlay, scanlines          |
| **IndustrialInput**     | Number input field with glitch/hologram FX                | CSS class contract (`.holo-input`, `.glitch-input-wrapper`)                          |
| **StatusDisplay**       | CRT-style status readout with bezel + scanlines + glass   | Scanline repeating-linear-gradient, 2-layer glass reflection, edge specular          |
| **IndustrialSelect**    | Dropdown select with glitch styling                       | CSS class contract (`.holo-input.holo-select`)                                       |

**Usage rule**: When building a component similar to one above, READ the existing component first and match its patterns. Import from `@/components/industrial/` (barrel `index.ts`) when possible.

### CSS INLINE RULE (PROJECT-SPECIFIC — CRITICAL)

In this project, **Prettier/format-on-save reformats CSS files** (including `neo-components.css`). Any visual override written in CSS classes gets reverted on save or build.

**Solution**: Apply ALL visual overrides via **inline `style={{}}`** in TSX components. CSS classes serve as structural base only (layout, display, transitions). This is documented in `.cursor/rules/10-linter-reverts-design-changes.mdc`.

```tsx
// CORRECT — visual overrides inline, Prettier cannot touch them
<div
  className="neo-card" // structural only
  style={{
    background: "linear-gradient(145deg, #1e1e1e 0%, #121212 100%)",
    boxShadow: `inset 0 1px 0 rgba(255,255,255,0.05), 0 2px 4px rgba(0,0,0,0.4), 0 8px 16px rgba(0,0,0,0.3)`,
    borderTop: "1px solid rgba(255,255,255,0.09)",
  }}
>

// WRONG — visual overrides in CSS class (Prettier will reformat/lose them)
.my-custom-card { box-shadow: ...; background: ...; }
```

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

Determine WHAT the component is and its ROLE on the page:

#### Button Decision Matrix

| Role                 | Visual weight                        | Shadow tier         | Gradient                              | Size                                  | When to use                               |
| -------------------- | ------------------------------------ | ------------------- | ------------------------------------- | ------------------------------------- | ----------------------------------------- |
| **CTA / Hero**       | Maximum — eye-catching, unique color | Advanced (8+)       | Bold themed gradient + shimmer/LED    | Large (48-56px height, 16px+ padding) | 1 per page max. Primary conversion action |
| **Primary action**   | High — solid, visible                | Standard (5+)       | Surface gradient matching page accent | Medium (40-44px height)               | Main actions: Save, Submit, Confirm       |
| **Secondary action** | Medium — understated solid           | Standard (5)        | Subtle surface gradient               | Medium (36-40px)                      | Alternative actions: Cancel, Back, Edit   |
| **Tertiary / Ghost** | Low — border only, no fill           | Minimal (2-3 inset) | None — transparent with border        | Small-Medium (32-40px)                | Minor actions: filters, toggles, options  |
| **Destructive**      | High — danger color                  | Standard (5+)       | Red gradient `#4a1010 → #2a0808`      | Medium (40-44px)                      | Delete, Remove, Reset                     |
| **Navigation**       | Low — text-like                      | None or minimal     | None                                  | Inline                                | Links, breadcrumbs, pagination            |

#### Container Decision Matrix

| Role                  | Background                        | Shadow type              | Borders                                    | When to use                         |
| --------------------- | --------------------------------- | ------------------------ | ------------------------------------------ | ----------------------------------- |
| **Page section well** | `#08-#0e` (darkest)               | Inset 4-6 layers         | Subtle top border `rgba(255,255,255,0.04)` | Grouping related content            |
| **Card (floating)**   | `#1c-#28` (lighter than well)     | Drop shadow Standard 5+  | Top/left bevel, bottom/right dark          | Individual items inside wells       |
| **Nested card**       | `#14-#1c` (between well and card) | Drop shadow 3-5 layers   | Subtle border                              | Sub-items inside cards              |
| **Modal / overlay**   | `#1a-#22`                         | Hero 11+ (max drama)     | Strong bevel all sides                     | Overlays, dialogs, important panels |
| **Header / toolbar**  | Match page bg or slightly lighter | Standard 5 bottom shadow | Bottom border only                         | Navigation, controls                |

#### PHYSICAL SIZE RULE — Cards as Hardware Panels

A skeuomorphic card represents a physical device (screen, gauge, instrument panel). Physical devices have FIXED dimensions — a CRT screen doesn't shrink when it shows less text.

**When rendering multiple instances of the same component** (e.g., 3 status cards with different states), ALL instances MUST have identical dimensions. Use explicit `width` + `height` (or `minWidth` + `minHeight`) in the container style.

```tsx
// CORRECT — fixed dimensions, content fills the space
<div style={{ width: 320, height: 280, overflow: "hidden" }}>
  {/* content adapts inside fixed frame */}
</div>

// WRONG — card shrinks/grows with content
<div style={{ padding: 16 }}>
  {/* variable height = not a physical device */}
</div>
```

**When rendering multiple variants** (e.g., 3 status cards: connected/disconnected/connecting), determine the dimensions from the variant with the MOST content. All other variants use the same dimensions — empty space stays empty, the chassis doesn't shrink.

**Disabled/inactive states** must also have the SAME dimensions as active states. A physical button doesn't get smaller when it's off.

**Content centering rule**: The main content (input, readout, display) must be visually CENTERED in the chassis. Labels and silkscreen marks are secondary — they don't push the primary content to the bottom or side. Use `display: flex; align-items: center; justify-content: center` on the chassis, with labels positioned absolutely or in thin header/footer zones. A frequency input with "3000 Hz" shoved to the bottom of a tall panel looks wrong — center it.

**When to apply**: any card/panel that represents a physical device, any button with active/disabled states. Not applicable to layout containers or flowing content.

#### Special Elements

| Type            | Shadow tier          | Reference file          | Notes                            |
| --------------- | -------------------- | ----------------------- | -------------------------------- |
| Gauge / meter   | Advanced 8+          | `01-shadows-materials`  | Circular gradient, rim light     |
| CRT display     | Hero 11+ or Ultra 31 | `11-retro-industrial`   | Phosphor glow, scanlines         |
| Toggle / switch | Standard 5           | `02-hardware-animation` | Track recess + thumb raised      |
| Knob / dial     | Advanced 8+          | `08-metal-effects`      | Conic gradient, pointer          |
| LED indicator   | Standard 5           | `11-retro-industrial`   | Radial gradient, pulse animation |

### Phase 3 — ASK before choosing (MANDATORY)

**If the style choice is not obvious from context, ASK the user.** Present options based on the scan.

**When to ask:**

| Situation                                 | Question format                                                                                                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New button, no clear role                 | "This button could be: (A) Primary action [amber gradient], (B) CTA hero [themed, with effects], (C) Ghost/subtle. Which fits?"                                           |
| New section, ambiguous hierarchy          | "This section should be: (A) A well/recess [dark, cards float inside], (B) A card panel [raised, lighter]. Which one?"                                                    |
| Page has no established theme             | "No theme detected. I propose: (A) Warm industrial [amber], (B) Cool steel [blue-grey], (C) [other based on context]. Which direction?"                                   |
| Multiple button styles already exist      | "The page already has [X] and [Y] button styles. This new button should: (A) Match the primary style, (B) Be a different tier [explain why], (C) Something new [propose]" |
| Building something that will be prominent | "This [component] will be visually prominent. I suggest [specific style + reasoning]. OK, or do you prefer something else?"                                               |

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
# Search all 16 reference files + 13 HTML assets
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

The search engine indexes 2600+ sections across all 29 source files (16 references + 13 HTML assets) using BM25 ranking. Use it instead of reading large files (04 = 8671 lines, 11 = 5392 lines).

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

/* LIGHT — bevel edges (warm tint, not pure white) */
border-top: 1px solid rgba(255, 250, 240, 0.08);
border-left: 1px solid rgba(255, 250, 240, 0.04);
border-bottom: 1px solid rgba(0, 0, 0, 0.3);
border-right: 1px solid rgba(0, 0, 0, 0.2);
```

### WARM light, not blafard white

Real light sources are warm (tungsten, halogen, ambient workshop lighting). Pure white `rgba(255,255,255)` at any visible opacity looks clinical and wrong on industrial surfaces. This is the #1 systematic failure in benchmarks — agents default to pure white for glass overlays, specular hotspots, and rim lights even when told not to. The fix is simple: **swap the 255,255,255 for 255,240,220** (warm) or **255,245,235** (neutral-warm) whenever opacity > 0.10.

| Purpose             | Color                      | Max opacity | When                            |
| ------------------- | -------------------------- | ----------- | ------------------------------- |
| Edge catch (subtle) | `rgba(255,255,255,...)`    | **0.08**    | box-shadow inset, every surface |
| Top bevel highlight | `rgba(255,250,240,...)`    | **0.12**    | border-top/left facing light    |
| Specular hotspot    | `rgba(255,240,220,...)`    | 0.25        | `::before` on curved surfaces   |
| Glass reflection    | `rgba(255,245,235,...)`    | 0.20        | `::before/::after` overlays     |
| Rim light (pseudo)  | `rgba(255,240,220,0.20)`  | 0.20        | radial-gradient, top edge       |
| Active glow         | `rgba(255,180,60,...)`     | 0.40        | Active/on states, LEDs          |
| CRT/LED emission    | `hsl(35 100% 60%)`        | Full color  | Display elements                |

**The rule**: if the opacity is above 0.10, the color MUST be warm (`r=255, g<=245, b<=235`), never pure `255,255,255`. Pure white is only acceptable at extremely low opacity (0.03-0.08) where the warmth is imperceptible.

```javascript
// WRONG — pure white glass overlay at visible opacity
"::before": { background: "radial-gradient(..., rgba(255,255,255,0.25), ...)" }

// CORRECT — warm-tinted glass overlay
"::before": { background: "radial-gradient(..., rgba(255,240,220,0.20), ...)" }

// WRONG — pure white rim light
background: "radial-gradient(ellipse, rgba(255,255,255,0.25) 0%, transparent 70%)"

// CORRECT — warm rim light
background: "radial-gradient(ellipse, rgba(255,240,220,0.20) 0%, transparent 70%)"
```

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

### 3d. SCREWS — Placement rules and quality (BENCHMARK FAILURE — READ CAREFULLY)

**Screws go on METAL only. Never on glass, screens, or display surfaces.** In real hardware, screws fasten metal panels together. A screw on a glass CRT face or screen bezel is physically impossible and looks absurd. If the component has both a metal chassis and a glass display, the screws go on the chassis/bezel frame — never on or over the glass.

**Screw quality matters.** The existing Phase 0 components (`SteelMountPlate`, `SkeuomorphicCounter`) set the quality bar. Copy from them, not from memory. Each screw needs:

```javascript
// CORRECT — High-quality torx screw (from SteelMountPlate)
// 1. Sphere body: radial gradient with specular hotspot at 32% 26% (consistent 135deg light)
background: "radial-gradient(circle at 32% 26%, rgba(255,240,220,0.25) 0%, #3a3a3a 25%, #252525 60%, #1a1a1a 100%)"
// 2. 7-layer shadow for REAL depth (screws sit ON the surface, they need pronounced shadows):
boxShadow: `
  inset 0 1px 0 rgba(255,240,220,0.08),
  inset 0 -1px 2px rgba(0,0,0,0.7),
  0 1px 1px rgba(0,0,0,0.6),
  0 1px 3px rgba(0,0,0,0.5),
  0 2px 4px rgba(0,0,0,0.4),
  0 3px 6px rgba(0,0,0,0.25),
  0 4px 8px rgba(0,0,0,0.15)
`
// 3. Torx/Phillips slot: inner div with cross shape or rotated lines, NOT just a border
// 4. Size PROPORTIONAL to chassis: 10-12px on small panels, 12-16px on large panels
```

**Screw size rule**: screws must be proportional to the chassis they sit on. A 16px screw on a 200px-wide panel looks like a bolt on a watch. Rule of thumb: screw diameter = ~3-4% of the panel's shortest dimension. A 320px panel → 10-12px screws. A 500px panel → 14-16px screws.

**FORBIDDEN**: Flat circle with a single inset shadow as "screw". Single-color dot. Screw on glass/screen area. Screw without shadow depth. Oversized screws (>20px or >5% of panel width).

**Placement**: 4 corners of rectangular metal panels. All screws must have the SAME quality. Vary torx slot rotation angle per screw (45, 135, 225, 315deg) for realism.

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
  inset 0 1px 0 rgba(255,240,220,0.25),
  inset 0 -1px 0 rgba(0,0,0,0.8),
  inset 1px 0 1px rgba(255,240,220,0.1),
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

EVERY interactive element needs ALL of these. Use React state + Tailwind classes + inline style overrides:

```tsx
// Define shadow stacks as constants (keeps JSX clean)
const REST_SHADOW = `
  inset 0 1px 0 rgba(255,255,255,0.05),
  inset 0 -1px 0 rgba(0,0,0,0.3),
  0 2px 4px rgba(0,0,0,0.4),
  0 8px 16px rgba(0,0,0,0.3),
  0 16px 32px rgba(0,0,0,0.2)
`;
const HOVER_SHADOW = `
  inset 0 1px 0 rgba(255,255,255,0.10),
  inset 0 -1px 0 rgba(0,0,0,0.3),
  0 4px 6px rgba(0,0,0,0.45),
  0 10px 20px rgba(0,0,0,0.35),
  0 20px 40px rgba(0,0,0,0.25)
`;
const ACTIVE_SHADOW = `
  inset 0 2px 4px rgba(0,0,0,0.5),
  inset 0 1px 1px rgba(0,0,0,0.3),
  0 1px 2px rgba(0,0,0,0.3)
`;

// In JSX — use Tailwind for base states, inline style for shadow stacks
<button
  className={cn(
    "transition-all duration-150",
    "hover:-translate-y-px",               // Hover — lift
    "active:translate-y-px",               // Active — depress
    "disabled:opacity-50 disabled:saturate-[0.3] disabled:pointer-events-none",
    "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-amber-500",
  )}
  style={{
    boxShadow: isActive ? ACTIVE_SHADOW : isHovered ? HOVER_SHADOW : REST_SHADOW,
    background: "linear-gradient(145deg, #2a2a2a 0%, #1a1a1a 100%)",
    borderTop: "1px solid rgba(255,255,255,0.08)",
  }}
  onMouseEnter={() => setIsHovered(true)}
  onMouseLeave={() => { setIsHovered(false); setIsActive(false); }}
  onMouseDown={() => setIsActive(true)}
  onMouseUp={() => setIsActive(false)}
>
```

**Why React state for shadows?** Tailwind `hover:` cannot express multi-layer boxShadow changes. Use `onMouseEnter/Leave/Down/Up` to swap the full shadow stack via inline style. Tailwind handles `translate`, `opacity`, `outline`.

### Input Focus Animations (BENCHMARK FAILURE — not just a cursor)

When an input field gets focus, a plain blinking cursor is not enough for skeuomorphic design. The input recess should come ALIVE — like powering on a VFD/CRT display. Add light animation effects on focus:

```javascript
// On focus, the recess well intensifies:
const WELL_FOCUSED = {
  // 1. Color bleed intensifies (inset shadow, NOT border — borders stay neutral warm or none)
  boxShadow: `
    ${REST_INSET_SHADOWS},
    inset 4px 0 10px rgba(255,180,60,0.08),  // amber bleed DOUBLED from 0.04 at rest
    inset 0 0 12px rgba(255,180,60,0.04),     // NEW — warm ambient from display powering up
    inset 0 0 24px rgba(255,180,60,0.02)      // NEW — wider ambient bloom
  `,

  // 2. Text glow intensifies
  textShadow: "0 0 8px rgba(255,180,60,0.6), 0 0 16px rgba(255,180,60,0.3)",

  // 3. Transition for smooth power-on feel
  transition: "all 0.3s ease",
};
```

This simulates the physical behavior of a VFD display brightening when activated. The entire recess responds to input, not just the text cursor. Apply similar logic to any interactive display element (not just inputs).

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

This checklist is aligned with **CLAUDE.md §C Design Gate U1-U8**. A component that fails this gate MUST NOT be delivered.

### U0 — Context Scan (BLOCKING — must be done FIRST)

- [ ] Page was READ before any styling began (Step 0.5 Phase 1)
- [ ] Existing palette, button styles, and container hierarchy were identified
- [ ] Component role was classified using Decision Matrix (Step 0.5 Phase 2)
- [ ] User was ASKED before choosing style (if ambiguous) or choice was justified by existing siblings
- [ ] Max 2 accent colors on the page — no 3rd accent introduced without approval
- [ ] New component matches sibling components of same role
- [ ] Phase 0 components in `components/industrial/` were consulted as reference
- [ ] Visual overrides applied via inline `style={{}}`, NOT CSS classes (Prettier rule)

### U1 — Shadow Depth (CRITICAL)

- [ ] Shadow layer count: Standard >= 5, Advanced >= 8, Hero >= 11. COUNT them.
- [ ] Shadow uses ONLY dark `rgba(0,0,0,...)` for ALL drop shadows (non-inset)
- [ ] NO colored drop shadows: no purple, amber, blue `0 Xpx Ypx rgba(color)` underneath elements
- [ ] Graduated blur progression: near shadows tight (2-4px), far shadows wide (16-32px)
- [ ] Started from golden-example, reference pattern, or Phase 0 component — NOT invented

### U2 — Light Source Consistency (CRITICAL)

- [ ] Single light direction (135deg) consistent across ALL components on the page
- [ ] Light and shadow are SEPARATE systems (not mixed in one confused stack)
- [ ] No pure white above 0.10: every `rgba(255,255,255,X)` with X>0.10 must be swapped to `rgba(255,240,220,X)` or warmer
- [ ] Edge catches at opacity 0.03-0.08 only. Glass/specular overlays max 0.20 with warm tint
- [ ] Surface gradient present for curvature (`linear-gradient(145deg, ...)`)

### U3 — 4-Layer Construction (HIGH)

- [ ] Physical object named explicitly ("machined aluminum", "Bakelite switch")
- [ ] 4-layer construction present: Chassis + Depth + Lighting + Detail
- [ ] Assembly order respected: depth BEFORE hardware
- [ ] Screws/rivets sit ON a surface with depth, not on flat div

### U4 — Hardware Placement (HIGH)

- [ ] Hardware placement realistic (screws at 4 corners if rectangle)
- [ ] Hardware uses radial gradients for beveled sphere effect (see SteelMountPlate)
- [ ] Torx/Phillips slots oriented consistently

### U5 — Interaction States (HIGH)

- [ ] hover, active, disabled, focus-visible all implemented
- [ ] Hover lifts (`hover:-translate-y-px`) with expanded shadow via React state
- [ ] Active depresses (`active:translate-y-px`) with compressed shadow
- [ ] Shadow stack CHANGES between states (not same for all)

### U6 — Physical Purpose (HIGH)

- [ ] Every CSS effect maps to a physical phenomenon (shadow=depth, gradient=curvature, highlight=reflection)
- [ ] No decorative-only effects — each layer represents a real physical property

### U7 — Typography as Surface (HIGH)

- [ ] Body text >= 13px, titles >= 14px, labels >= 12px, NOTHING below 10px
- [ ] Primary text opacity >= 0.85, secondary >= 0.5
- [ ] Labels use silkscreen (`text-shadow`) or engraved (clip + gradient) — NOT plain text
- [ ] Typography is a SURFACE treatment, not floating text
- [ ] Embossed/engraved text has enough contrast to be readable (min opacity 0.35 for tertiary, 0.5 for secondary)

### U8 — Accessibility (MEDIUM)

- [ ] WCAG contrast ratio OK for all text
- [ ] `focus-visible` present on all interactive elements
- [ ] Touch targets >= 44px
- [ ] `prefers-reduced-motion` respected
- [ ] `will-change` on animated elements
- [ ] `pointer-events-none` on texture overlays
- [ ] No `filter: blur()` in animations (use `opacity` + `transform` only)

### U9 — Benchmark Lessons (see `references/16-benchmark-lessons.md`)

- [ ] Display wells use inset shadows for depth, NOT borders (§16.13)
- [ ] Display wells have borderRadius: 0 (sharp CRT corners) + overflow: hidden (§16.12)
- [ ] All 5 display well overlays present: glass reflection, left-edge specular, content depth gradient, scanlines, color bleed (§16.17)
- [ ] Device cards have fixed dimensions (same across all variants) (§16.6)
- [ ] Component size proportional to content density (§16.11)
- [ ] Screw spacing >= 8px from any content element (§16.14)
- [ ] No unexplained light bars or glowing lines on chassis (§16.15)
- [ ] Glass reflection overlay present and visible on all display wells (§16.16)
- [ ] Color bleed = inset box-shadow in content color, NOT colored border (§16.1)
- [ ] Emboss labels >= 0.50 primary, >= 0.45 secondary, >= 0.35 tertiary (§16.3)

### Contrast Separation (CRITICAL — cross-cutting)

- [ ] Container/well backgrounds are DARKER than card backgrounds (>= #12 hex delta)
- [ ] Cards inside dark wells have reinforced top/left borders (opacity >= 0.09)
- [ ] No two nested elements share the same brightness level

---

## Anti-Patterns (Do / Don't)

| BAD                                             | WHY                                                                | GOOD                                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| 2-3 layer box-shadow                            | = flat design, no physical depth                                   | 5-15 layers, graduated blur                                              |
| Screws on a flat surface                        | Screws without depth = decorative contradiction                    | Build depth FIRST, add screws on top                                     |
| Screws on glass/screen                          | Physically impossible — screws fasten metal, not glass             | Screws on METAL chassis/bezel only, never on display surface             |
| Low-quality flat-circle screws                  | Single inset shadow ≠ machined screw, looks fake                   | Radial gradient sphere + 5-layer shadow + torx slot (see §3d)            |
| Cards resizing with content                     | Physical device (CRT/gauge) has fixed dimensions                   | Explicit width+height on device cards, content fills fixed frame         |
| Recess without inner rim light                  | Flat dark rectangle instead of machined cavity                     | 1px warm border at recess edge, top brighter than bottom (see §14 addendum) |
| Shallow screen depth (1-3 inset layers)         | Screen looks like a dark div, no sense of physical cavity          | CRT/display recess needs 12+ inset layers + inner rim light             |
| Rim light with glow/blur                        | A reflection is sharp, not diffuse — glow = neon, not machined lip | Clean 1px border only, NO box-shadow bloom around it                     |
| No color bleed from screen content              | Recess looks disconnected from its display content                 | Inner rim picks up display color (amber text → amber rim at 0.06-0.10)   |
| Embossed text too faint (opacity < 0.25)        | Invisible silkscreen/stamped labels, defeats the purpose           | Embossed text min 0.35 opacity (tertiary), 0.5 (secondary)              |
| Button/disabled state different size than active | Physical device doesn't shrink when turned off                     | Same explicit width+height for all states of same component              |
| Decorative rim light without physical reason     | Random glowing line on a button top — why is it there?             | Every light effect needs a physical source (LED slot, edge catch, etc.)  |
| Pure white `rgba(255,255,255,X)` at X>0.10      | Looks blafard/clinical, wrong light temperature on industrial metal | `rgba(255,240,220,X)` or `rgba(255,245,235,X)` — always warm above 0.10 |
| Same box-shadow for rest/hover/active           | No physical feedback, button feels dead                            | Different stacks per state (Step 6)                                      |
| `filter: blur()` in animation                   | Performance killer, causes repaint                                 | `opacity` + `transform` only                                             |
| Multiple light directions                       | Physically impossible, breaks realism                              | Single source 135deg everywhere                                          |
| Inventing a shadow stack                        | Inconsistent, likely too shallow                                   | Copy-adapt from golden-examples                                          |
| Hardware BEFORE depth                           | Cosmetic, not structural                                           | Assembly order: depth layers first                                       |
| Light mixed with shadow in one confused stack   | Muddy, unrealistic surfaces                                        | Dark for depth, warm for specular — separate                             |
| `rgba(255,255,255,0.5)` edge catch              | Glowing white line, not realistic                                  | `rgba(255,255,255,0.08)` max for edges                                   |
| Colored drop shadows `rgba(140,80,255,0.2)`     | Shadows are absence of light — always black in reality             | `rgba(0,0,0,...)` for ALL drop shadows. Color only in `inset` highlights |
| Body text < 13px / titles < 14px                | Unreadable on most screens, looks like fine print                  | Body >= 13px, titles >= 14px, labels >= 11px (see Step 6b)               |
| Container and card same brightness (#18 vs #1c) | Everything melts together, no visual hierarchy                     | Container #08-#10, card #1c-#28, minimum #12 hex delta                   |
| Always amber-on-dark industrial                 | Monotonous, every page looks identical                             | Propose 2-3 themes from the 6 palettes (see Step 6c)                     |
| Styling without reading the page first          | Random choices that clash with existing patterns                   | STEP 0.5: scan page, extract palette, match hierarchy                    |
| Choosing button style without asking            | Wrong tier: CTA where secondary needed, ghost where primary needed | Use Button Decision Matrix, ask if ambiguous                             |
| Adding a 3rd accent color silently              | Visual chaos, page loses coherence                                 | Max 2 accents per page. Ask before introducing a new one                 |
| Ignoring existing sibling components            | New card looks nothing like the 5 existing cards                   | Same role = same style. Match siblings first                             |

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

### Display Well Depth — Inset Shadows Only (NO borders)

For display wells (CRT screens, input recesses), depth comes ONLY from inset box-shadows. Do NOT use borders on display wells — borders make the glass look like it's sticking OUT instead of being recessed IN. See `references/16-benchmark-lessons.md` §16.13 for the full history.

```javascript
const DISPLAY_WELL = {
  background: "linear-gradient(180deg, #050505 0%, #0a0a0a 100%)",
  borderRadius: 0,  // sharp CRT corners
  overflow: "hidden",
  border: "none",   // NO border on display wells
  boxShadow: `
    inset 0 3px 8px rgba(0,0,0,0.7),
    inset 0 -2px 4px rgba(0,0,0,0.4),
    inset 3px 0 6px rgba(0,0,0,0.5),
    inset -3px 0 6px rgba(0,0,0,0.5),
    inset 0 1px 2px rgba(0,0,0,0.8),
    inset 0 6px 12px rgba(0,0,0,0.3),
    inset 0 -1px 0 rgba(255,250,240,0.15)
  `,
};
```

The bottom `inset 0 -1px 0` creates a subtle bottom catch light (light entering the recess from above), which is physically correct for a recessed well.

### IMPORTANT: Rim Light vs Color Bleed — TWO SEPARATE THINGS

These are often confused. They are physically different phenomena and must be implemented separately:

1. **RIM LIGHT** (border) = ambient light catching the machined metal edge of the recess. Color is **NEUTRAL WARM** (`rgba(255,250,240,...)`) matching the chassis palette. Direction follows the 135deg light source (top/left brighter). This looks identical on EVERY recess regardless of content.

2. **COLOR BLEED** (inset box-shadow) = light emitted by the screen content reflecting off the recess walls. Color **MATCHES THE CONTENT** (green, amber, red). Position follows WHERE THE CONTENT IS inside the screen — if "2.1ms" is on the right side of the display, the color bleed is strongest on the RIGHT wall.

```javascript
// CORRECT — two separate systems
const RECESS = {
  // 1. RIM LIGHT: neutral warm, follows 135deg ambient light (same on every recess)
  borderTop: "1px solid rgba(255,250,240,0.20)",
  borderLeft: "1px solid rgba(255,250,240,0.14)",
  borderBottom: "1px solid rgba(255,250,240,0.06)",
  borderRight: "1px solid rgba(255,250,240,0.06)",

  // 2. COLOR BLEED: content color, follows content position (separate inset shadow)
  // "2.1ms" readout is on the right side → right wall gets green bleed
  boxShadow: `
    ${DEPTH_SHADOWS},
    inset -4px 0 8px rgba(60,220,120,0.04)  /* green bleed on RIGHT wall from readout */
  `,
};

// WRONG — colored border as "rim light"
borderLeft: "1px solid rgba(60,220,120,0.22)"  // NO — green border = not a rim light, it's wrong
```

### Color Bleed from Display Content (CRITICAL for realism)

When a screen/display shows colored content (amber text, green readout, red warning), the walls of the recess pick up that color as a subtle glow. This is NOT done with border (that's the rim light above) — it's done with **inset box-shadow** to simulate light bouncing off the recess walls.

**CRITICAL**: Identify the glowing content that is INSIDE the screen recess (not labels outside it). For a status card, "CONNECTED" might be outside the screen as a title — the actual screen content is "2.1ms" or "NO SIGNAL". The color bleed comes from what's INSIDE the display well.

```javascript
// Color bleed is implemented as INSET BOX-SHADOW, not border
// The border stays neutral warm (rim light from ambient)

// "2.1ms" readout on the RIGHT side of the display → green bleed on RIGHT wall
boxShadow: `
  ${DEPTH_INSET_SHADOWS},
  inset -4px 0 10px rgba(60,220,120,0.04)  /* green bleed on right wall */
`

// "NO SIGNAL" centered in display → red bleed diffuse from center
boxShadow: `
  ${DEPTH_INSET_SHADOWS},
  inset 0 0 16px rgba(220,60,60,0.03)  /* red bleed ambient from center */
`

// "3000" amber digits left-aligned in input well → amber on LEFT wall
boxShadow: `
  ${DEPTH_INSET_SHADOWS},
  inset 4px 0 10px rgba(255,180,60,0.04)  /* amber bleed on left wall from digits */
`
```

**NEVER use colored borders for color bleed.** Borders = rim light = neutral warm = matches chassis. Color bleed = inset box-shadow = matches content color = positioned where content projects.

The color bleed is subtle (0.06-0.10 opacity) but it dramatically increases realism. Without it, the recess looks disconnected from its content — like a picture frame instead of a real CRT cavity.

### Color Bleed Follows Content Position (via inset box-shadow, NOT border)

Screen content projects colored light onto the recess walls. This is implemented as **inset box-shadow** (never border — borders are for raised elements, not recessed wells). The color matches the screen content, and the shadow is positioned on the wall closest to the glowing content.

```javascript
// "2.1 ms" green readout on right side → green bleed on RIGHT wall
boxShadow: `${DEPTH_SHADOWS}, inset -4px 0 10px rgba(60,220,120,0.05)`

// "3000" amber digits left-aligned → amber bleed on LEFT wall
boxShadow: `${DEPTH_SHADOWS}, inset 4px 0 10px rgba(255,180,60,0.05)`

// "NO SIGNAL" centered → red diffuse bleed
boxShadow: `${DEPTH_SHADOWS}, inset 0 0 16px rgba(220,60,60,0.03)`
```

See `references/16-benchmark-lessons.md` §16.1 for the full distinction between rim light and color bleed.

### Screen Depth Gradient (Content Color, Opposite to Glass Reflection)

CRT/display screens need TWO overlapping gradients to create depth:

1. **Glass reflection** (top-left → bottom-right): warm white tint `rgba(255,245,235,0.08)` — simulates ambient light on the glass surface
2. **Content depth gradient** (bottom-right → top-left, or right → left): uses the TEXT COLOR at very low opacity — simulates the screen content illuminating the display cavity from within

These two gradients go in OPPOSITE directions. The glass reflection comes from outside (ambient light hitting the surface), while the content gradient comes from inside (the phosphor/LED emitting light into the cavity).

```javascript
// Display shows GREEN text → add green depth gradient from right-to-left
const SCREEN_OVERLAYS = {
  // Glass reflection (from outside, top-left)
  glassReflection: {
    background: "linear-gradient(125deg, rgba(255,245,235,0.08) 0%, transparent 50%)",
    pointerEvents: "none",
  },
  // Content depth gradient (from inside, opposite direction: right-to-left)
  contentDepth: {
    background: "linear-gradient(270deg, rgba(60,220,120,0.06) 0%, transparent 60%)",
    pointerEvents: "none",
  },
};

// AMBER text → amber depth gradient right-to-left
contentDepth: { background: "linear-gradient(270deg, rgba(255,180,60,0.05) 0%, transparent 60%)" }

// RED text → red depth gradient right-to-left
contentDepth: { background: "linear-gradient(270deg, rgba(220,60,60,0.05) 0%, transparent 60%)" }
```

Stack both as `::before`/`::after` or as absolute-positioned overlay divs. The content depth gradient adds the feeling that the text is physically INSIDE the screen emitting light, not printed on a flat surface.

**This applies to**: CRT screens, display wells, input recesses, gauge pits, LED holes — ANY sunken surface.

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

## Reference Files (16 references + 13 HTML assets)

**ALWAYS start with `00-golden-examples.md`** — it has the Lookup Table to find component patterns.

| File                                               | Content                                                                                                                                       | Lines    | Search?         |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- |
| `00-golden-examples.md`                            | **START HERE** — Shadow stacks, button/card/CRT, Lookup Table, Palette                                                                        | ~540     | Read full       |
| `01-shadows-materials-textures.md`                 | 16 material gradients (chrome, leather, wood, rubber...)                                                                                      | 321      | Read full       |
| `02-hardware-animation-neumorphism.md`             | Screws, vents, rivets, 8 animations, neumorphism                                                                                              | 166      | Read full       |
| `03-blueprints-performance-palettes.md`            | 14 component blueprints, performance rules, 6 palettes                                                                                        | 130      | Read full       |
| `04-community-techniques.md`                       | 102 community patterns (14.1-14.102)                                                                                                          | **8671** | **SEARCH ONLY** |
| `05-physics-composition-interaction-typography.md` | Light physics, sphere/cylinder/flat lighting                                                                                                  | 258      | Read full       |
| `06-aging-safety-tokens-palettes.md`               | Aging/patina, safety colors, design tokens                                                                                                    | 160      | Read full       |
| `07-glass-effects.md`                              | 10 glass techniques (frosted, dark glass, sphere)                                                                                             | 1163     | Read or search  |
| `08-metal-effects.md`                              | 8 metal techniques (brushed, chrome, gold, conic)                                                                                             | 690      | Read or search  |
| `09-rim-light-effects.md`                          | 7 common mistakes + 5 rim light techniques with 4-layer system                                                                                | ~530     | Read or search  |
| `10-particle-effects.md`                           | 10 particle systems (CSS, Canvas, WebGL, fire)                                                                                                | 877      | Read or search  |
| `11-retro-industrial-patterns.md`                  | Bezel, CRT, LED, screw, texture, counter                                                                                                      | **5392** | **SEARCH ONLY** |
| `12-production-components.md`                      | 11 production patterns: button, dashboard, VU, switch, LCD, lever, gauge, alert, CRT, accordion, thermometer                                  | ~500     | Read or search  |
| `13-3d-depth-techniques.md`                        | **3D glossary**, shadow depth, perspective/transforms, button press, flip card, isometric, emboss, glass dome, parallax, @property animations | ~880     | Read or search  |
| `14-metal-recess-wells.md`                         | **Metal recesses/wells** — 4-zone anatomy, 6/9/12-layer inset stacks, gorges, punched holes, LCD wells, color bleed                           | ~360     | Read or search  |
| `15-detailed-chassis.md`                           | **Detailed chassis** — 6-zone anatomy, bezel frame, brushed texture, hex perf, panel joints, torx screws, stamped labels                      | ~570     | Read or search  |

### HTML Assets — Quick Lookup

| Need                    | File                                | Search key     | Key patterns                                        |
| ----------------------- | ----------------------------------- | -------------- | --------------------------------------------------- |
| Push button with LED    | `power-button.html`                 | `power-button` | 17-layer button, glow slot, Phillips screws         |
| Dashboard / analytics   | `synthscore-analytics.html`         | `synthscore`   | Gradient bar, metallic border, tech brackets        |
| VU meter / gauge        | `tube-compressor-vu.html`           | `vu-meter`     | 16-layer well, 5-layer glass, animated needle       |
| Toggle switch           | `skeuomorphic-switch.html`          | `switch`       | Recessed track, grip handle, LED indicators         |
| LCD numeric display     | `lcd-db-display.html`               | `lcd`          | Olive screen, scanlines, Digital-7 font             |
| Rotary lever / knob     | `industrial-lever.html`             | `lever`        | 11-layer knob, SVG screws, CSS-only checkbox        |
| Score gauge / radial    | `credit-score-gauge.html`           | `gauge`        | SVG arc, 16-layer chassis, brushed metal            |
| Alert / warning panel   | `autochord-alert-panel.html`        | `alert`        | Dome icon, red glow, perforated backplate           |
| CRT danger screen       | `deep-screen-phosphor.html`         | `phosphor`     | Red phosphor, 31-layer chassis hole, breathing anim |
| Folding / accordion     | `folding-header.html`               | `folding`      | Collapsible, glowing icon, neomorphic well          |
| Horizontal bar meter    | `horizontal-thermometer.html`       | `thermometer`  | Glass bulb, recessed tube, color-reactive fill      |
| Deep CRT (31 layers)    | `codepen-deep-screen.html`          | `deep-screen`  | Ultra shadow stack gold standard                    |
| Full page (15+ buttons) | `agile-tech-skeuomorphic-site.html` | `site`         | Multiple button tiers, full layout                  |

All files in `assets/`. Detailed breakdowns: `references/12-production-components.md`

### Searching References

Use the BM25 search engine for efficient pattern discovery:

```bash
# Cross-file search (all 29 sources)
python3 scripts/search.py "button shadow"

# Targeted file search (for 04 or 11)
python3 scripts/search.py "CRT bezel" --file 11

# Code blocks only (skip prose)
python3 scripts/search.py "knob gradient" --code-only -n 5

# Limited preview
python3 scripts/search.py "rim light" --context 5
```

Common search terms: `button`, `shadow`, `CRT`, `knob`, `glass`, `metal`, `rim light`, `LED`, `bezel`, `screw`, `gauge`, `meter`, `panel`, `switch`, `dial`, `lever`, `LCD`, `VU`, `dashboard`, `toggle`, `alert`, `phosphor`, `thermometer`, `folding`, `accordion`, `dome`, `bulb`, `arc`, `score`, `3D`, `depth`, `perspective`, `emboss`, `parallax`, `isometric`, `flip`, `floating`, `recess`, `well`, `inset`, `gorge`, `chassis`, `brushed`, `perforation`, `seam`, `torx`, `stamped`, `label`, `channel`
