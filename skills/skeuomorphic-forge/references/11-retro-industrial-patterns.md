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

## Quick Reference — Retro-Industrial Decision Matrix

| Building... | Use pattern | Key technique |
|---|---|---|
| Instrument readout | 27 (3-ring bezel) + 28 (CRT) | Conic gradient chassis + scanline display |
| Status indicator | 29 (LED system) | Multi-shadow halo + pulse animation |
| Mounting panel | 30 (Torx screws) + file 01 raised surface | Cast iron texture + corner screws |
| Text input field | 32 (Glitch input) | Corner brackets + scanline sweep |
| Numeric display | 33 (Mechanical counter) | Rolling digits + digit well + vignette |
| Metal surface | 31 (feTurbulence) | SVG noise overlay + warm gradient |
| Panel label | Section 28 phosphor glow | Silkscreen or phosphor text-shadow |
