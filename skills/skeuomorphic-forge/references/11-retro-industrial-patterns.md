# Retro-Industrial Patterns

Production-ready patterns for vintage 1970s-1990s aerospace/automotive instrumentation UI. All patterns use **warm tones** (hue 25-40) and assume **top-left light source**.

---

## 27. 3-Ring Bezel Assembly

The signature construction for instrument displays. Three concentric rings create a machined housing around a recessed screen/readout.

### Ring 1 — Outer Chassis (Machined Aluminum)

Conic gradient with 7+ warm hue stops simulating curved metal reflection under directional light.

```css
/* Outer ring */
.bezel-outer {
  padding: 6px;
  border-radius: 12px;
  background: conic-gradient(
    from 0deg,
    hsl(35 10% 28%),
    hsl(40 8% 38%),
    hsl(35 12% 32%),
    hsl(30 10% 22%),
    hsl(35 8% 30%),
    hsl(40 10% 36%),
    hsl(35 10% 28%)
  );
  box-shadow:
    0 4px 10px rgba(0,0,0,0.45),
    inset 0 1px 1px rgba(255,255,255,0.08),
    inset 0 -1px 1px rgba(0,0,0,0.7);
}
```

### Ring 2 — Bevel Ring (Chamfered Edge)

Transitional ring between chassis and display well. Creates the machined chamfer effect.

```css
/* Bevel ring */
.bezel-bevel {
  padding: 4px;
  border-radius: 8px;
  background: linear-gradient(
    154deg,
    hsl(35 8% 26%),
    hsl(30 10% 18%),
    hsl(25 12% 14%),
    hsl(30 8% 20%)
  );
  box-shadow:
    inset 0 2px 4px rgba(0,0,0,0.6),
    inset 0 -1px 2px rgba(255,255,255,0.04),
    0 1px 0 rgba(255,255,255,0.03);
}
```

### Ring 3 — Inner Well (CRT-Style Recess)

Deep recessed cavity where the display content lives. Ultra-dark with radial vignette.

```css
/* Inner well */
.bezel-well {
  border-radius: 6px;
  padding: 12px;
  background: radial-gradient(
    ellipse at 50% 30%,
    hsl(30 15% 7%),
    hsl(25 20% 3%),
    hsl(20 20% 1%)
  );
  box-shadow:
    inset 0 5px 14px rgba(0,0,0,0.9),
    inset 0 2px 6px rgba(0,0,0,0.95),
    inset 3px 0 8px rgba(0,0,0,0.4),
    inset -3px 0 8px rgba(0,0,0,0.4),
    inset 0 0 1px rgba(245,158,11,0.3);
}
```

### Complete Assembly (React inline style)

```tsx
const BEZEL_OUTER: React.CSSProperties = {
  padding: 6,
  borderRadius: 12,
  background: `conic-gradient(from 0deg, hsl(35 10% 28%), hsl(40 8% 38%), hsl(35 12% 32%), hsl(30 10% 22%), hsl(35 8% 30%), hsl(40 10% 36%), hsl(35 10% 28%))`,
  boxShadow: '0 4px 10px rgba(0,0,0,0.45), inset 0 1px 1px rgba(255,255,255,0.08), inset 0 -1px 1px rgba(0,0,0,0.7)',
};

const BEZEL_BEVEL: React.CSSProperties = {
  padding: 4,
  borderRadius: 8,
  background: 'linear-gradient(154deg, hsl(35 8% 26%), hsl(30 10% 18%), hsl(25 12% 14%), hsl(30 8% 20%))',
  boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.6), inset 0 -1px 2px rgba(255,255,255,0.04), 0 1px 0 rgba(255,255,255,0.03)',
};

const BEZEL_WELL: React.CSSProperties = {
  borderRadius: 6,
  padding: 12,
  background: 'radial-gradient(ellipse at 50% 30%, hsl(30 15% 7%), hsl(25 20% 3%), hsl(20 20% 1%))',
  boxShadow: 'inset 0 5px 14px rgba(0,0,0,0.9), inset 0 2px 6px rgba(0,0,0,0.95), inset 3px 0 8px rgba(0,0,0,0.4), inset -3px 0 8px rgba(0,0,0,0.4), inset 0 0 1px rgba(245,158,11,0.3)',
};

// Usage:
<div style={BEZEL_OUTER}>
  <div style={BEZEL_BEVEL}>
    <div style={BEZEL_WELL}>
      {/* Display content here */}
    </div>
  </div>
</div>
```

---

## 28. CRT Display Construction

7-layer assembly for authentic CRT monitor/terminal display effect.

### Layer stack (bottom to top)

```tsx
// 1. Screen base — pitch black
const CRT_BASE: React.CSSProperties = {
  background: 'hsl(0 0% 4%)',
  position: 'relative',
  overflow: 'hidden',
};

// 2. Vignette shadow — darkens edges like real CRT
const CRT_VIGNETTE: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'linear-gradient(180deg, rgba(0,0,0,0.65) 0%, transparent 30%, transparent 70%, rgba(0,0,0,0.65) 100%)',
  pointerEvents: 'none',
};

// 3. Inner backlight — warm amber tint from behind
const CRT_BACKLIGHT: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'radial-gradient(ellipse at 50% 50%, rgba(255,220,140,0.05) 0%, transparent 70%)',
  pointerEvents: 'none',
};

// 4. Scanlines — horizontal CRT scan
const CRT_SCANLINES: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'repeating-linear-gradient(0deg, transparent 0px, transparent 2px, rgba(0,0,0,0.06) 2px, rgba(0,0,0,0.06) 3px)',
  pointerEvents: 'none',
};

// 5. Glass reflection — top-left specular highlight
const CRT_SPECULAR: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'radial-gradient(ellipse 60% 30% at 25% 10%, rgba(255,255,255,0.05), transparent)',
  pointerEvents: 'none',
};

// 6. Color accent line — top edge CRT mask
const CRT_ACCENT = (color: string): React.CSSProperties => ({
  position: 'absolute',
  top: 0,
  left: '10%',
  right: '10%',
  height: 1,
  background: `linear-gradient(90deg, transparent, ${color}, transparent)`,
  pointerEvents: 'none',
});

// 7. Content layer — actual text/numbers
const CRT_TEXT: React.CSSProperties = {
  position: 'relative',
  zIndex: 1,
  fontFamily: "'Orbitron', sans-serif",
  fontWeight: 700,
  letterSpacing: '0.05em',
  textTransform: 'uppercase' as const,
};
```

### Phosphor glow per color

```tsx
const phosphorGlow = (color: string, glowColor: string) => ({
  color,
  textShadow: `0 0 4px ${color}, 0 0 10px ${glowColor}`,
});

// Amber (most common for retro-industrial)
phosphorGlow('hsl(35 100% 65%)', 'rgba(255,180,0,0.4)');

// Green (classic terminal)
phosphorGlow('hsl(120 80% 60%)', 'rgba(0,255,100,0.3)');

// Red (warning/critical)
phosphorGlow('hsl(0 90% 60%)', 'rgba(255,50,50,0.3)');
```

---

## 29. LED Indicator System

Multi-shadow halo system for realistic LED indicators.

### LED construction

```tsx
const LED = (color: { core: string; mid: string; halo: string; bg: string }) => ({
  width: 8,
  height: 8,
  borderRadius: '50%',
  background: `radial-gradient(circle at 35% 30%, ${color.core}, ${color.mid}, ${color.bg})`,
  boxShadow: `
    0 0 2px ${color.mid},
    0 0 5px ${color.mid},
    0 0 10px ${color.halo},
    inset 0 -1px 2px rgba(0,0,0,0.5)
  `,
  animation: 'led-pulse 2.4s ease-in-out infinite',
});

// Preset colors
const LED_GREEN  = { core: '#80ffa0', mid: '#30cc55', halo: 'rgba(48,204,85,0.4)', bg: '#1a8833' };
const LED_AMBER  = { core: '#ffd080', mid: '#ffb000', halo: 'rgba(255,176,0,0.4)', bg: '#b87800' };
const LED_RED    = { core: '#ff8080', mid: '#ff3030', halo: 'rgba(255,48,48,0.4)', bg: '#b82020' };
const LED_BLUE   = { core: '#80c0ff', mid: '#3090ff', halo: 'rgba(48,144,255,0.4)', bg: '#1a60b8' };
```

### Pulse animation

```css
@keyframes led-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}
```

### LED with label (silkscreen style)

```tsx
<div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
  <div style={LED(LED_GREEN)} />
  <span style={{
    fontFamily: 'monospace',
    fontSize: 10,
    fontWeight: 600,
    letterSpacing: '0.12em',
    textTransform: 'uppercase',
    color: 'rgba(255,255,255,0.06)',
    textShadow: '0 1px 0 rgba(0,0,0,0.9)',
  }}>
    SIGNAL
  </span>
</div>
```

---

## 30. Torx Screw

Decorative mounting hardware with realistic radial gradient and slot shadow.

```tsx
const SCREW_SIZE = 14;

const TorxScrew = () => (
  <div style={{
    width: SCREW_SIZE,
    height: SCREW_SIZE,
    borderRadius: '50%',
    background: `radial-gradient(circle at 32% 26%, hsl(40 15% 50%), hsl(35 18% 38%), hsl(30 20% 25%), hsl(25 22% 15%))`,
    boxShadow: `
      inset 0 2px 4px rgba(0,0,0,0.95),
      inset 0 -1px 1px rgba(255,255,255,0.08),
      0 1px 3px rgba(0,0,0,0.5)
    `,
    position: 'relative',
  }}>
    {/* Horizontal slot */}
    <div style={{
      position: 'absolute',
      top: '50%',
      left: '25%',
      right: '25%',
      height: 1,
      background: 'rgba(0,0,0,0.8)',
      transform: 'translateY(-50%)',
      boxShadow: '0 1px 0 rgba(255,255,255,0.05)',
    }} />
    {/* Vertical slot */}
    <div style={{
      position: 'absolute',
      left: '50%',
      top: '25%',
      bottom: '25%',
      width: 1,
      background: 'rgba(0,0,0,0.8)',
      transform: 'translateX(-50%)',
      boxShadow: '1px 0 0 rgba(255,255,255,0.05)',
    }} />
  </div>
);
```

---

## 31. SVG feTurbulence Texture Overlay

Add cast-iron or noise texture to any surface using inline SVG filter.

### Cast iron texture

```tsx
const NOISE_SVG = `data:image/svg+xml,${encodeURIComponent(`
  <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
    <filter id="n">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="4" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <rect width="200" height="200" filter="url(#n)" opacity="0.08"/>
  </svg>
`)}`;

// Apply as background layer
const CAST_IRON: React.CSSProperties = {
  background: `url("${NOISE_SVG}"), linear-gradient(142deg, hsl(40 10% 16%), hsl(35 12% 11%), hsl(30 14% 8%))`,
};
```

### Fine metal grain

```tsx
// Higher frequency = finer grain
const FINE_GRAIN_SVG = `data:image/svg+xml,${encodeURIComponent(`
  <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
    <filter id="n">
      <feTurbulence type="fractalNoise" baseFrequency="2.5" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <rect width="200" height="200" filter="url(#n)" opacity="0.04"/>
  </svg>
`)}`;
```

### Brushed metal texture (directional)

```css
/* Repeating fine lines simulating brush marks */
background: repeating-linear-gradient(
  155deg,
  transparent,
  rgba(255,255,255,0.01) 1px,
  transparent 2px
);
```

---

## 32. Glitch / Holographic Input

CRT-style input fields with corner brackets, scanline overlay, and data stream glitch effect.

### Structure

```html
<div class="glitch-input-wrapper">
  <div class="glitch-input-container">
    <input class="holo-input" />
    <div class="input-border" />
    <div class="input-corners">
      <span class="corner tl" /><span class="corner tr" />
      <span class="corner bl" /><span class="corner br" />
    </div>
    <div class="input-scanline" />
    <div class="input-glow" />
    <div class="input-data-stream" />
  </div>
</div>
```

### Key CSS patterns

```css
/* Base input — transparent with monospace font */
.holo-input {
  background: transparent;
  border: none;
  color: hsl(35 80% 65%);
  font-family: 'Share Tech Mono', monospace;
  letter-spacing: 0.05em;
  caret-color: hsl(35 100% 60%);
}

/* Corner brackets — CRT monitor bezel accents */
.corner {
  position: absolute;
  width: 8px;
  height: 8px;
  border-color: hsl(35 60% 40%);
  border-style: solid;
  border-width: 0;
}
.corner.tl { top: 0; left: 0; border-top-width: 1px; border-left-width: 1px; }
.corner.tr { top: 0; right: 0; border-top-width: 1px; border-right-width: 1px; }
.corner.bl { bottom: 0; left: 0; border-bottom-width: 1px; border-left-width: 1px; }
.corner.br { bottom: 0; right: 0; border-bottom-width: 1px; border-right-width: 1px; }

/* Scanline sweep */
.input-scanline {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(255,200,100,0.03) 50%,
    transparent 100%
  );
  animation: scanline-sweep 3s linear infinite;
  pointer-events: none;
}

@keyframes scanline-sweep {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100%); }
}

/* Data stream glitch bars */
.input-data-stream {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px,
    transparent 8px,
    rgba(255,180,50,0.02) 8px,
    rgba(255,180,50,0.02) 9px
  );
  animation: data-glitch 0.1s steps(3) infinite;
  pointer-events: none;
}

@keyframes data-glitch {
  0% { clip-path: inset(0 0 80% 0); }
  33% { clip-path: inset(30% 0 40% 0); }
  66% { clip-path: inset(60% 0 10% 0); }
  100% { clip-path: inset(0 0 80% 0); }
}
```

---

## 33. Mechanical Counter (Rolling Digits)

Odometer-style digit display with rolling animation.

### Digit well construction

```tsx
const DIGIT_WELL: React.CSSProperties = {
  background: 'linear-gradient(180deg, #000 0%, #0a0a0a 50%, #000 100%)',
  position: 'relative',
  overflow: 'hidden',
  width: 28,
  padding: '8px 0',
  textAlign: 'center',
};

// Vignette overlay (top/bottom darkness)
const DIGIT_VIGNETTE: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'linear-gradient(180deg, rgba(0,0,0,0.65) 0%, transparent 30%, transparent 70%, rgba(0,0,0,0.65) 100%)',
  pointerEvents: 'none',
};

// Inner backlight (warm amber)
const DIGIT_BACKLIGHT: React.CSSProperties = {
  position: 'absolute',
  inset: 0,
  background: 'radial-gradient(ellipse at 50% 50%, rgba(255,220,140,0.05), transparent 70%)',
  pointerEvents: 'none',
};

// Digit style
const DIGIT_TEXT: React.CSSProperties = {
  fontFamily: "'Orbitron', sans-serif",
  fontWeight: 700,
  fontSize: 20,
  color: 'hsl(40 60% 72%)',    // aged amber/cream
  textShadow: '0 0 6px rgba(255,200,100,0.3)',
  position: 'relative',
  zIndex: 1,
};
```

### Rolling animation (React)

```tsx
const rollDigit = (target: number, onComplete: () => void) => {
  let frame = 0;
  const totalFrames = 10;
  const interval = setInterval(() => {
    frame++;
    if (frame >= totalFrames) {
      clearInterval(interval);
      onComplete();
      return;
    }
    // Show random digit during roll
    setDisplayDigit(Math.floor(Math.random() * 10));
  }, 50);
  // Final frame shows target
  setTimeout(() => setDisplayDigit(target), totalFrames * 50);
};
```

---

## 34. Deep Chassis Hole (Ultra-Recess Display Mount)

Advanced variant of the 3-ring bezel that creates an **extreme depth illusion** — the display appears to sit deep inside a machined cavity. Uses 30+ box-shadow layers for omnidirectional darkness.

### Chassis hole construction

The key innovation: shadows attack from **all 8 directions** (top, bottom, left, right, and 4 diagonals) with progressive blur distances, creating a tunnel-like depth.

```css
.chassis-hole {
  position: relative;
  padding: 5px 6px 8px 6px;
  border-radius: 16px;
  background: radial-gradient(ellipse 100% 100% at 50% 50%, #000 0%, #020202 70%, #080808 100%);
  box-shadow:
    /* === TOP EDGE (7 layers, progressive depth) === */
    inset 0 1px 0 #000,
    inset 0 2px 0 #000,
    inset 0 3px 1px #000,
    inset 0 4px 4px rgba(0,0,0,1),
    inset 0 8px 10px rgba(0,0,0,1),
    inset 0 14px 18px rgba(0,0,0,0.95),
    inset 0 22px 30px rgba(0,0,0,0.85),
    inset 0 32px 50px rgba(0,0,0,0.6),
    /* === LEFT EDGE (5 layers) === */
    inset 1px 0 0 #000,
    inset 2px 0 0 #000,
    inset 6px 0 8px rgba(0,0,0,1),
    inset 12px 0 16px rgba(0,0,0,0.9),
    inset 20px 0 24px rgba(0,0,0,0.6),
    /* === RIGHT EDGE (5 layers) === */
    inset -1px 0 0 #000,
    inset -2px 0 0 #000,
    inset -6px 0 8px rgba(0,0,0,1),
    inset -12px 0 16px rgba(0,0,0,0.9),
    inset -20px 0 24px rgba(0,0,0,0.6),
    /* === BOTTOM EDGE (5 layers) === */
    inset 0 -4px 4px rgba(0,0,0,1),
    inset 0 -8px 10px rgba(0,0,0,1),
    inset 0 -14px 18px rgba(0,0,0,0.95),
    inset 0 -22px 30px rgba(0,0,0,0.85),
    inset 0 -32px 50px rgba(0,0,0,0.6),
    /* === DIAGONAL CORNERS (4 layers) === */
    inset 10px 10px 18px rgba(0,0,0,0.9),
    inset -10px 10px 18px rgba(0,0,0,0.9),
    inset 10px -10px 18px rgba(0,0,0,0.9),
    inset -10px -10px 18px rgba(0,0,0,0.9),
    /* === EXTERNAL (lip highlight + drop shadow) === */
    0 1px 0 rgba(255,255,255,0.05),
    0 2px 0 rgba(255,255,255,0.02),
    0 -1px 0 rgba(0,0,0,0.9),
    0 -2px 4px rgba(0,0,0,0.6),
    0 6px 24px rgba(0,0,0,0.6),
    0 12px 48px rgba(0,0,0,0.4);
  border-top: 1px solid #000;
  border-left: 1px solid #010101;
  border-right: 1px solid #010101;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
```

### Colored rim bleed (::before)

A subtle colored glow at the top edge where the display light "bleeds" through the chassis gap.

```css
.chassis-hole::before {
  content: '';
  position: absolute;
  top: -1px;
  left: 12%;
  width: 76%;
  height: 1px;
  z-index: 25;
  pointer-events: none;
  /* Change rgba(255,65,45,...) to match display color */
  background: radial-gradient(ellipse 55% 100% at 50% 50%,
    rgba(255,65,45,0.45) 0%,
    rgba(255,55,35,0.18) 45%,
    transparent 100%);
  box-shadow: 0 0 2px rgba(255,60,40,0.15);
}
```

### Directional vignette (::after)

5-layer overlay that darkens all edges independently, creating a tunnel perspective.

```css
.chassis-hole::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  pointer-events: none;
  z-index: 1;
  background:
    linear-gradient(180deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 20%, transparent 45%),
    linear-gradient(90deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.2) 15%, transparent 35%),
    linear-gradient(270deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.2) 15%, transparent 35%),
    linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 20%, transparent 45%),
    radial-gradient(ellipse 100% 100% at 50% 50%, transparent 40%, rgba(0,0,0,0.3) 80%, rgba(0,0,0,0.6) 100%);
}
```

### Screen glass (display inside the hole)

Multi-layer glass surface with colored gradient base, deep inset shadows, and 6-layer specular reflection.

```css
.screen-glass {
  position: relative;
  width: 420px;
  min-height: 90px;
  border-radius: 10px;
  overflow: hidden;
  /* Colored gradient base — change rgba(80,8,4) to match theme */
  background: linear-gradient(270deg,
    rgba(80,8,4,0.7) 0%,
    rgba(40,4,2,0.5) 40%,
    #020101 75%);
  box-shadow:
    0 0 0 1px rgba(255,80,50,0.8),      /* color border */
    0 0 8px 1px rgba(255,60,40,0.25),    /* outer glow */
    0 4px 12px rgba(255,40,20,0.15),     /* cast glow */
    inset 0 18px 20px -10px rgba(0,0,0,1),
    inset 0 -18px 20px -10px rgba(0,0,0,1),
    inset 24px 0 24px -12px rgba(0,0,0,1),
    inset 40px 0 35px -15px rgba(0,0,0,1),
    inset 60px 0 50px -20px rgba(0,0,0,0.95),
    inset 80px 0 60px -25px rgba(0,0,0,0.85),
    inset 110px 0 80px -30px rgba(0,0,0,0.6),
    inset -24px 0 24px -12px rgba(0,0,0,1);
}

/* 6-layer glass reflection */
.screen-glass::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  z-index: 15;
  background:
    radial-gradient(ellipse 160% 45% at 50% -8%, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.06) 35%, transparent 50%),
    radial-gradient(ellipse 40% 25% at 30% 8%, rgba(255,255,255,0.1) 0%, transparent 70%),
    linear-gradient(125deg, transparent 20%, rgba(255,255,255,0.025) 24%, rgba(255,255,255,0.05) 28%, rgba(255,255,255,0.025) 32%, transparent 36%),
    radial-gradient(ellipse 60% 50% at 50% 50%, rgba(255,255,255,0.012) 0%, transparent 70%),
    radial-gradient(ellipse 50% 12% at 50% 98%, rgba(255,255,255,0.03) 0%, transparent 80%),
    linear-gradient(90deg, rgba(255,255,255,0.025) 0%, transparent 2.5%);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.08),
    inset 0 2px 4px rgba(255,255,255,0.02),
    inset 0 -1px 0 rgba(255,255,255,0.02);
}
```

### Phosphor text (content inside screen)

```css
.phosphor-title {
  font-family: 'Space Mono', monospace;
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 6px;
  color: #ff6b5a;
  text-shadow:
    0 0 1px rgba(255,107,90,1),
    0 0 6px rgba(255,80,60,0.7),
    0 0 12px rgba(255,40,20,0.3);
  animation: text-breathe 4s infinite ease-in-out;
}

@keyframes text-breathe {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.9; }
}
```

**Color variants** — replace red values to theme the entire assembly:

| Theme | Phosphor color | Glow base | Rim bleed |
|---|---|---|---|
| **Red/Danger** | `#ff6b5a` | `rgba(255,80,60,...)` | `rgba(255,65,45,...)` |
| **Amber/Warm** | `#ffb060` | `rgba(255,160,60,...)` | `rgba(255,150,45,...)` |
| **Green/Status** | `#60ff90` | `rgba(60,255,100,...)` | `rgba(45,255,65,...)` |
| **Blue/Info** | `#60a0ff` | `rgba(60,120,255,...)` | `rgba(45,100,255,...)` |

**Full working demo**: `assets/codepen-deep-screen.html`

---

## Quick Reference — Retro-Industrial Decision Matrix

| Building... | Use pattern | Key technique |
|---|---|---|
| Instrument readout | 27 (3-ring bezel) + 28 (CRT) | Conic gradient chassis + scanline display |
| Deep-set display | 34 (chassis hole) + 28 (CRT) | 30+ shadow omnidirectional depth + glass |
| Status indicator | 29 (LED system) | Multi-shadow halo + pulse animation |
| Mounting panel | 30 (Torx screws) + file 01 raised surface | Cast iron texture + corner screws |
| Text input field | 32 (Glitch input) | Corner brackets + scanline sweep |
| Numeric display | 33 (Mechanical counter) | Rolling digits + digit well + vignette |
| Metal surface | 31 (feTurbulence) | SVG noise overlay + warm gradient |
| Panel label | Section 28 phosphor glow | Silkscreen or phosphor text-shadow |
| Warning/alert screen | 34 (chassis hole, red theme) | Color-themed phosphor + rim bleed |
| Concave toggle/header | 35 (Concave button) | 15-layer inset shadow + mask-composite rim light |
| Equipment faceplate | 36 (Faceplate panel) | 6-layer stack (dots, noise, vignette, glass, projection) |
| Glass dome icon | 36 (icon-dome) | 3-ring well → mid-ring → convex dome specular |
| Frequency analyzer | 37 (Analyzer screen) | SVG filter neon glow + Butterworth curves + FFT bars |
| Anomaly warning | 38 (Erratic curve) | 60-seed chaotic sine sum + fog blur + warning overlay |
| 3D push button | 39 (Glow projection button) | 14px translateY travel + massive glow + rim light bleed |

---

## 35. Concave Button (Folding Header)

An input/trigger button that appears **pressed into** the panel rather than raised above it. Uses 15 inset box-shadow layers attacking from all directions to create a bowl-like concavity.

### Concave shadow construction

```css
.concave-button {
  background: #232128;
  border-radius: 12px;
  padding: 18px 24px;
  cursor: pointer;
  position: relative;
  box-shadow:
    /* TOP (3 progressive depths) */
    inset 0 8px 14px -3px rgba(0,0,0,0.75),
    inset 0 4px 6px -1px rgba(0,0,0,0.6),
    inset 0 2px 2px rgba(0,0,0,0.5),
    /* LEFT (2 depths) */
    inset 6px 0 10px -4px rgba(0,0,0,0.55),
    inset 3px 0 4px -1px rgba(0,0,0,0.35),
    /* RIGHT (2 depths) */
    inset -6px 0 10px -4px rgba(0,0,0,0.55),
    inset -3px 0 4px -1px rgba(0,0,0,0.35),
    /* DIAGONAL CORNERS (4 layers) */
    inset 5px 5px 8px -3px rgba(0,0,0,0.4),
    inset -5px 5px 8px -3px rgba(0,0,0,0.4),
    inset 4px -3px 6px -3px rgba(0,0,0,0.15),
    inset -4px -3px 6px -3px rgba(0,0,0,0.15),
    /* BOTTOM (catch light — simulates light bouncing off lip) */
    inset 0 -3px 6px -2px rgba(255,255,255,0.035),
    inset 0 -1px 1px rgba(255,255,255,0.05),
    /* EXTERNAL (panel surface continuity) */
    0 -1px 0 rgba(255,255,255,0.05),
    0 1px 0 rgba(0,0,0,0.25);
  border-top: 1px solid #08070a;
  border-left: 1px solid #08070a;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  border-right: 1px solid rgba(255,255,255,0.04);
  transition: box-shadow 0.1s ease;
}
```

### Mask-composite rim light

The amber rim light uses the **CSS mask-composite trick** — two layers with `xor`/`exclude` compositing to create a border-only gradient.

```css
/* Sharp inner glow ring */
.inner-well::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: radial-gradient(circle at 0 0,
    rgba(255,139,61,0.85) 0%,
    rgba(255,139,61,0.3) 6%,
    transparent 15%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box,
               linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
  z-index: 5;
  filter: drop-shadow(0 0 3px rgba(255,139,61,0.6));
}

/* Blurred outer halo */
.inner-well::after {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 2px;
  background: radial-gradient(circle at 0 0,
    rgba(255,139,61,0.6) 0%,
    rgba(255,139,61,0.15) 8%,
    transparent 20%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box,
               linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
  z-index: 4;
  filter: blur(6px) drop-shadow(0 0 8px rgba(255,139,61,0.3));
  mix-blend-mode: screen;
}
```

### Folding content animation

```css
.folding-content {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease;
}
.folding-content.open {
  max-height: 500px;
  opacity: 1;
  padding-top: 16px;
}
```

**Full working demo**: `assets/codepen-folding-header.html`

---

## 36. Faceplate Panel (Equipment Module)

Full industrial module faceplate with 6 decorative layers, machined icon dome, vertical separators, and a bottom status bar.

### 6-layer panel stack

```css
/* 1. BACKPLATE — outer chassis bevel */
.backplate {
  padding: 5px;
  border-radius: 34px;
  background: linear-gradient(145deg, #2e3238, #1e2226);
  box-shadow:
    6px 6px 22px rgba(0,0,0,0.6),
    -3px -3px 10px rgba(50,55,65,0.05),
    0 14px 40px rgba(0,0,0,0.45),
    inset 0 1px 0 rgba(255,255,255,0.06),
    inset 0 -1px 0 rgba(0,0,0,0.4);
}

/* 2. PANEL — inner faceplate */
.panel {
  position: relative;
  background: linear-gradient(180deg, #1a1d20 0%, #24282c 10%, #16191c 50%, #0d0f11 100%);
  border-radius: 30px;
  overflow: hidden;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.06),
    inset 0 -1px 0 rgba(0,0,0,0.6);
}

/* 3. DOT TEXTURE — perforated metal effect */
.dots {
  position: absolute; inset: 0;
  pointer-events: none; z-index: 1;
  background-image: radial-gradient(rgba(0,0,0,0.6) 1px, transparent 1px);
  background-size: 6px 6px;
  opacity: 0.4;
}

/* 4. NOISE OVERLAY */
.noise {
  position: absolute; inset: 0;
  pointer-events: none; z-index: 2;
  background-image: url("data:image/svg+xml,...feTurbulence...");
  mix-blend-mode: overlay;
  opacity: 0.35;
}

/* 5. EDGE VIGNETTE — all-border darkening */
.edge-vignette {
  position: absolute; inset: 0;
  pointer-events: none; z-index: 4;
  box-shadow:
    /* Top edge (strongest) */
    inset 0 12px 20px -4px rgba(0,0,0,0.6),
    inset 0 6px 8px -2px rgba(0,0,0,0.4),
    /* Bottom edge */
    inset 0 -10px 18px -4px rgba(0,0,0,0.5),
    inset 0 -5px 6px -2px rgba(0,0,0,0.3),
    /* Left + right edges */
    inset 12px 0 18px -4px rgba(0,0,0,0.45),
    inset 5px 0 6px -2px rgba(0,0,0,0.25),
    inset -12px 0 18px -4px rgba(0,0,0,0.45),
    inset -5px 0 6px -2px rgba(0,0,0,0.25),
    /* Diagonal corners */
    inset 8px 8px 14px -4px rgba(0,0,0,0.3),
    inset -8px 8px 14px -4px rgba(0,0,0,0.3),
    inset 8px -8px 14px -4px rgba(0,0,0,0.3),
    inset -8px -8px 14px -4px rgba(0,0,0,0.3);
}

/* 6. GLASS REFLECTION */
.glass-reflection {
  position: absolute; inset: 0;
  pointer-events: none; z-index: 3;
  background: linear-gradient(135deg,
    rgba(255,255,255,0.02) 0%, transparent 40%, rgba(0,0,0,0.1) 100%);
}
```

### Icon glass dome (3-ring construction)

A convex glass indicator with the display icon inside.

```css
/* Ring 1 — Icon well (deep recess) */
.icon-well {
  background: #020304;
  border-radius: 50%;
  padding: 4px;
  box-shadow:
    inset 0 6px 14px rgba(0,0,0,0.9),
    inset 0 2px 4px rgba(0,0,0,1),
    inset 3px 0 8px rgba(0,0,0,0.5),
    inset -3px 0 8px rgba(0,0,0,0.5),
    inset 0 -3px 6px rgba(255,255,255,0.015),
    0 1px 0 rgba(255,255,255,0.06),
    0 4px 12px rgba(0,0,0,0.4);
}

/* Ring 2 — Machined step */
.icon-mid-ring {
  background: linear-gradient(180deg, #0a0b0d, #141618, #0a0b0d);
  border-radius: 50%;
  padding: 2px;
  box-shadow:
    inset 0 1px 3px rgba(0,0,0,0.7),
    inset 0 -1px 2px rgba(255,255,255,0.02),
    0 1px 0 rgba(255,255,255,0.03);
}

/* Ring 3 — Glass dome */
.icon-dome {
  position: relative;
  width: 68px; height: 68px;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 60%, #1a0808, #0c0305, #050102);
  box-shadow:
    inset 0 0 25px rgba(0,0,0,0.7),
    inset 0 4px 8px rgba(0,0,0,0.6),
    inset 0 8px 16px rgba(0,0,0,0.3),
    inset 0 -3px 6px rgba(255,26,26,0.05),
    inset 4px 0 8px rgba(0,0,0,0.4),
    inset -4px 0 8px rgba(0,0,0,0.4),
    0 0 8px rgba(255,26,26,0.06);
  overflow: hidden;
}

/* Dome convex specular (5 highlights) */
.icon-dome::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: 50%;
  pointer-events: none; z-index: 10;
  background:
    /* Primary apex */
    radial-gradient(ellipse 30% 22% at 45% 22%,
      rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.06) 50%, transparent 100%),
    /* Wider diffuse */
    radial-gradient(ellipse 55% 40% at 48% 28%,
      rgba(255,255,255,0.06) 0%, transparent 100%),
    /* Secondary catch */
    radial-gradient(ellipse 25% 18% at 65% 72%,
      rgba(255,255,255,0.035) 0%, transparent 100%),
    /* Left rim */
    radial-gradient(ellipse 12% 50% at 12% 45%,
      rgba(255,255,255,0.03) 0%, transparent 100%),
    /* Convex edge vignette */
    radial-gradient(circle at 50% 50%,
      transparent 40%, rgba(0,0,0,0.25) 70%, rgba(0,0,0,0.5) 100%);
}
```

### Projected color light on panel surface

```css
.color-projection {
  position: absolute; z-index: 4; pointer-events: none;
  width: 500px; height: 200px;
  left: 50%; top: 40%; transform: translate(-50%, -50%);
  background: radial-gradient(ellipse 80% 70% at 50% 50%,
    rgba(255,26,26,0.04) 0%,
    rgba(255,26,26,0.015) 40%,
    transparent 70%);
  animation: proj-pulse 3s infinite ease-in-out;
}
```

### Vertical separator (machined groove)

```css
.v-separator {
  width: 2px; align-self: stretch;
  background: linear-gradient(180deg, transparent, #080a0c 20%, #080a0c 80%, transparent);
  box-shadow: 1px 0 0 rgba(255,255,255,0.02), -1px 0 0 rgba(0,0,0,0.5);
  margin: 8px 0;
}
```

### Bottom status bar

```css
.bottom-groove {
  height: 2px;
  background: #080a0c;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.8), 0 1px 0 rgba(255,255,255,0.03);
}
.bottom-bar {
  background: linear-gradient(180deg, #1e2226, #12151a 40%, #0a0c0e);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
}
```

**Full working demo**: `assets/codepen-autochord-ui.html`

---

## 37. Frequency Analyzer Screen (Animated SVG)

A CRT-embedded frequency response analyzer with morphing Butterworth curves, FFT bars, neon glow, and log-frequency grid. Designed for DSP crossover visualization.

### Screen construction (chassis + bezel)

```css
.chassis {
  background: linear-gradient(180deg, #2a2c31 0%, #15171a 100%);
  padding: 2px; border-radius: 16px;
  box-shadow: 0 60px 100px -20px rgba(0,0,0,1),
              0 20px 40px rgba(0,0,0,0.9),
              0 0 0 1px rgba(255,255,255,0.05);
}
.chassis-inner {
  background: linear-gradient(135deg, #121316, #08090a);
  padding: 36px; border-radius: 15px;
  border-top: 1px solid rgba(255,255,255,0.08);
  border-bottom: 1px solid rgba(0,0,0,1);
  box-shadow: inset 0 6px 15px rgba(0,0,0,0.8);
}
.screen-bezel {
  position: relative;
  background-color: #020304; border-radius: 10px;
  box-shadow:
    inset 0 35px 60px -10px rgba(0,0,0,1),
    inset 0 0 30px 10px rgba(0,0,0,1),
    inset 0 2px 2px rgba(0,0,0,1),
    0 1px 0 rgba(255,255,255,0.12);
  border-top: 3px solid #000; border-left: 3px solid #000;
  border-bottom: 1px solid #22252a; border-right: 1px solid #15181c;
  overflow: hidden;
}
```

### SVG neon glow filters

```xml
<!-- Blue neon for curves -->
<filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="5" result="blur" />
  <feMerge>
    <feMergeNode in="blur" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>

<!-- Amber for warnings/indicators -->
<filter id="amberGlow" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur stdDeviation="10" result="g" />
  <feMerge>
    <feMergeNode in="g" />
    <feMergeNode in="g" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

### Butterworth curve math (4th order, 24dB/oct)

```tsx
const butterworth4 = (fRatio: number) => {
  const f4 = Math.pow(fRatio, 4);
  return 1 / Math.sqrt(1 + f4);
};

// HPF at fc=2000Hz
const hpfDb = (freq: number) => {
  const mag = butterworth4(2000 / freq);
  return 20 * Math.log10(Math.max(mag, 0.0001));
};

// LPF at fc=500Hz
const lpfDb = (freq: number) => {
  const mag = butterworth4(freq / 500);
  return 20 * Math.log10(Math.max(mag, 0.0001));
};
```

### Log-frequency axis helpers

```tsx
const LOG_MIN = Math.log10(20);
const LOG_MAX = Math.log10(20000);
const LOG_RANGE = LOG_MAX - LOG_MIN;

const freqToX = (hz: number, plotWidth: number, marginLeft: number) =>
  ((Math.log10(hz) - LOG_MIN) / LOG_RANGE) * plotWidth + marginLeft;
```

### Scanline + glass overlays

```css
.scanlines {
  position: absolute; inset: 0;
  background: linear-gradient(to bottom,
    rgba(255,255,255,0) 0%,
    rgba(255,255,255,0) 50%,
    rgba(0,0,0,0.1) 50%,
    rgba(0,0,0,0.1) 100%);
  background-size: 100% 4px;
  pointer-events: none; z-index: 40;
}
.glass-reflection {
  position: absolute; inset: 0;
  background:
    linear-gradient(110deg, rgba(255,255,255,0.01) 0%, rgba(255,255,255,0.06) 30%, transparent 31%),
    radial-gradient(150% 100% at 50% -25%, rgba(255,255,255,0.05) 0%, transparent 45%);
  pointer-events: none; z-index: 50;
  mix-blend-mode: screen;
}
```

**Full working demo**: `assets/codepen-curve-search.html`

---

## 38. Erratic/Anomaly Curve (Warning State)

Variant of the analyzer screen (pattern 37) showing a **chaotic, unpredictable curve** for anomaly/error states. Uses sum-of-sines with 60 random seeds for organic randomness.

### Chaotic curve generation

```tsx
// 60 random seeds for organic chaos
const seeds = Array.from({ length: 60 }, () => ({
  amp: (Math.random() - 0.5) * 2,
  freq: 0.5 + Math.random() * 3,
  phase: Math.random() * Math.PI * 2,
  drift: (Math.random() - 0.5) * 0.01,
}));

// Build erratic curve: sum oscillations + spike regions
const buildErratic = (time: number) => {
  const pts = [];
  for (let i = 0; i <= 300; i++) {
    const norm = i / 300;
    let y = zeroDbY;
    // Sum chaotic oscillations
    for (const seed of seeds) {
      y += seed.amp * 18 * Math.sin(
        norm * seed.freq * 12 + seed.phase + time * 0.3
      );
    }
    // Sharp spikes at specific frequency regions
    if (norm > 0.15 && norm < 0.25) y -= 45 + Math.sin(time * 0.5) * 10;
    if (norm > 0.4 && norm < 0.48) y += 55 + Math.sin(time * 0.7) * 8;
    if (norm > 0.6 && norm < 0.65) y -= 35;
    if (norm > 0.78 && norm < 0.85) y += 40 + Math.sin(time * 0.4) * 12;
    if (norm > 0.9) y += (norm - 0.9) * 300;  // High-freq rolloff
    pts.push(Math.max(60, Math.min(420, y)));
  }
  return pts;
};
```

### Fog/haze effect (SVG filters)

```xml
<!-- Heavy atmospheric fog -->
<filter id="heavyFog" x="-10%" y="-10%" width="120%" height="120%">
  <feGaussianBlur stdDeviation="12" />
</filter>

<!-- Medium blur for curve strokes -->
<filter id="fogBlur" x="-10%" y="-10%" width="120%" height="120%">
  <feGaussianBlur stdDeviation="6" result="fog" />
  <feMerge>
    <feMergeNode in="fog" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

### Warning overlay construction

```xml
<!-- Semi-transparent backdrop + glowing text -->
<rect x="200" y="170" width="600" height="90" rx="8"
  fill="rgba(0,0,0,0.65)" stroke="rgba(255,68,34,0.25)" />
<text x="500" y="210" fill="#ff6644" font-size="38" font-weight="700"
  text-anchor="middle" filter="url(#warningGlow)">
  DIFFERENT CURVE
</text>
<text x="500" y="242" fill="#ff4422" font-size="17" font-weight="600"
  text-anchor="middle" opacity="0.7" filter="url(#softGlow)">
  VERIFICATION REQUIRED
</text>
```

### Color scheme (red/amber fog vs blue/cyan normal)

| State | Curve stroke | Fill gradient | Ambient glow | Badge text |
|---|---|---|---|---|
| **Normal** (37) | `#38bdf8` cyan | `#0ea5e9` → `#020617` | `#0a1830` blue | `DSP CROSSOVER — SCANNING` |
| **Anomaly** (38) | `#ff6644` red-orange | `#ff4422` → `#020617` | `#100808` red | `DSP CROSSOVER — ANOMALY DETECTED` |

**Full working demo**: `assets/codepen-different-curve.html`

---

## 39. Glow Projection Push Button

A 3D push button with **massive** color glow that bleeds onto neighboring elements. Features 14px physical travel depth, per-color specular, and rim light from adjacent button colors.

### Socket well (button housing)

```css
.socket {
  background: #050607;
  padding: 3px;
  border-radius: 20px;
  box-shadow: inset 0 8px 16px rgba(0,0,0,0.8);
  position: relative;
  z-index: 1;
}
```

### Glow projection (bleeds onto neighbors)

The key effect: `::before` with `inset: -15px` + `blur(10px)` on the socket, creating a massive colored glow that extends beyond the button bounds and illuminates adjacent elements.

```css
/* Orange glow (FX button) */
.socket-fx.glow::before {
  content: '';
  position: absolute;
  inset: -15px;
  border-radius: 30px;
  background: radial-gradient(circle at center,
    rgba(255,60,0,0.45) 0%,
    rgba(255,60,0,0.1) 50%,
    transparent 80%);
  filter: blur(10px);
  pointer-events: none;
  z-index: -1;
}

/* Blue glow (MIC button) */
.socket-mic.glow::before {
  content: '';
  position: absolute;
  inset: -15px;
  border-radius: 30px;
  background: radial-gradient(circle at center,
    rgba(0,130,255,0.45) 0%,
    rgba(0,130,255,0.1) 50%,
    transparent 80%);
  filter: blur(10px);
  pointer-events: none;
  z-index: -1;
}
```

### Button OFF state (raised dark slab)

```css
.btn-base {
  width: 240px; height: 120px;
  border-radius: 16px;
  cursor: pointer;
  position: relative;
  transition: all 0.15s cubic-bezier(0.2, 0, 0, 1);
  /* Raised slab */
  background: linear-gradient(145deg, #2d2f35 0%, #16171a 100%);
  border: 1px solid #3a3d45;
  /* 14px physical travel depth */
  transform: translateY(-14px);
  box-shadow:
    0 4px 0 #0d0e10,
    0 10px 0 #08090a,
    0 14px 0 #040506,
    0 18px 30px rgba(0,0,0,0.8),
    inset 2px 2px 5px rgba(255,255,255,0.08),
    inset -2px -2px 8px rgba(0,0,0,0.7);
}

/* Glass highlight */
.btn-base::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 50%);
  z-index: 1; pointer-events: none;
}

/* Press action */
.btn-base:active {
  transform: translateY(-1px);
  box-shadow:
    0 1px 0 #08090a,
    inset 1px 1px 4px rgba(0,0,0,0.9);
}
```

### Button ON state (orange / FX)

```css
.btn-fx.active {
  background: radial-gradient(circle at center, #ffa05d 0%, #ff4d00 45%, #9b1d00 100%);
  border: 1px solid rgba(80,30,0,0.5);
  transform: translateY(-16px);
  box-shadow:
    /* Massive glow projection */
    0 0 50px rgba(255,60,0,0.7),
    /* Thickness steps (side walls) */
    0 4px 0 #7a1800,
    0 8px 0 #5a1100,
    0 12px 0 #3a0a00,
    0 16px 20px rgba(0,0,0,0.9),
    /* Internal lighting */
    inset 0 18px 22px rgba(255,255,255,0.6),
    inset 0 -12px 30px rgba(0,0,0,0.8);
}

/* Specular hotspot (not flat glass) */
.btn-fx.active::before {
  background: radial-gradient(ellipse 55% 40% at 38% 20%,
    rgba(255,255,255,0.2) 0%,
    rgba(255,200,150,0.05) 60%,
    transparent 100%);
}
```

### Button ON state (blue / MIC)

```css
.btn-mic.active {
  background: radial-gradient(circle at center, #5dc8ff 0%, #0084ff 50%, #003d7a 100%);
  border: 1px solid rgba(0,30,80,0.5);
  transform: translateY(-16px);
  box-shadow:
    0 0 50px rgba(0,130,255,0.7),
    0 4px 0 #002d5a,
    0 8px 0 #001a3a,
    0 12px 0 #000d1e,
    0 16px 20px rgba(0,0,0,0.9),
    inset 0 18px 22px rgba(255,255,255,0.5),
    inset 0 -12px 30px rgba(0,0,0,0.8);
}
```

### Rim light from adjacent button

When one button is active, its color bleeds a subtle rim light onto the facing edge of the adjacent button.

```css
/* Orange rim on MIC's left edge (FX is ON) */
.btn-mic.rim-orange::after {
  content: '';
  position: absolute;
  top: 18%; bottom: 18%; left: 0;
  width: 2px;
  border-radius: 1px;
  z-index: 15; pointer-events: none;
  background: linear-gradient(180deg,
    transparent 0%,
    rgba(255,120,40,0.12) 18%,
    rgba(255,120,40,0.55) 50%,
    rgba(255,60,0,0.12) 82%,
    transparent 100%);
  box-shadow:
    0 0 3px rgba(255,60,0,0.2),
    0 0 8px rgba(255,60,0,0.08);
}

/* Blue rim on FX's right edge (MIC is ON) */
.btn-fx.rim-blue::after {
  content: '';
  position: absolute;
  top: 18%; bottom: 18%; right: 0;
  width: 2px;
  border-radius: 1px;
  z-index: 15; pointer-events: none;
  background: linear-gradient(180deg,
    transparent 0%,
    rgba(80,180,255,0.12) 18%,
    rgba(80,180,255,0.55) 50%,
    rgba(0,130,255,0.12) 82%,
    transparent 100%);
  box-shadow:
    0 0 3px rgba(0,130,255,0.2),
    0 0 8px rgba(0,130,255,0.08);
}
```

### Active text glow

```css
.active .text-label {
  color: #ffffff;
  text-shadow:
    0 0 15px rgba(255,255,255,0.9),
    0 0 30px rgba(255,120,0,1);  /* Match button color */
}
```

**Full working demo**: `assets/codepen-audio-interface-pro.html`
