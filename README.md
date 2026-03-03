# Skeuomorphic Forge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-blueviolet?logo=anthropic)](https://claude.ai/claude-code)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mmmprod/skeuomorphic-forge/pulls)
[![GitHub issues](https://img.shields.io/github/issues/mmmprod/skeuomorphic-forge)](https://github.com/mmmprod/skeuomorphic-forge/issues)
[![GitHub stars](https://img.shields.io/github/stars/mmmprod/skeuomorphic-forge?style=social)](https://github.com/mmmprod/skeuomorphic-forge)

A Claude Code skill for creating production-grade skeuomorphic UI with Tailwind CSS.

## What it does

Generates physically-realistic UI elements: buttons with mechanical depth, gauges, meters, LED/nixie indicators, toggle switches, sliders, progress bars, cards with material textures (metal, glass, leather, wood, paper, fabric, concrete, plastic), industrial panels, CRT/VFD displays, neumorphic components, and particle effects.

Covers both **dark** (industrial, military) and **light** (classic, iOS-era, neumorphic) themes.

## Triggers

Use when building UI that mimics real-world objects:

- Skeuomorphic, realistic, 3D buttons
- Industrial UI, gauges, meters
- LED, nixie, analog, physical, tactile elements
- Metal texture, glass effect, depth effect
- Neumorphic, soft UI
- Leather, wood grain, brushed metal, chrome, gold
- Rim light effects
- Particle systems, starfield, vortex, disintegration

## Install

```bash
claude /install-plugin github:mmmprod/skeuomorphic-forge
```

## Structure

```
skeuomorphic-forge/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── skeuomorphic-forge/
│       ├── SKILL.md              # Main skill file
│       ├── references/           # 10 detailed reference guides
│       │   ├── 01-shadows-materials-textures.md
│       │   ├── 02-hardware-animation-neumorphism.md
│       │   ├── 03-blueprints-performance-palettes.md
│       │   ├── 04-community-techniques.md
│       │   ├── 05-physics-composition-interaction-typography.md
│       │   ├── 06-aging-safety-tokens-palettes.md
│       │   ├── 07-glass-effects.md
│       │   ├── 08-metal-effects.md
│       │   ├── 09-rim-light-effects.md
│       │   └── 10-particle-effects.md
│       └── assets/
│           └── agile-tech-skeuomorphic-site.html
└── README.md
```

## Contributing

Contributions are welcome! Feel free to:

- Open an **issue** to report bugs or suggest new material/effect types
- Submit a **pull request** with improvements, new reference guides, or fixes
- Fork and adapt for your own projects

### How to contribute

1. Fork this repo
2. Create a branch (`git checkout -b feature/new-material`)
3. Make your changes
4. Commit (`git commit -m "Add ceramic material reference"`)
5. Push (`git push origin feature/new-material`)
6. Open a Pull Request

## License

[MIT](LICENSE) — use it, modify it, share it, sell it, do whatever you want.
