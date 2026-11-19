# Padda Bil — Terokhada, Khulna

An interactive, scroll-driven editorial showcase highlighting **Padda Bil** (`22.94° N, 89.66° E`), a seasonal pink water lotus wetland sanctuary in Terokhada Upazila, Khulna, Bangladesh.

Built with a minimalist pitch-black (`#000000`) gallery aesthetic and **DM Sans** typography, the experience synchronizes smooth scroll choreography with a continuous 3D macro-to-water-level visual sequence—taking visitors from a single unfolding lotus bud to a dawn wooden *nouka* journey across the bil.

---

## ✨ Key Features

- **Scroll-Driven Visual Storytelling:** Seamless frame-by-frame / video scrub progression transitioning across four distinct visual chapters:
  1. **The Awakening (Hero):** Macro pink lotus bloom emerging from pure `#000000` still water.
  2. **The Sanctuary:** Vertical crane pullback revealing a vast mosaic of emerald lily pads and wild blossoms.
  3. **The Voyage:** Bird's-eye channel traverse following a local boatman guiding a traditional wooden *nouka* with a weathered bamboo pole.
  4. **Plan Your Visit (Hero Reveal):** Water-level closing reveal with visitor information, peak season details, and navigation links.
- **Minimalist Dark-Mode Design System:** Pure `#000000` canvas, high-contrast `#FFFFFF` **DM Sans** typography, and translucent frosted-glass navigation pills designed to keep 75%+ of the viewport unobstructed.
- **Responsive & Lightweight:** Engineered for smooth frame interpolation and crisp legibility across desktop and mobile viewports.

---

## 🎨 Design & Visual Architecture

| Token / Element | Specification |
| :--- | :--- |
| **Background Canvas** | `#000000` (Pure Pitch Black) |
| **Primary Typography** | `DM Sans` (Weights: `400`, `500`, `700`) |
| **Primary Text Color** | `#FFFFFF` (Pure White) |
| **UI Surfaces** | Frosted glass pill navbar (`backdrop-filter: blur`) & outlined pill CTAs |
| **Motion Pipeline** | AI-assisted 3D macro & aerial sequence generated with **Veo 3** using start-to-end keyframe locking |

---

## 🗂️ Project Structure

```text
padda-bil/
├── index.html          # Main scroll-driven layout & section markup
├── styles/
│   └── main.css        # Pure #000000 theme, DM Sans typography & frosted glass UI
├── scripts/
│   └── scroll.js       # Scroll progress tracking & frame/video scrubbing logic
├── assets/
│   ├── frames/         # Extracted WebP/AVIF sequence frames (or stitched video)
│   └── media/          # Fallback posters and social preview assets
└── README.md
