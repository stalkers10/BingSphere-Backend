---
name: Cinematic Dark
colors:
  surface: '#200e0c'
  surface-dim: '#200e0c'
  surface-bright: '#4a3330'
  surface-container-lowest: '#1a0908'
  surface-container-low: '#2a1614'
  surface-container: '#2e1a18'
  surface-container-high: '#3a2522'
  surface-container-highest: '#462f2c'
  on-surface: '#ffdad5'
  on-surface-variant: '#e9bcb6'
  inverse-surface: '#ffdad5'
  inverse-on-surface: '#412b28'
  outline: '#af8782'
  outline-variant: '#5e3f3b'
  surface-tint: '#ffb4aa'
  primary: '#ffb4aa'
  on-primary: '#690003'
  primary-container: '#e50914'
  on-primary-container: '#fff7f6'
  inverse-primary: '#c0000c'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#a7c8ff'
  on-tertiary: '#003061'
  tertiary-container: '#0072d7'
  on-tertiary-container: '#f8f9ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#930007'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#d5e3ff'
  tertiary-fixed-dim: '#a7c8ff'
  on-tertiary-fixed: '#001b3c'
  on-tertiary-fixed-variant: '#004689'
  background: '#200e0c'
  on-background: '#ffdad5'
  surface-variant: '#462f2c'
typography:
  display-lg:
    fontFamily: Bebas Neue
    fontSize: 72px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: 0.02em
  display-md:
    fontFamily: Bebas Neue
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1920px
  gutter: 1.5rem
  margin-sm: 1rem
  margin-md: 3rem
  margin-lg: 4rem
---

## Brand & Style

The design system is engineered for high-impact visual storytelling, prioritizing content immersion above all else. The brand personality is premium, authoritative, and theatrical, designed to fade into the background to let the cinematography shine. 

The visual style is **High-Contrast / Bold**, utilizing a "Void" aesthetic where deep blacks and charcoals provide a limitless canvas for vibrant media. Every interaction is designed to feel like a premiere, utilizing large-scale imagery, subtle motion, and a color-agnostic framework that adapts to the mood of the featured content. This system targets a diverse global audience, evoking feelings of excitement, relaxation, and high-end entertainment.

## Colors

The palette is strictly curated to maintain a cinematic atmosphere. 

- **Primary Red (#e50914):** Reserved exclusively for critical brand moments and primary calls to action. It must be used sparingly to maintain its psychological impact.
- **Surface & Backgrounds:** We utilize a dual-tone dark strategy. Pure Black (#000000) is used for the base canvas to maximize OLED display efficiency and contrast. Deep Charcoal (#0f0f0f) is used for elevated surfaces like navigation bars and sidebars to provide subtle depth.
- **Typography:** Primary text is pure white for maximum legibility. Secondary text uses light gray (#b3b3b3) to establish hierarchy and reduce visual noise in metadata.

## Typography

This design system uses a two-tier typographic approach. 

For high-level impact and title treatments, **Bebas Neue** provides a tall, condensed, cinematic feel that mirrors movie posters. For all functional UI, metadata, and long-form descriptions, **Inter** is used for its exceptional clarity and neutral character.

Large display sizes should be used for featured "Hero" content titles. Headlines use tighter letter-spacing to feel more integrated into the UI. Body text uses generous line-height to ensure readability against dark backgrounds.

## Layout & Spacing

The design system employs a **Fluid Grid** model with high-density content rows. 

- **Desktop (1200px+):** 12-column grid with 24px gutters and 64px side margins. Content is organized in horizontal scrolling "shelves."
- **Tablet (768px - 1199px):** 8-column grid with 16px gutters and 48px side margins.
- **Mobile (<768px):** 4-column grid with 12px gutters and 16px side margins.

Spacing follows an 8px base unit. Generous vertical spacing (48px to 80px) is used between content categories to prevent the UI from feeling cluttered, while internal component spacing remains tight and efficient.

## Elevation & Depth

In a dark-mode-first system, elevation is conveyed through **Tonal Layers** and **Subtle Gradients** rather than traditional drop shadows.

- **Background:** Pure Black (#000000).
- **Surface (Level 1):** Deep Charcoal (#0f0f0f) for headers and persistent sidebars.
- **Overlays:** 60% opacity black gradients are applied to the bottom 40% of all images where text is present to ensure legibility.
- **Focus States:** High-contrast 2px white borders are used to indicate keyboard or remote-control navigation focus, ensuring clear visibility from a 10-foot viewing distance.

## Shapes

The shape language is **Soft**, utilizing small radii to maintain a modern look without appearing overly "bubbly" or juvenile. 

- **Cards:** 0.25rem (4px) corner radius for movie posters and thumbnails. This subtle rounding provides a clean, modern edge that fits the grid.
- **Buttons:** Fully pill-shaped (rounded-xl) for primary actions to distinguish them from content thumbnails.
- **Interactive Elements:** Checkboxes and inputs use the base 4px radius for consistency.

## Components

### Buttons
- **Primary:** Filled with Primary Red (#e50914), white text, bold weight. No border.
- **Secondary:** Semi-transparent white (20% opacity) with a background blur, white text.
- **Icon Only:** Circular, semi-transparent background, used for "Add to List" or "Like."

### Cards & Thumbnails
- **Posters:** 2:3 or 16:9 aspect ratio with a 4px corner radius. On hover, cards should scale slightly (1.05x) and display a play icon overlay.
- **Metadata:** Displayed immediately below the card in Secondary Text (#b3b3b3) at the `label-sm` scale.

### Navigation
- **Global Header:** Transparent at the top of the page, transitioning to Deep Charcoal (#0f0f0f) upon scroll.
- **Active State:** Red bottom-border (2px) or bold white text to indicate the current section.

### Form Fields
- **Search:** Outlined with 1px gray, transitioning to a white border on focus. Background is slightly lighter than the base canvas to denote interactivity.

### Progress Bars
- **Video Playback:** Thin 4px height. Unfilled state is dark gray; filled state is Primary Red (#e50914).