# Skeuomorphic Forge

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

## License

MIT
