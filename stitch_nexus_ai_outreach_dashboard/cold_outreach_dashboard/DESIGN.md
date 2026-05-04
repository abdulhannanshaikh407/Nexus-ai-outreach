---
name: Cold Outreach Dashboard
colors:
  surface: '#13131b'
  surface-dim: '#13131b'
  surface-bright: '#393841'
  surface-container-lowest: '#0d0d15'
  surface-container-low: '#1b1b23'
  surface-container: '#1f1f27'
  surface-container-high: '#292932'
  surface-container-highest: '#34343d'
  on-surface: '#e4e1ed'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e4e1ed'
  inverse-on-surface: '#303038'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#4ae176'
  on-secondary: '#003915'
  secondary-container: '#00b954'
  on-secondary-container: '#004119'
  tertiary: '#ffb783'
  on-tertiary: '#4f2500'
  tertiary-container: '#d97721'
  on-tertiary-container: '#452000'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#6bff8f'
  secondary-fixed-dim: '#4ae176'
  on-secondary-fixed: '#002109'
  on-secondary-fixed-variant: '#005321'
  tertiary-fixed: '#ffdcc5'
  tertiary-fixed-dim: '#ffb783'
  on-tertiary-fixed: '#301400'
  on-tertiary-fixed-variant: '#703700'
  background: '#13131b'
  on-background: '#e4e1ed'
  surface-variant: '#34343d'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-stats:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: -0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 0.25rem
  sm: 0.5rem
  md: 1rem
  lg: 1.5rem
  xl: 2rem
  gutter: 1.5rem
  container-max: 1440px
---

## Brand & Style

The design system is engineered for a high-performance AI cold email platform, targeting growth teams and sales engineers who demand precision and speed. The aesthetic is a fusion of **Minimalism** and **Modern Corporate**, drawing inspiration from the technical rigor of Vercel and the atmospheric depth of Linear.

The UI communicates reliability through high-contrast legibility and "developer-grade" precision. It avoids unnecessary flourishes, relying instead on mathematical spacing, subtle borders, and purposeful indigo accents to guide the user through complex outreach pipelines. The emotional response is one of controlled efficiency—providing a "command center" feel for high-volume communication workflows.

## Colors

This design system utilizes a deep, nocturnal palette to reduce eye strain during prolonged campaign management. 

- **Primary (#6366f1):** A vibrant Indigo used exclusively for primary actions, active navigation states, and critical progress indicators.
- **Success (#22c55e):** Used for positive metrics (open rates, click rates) and successful "Sent" statuses.
- **Neutrals:** The background uses a deep navy-black (#0f0f1a) to provide maximum contrast for the surface cards (#1a1a2e). 
- **Borders:** A slightly lighter indigo-tinted grey (#2e2e48) is used for hairlines to define structure without adding visual bulk.

## Typography

The design system relies on **Inter** for its neutral, utilitarian character. It uses a tight scale to maximize information density.

- **Headings:** Set at 600 weight with slight negative letter-spacing to create a "compact" and professional look.
- **Body Text:** Standardized at 14px for readability, using the 400 weight for all descriptive text.
- **Labels:** Small, uppercase labels are used for table headers and metadata categories to create a clear hierarchy.
- **Numerical Data:** While using Inter, statistics should utilize tabular figures to ensure alignment in data grids and pipeline columns.

## Layout & Spacing

This design system uses a **fixed grid** approach for the main dashboard content, constrained to a 1440px max-width container, while the sidebar remains fixed to the viewport.

- **Grid:** A 12-column system with 24px (1.5rem) gutters.
- **Rhythm:** An 8px base unit drives all padding and margins, ensuring vertical rhythm across disparate card components.
- **Pipeline View:** Specifically for the outreach workflow, a horizontal scrolling flex-container is used where each "stage" card has a fixed width of 320px.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows.

- **Level 0 (Background):** #0f0f1a.
- **Level 1 (Cards/Surfaces):** #1a1a2e with a 1px solid border of #2e2e48.
- **Level 2 (Modals/Popovers):** #1a1a2e with a slightly brighter border (#3f3f5a) and a very subtle, 15% opacity black shadow (0px 10px 30px) to provide separation from the dashboard layer.
- **Active State:** Any "focused" card or input receives a primary color border glow (thin 1px stroke of #6366f1).

## Shapes

The shape language is "Soft" (0.25rem), leaning towards a technical, sharp-edged look that conveys precision.

- **Standard Elements:** Buttons, inputs, and small cards use a 4px (0.25rem) radius.
- **Container Elements:** Larger dashboard widgets and main content areas use 8px (0.5rem) to slightly soften the layout.
- **Selection Indicators:** Vertical bars (2px wide) used on the left side of active navigation items or table rows.

## Components

- **Buttons:** Primary buttons are solid #6366f1 with white text. Secondary buttons are ghost-style with a #2e2e48 border that transitions to #3f3f5a on hover.
- **Inputs:** Darker than the card surface (#0f0f1a), using a 1px border. Focus states use the primary indigo for the border.
- **Cards:** The core unit of the dashboard. They must include a `card-header` with a 1px bottom border and the `label-caps` typography for titles.
- **Status Chips:** Small, low-saturation backgrounds with high-saturation text (e.g., Success: dark green background with #22c55e text).
- **Pipeline Columns:** Vertical containers that stack "Lead Cards." Each card displays a lead name, email status, and a "last contacted" timestamp.
- **Data Visualization:** Charts should use stroke-only line graphs (no fills) with primary indigo or success green, utilizing a subtle glow effect on the data points.