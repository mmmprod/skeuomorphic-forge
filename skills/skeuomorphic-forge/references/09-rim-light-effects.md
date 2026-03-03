# Section 25 — Rim Light Effects

Edge-concentrated light effects for dark UI components. Simulates a backlight or ambient light source bleeding around the edges of opaque objects — commonly seen on dark cards, panels, and containers in modern dark-mode interfaces.

---

## 25.1 Rim Light Physics

Rim light (also called edge light or backlight) occurs when a light source behind or above an object illuminates its contour. In CSS, this creates the illusion that the component exists in a dark environment with subtle ambient lighting.

**Physical properties to simulate:**

| Property | Physical behavior | CSS technique |
|----------|-------------------|---------------|
| **Top edge glow** | Light catches the top rim | `box-shadow` outer (positive Y, white, low opacity) + `::before` radial gradient |
| **Bottom edge glow** | Reflected/ambient light on bottom | `box-shadow` outer (negative Y, white, very low opacity) + `::after` radial gradient |
| **Edge concentration** | Light is brightest at center of each edge, fading toward corners | `radial-gradient` positioned at edge center |
| **Falloff** | Light intensity decreases with distance from edge | Multiple shadow layers with increasing blur and decreasing opacity |

**Critical rule:** Rim light is ALWAYS subtler than direct light. Maximum opacity for rim highlight elements: 0.2 (20%). Going higher creates an unrealistic "glowing border" effect rather than ambient rim light.

---

## 25.2 Dark Card with Rim Light — Box-Shadow + Pseudo-Elements

Production pattern for dark cards with top and bottom rim light accents. Uses a 4-layer box-shadow system + pseudo-element radial gradients for concentrated edge highlights.

### Card foundation

```css
.card {
  position: relative;
  background-image: linear-gradient(0deg,
    rgba(19, 19, 19, 1),
    rgba(17, 17, 17, 1)
  );
  border-radius: 12px;
  padding: 20px;
}
```

### Box-shadow rim light system (4 layers)

```css
.card {
  box-shadow:
    /* 1. Top rim glow — ambient light catching top edge */
    0 -4px 8px 6px rgba(255, 255, 255, 0.05),

    /* 2. Inner top highlight — subtle surface reflection */
    inset 0 -4px 8px -8px rgba(255, 255, 255, 0.15),

    /* 3. Inner top shadow — depth from top surface */
    inset 0 8px 8px 2px rgba(0, 0, 0, 0.03),

    /* 4. Bottom cast shadow — card floating above surface */
    0 4px 8px 6px rgba(0, 0, 0, 0.6);
}
```

**Shadow anatomy:**

| Layer | Direction | Color | Opacity | Role |
|-------|-----------|-------|---------|------|
| 1 | Outer, upward (-4px) | White | 0.05 | Top rim glow — the primary rim light effect |
| 2 | Inset, downward (-4px) | White | 0.15 | Inner top reflection — light entering the surface |
| 3 | Inset, downward (8px) | Black | 0.03 | Top edge shadow — provides depth contrast against highlight |
| 4 | Outer, downward (4px) | Black | 0.6 | Ground shadow — card elevation |

**Key insight:** Layer 1 (outer white upward) and Layer 4 (outer black downward) create the rim light illusion — the top glows while the bottom casts a dark shadow, simulating light coming from above/behind.

### Top rim highlight (::before)

Concentrated bright spot at the top center edge:

```css
.card::before {
  content: '';
  position: absolute;
  top: -1px;
  left: 50%;
  z-index: 1;
  width: 40%;
  height: 1px;

  background:
    /* Sharp center highlight */
    radial-gradient(circle at center top,
      rgba(255, 255, 255, 0.2),
      rgba(255, 255, 255, 0)
    ),
    /* Wider soft glow */
    radial-gradient(circle at center top,
      rgba(255, 255, 255, 0.05) 10%,
      rgba(255, 255, 255, 0) 50%
    );

  filter: blur(0px);
  mix-blend-mode: screen;
  pointer-events: none;
}
```

**Dual radial gradient:** Two overlapping `radial-gradient` at the same position create a bright core (0.2) with a soft halo (0.05) — mimicking how real light has a bright center and soft falloff.

### Bottom rim highlight (::after)

Subtle reflected light at the bottom edge:

```css
.card::after {
  content: '';
  position: absolute;
  bottom: 0px;
  left: 20%;
  z-index: 1;
  width: 70%;
  height: 1px;

  background:
    radial-gradient(circle at center bottom,
      rgba(255, 255, 255, 0.2),
      rgba(255, 255, 255, 0)
    ),
    radial-gradient(circle at center bottom,
      rgba(255, 255, 255, 0.05) 10%,
      rgba(255, 255, 255, 0) 50%
    );

  filter: blur(0px);
  mix-blend-mode: screen;
  pointer-events: none;
}
```

**Asymmetry:** Top is 40% width at center, bottom is 70% width offset left (20%). This asymmetry is intentional — the bottom reflected light is wider but positioned differently than the top direct light, adding physical realism.

### Width scaling for different card sizes

```css
.card-small  { max-width: 200px; }  /* Default pseudo-element widths work */
.card-medium { max-width: 400px; }  /* ::before/::after scale proportionally */
.card-large  { max-width: 600px; }
.card-xlarge { max-width: 700px; }
```

The percentage-based widths (40%, 70%) and positions (50%, 20%) scale automatically with card width.

---

## 25.3 Rim Light Variations

### Colored rim light (accent color)

Replace white with a tinted color for branded rim light:

```css
.card-accent {
  box-shadow:
    0 -4px 8px 6px rgba(59, 130, 246, 0.08),     /* Blue top glow */
    inset 0 -4px 8px -8px rgba(59, 130, 246, 0.2),
    inset 0 8px 8px 2px rgba(0, 0, 0, 0.03),
    0 4px 8px 6px rgba(0, 0, 0, 0.6);
}

.card-accent::before {
  background:
    radial-gradient(circle at center top,
      rgba(59, 130, 246, 0.3),
      rgba(59, 130, 246, 0)
    );
}
```

### Full-perimeter rim light

For objects lit from all sides (e.g., floating in space):

```css
.card-full-rim {
  box-shadow:
    0 -4px 8px 6px rgba(255, 255, 255, 0.04),
    0  4px 8px 6px rgba(255, 255, 255, 0.02),
    -4px 0 8px 6px rgba(255, 255, 255, 0.02),
     4px 0 8px 6px rgba(255, 255, 255, 0.02),
    inset 0 0 0 1px rgba(255, 255, 255, 0.05),
    0 8px 24px rgba(0, 0, 0, 0.4);
}
```

### Animated rim light (hover glow intensification)

```css
.card-animated {
  transition: box-shadow 0.3s ease;
}

.card-animated:hover {
  box-shadow:
    0 -4px 12px 8px rgba(255, 255, 255, 0.10),   /* Intensified top glow */
    inset 0 -4px 8px -8px rgba(255, 255, 255, 0.25),
    inset 0 8px 8px 2px rgba(0, 0, 0, 0.03),
    0 4px 12px 8px rgba(0, 0, 0, 0.7);
}
```

---

## 25.4 Rim Light Recipes Quick Reference

### Recipe 1: Standard dark card with rim light (Tailwind + inline)
```css
class="relative rounded-xl bg-[#131313] p-5"
style="
  box-shadow:
    0 -4px 8px 6px rgba(255,255,255,0.05),
    inset 0 -4px 8px -8px rgba(255,255,255,0.15),
    inset 0 8px 8px 2px rgba(0,0,0,0.03),
    0 4px 8px 6px rgba(0,0,0,0.6);
"
```

### Recipe 2: Minimal rim light (shadow only, no pseudo-elements)
```css
style="
  box-shadow:
    0 -3px 6px 4px rgba(255,255,255,0.04),
    0 3px 6px 4px rgba(0,0,0,0.5);
"
```

### Decision matrix

| Need | Technique | Section |
|------|-----------|---------|
| Standard dark card with top rim | 4-layer box-shadow + ::before/::after | 25.2 |
| Colored/branded rim light | Tinted rgba in shadow + pseudo-elements | 25.3 |
| Floating object (all-side rim) | 4-direction outer shadows + inset border | 25.3 |
| Hover glow intensification | Transition on box-shadow values | 25.3 |

### Opacity guidelines

| Element | Min | Recommended | Max |
|---------|-----|-------------|-----|
| Outer rim shadow (white) | 0.02 | 0.04–0.06 | 0.10 |
| Inner rim highlight | 0.08 | 0.12–0.15 | 0.20 |
| Pseudo-element radial center | 0.10 | 0.15–0.20 | 0.25 |
| Pseudo-element radial halo | 0.02 | 0.04–0.05 | 0.08 |

Going above these maximums creates a "neon border" effect rather than subtle rim light. Rim light should be barely perceptible — the viewer should feel it rather than see it.
