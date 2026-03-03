---
name: skeuomorphic-forge
description: "Create production-grade skeuomorphic UI with Tailwind CSS. Use when building physically-realistic elements: buttons with mechanical depth, gauges, meters, LED/nixie indicators, toggle switches, sliders, progress bars, cards with material textures (metal, glass, leather, wood, paper, fabric, concrete, plastic), industrial panels, CRT/VFD displays, neumorphic components, particle effects, or any UI mimicking real-world objects. Covers dark (industrial, military) and light (classic, iOS-era, neumorphic) themes. Triggers: skeuomorphic, realistic, 3D button, industrial UI, gauge, meter, LED, nixie, analog, physical, tactile, metal texture, glass effect, depth effect, neumorphic, soft UI, leather, wood grain, rim light, chrome, gold, brushed metal, particles, starfield, space dust, vortex, particle system, disintegration, GPGPU, material with depth. Do NOT trigger for flat/minimal UI, standard Material/Shadcn components, or conventional Tailwind layouts without physical realism."
---

# Skeuomorphic Forge

Build physically-realistic UI components using Tailwind CSS. Every component must look like it could exist as a real physical object — with correct lighting, shadow depth, material textures, and mechanical behavior.

## Design Philosophy

**Physical realism over decoration.** Every shadow, gradient, and highlight must serve a physical purpose:
- Shadows indicate depth and light direction
- Gradients simulate material curvature
- Highlights mark specular reflection points
- Animations mimic mechanical behavior (springs, inertia, depression)

**The 4-layer construction rule.** Every skeuomorphic component has at minimum:
1. **Chassis/body** — the physical material (metal, glass, plastic, leather, wood, paper, fabric)
2. **Depth** — inset or raised shadows establishing spatial position
3. **Lighting** — specular highlights and rim light consistent with a single light source
4. **Detail** — texture overlays, screws, mesh, stitching, grain, wear marks

**Shadow depth standard (MANDATORY).** Flat, lazy shadows destroy realism. The cerpow compressor analysis (pattern 14.16) proves that 8-15 stacked inner shadows create the illusion of real machined metal. Each layer serves a distinct physical role: edge catch (1px, white, high opacity) -> bevel (blur 4-10px, gray) -> mid-depth shaping (offset, directional) -> ambient occlusion (blur 20px, black, low opacity) -> cast shadow (external). Minimum layer counts:
- **Standard components** (buttons, cards, toggles): minimum 5 box-shadow layers
- **Advanced components** (knobs, dials, meters, CRT screens): minimum 8 box-shadow layers
- **Hero components** (faceplates, full panel assemblies): 11-15 box-shadow layers
- 2-3 shadow layers is FLAT DESIGN pretending to be skeuomorphic. NEVER acceptable for this skill.

**Hardware placement rules (MANDATORY).** Decorative fasteners follow real-world structural logic:
- Rectangle/square panel -> 4 screws (one per corner, inset 8-16px from edges)
- Narrow horizontal/vertical strip -> 2 screws (centered vertically at each end)
- Triangle -> 3 screws (one per vertex)
- Circle/dial bezel -> 0 screws (bezel ring suffices) or 4+ evenly spaced
- **NEVER place a single screw on a panel** — one fastener cannot prevent rotation. Physically impossible and visually absurd.
- Symmetry is mandatory: if top-left has a screw, top-right must also.
- Scale with panel size: small (<100px) = 2 screws, medium (100-300px) = 4, large (>300px) = 4-6.

## Aesthetic Families

The catalog supports three distinct aesthetic families. Identify which family the user wants before building.

### Industrial / Dark
Dark backgrounds (#050505-#1a1a1a). Brushed metal, gunmetal, cast iron. Amber/green/red glows. CRT displays, nixie tubes, VFD readouts. Mechanical switches, screws, ventilation slats.

### Classic Skeuomorphic / Light
Light backgrounds (#d0d0d0-#f0f0f0). Leather, wood, paper, linen, glossy plastic. Warm or cool tones. iOS 6 / macOS pre-flat era. Stitched edges, embossed labels, physical book/notepad metaphors.

### Neumorphic / Soft UI
Mid-tone backgrounds (#e0e0e0 or tinted). Objects appear extruded from or pressed into the background. Two-shadow system (dark bottom-right + light top-left). Minimal color, maximum shape. See pattern catalog Section 8 for rules and limitations.

## Workflow

When asked to create a skeuomorphic component:

1. **Identify the physical analog** — What real-world object does this represent?
2. **Choose the aesthetic family** — Industrial, Classic, or Neumorphic. If unclear, ask.
3. **Establish the light source** — Default: top-left (135deg). All shadows, highlights, bevels, and gradients must be consistent with this single light direction. Apply correct reflectance model per material (Section 15.5).
4. **Load relevant reference files** — Read only the files needed for the current component (see References section). Do NOT load all 10 files at once.
5. **Build the component** following assembly order (Section 16.1): backplate -> sub-panels -> wells -> hardware -> instruments -> displays -> labels -> overlays. Shadow stack: 5-15 layers per depth standard. will-change on animated elements, pointer-events-none on textures.
6. **Place hardware** — Follow hardware placement rules: 4 screws for rectangles, 2 for strips, never 1. See Section 6 placement table.
7. **Apply typography** — Match text application method to material: silkscreened (most common), engraved, embossed, stamped, backlit. See Section 18.
8. **Add state transitions** — hover, active/pressed, disabled, focus for every interactive element.
9. **Verify accessibility** — Contrast ratios, touch targets, focus indicators, reduced-motion support. See Section 11.

## Component Archetypes

Button (industrial, iOS 6 glass, membrane, jelly), Toggle (spring, rocker), Card/Panel (metal, leather, wood, paper, glass), Gauge/Meter (VU, oscilloscope, bargraph), LED Indicator, Display/Screen (CRT, VFD, 7-segment, nixie tube, burn-through LED), Knob/Dial (machined, sphere, Arturia multi-layer, brushed anisotropic, detent rotary, chickenhead selector), Slider/Range, Progress Bar, Radio/Checkbox, Dropdown/Select, Tab Bar, Badge, Tooltip, Metallic Card, Vintage Radio, VU Meter, Watch Face, Compressor Faceplate, Footswitch (stomp box), Eurorack Jack + Patch Cable, 3D Toolbar Button, Dark Glass Widget, Rubber Overmold Panel, Wood Side Panel, **Glass Panel** (frosted, dark glassmorphism, glow+shine), **Glass Sphere/Bead** (multi-gradient radial, layered-div marble), **Glass Icon/Tile** (box-shadow stack + caustic), **SVG Filter Glass** (displacement warp, chromatic RGB split), **Glass Select/Dropdown** (frosted options panel), **Brushed Metal Button** (radial/linear repeating gradients + 6-layer bevel), **Metallic Button** (conic gradient 28+ stops: gold, silver, bronze, rose gold), **Chrome Text** (background-clip:text + animated shine), **Gold Text** (dual-layer repeating gradient), **Metallic Border** (padding-box/border-box: gold, silver, bronze, platinum, black), **Rim Light Card** (4-layer box-shadow + radial-gradient pseudo-elements), **CSS Starfield** (SCSS box-shadow mixin, parallax layers), **Canvas Particle Engine** (multi-layer depth, click-burst, mouse-attracted fire), **Orbital Starfield** (elliptical orbits + twinkle + nebula), **Black Hole Vortex** (spiral infall + accretion disk + gravitational lensing), **WebGL GPGPU Particles** (Three.js FBO ping-pong, 262K+ particles, curl noise), **Text Disintegration** (Three.js BAS per-face animation + turbulence). See file 03 for blueprints, file 04 for 94 community techniques, files 05-06 for physics, composition, interaction, typography, aging, safety, tokens, palettes, **file 07 for glass effects (10 techniques)**, **file 08 for metal effects (8 techniques)**, **file 09 for rim light effects (4 techniques)**, **file 10 for particle effects (10 techniques)**.

## Quality Checklist

- [ ] Light consistency (single direction)
- [ ] Depth coherence (raised=cast shadow+specular, recessed=inset)
- [ ] Shadow depth (standard >= 5 layers, advanced >= 8, hero >= 11 — see depth standard)
- [ ] Hardware placement (screws match panel geometry, never single screw — see placement rules)
- [ ] State coverage (hover, active, disabled, focus)
- [ ] Performance (will-change, no animated blur, pointer-events-none on textures)
- [ ] Tailwind-first (inline style only for complex multi-shadow stacks)
- [ ] Accessibility (contrast, focus visible, touch targets >= 44px, reduced-motion)
- [ ] Responsive (shadows scale on mobile, see Section 12)
- [ ] Light physics (correct reflectance model per material — see Section 15)
- [ ] Typography method (silkscreen/engraved/embossed matches surface — see Section 18)
- [ ] Assembly order (backplate -> panels -> wells -> hardware -> instruments -> labels — see Section 16)

## Anti-Patterns

- **Lazy 2-3 layer shadows on 3D objects** — use 5-15 layers per depth standard. If it looks flat, add more layers.
- **Single screw on a rectangular panel** — minimum 2 for a strip, 4 for a rectangle. One screw = free rotation = not a real fastener.
- Flat shadows on 3D objects (need both cast shadow AND specular)
- Uniform glow (always multi-distance: core, mid, halo)
- Symmetric lighting (one direction only)
- Animated blur/filter (use opacity and transform only)
- Decorative-only effects (every effect must represent something physical)
- Neumorphism on wrong background (must be mid-tone)
- Missing focus indicators
- Unscaled mobile shadows

## References (10 thematic files — load only what is needed)

### references/01-shadows-materials-textures.md
**Sections 1-5.** Shadows (raised/recessed/deep well, dark+light themes), Materials (16 types: brushed metal, gunmetal, cast iron, aluminum, chrome, leather, stitched leather, wood, paper, fabric, concrete, rubber, plastic glossy/matte, glass dark/frosted), Lighting (8 patterns: specular, rim light, beveled border, ambient, under-glow, edge catch, backlit), Glow Effects (6: amber, green, red, blue, CRT phosphor, neon tube), Textures (6: noise, scanlines, grid dots, carbon fiber, diamond plate, dot matrix).
**Load for:** Any component build — this is the core building-block file.

### references/02-hardware-animation-neumorphism.md
**Sections 6-8.** Hardware Details (screw, vent slat, bezel ring, rivet, hinge + placement rules table), Animations (8: button press, toggle spring, LED, needle sweep, knob rotation, flip, bounce, rubber-band), Neumorphism (base rules, shadow calc, raised/pressed, when NOT to use).
**Load for:** Panels with screws/rivets, animated elements, soft-UI components.

### references/03-blueprints-performance-palettes.md
**Sections 9-13.** Component Blueprints (14 types incl. full CRT 7-layer assembly), Performance Rules (10), Accessibility, Responsive Scaling, Color Palettes (6: industrial dark, military, midnight blue, classic light, warm light, neumorphic).
**Load for:** New component from scratch, performance optimization, palette selection.

### references/04-community-techniques.md
**Section 14.** 93 production-proven community patterns (14.1-14.93): cerpow compressor, CRT monitor, iOS 6 glass button, leather+stitching, wood shelf, torn paper, Eurorack jack, patch cable, 7-segment, Arturia knob, footswitch, rotary selector, nixie tube, 3D toolbar, dark glassmorphism, oscilloscope, **engraved glow button with inter-button reflex** (14.38), **gradient-border button with light notch** (14.39), **circuit relay button with clip-path** (14.53), **conic gradient animated border** (14.55), **slit light system** (14.56), **rotary knob radial menu with @property + :has()** (14.61), **interactive speaker with inverse-phase vibration** (14.71), **SCSS spring-ring speaker with @for + bass gradient animation** (14.72), **dynamic cursor-tracked text shadow with lantern** (14.73), **neon text with triple mix-blend-mode stack** (14.74), **rotating conic gradient border + starfield** (14.75), **CSS 3D cube with volumetric light** (14.76), **swinging pendant light with diverging rays** (14.77), **3D perspective ambient glow orb** (14.78), **neon sign flicker with irregular off-states** (14.79), **plasma orb with 8-layer dual-color box-shadow** (14.80), **SCSS neon triangle with clip-path + volumetric blur** (14.81), **toggle luminaire orbits with spinning glow** (14.82), **multi-style text shadow collection (28-layer elegant + deep + inset + retro)** (14.83), **neon sign multi-color theme system with steps() flicker** (14.84), **3D animated letter shadows with rotateY + skew** (14.85), **3D extruded chrome text with chained drop-shadow** (14.86), **CSS paper card shadows (lifted, curled, perspective, raised, curved)** (14.87), **CSS 3D slab construction (6-face + 8 beveled corners + animated reflection)** (14.88), **CSS 3D ribbon bar with 4-face perspective + slider** (14.89), **CSS 3D layered text extrusion (20 translateZ copies + progressive text-stroke)** (14.90), **SCSS isometric 3D cube mixin system with neon lighting** (14.91), **CSS cuboid generator system with HSL auto-shading + camera rig** (14.92), **glass thermostat with plasma fill + draggable knob + 6-color gradient** (14.93), **horizontal glass slider with equalizer tick visualization + ambient blur circle** (14.94).
**Load for:** Inspiration, specific component reproduction, advanced technique lookup.

### references/05-physics-composition-interaction-typography.md
**Sections 15-18.** Light Physics (7 reflectance models), Composition & Assembly Rules (5 build order rules), Interaction Patterns (6 state patterns), Typography on Physical Surfaces (6 application methods: silkscreen, engrave, emboss, stamp, backlit, transfer).
**Load for:** Complex multi-element panels, faceplate assemblies, labeled instruments.

### references/06-aging-safety-tokens-palettes.md
**Sections 19-22.** Aging & Patina (4 wear effects), Safety & Industrial Colors (2 palettes), Design Tokens (5 groups: shadow scale, material colors, glow intensities, animation timing, depth levels), Additional Color Palettes (4 extra).
**Load for:** Vintage/weathered aesthetics, industrial safety UI, design system token setup.

### references/07-glass-effects.md
**Section 23.** Glass Effects (10 subsections): Glass Physics Primer (4 optical properties), Frosted Glass clip-path+blur (no backdrop-filter needed), Frosted Glass Card (backdrop-filter + 5-layer progressive shadow), Dark Glassmorphism with Glow (conic gradient shine + noise-masked glow + animated reveal + @property list items), Glass Icon/Tile (10-layer box-shadow + caustic ::before), Glass Sphere multi-gradient (15+ radial gradients + 7-layer rim shadow + specular ::after with perspective), Glass Bead layered-div (8 stacked elements: crop, rim, inner shadow, highlights, caustics, ground shadow), SVG Filter Glass (displacement map, warp, chromatic RGB split via feColorMatrix + feBlend), Glass Select/Dropdown (full UI component with frosted options), Quick Reference recipes (4 Tailwind/inline recipes + decision matrix).
**Load for:** Any glass effect — frosted panels, glass spheres, dark glassmorphism, refractive/warp effects, chromatic aberration, glass form controls.

### references/08-metal-effects.md
**Section 24.** Metal Effects (8 subsections): Metal Physics Primer (anisotropic reflection, specular highlight, depth/bevel + 8 metal type signatures), Brushed Metal Button (radial + linear variants with 6-layer box-shadow bevel + 3-layer repeating gradient brush texture + fake conical gradient via rotated pseudo-elements + active state), Metallic Buttons with Conic Gradient (28+ stop conic-gradient for gold, silver, bronze/copper, rose gold), Chrome Text (6-stop vertical gradient + background-clip:text + animated shine sweep ::before), Gold Metallic Text (dual-layer overlapping div with different gradient angles for cross-hatch effect), Metallic Borders (padding-box/border-box gradient trick for gold, silver, bronze, platinum, black metal + animated shine overlay), Procedural Brushed Metal (canvas Perlin noise + blend modes for ultra-realistic texture), Quick Reference recipes + decision matrix.
**Load for:** Any metal surface — brushed metal buttons, chrome/gold/silver text, metallic borders/frames, conic gradient metal buttons, procedural metal textures.

### references/09-rim-light-effects.md
**Section 25.** Rim Light Effects (4 subsections): Rim Light Physics (edge glow, concentration, falloff), Dark Card with Rim Light (4-layer box-shadow system + ::before top highlight + ::after bottom highlight using dual radial gradients + mix-blend-mode screen), Rim Light Variations (colored/branded, full-perimeter, animated hover intensification), Quick Reference recipes + opacity guidelines table.
**Load for:** Dark UI cards/panels with edge lighting, backlit containers, ambient rim glow on dark backgrounds.

### references/10-particle-effects.md
**Section 26.** Particle Effects (10 subsections): Particle System Fundamentals (CSS vs Canvas vs WebGL decision matrix, performance budgets), CSS-Only Starfield SCSS (box-shadow mixin + parallax layers + @keyframes drift), Canvas Particle Engine multi-layer (CreateJS-style depth sorting + cached sprite optimization), Click-Burst Space Dust (inverse-square gravity + radial burst + fade trails), Mouse-Attracted Fire Particles (cursor tracking + HSL flame gradient + globalCompositeOperation lighter), Starfield Orbital + Twinkle (elliptical orbits + sine-wave opacity + nebula clouds), Black Hole Vortex (spiral infall + accretion disk + gravitational lensing + Doppler color shift), WebGL GPGPU Cursor Particles (Three.js FBO ping-pong + curl noise + 262K particles + RawShaderMaterial), Three.js Text Disintegration BAS (per-face centroid animation + turbulence displacement + stagger by distance), Quick Reference recipes + performance guidelines table.
**Load for:** Any particle system — CSS starfields, Canvas 2D particle engines, mouse-interactive particles, orbital/vortex effects, WebGL/Three.js GPU particle systems, text disintegration effects.

### assets/agile-tech-skeuomorphic-site.html
Full 8000-line skeuomorphic website (Agile Tech) with 300+ advanced CSS techniques. Dark industrial aesthetic with conic gradient borders, volumetric light systems, 3D carousels, multi-layer metallic cards, starfield backgrounds, and Apple-style modals.
**Load for:** Deep-dive inspiration when patterns 14.53-14.60 reference specific techniques. Too large to load fully — use grep -i "keyword" to find specific sections.

### Search across all files
```bash
grep -ri "keyword" references/
```
