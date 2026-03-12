<!-- CI: 7 jobs | CodeRabbit: assertive -->
```
    ______ __ __                                      __    _         ______
   / ____// //_/___   __  __ ____   ____ ___   ____  / /__ (_)____   / ____/____   _____ ____ _ ___
  / /_   / ,<  / _ \ / / / // __ \ / __ `__ \ / __ \/ //_// // __ \ / /_   / __ \ / ___// __ `// _ \
 / __/  / /| |/ __// /_/ // /_/ // / / / / // /_/ / ,<  / // /_/ // __/  / /_/ // /   / /_/ //  __/
/_/    /_/ |_|\___/ \__,_/ \____//_/ /_/ /_/ \____/_/|_|/_/ \____//_/     \____//_/    \__, / \___/
                                                                                      /____/
```

# Skeuomorphic Forge

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
# As a Claude Code plugin
claude /install-plugin github:mmmprod/skeuomorphic-forge
```

```bash
# Or clone into your project skills
mkdir -p .claude/skills && cd .claude/skills
git clone https://github.com/mmmprod/skeuomorphic-forge.git
```

Auto-triggers on: `skeuomorphic`, `industrial UI`, `3D button`, `gauge`, `meter`, `realistic depth`, `retro-industrial`, `DSP cockpit`, `CRT display`, `glass effect`, `metal texture`.

---

## The Problem It Solves

| You ask for | Claude gives you | With this skill |
|-------------|------------------|-----------------|
| Skeuomorphic button | `box-shadow: 0 2px 4px black` | 5-layer graduated shadow + hover/active states |
| Industrial panel | Flat div + decorative screws | 11-layer chassis + depth wells + THEN screws |
| CRT display | Green text on black bg | Phosphor glow + scanlines + glass reflection |
| Warm lighting | `rgba(255,255,255,0.4)` | `rgba(255,240,220,0.2)` warm specular |
| Metal knob | Circle with gradient | 8-layer shadow + rim light + specular hotspot |

---

## What's Inside

```
skeuomorphic-forge/
|
|-- SKILL.md                    <- The brain (386 lines of battle-tested rules)
|
|-- references/                 <- The knowledge (12 files, 18,830 lines)
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
|
|-- assets/                     <- The gold standards (2 production HTML files)
|   |-- agile-tech-site.html         8,000-line production skeuomorphic site
|   |-- codepen-deep-screen.html     31-layer ultra shadow stack
|
|-- scripts/                    <- The tools
    |-- search.py                    BM25 search engine across all 14 sources
```

**Total: 27,583 lines** of copy-paste-ready patterns, shadow stacks, and production code.

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
 golden-examples.md         search.py "knob"            assembly order              pre-delivery gate
 (always first)             (BM25 across 14 files)      back -> front               6 checklists
                                                                                    by priority
   [00-golden]                $ python3 search.py        Backplate                    CRITICAL
       |                        "rim light" -n 5           +-- Panels                  |
       v                              |                      +-- Wells               HIGH
   Lookup Table                       v                        +-- Content              |
       |                        Result 1 (4.2)                   +-- Hardware        MEDIUM
       v                        Result 2 (3.8)                     +-- Labels
   Load ref file                Result 3 (2.1)                       +-- Glass
```

---

## Priority System

| # | Rule | Priority | One-liner |
|---|------|----------|-----------|
| 1 | Shadow Depth | CRITICAL | Count layers: 5 / 8 / 11 minimum |
| 2 | Light vs Shadow | CRITICAL | Dark rgba = depth, warm rgba = specular. Separate. |
| 3 | Warm Highlights | CRITICAL | `rgba(255,240,220,...)` not pure white |
| 4 | Assembly Order | HIGH | Depth first, hardware last |
| 5 | Interaction States | HIGH | hover + active + disabled + focus-visible |
| 6 | Physical Naming | HIGH | "machined aluminum" not "container div" |
| 7 | Typography | MEDIUM | Silkscreen / engraved / embossed |
| 8 | Accessibility | MEDIUM | Contrast, focus rings, 44px targets |
| 9 | Performance | MEDIUM | transform + opacity only in animations |

---

## Search Engine

Don't read 8,671 lines manually. Use BM25-powered search:

```bash
python3 scripts/search.py "button shadow"              # Search all 14 sources
python3 scripts/search.py "CRT display" -n 5           # Top 5 results
python3 scripts/search.py "box-shadow" --file 04        # Search specific file
python3 scripts/search.py "knob gradient" --code-only   # Only code blocks
python3 scripts/search.py "rim light" --context 5       # Limited preview
```

Indexes 2,400+ sections. Returns ranked results with file, line numbers, and matching content.

---

## Before / After

```css
/* BEFORE — what Claude typically generates */
.button {
  background: #333;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);     /* 1 layer. flat. */
  color: white;
}

/* AFTER — with Skeuomorphic Forge */
.button {
  background: linear-gradient(145deg, #2a2a2a 0%, #1a1a1a 100%);
  border-radius: 8px;
  border-top: 1px solid rgba(255,255,255,0.08);
  border-left: 1px solid rgba(255,255,255,0.04);
  border-bottom: 1px solid rgba(0,0,0,0.3);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.05),      /* edge catch */
    inset 0 -1px 0 rgba(0,0,0,0.3),            /* bottom gorge */
    0 2px 4px rgba(0,0,0,0.4),                 /* close shadow */
    0 8px 16px rgba(0,0,0,0.3),                /* mid depth */
    0 16px 32px rgba(0,0,0,0.2);               /* ambient shadow */
  color: rgba(255,255,255,0.9);
  text-shadow: 0 1px 2px rgba(0,0,0,0.5);
}
.button:hover {
  transform: translateY(-1px);                  /* lift */
}
.button:active {
  transform: translateY(1px);                   /* depress */
  box-shadow:
    inset 0 2px 4px rgba(0,0,0,0.5),
    inset 0 1px 1px rgba(0,0,0,0.3),
    0 1px 2px rgba(0,0,0,0.3);                 /* compressed */
}
```

---

## Stats

```
   References      12 files       18,830 lines
   HTML Assets      2 files        8,495 lines
   Search Engine    1 script       2,400+ indexed sections
   Shadow Tiers     4 levels       5 / 8 / 11 / 31 layers
   Materials       16 gradients    chrome, leather, wood, rubber...
   Glass Effects   10 techniques   frosted, dark, sphere, SVG warp
   Metal Effects    8 techniques   brushed, chrome, gold, conic
   Particles       10 systems      CSS, Canvas, WebGL, fire, vortex
   Animations       8 patterns     spring, sweep, fade, bounce...
   Palettes         6 sets         retro-industrial, aerospace, CRT...
   Community      102 patterns     from CodePen, CSS-Tricks, Dribbble
```

---

## Contributing

Contributions welcome! Feel free to:

- Open an **issue** to report bugs or suggest new material/effect types
- Submit a **pull request** with improvements or new reference guides
- Fork and adapt for your own projects

```bash
git checkout -b feature/new-material
# make changes
git commit -m "Add ceramic material reference"
git push origin feature/new-material
# open PR
```

---

## Credits

Built for the [DSP Tuner Pro](https://github.com/mmmprod) project — a Next.js automotive DSP calibration app with a retro-industrial cockpit aesthetic.

Patterns sourced from production components, CodePen experiments, CSS-Tricks articles, and the audiophile hardware design community.

---

## License

[MIT](LICENSE) — use it, modify it, share it, do whatever you want.
