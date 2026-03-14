<!-- CI: 7 jobs | CodeRabbit: assertive -->

```
    ______ __ __                                      __    _         ______
   / ____// //_/___   __  __ ____   ____ ___   ____  / /__ (_)____   / ____/____   _____ ____ _ ___
  / /_   / ,<  / _ \ / / / // __ \ / __ `__ \ / __ \/ //_// // __ \ / /_   / __ \ / ___// __ `// _ \
 / __/  / /| |/ __// /_/ // /_/ // / / / / // /_/ / ,<  / // /_/ // __/  / /_/ // /   / /_/ //  __/
/_/    /_/ |_|\___/ \__,_/ \____//_/ /_/ /_/ \____/_/|_|/_/ \____//_/     \____//_/    \__, / \___/
                                                                                      /____/
```

# Skeuomorphic Forge v2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blueviolet?logo=anthropic)](https://claude.ai/claude-code)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mmmprod/skeuomorphic-forge/pulls)
[![GitHub stars](https://img.shields.io/github/stars/mmmprod/skeuomorphic-forge?style=social)](https://github.com/mmmprod/skeuomorphic-forge)

**A Claude Code skill that builds physically-realistic UI components.**

Not flat divs with drop shadows. Real objects — machined metal, CRT glass, brushed aluminum, industrial hardware.

---

```
                     FLAT DESIGN                 vs              SKEUOMORPHIC FORGE
                ___________________                         ___________________________
               |                   |                       |   o                   o   |
               |                   |                       |  /|\ ~ ~ ~ ~ ~ ~ ~ /|\  |
               |      Button       |                       |  |||  ___________  |||  |
               |                   |                       |  |||  | B u t t o n|  |||  |
               |___________________|                       |  |||  |___________|  |||  |
               box-shadow: 0 2px black                     |  \|/ 13 shadow layers \|/  |
                                                           |_____________________________|
               2 layers. sad.                              screws. depth. warm light.
```

---

## Install

```bash
# Claude Code skill
claude install-skill https://github.com/mmmprod/skeuomorphic-forge
```

```bash
# Or clone into your project skills
mkdir -p .claude/skills && cd .claude/skills
git clone https://github.com/mmmprod/skeuomorphic-forge.git
```

Auto-triggers on: `skeuomorphic`, `industrial UI`, `3D button`, `gauge`, `meter`, `realistic depth`, `retro-industrial`, `DSP cockpit`, `CRT display`, `glass effect`, `metal texture`.

---

## What's New in v2.0

### Benchmark Lessons (10 iterations of visual review)

v2.0 includes `references/16-benchmark-lessons.md` — **17 sections of battle-tested design corrections** from 10 rounds of visual benchmarking with a professional audio hardware designer. Key rules:

| Rule | What it prevents |
|------|-----------------|
| Display wells = inset shadows only, NO borders | Glass appearing to stick OUT instead of being recessed IN |
| Color bleed = inset box-shadow, NOT colored border | Borders and rim lights being confused with content glow |
| 5 mandatory display overlays | Over-simplified flat screens missing glass/scanlines/depth |
| Screws proportional + 8px clearance | Bolts on watches, screws touching labels |
| No unexplained light sources | Random glowing bars on flat metal with no physical feature |
| Warm highlights only (no pure white >0.10) | Clinical/washed-out look on industrial surfaces |
| Content centered in chassis | Input wells pushed to bottom of oversized panels |

### Code Review Fixes

All contradictions between SKILL.md and benchmark lessons resolved. Step 7 verification gate expanded with U9 checklist covering all benchmark topics.

---

## The Problem It Solves

| You ask for         | Claude gives you              | With this skill                                |
| ------------------- | ----------------------------- | ---------------------------------------------- |
| Skeuomorphic button | `box-shadow: 0 2px 4px black` | 9-layer graduated shadow + hover/active states |
| Industrial panel    | Flat div + decorative screws  | 11-layer chassis + depth wells + THEN screws   |
| CRT display         | Green text on black bg        | Phosphor glow + scanlines + glass reflection + content depth gradient |
| Warm lighting       | `rgba(255,255,255,0.4)`       | `rgba(255,240,220,0.2)` warm specular          |
| Metal knob          | Circle with gradient          | 8-layer shadow + rim light + specular hotspot  |
| Input well          | Dark div with border          | 9-layer inset recess + 5 overlay layers + focus animation |

---

## What's Inside

```
skeuomorphic-forge/
|
|-- SKILL.md                    <- The brain (~1050 lines of battle-tested rules)
|
|-- references/                 <- The knowledge (17 files, 20,000+ lines)
|   |-- 00-golden-examples.md       Production shadow stacks, complete components
|   |-- 01-shadows-materials.md      16 material gradients (chrome, leather, wood...)
|   |-- 02-hardware-animation.md     Screws, vents, rivets, 8 animations
|   |-- 03-blueprints-palettes.md    14 component blueprints, 6 color palettes
|   |-- 04-community-techniques.md   102 community patterns [8,671 lines!]
|   |-- 05-physics-interaction.md    Light physics, sphere/cylinder/flat lighting
|   |-- 06-aging-tokens.md           Patina, safety colors, design tokens
|   |-- 07-glass-effects.md          10 glass techniques (frosted, sphere, SVG warp)
|   |-- 08-metal-effects.md          8 metal techniques (brushed, chrome, gold)
|   |-- 09-rim-light-effects.md      5 rim light techniques, 4-layer system
|   |-- 10-particle-effects.md       10 particle systems (CSS, Canvas, WebGL)
|   |-- 11-retro-industrial.md       Bezel, CRT, LED, screw, counter [5,392 lines!]
|   |-- 12-production-components.md  11 production patterns with full code
|   |-- 13-3d-depth-techniques.md    3D glossary, perspective, emboss, parallax
|   |-- 14-metal-recess-wells.md     4-zone anatomy, 6/9/12-layer inset stacks
|   |-- 15-detailed-chassis.md       6-zone chassis anatomy, torx screws, labels
|   |-- 16-benchmark-lessons.md      17 sections from 10 visual benchmark iterations
|
|-- assets/                     <- The gold standards (13 production HTML files)
|   |-- power-button.html            17-layer button with LED + Phillips screws
|   |-- tube-compressor-vu.html      VU meter with 16-layer well + glass
|   |-- codepen-deep-screen.html     31-layer ultra shadow stack
|   |-- ... and 10 more
|
|-- scripts/                    <- The tools
    |-- search.py                    BM25 search engine across all 29 sources
```

---

## Shadow Depth at a Glance

```
Standard (5 layers)        Advanced (8 layers)         Hero (11 layers)          Ultra (31 layers)
buttons, cards             knobs, meters               panels, chassis           showcase CRT

  _________                 ___________                 _____________             _________________
 |         |               |           |               |             |           |                 |
 |  [ OK ] |               |    (O)    |               | +---------+ |           | +-------------+ |
 |_________|               |___________|               | | DISPLAY | |           | |  > SIGNAL <  | |
     |                          ||                     | +---------+ |           | | ~~~~~~~~~~~~ | |
     v                          vv                     |_____________|           | +-------------+ |
   subtle                    medium                          |||                |___________________|
                                                         deep depth                  |||||||
                                                                               maximum realism
```

---

## How It Works

```
 1. READ                    2. FIND                     3. BUILD                    4. VERIFY
 16-benchmark-lessons.md    search.py "knob"            assembly order              U0-U9 gate
 (always FIRST)             (BM25 across 29 files)      back -> front               10 checklists
 then golden-examples.md                                                            by priority

   [16-benchmark]              $ python3 search.py        Backplate                    CRITICAL
       |                         "rim light" -n 5           +-- Panels                  |
       v                              |                      +-- Wells               HIGH
   [00-golden]                         v                        +-- Content              |
       |                        Result 1 (4.2)                   +-- Hardware        MEDIUM
       v                        Result 2 (3.8)                     +-- Labels
   Lookup Table                Result 3 (2.1)                       +-- Glass
```

---

## Priority System

| #   | Rule                | Priority | One-liner                                              |
| --- | ------------------- | -------- | ------------------------------------------------------ |
| 0   | Context Scan        | BLOCKING | Read the page before styling anything                  |
| 1   | Shadow Depth        | CRITICAL | Count layers: 5 / 8 / 11 minimum                      |
| 2   | Black Shadows Only  | CRITICAL | Drop shadows = `rgba(0,0,0,...)` always                |
| 3   | Contrast Separation | CRITICAL | Wells dark, cards lighter, >= #12 hex delta             |
| 4   | Light/Shadow Split  | CRITICAL | Dark rgba = depth, warm rgba = specular. Separate.     |
| 5   | Warm Highlights     | CRITICAL | `rgba(255,240,220,...)` not pure white above 0.10      |
| 6   | Typography          | HIGH     | Silkscreen / engraved / embossed, min 0.50 opacity     |
| 7   | Assembly Order      | HIGH     | Depth first, hardware last                             |
| 8   | Interaction States  | HIGH     | hover + active + disabled + focus-visible               |
| 9   | Benchmark Lessons   | HIGH     | 17 rules from 10 iterations — see §16                  |

---

## Search Engine

Don't read 8,671 lines manually. Use BM25-powered search:

```bash
python3 scripts/search.py "button shadow"              # Search all 29 sources
python3 scripts/search.py "CRT display" -n 5           # Top 5 results
python3 scripts/search.py "box-shadow" --file 04        # Search specific file
python3 scripts/search.py "knob gradient" --code-only   # Only code blocks
python3 scripts/search.py "rim light" --context 5       # Limited preview
```

Indexes 2,600+ sections across 16 references + 13 HTML assets. Returns ranked results with file, line numbers, and matching content.

---

## Stats

```
   References      17 files       20,000+ lines
   HTML Assets     13 files        8,495 lines
   Search Engine    1 script       2,600+ indexed sections
   Shadow Tiers     4 levels       5 / 8 / 11 / 31 layers
   Materials       16 gradients    chrome, leather, wood, rubber...
   Glass Effects   10 techniques   frosted, dark, sphere, SVG warp
   Metal Effects    8 techniques   brushed, chrome, gold, conic
   Particles       10 systems      CSS, Canvas, WebGL, fire, vortex
   Animations       8 patterns     spring, sweep, fade, bounce...
   Palettes         6 sets         retro-industrial, aerospace, CRT...
   Community      102 patterns     from CodePen, CSS-Tricks, Dribbble
   Benchmarks      10 iterations   17 design correction sections
```

---

## Contributing

Contributions welcome! Feel free to:

- Open an **issue** to report bugs or suggest new material/effect types
- Submit a **pull request** with improvements or new reference guides
- Fork and adapt for your own projects

---

## Credits

Built for the [DSP Tuner Pro](https://github.com/mmmprod) project — a Next.js automotive DSP calibration app with a retro-industrial cockpit aesthetic.

Patterns sourced from production components, CodePen experiments, CSS-Tricks articles, and the audiophile hardware design community. Benchmark lessons from 10 iterations of visual review with a professional audio hardware designer.

---

## License

[MIT](LICENSE) — use it, modify it, share it, do whatever you want.
