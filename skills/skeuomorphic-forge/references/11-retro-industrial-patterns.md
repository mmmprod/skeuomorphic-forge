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
| Thick info card | 40 (Thick card surface) | Top specular + bottom bevel darkness + inner recess |
| Toggle / binary switch | 41 (Trench toggle) | 3-layer (outer → trench → thumb) + LED indicator dot |
| CNC-milled pushbutton | 42 (Well-mounted button) | Button in machined well + 8-radial light projection |
| Mechanical key | 43 (Keyboard key) | 14-layer shadow + 4px→1px border travel + spring bezier |
| OEM EQ / parametric curve | 44 (OEM EQ curve) | SVG bell/shelf filters + annotated callouts + neon glow |
| Flat response display | 45 (Full-range display) | `<rect>` bands + log-frequency axis + bandwidth arrows |

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

---

## 40. Thick Card Surface (Reports Card)

A raised card component with visible material thickness — top specular highlight, bottom bevel darkness, and a recessed inner container for content. Bridges neumorphic softness with skeuomorphic depth.

### Card surface (outer slab)

```css
.card-surface {
  background: linear-gradient(145deg, #32343a, #1a1b1f);
  border-radius: 48px;
  position: relative;
  box-shadow:
    /* Deep drop shadow */
    0 50px 100px -20px rgba(0,0,0,0.9),
    /* Outline rim */
    0 0 0 1px rgba(255,255,255,0.05),
    /* Bottom bevel (visible thickness) */
    inset 0 -10px 15px rgba(0,0,0,0.6),
    /* Top specular (light source above) */
    inset 0 3px 3px rgba(255,255,255,0.18);
}

/* ::after — subtle upper sheen wash */
.card-surface::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 48px;
  pointer-events: none;
  box-shadow: inset 0 25px 50px rgba(255,255,255,0.04);
}
```

### Inner content recess

```css
.card-inner {
  background: #121317;
  border-radius: 40px;
  box-shadow:
    /* Depth hole */
    inset 0 12px 24px rgba(0,0,0,0.7),
    /* Rim highlight (top of inner lip) */
    0 2px 2px rgba(255,255,255,0.12),
    /* Outer bevel thickness */
    0 5px 8px rgba(0,0,0,0.5);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  border-right: 1px solid rgba(255,255,255,0.04);
}
```

### Status pill (glossy colored badge)

```tsx
// Green status badge
const STATUS_PILL: React.CSSProperties = {
  background: 'linear-gradient(to bottom right, #194a2b, #0f2218)',
  border: '1px solid rgba(58,255,116,0.3)',
  borderRadius: 16,
  padding: '12px 20px',
  boxShadow: 'inset 0 2px 4px rgba(255,255,255,0.15), 0 10px 20px rgba(0,0,0,0.5)',
};

// Blue channel badge
const CHANNEL_PILL: React.CSSProperties = {
  background: 'linear-gradient(to bottom right, #5fa2ff, #3b6bff)',
  color: '#0b1120',
  fontWeight: 700,
  borderRadius: 12,
  padding: '8px 16px',
  boxShadow: 'inset 0 2px 3px rgba(255,255,255,0.35), 0 8px 18px rgba(0,0,0,0.45)',
  border: '1px solid rgba(255,255,255,0.2)',
};
```

**Full working demo**: `assets/codepen-reports-card.html`

---

## 41. Trench Toggle (Sliding Switch)

A large binary toggle where a beveled thumb slides inside a machined trench. 3-layer construction: outer housing → trench cavity → sliding thumb with LED indicator.

### Outer housing

```css
.toggle-outer {
  position: relative;
  width: 480px; height: 110px;
  padding: 3px;
  border-radius: 100px;
  background: linear-gradient(180deg, #14181c 0%, #242a31 100%);
  box-shadow:
    0 20px 40px rgba(0,0,0,0.5),
    0 2px 3px rgba(255,255,255,0.1);
  cursor: pointer;
  user-select: none;
}
```

### Trench (deep cavity)

```css
.toggle-trench {
  position: relative;
  width: 100%; height: 100%;
  background: #0d0f12;
  border-radius: 100px;
  box-shadow:
    inset 0 12px 20px rgba(0,0,0,0.9),
    inset 0 -4px 8px rgba(255,255,255,0.05);
  overflow: hidden;
}
```

### Sliding thumb

```css
.thumb {
  position: absolute;
  top: 2px; bottom: 2px; left: 2px;
  width: calc(50% - 4px);
  border-radius: 100px;
  transition: transform 0.4s cubic-bezier(0.65, 0, 0.35, 1);
  z-index: 10;
  /* Directional bevel borders */
  border-top: 1px solid rgba(255,255,255,0.2);
  border-left: 1px solid rgba(255,255,255,0.1);
  border-right: 1px solid rgba(0,0,0,0.3);
  border-bottom: 2px solid rgba(0,0,0,0.5);
  box-shadow:
    0 10px 20px rgba(0,0,0,0.6),
    inset 0 1px 1px rgba(255,255,255,0.15);
}
/* Left position */
.thumb.left {
  background: linear-gradient(165deg, #586170 0%, #3a424b 48%, #22272e 100%);
}
/* Right position (slides 100%) */
.thumb.right {
  background: linear-gradient(165deg, #4c5560 0%, #303740 50%, #1b1f25 100%);
  transform: translateX(100%);
}
```

### Color-switching glow text

```css
.glow-cyan {
  color: #cffafe;
  text-shadow: 0 0 10px rgba(103,232,249,0.7), 0 0 20px rgba(103,232,249,0.4);
}
.glow-amber {
  color: #ffedd5;
  text-shadow: 0 0 10px rgba(251,191,36,0.6), 0 0 20px rgba(251,191,36,0.3);
}
```

### LED indicator dot (recessed in thumb)

```css
.dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #111418;
  box-shadow: inset 1px 1px 3px rgba(0,0,0,0.8);
}
.dot-active {
  width: 4px; height: 4px;
  border-radius: 50%;
  /* Cyan or amber depending on state */
  background: rgba(103,232,249,0.8);
  box-shadow: 0 0 6px rgba(103,232,249,1);
}
```

**Full working demo**: `assets/codepen-toggle-hifi.html`

---

## 42. Well-Mounted Button (Anodized with Light Projection)

A large oval button recessed in a machined well, with full lighting system: OFF state (dark anodized), ON state (lit with rim light, internal glow, and light projected onto the surrounding panel surface).

### Button well (machined recess)

```css
.button-well {
  position: relative;
  padding: 14px;
  border-radius: 9999px;
  background: linear-gradient(180deg, #040404, #080808, #060606);
  box-shadow:
    inset 0 3px 8px rgba(0,0,0,0.9),
    inset 0 6px 20px rgba(0,0,0,0.5),
    inset 0 -1px 2px rgba(255,255,255,0.02),
    0 -1px 0 rgba(255,255,255,0.05),
    0 1px 0 rgba(0,0,0,0.8),
    0 4px 20px rgba(0,0,0,0.6);
  border: 1px solid #060606;
  transition: box-shadow 0.5s ease, border-color 0.5s ease;
}
```

### Well-lit state (8-layer rim light on chassis lip)

```css
.button-well.well-lit {
  border-color: rgba(220,60,50,0.24);
  box-shadow:
    /* Retained depth shadows */
    inset 0 3px 8px rgba(0,0,0,0.9),
    inset 0 6px 20px rgba(0,0,0,0.5),
    inset 0 -1px 2px rgba(255,255,255,0.02),
    /* RIM LIGHT on chassis lip (8 layers, directional) */
    0 -1px 0 rgba(255,180,160,0.36),     /* top: primary catch */
    0 -2px 4px rgba(220,50,40,0.28),
    0 -3px 10px rgba(200,40,30,0.16),
    -1px 0 0 rgba(255,170,150,0.24),     /* left: light-side */
    -2px 0 6px rgba(200,45,35,0.16),
    0 1px 0 rgba(220,60,50,0.16),        /* bottom: bounce */
    0 2px 6px rgba(200,40,30,0.12),
    1px 0 0 rgba(200,50,40,0.08),        /* right: weakest */
    0 4px 20px rgba(0,0,0,0.6);
}
```

### Red light bouncing inside well walls (::before, 8 radial gradients)

```css
.button-well.well-lit::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: 9999px;
  pointer-events: none; z-index: 1;
  background:
    /* top rim (hot spot) */
    radial-gradient(ellipse 70% 12% at 50% 0%,
      rgba(240,60,50,0.44) 0%, rgba(220,50,40,0.2) 40%, transparent 100%),
    radial-gradient(ellipse 85% 18% at 50% 2%,
      rgba(200,40,30,0.16) 0%, transparent 100%),
    /* bottom rim */
    radial-gradient(ellipse 60% 10% at 50% 100%,
      rgba(220,50,40,0.28) 0%, transparent 100%),
    radial-gradient(ellipse 75% 15% at 50% 98%,
      rgba(190,35,25,0.1) 0%, transparent 100%),
    /* left rim */
    radial-gradient(ellipse 6% 40% at 0% 50%,
      rgba(230,55,45,0.32) 0%, transparent 100%),
    radial-gradient(ellipse 10% 55% at 1% 50%,
      rgba(190,35,25,0.1) 0%, transparent 100%),
    /* right rim */
    radial-gradient(ellipse 5% 35% at 100% 50%,
      rgba(210,45,35,0.24) 0%, transparent 100%),
    radial-gradient(ellipse 8% 50% at 99% 50%,
      rgba(180,30,20,0.08) 0%, transparent 100%);
}
```

### Button ON state (multi-layer lit surface)

```css
.skeuo-on {
  background-color: #8a1515;
  background-image:
    /* Surface glow (on the button itself) */
    radial-gradient(ellipse 80% 50% at 50% 35%,
      rgba(255,80,60,0.14) 0%, transparent 70%),
    /* Specular: top-left offset */
    radial-gradient(ellipse 40% 25% at 35% 20%,
      rgba(255,255,255,0.22) 0%, rgba(255,200,200,0.06) 50%, transparent 100%),
    /* Brush texture */
    repeating-radial-gradient(ellipse at 50% 50%,
      transparent 0%, transparent 2.5%, rgba(255,255,255,0.015) 2.8%, transparent 3.1%),
    /* Curvature */
    radial-gradient(ellipse 130% 90% at 50% 38%,
      #cc2222 0%, #a01818 30%, #651010 65%, #350808 100%);
  box-shadow:
    /* Rim light (directional, 5 edges) */
    inset 0 1px 0 rgba(255,220,200,0.18),
    inset 1px 1px 0 rgba(255,200,180,0.08),
    inset 1px 0 0 rgba(255,180,160,0.06),
    inset 0 -1px 0 rgba(255,150,130,0.03),
    inset -1px 0 0 rgba(0,0,0,0.3),
    /* Body surface glow */
    inset 0 0 24px rgba(255,60,50,0.14),
    inset 0 0 40px rgba(255,40,30,0.06),
    /* Depth */
    inset 0 -8px 20px rgba(0,0,0,0.5),
    /* Projected light (close) */
    0 0 12px rgba(200,30,30,0.12),
    0 0 30px rgba(180,20,20,0.06);
}
```

### Surface light projection (onto panel behind)

```css
.light-projection {
  position: absolute;
  width: 550px; height: 350px;
  border-radius: 50%;
  pointer-events: none;
  transition: opacity 0.6s ease;
  opacity: 0;
  background:
    radial-gradient(ellipse 60% 50% at 50% 40%,
      rgba(220,40,30,0.2) 0%, rgba(200,30,20,0.1) 40%, transparent 70%),
    radial-gradient(ellipse 100% 80% at 50% 38%,
      rgba(180,25,15,0.1) 0%, transparent 80%);
  animation: projection-breathe 3s infinite ease-in-out;
}
.light-projection.active { opacity: 1; }
```

**Full working demo**: `assets/codepen-bouton-skeuomorphique.html`

---

## 43. Mechanical Keyboard Key (Spring Return)

A compact rectangular button with 14-layer shadow stack, 4px bottom border simulating key travel, and spring-back animation. Pure CSS mechanical press feel.

### Key construction (OFF/resting state)

```css
.key-button {
  padding: 22px 58px;
  border-radius: 10px;
  cursor: pointer;
  /* 3-stop gradient for curvature */
  background: linear-gradient(180deg, #2e2e34 0%, #222226 35%, #161618 100%);
  /* Thick directional bevel */
  border-top: 2px solid rgba(255,255,255,0.11);
  border-left: 1px solid rgba(255,255,255,0.05);
  border-right: 1px solid rgba(0,0,0,0.4);
  border-bottom: 4px solid #050506;   /* ← travel height */
  /* 14-layer shadow stack */
  box-shadow:
    /* Inner depth */
    inset 0 1px 0 rgba(255,255,255,0.1),
    inset 0 2px 1px rgba(255,255,255,0.05),
    inset 0 6px 8px rgba(255,255,255,0.02),
    inset 0 -2px 3px rgba(0,0,0,0.5),
    inset 0 -5px 10px rgba(0,0,0,0.3),
    inset 0 -8px 16px rgba(0,0,0,0.15),
    inset 3px 0 4px rgba(0,0,0,0.2),
    inset -3px 0 4px rgba(0,0,0,0.2),
    /* External cast (6 progressive distances) */
    0 2px 1px rgba(0,0,0,0.7),
    0 4px 6px rgba(0,0,0,0.6),
    0 8px 16px rgba(0,0,0,0.5),
    0 16px 32px rgba(0,0,0,0.4),
    0 24px 48px rgba(0,0,0,0.25),
    0 32px 64px rgba(0,0,0,0.15);
  /* Spring return animation */
  transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 0.15s ease-out,
              border-bottom-width 0.08s ease-out;
}
```

### Pressed state (mechanical travel)

```css
.key-button:active {
  transform: translateY(3px);          /* physical press */
  border-bottom-width: 1px;            /* border shrinks = key sinks */
  background: linear-gradient(180deg, #1a1a1e, #121214 35%, #0a0a0c);
  box-shadow:
    /* Reduced inner glow */
    inset 0 1px 0 rgba(255,255,255,0.04),
    inset 0 3px 6px rgba(0,0,0,0.4),
    inset 0 -1px 2px rgba(0,0,0,0.3),
    inset 3px 0 4px rgba(0,0,0,0.2),
    inset -3px 0 4px rgba(0,0,0,0.2),
    /* Reduced cast (closer to surface) */
    0 1px 1px rgba(0,0,0,0.6),
    0 2px 4px rgba(0,0,0,0.5),
    0 4px 8px rgba(0,0,0,0.4),
    0 8px 16px rgba(0,0,0,0.3);
}
```

### Neon text activation (lit after press)

```css
.key-text.lit {
  color: #38bdf8;
  text-shadow:
    0 0 4px rgba(56,189,248,0.9),
    0 0 12px rgba(56,189,248,0.6),
    0 0 28px rgba(56,189,248,0.3),
    0 0 50px rgba(56,189,248,0.12);
}
```

**Key insight**: The `border-bottom: 4px → 1px` on `:active` combined with `translateY(3px)` creates a convincing mechanical key travel. The `cubic-bezier(0.34, 1.56, 0.64, 1)` spring overshoot makes the return feel physical.

**Full working demo**: `assets/codepen-valider-button.html`

---

## 44. OEM EQ Curve Analyzer (Annotated Parametric Display)

Extends the frequency analyzer screen (pattern 37) with **parametric EQ modeling** — bass boost, mid scoop, presence peak, treble rolloff — and annotated callout markers. Designed for OEM factory signal analysis.

### Parametric EQ filter math

```tsx
// Bell (peaking) filter approximation
const parametricBell = (freq: number, fc: number, gainDb: number, Q: number) => {
  const ratio = freq / fc;
  const x2 = ratio * ratio;
  const bw = 1 / Q;
  const denom = (1 - x2) * (1 - x2) + (bw * ratio) * (bw * ratio);
  const response = (bw * ratio) * (bw * ratio) / denom;
  return gainDb * response;
};

// High shelf filter
const highShelf = (freq: number, fc: number, gainDb: number, slope: number) => {
  const rn = Math.pow(freq / fc, slope);
  return gainDb * rn / (1 + rn);
};
```

### Typical OEM EQ shape

```tsx
const getOemEqDb = (freq: number) => {
  let db = 0;
  // Sub-bass rolloff (HPF ~35Hz, gentle)
  const subR4 = Math.pow(freq / 35, 4);
  db += 10 * Math.log10(subR4 / (1 + subR4));
  // Bass boost: +5.5dB at 100Hz, Q=1.2
  db += parametricBell(freq, 100, 5.5, 1.2);
  // Mid scoop: -4dB at 500Hz, Q=0.8
  db += parametricBell(freq, 500, -4.0, 0.8);
  // Presence peak: +3dB at 2500Hz, Q=1.5
  db += parametricBell(freq, 2500, 3.0, 1.5);
  // Treble rolloff: -10dB above 8kHz
  db += highShelf(freq, 8000, -10, 3);
  return db;
};
```

### SVG annotation callouts

```xml
<!-- Dot marker + dashed leader line + label -->
<g opacity="0.6">
  <circle cx={freqToX(100)} cy={dbToY(5.5)} r="5" fill="#f59e0b"
    filter="url(#annotGlow)" />
  <line x1={x} y1={y-8} x2={x} y2={y-35}
    stroke="#f59e0b" stroke-width="1" stroke-dasharray="3 2" />
  <text x={x} y={y-40} fill="#f59e0b" font-size="9" font-weight="700"
    text-anchor="middle">BASS BOOST</text>
  <text x={x} y={y-28} fill="#b37a0a" font-size="8" font-weight="600"
    text-anchor="middle">+5.5 dB @ 100 Hz</text>
</g>
```

### Blinking detection label

```xml
<text x="500" y="340" fill="#f59e0b" font-size="36" font-weight="700"
  text-anchor="middle" filter="url(#neonGlow)">
  <animate attributeName="opacity" values="1;0.3;1" dur="1.5s"
    repeatCount="indefinite" />
  OEM EQ DETECTED
</text>
```

### Info panel (DSP-style readout)

```xml
<rect x="780" y="48" width="170" height="120" rx="4"
  fill="rgba(0,0,0,0.5)" stroke="rgba(245,158,11,0.15)" />
<!-- Key/value rows -->
<text x="795" y="110" fill="#4a5a78" font-size="9">SOURCE</text>
<text x="940" y="110" fill="#8898b8" font-size="10" text-anchor="end">Head Unit</text>
<text x="795" y="142" fill="#4a5a78" font-size="9">CORRECTION</text>
<text x="940" y="142" fill="#ef4444" font-size="10" text-anchor="end">REQUIRED</text>
```

### Color scheme: amber for OEM (vs cyan for crossover)

| Element | Crossover (37) | OEM EQ (44) |
|---|---|---|
| Curve stroke | `#38bdf8` cyan | `#f59e0b` amber |
| Fill gradient | blue tones | amber/brown tones |
| Ambient glow | `#0a1830` | `#061020` |
| Badge | `DSP CROSSOVER` | `DSP INPUT ANALYSIS` |

**Full working demo**: `assets/codepen-oem-eq-curve.html`

---

## 45. Full-Range / Flat Response Display

Extends the analyzer screen (pattern 37) for displaying a **flat 0dB passband** (no crossover applied). Uses a thick neon line at 0dB with endpoint markers and bandwidth arrows.

### Flat response rendering

Unlike Butterworth curves, the full-range display uses a simple horizontal rect at `zeroDbY` with neon glow filter, since `preserveAspectRatio="none"` would squish a horizontal SVG path to invisible.

```xml
<!-- Thick flat line (rect instead of path) -->
<rect x={MARGIN_L} y={zeroDbY - 3} width={PLOT_W} height="6"
  rx="3" fill="#38bdf8" filter="url(#neonGlow)" />

<!-- Endpoint markers -->
<circle cx={MARGIN_L} cy={zeroDbY} r="4" fill="#38bdf8" filter="url(#softGlow)" />
<circle cx={MARGIN_R} cy={zeroDbY} r="4" fill="#38bdf8" filter="url(#softGlow)" />
```

### Bandwidth indicator arrows

```xml
<g opacity="0.35">
  <!-- Left arrow -->
  <line x1={MARGIN_L+10} y1={y+20} x2={MARGIN_L+60} y2={y+20}
    stroke="#4ade80" stroke-width="1.5" />
  <line x1={MARGIN_L+10} y1={y+16} x2={MARGIN_L+10} y2={y+24}
    stroke="#4ade80" stroke-width="1.5" />
  <!-- Right arrow -->
  <line x1={MARGIN_R-60} y1={y+20} x2={MARGIN_R-10} y2={y+20}
    stroke="#4ade80" stroke-width="1.5" />
  <!-- Center label -->
  <text x="500" y={y+24} fill="#4ade80" font-size="10" text-anchor="middle">
    20 Hz ~ 20 kHz
  </text>
</g>
```

### Color scheme: green for full-range pass

| Element | Crossover (37) | Full Range (45) |
|---|---|---|
| Curve/line | `#38bdf8` cyan | `#38bdf8` cyan + `#4ade80` green markers |
| Fill | Blue gradient | Green gradient (`#0ea5e9` → transparent) |
| Info panel | — | Green border `rgba(74,222,128,0.15)` |
| Badge | `DSP CROSSOVER — SCANNING` | `DSP CROSSOVER` (green glow) |
| Status | HPF/LPF values | `BYPASS` / `BYPASS` |

### Info panel (bypass status)

```xml
<rect x="780" y="300" width="170" height="105" rx="4"
  fill="rgba(0,0,0,0.5)" stroke="rgba(74,222,128,0.15)" />
<text x="865" y="322" fill="#4ade80" font-size="20" font-weight="700"
  text-anchor="middle">FULL RANGE</text>
<text x="865" y="338" fill="#2a6545" font-size="10">NO CROSSOVER</text>
<!-- HPF/LPF both BYPASS -->
<text x="795" y="362" fill="#4a5a78" font-size="9">HPF</text>
<text x="940" y="362" fill="#5a6a4a" font-size="10" text-anchor="end">BYPASS</text>
```

**Full working demo**: `assets/codepen-fullrange-no-crossover.html`
