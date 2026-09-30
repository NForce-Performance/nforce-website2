# NForce website: the design system as it is (30 Sep 2026)
Written for the visual-direction work. It documents what the site already does, so changes stay one system. Brand rules live in the Brand Style Guide (v1, and the v1.1 draft awaiting Nick's decision).

## Tokens (assets/css/site.css, `:root`)
- **Colour:** `--ink` black base; `--ink-1/2/3` surface tiers (#0a0a0a, #0f0f0f, #1a1a1a); `--line`, `--line-soft`; `--text`, `--text-2` (#b8b8b8), `--text-3` (#8c8c8c); `--blue` #7ec8ff, the only accent. Nothing else.
- **Type:** one family (Archivo, regular and bold) until the NForce typeface is chosen. Fluid scale `--text-xl` to `--text-hero` with `clamp()`. `.num` for figures.
- **Space:** `--sp-1..8` and three section rhythms: `--rhythm-tight`, `--rhythm-base`, `--rhythm-air`.
- **Shape:** `--radius` 2px, `--radius-lg` 4px, `--shadow: none`.

## Five section templates (built from existing components in tools/pages.py)
| Template | Job | Built with |
| --- | --- | --- |
| Statement | One claim, one focal point | `page_hero` / `hero_ice` |
| System | Show how it works | `section(head(...) + rink_circle(...), "panel")` |
| Offer | What you can buy or ask for | `section(head(...) + cards / linkcards)` |
| Proof | Why believe it | `section(...)` with real photography and Hub frames (not built yet) |
| Action | The one next step | `ctaband` |
Rule: one template per section, one focal point per view, at most three hierarchy levels, light blue on the single most important thing in the view.

## Motion (what exists, and the rules)
- Entering sections fade and rise (CSS `animation-timeline: view()`); the circle draws itself. Motion only where it explains something. `prefers-reduced-motion` turns it off. Browsers without support show everything at once.
- **Prototype (branch `prototype-scroll-system`):** on wide screens the face-off circle stays in view while its list scrolls, and lights one variable at a time (`assets/js/nf-system.js`, CSS block at the end of `site.css`). Off on phones, with reduced motion, and without JavaScript.

## Not decided yet (Nick)
Typeface (guide question 1), exact greys (question 5), real photography and consent (question 6), the WebGL hero and this scroll stage (they go beyond Brand Style Guide v1 §6 and §8; see the v1.1 draft).
