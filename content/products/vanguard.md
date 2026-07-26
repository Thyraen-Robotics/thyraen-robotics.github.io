+++
title = "Vanguard"
slug = "vanguard"
weight = 10

[extra]
group = "operate"
hero_title = "Vanguard"
hero_subtitle = "The onboard autonomy and mission-computer runtime for unmanned systems"
card = "Turns mission intent into bounded local action onboard the platform — mission reasoning, autopilot and payload command, sensing, and operator visibility, from simulation to fielded mission computer."
epigraph = "An Agent when it must be. An Asset when it should be."
related = ["echelon", "simulator", "crucible", "tacit"]
masthead = "/images/mastheads/org-masthead.png"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Vanguard** is the onboard autonomy and mission-computer runtime for unmanned systems
within the Thyraen Robotics ecosystem.

Vanguard is the vehicle-side runtime that turns mission intent into bounded local action
on an unmanned platform: local mission reasoning, autopilot and payload command, RF and
visual sensing, operator visibility, and a clean path from simulation to field deployment.

> *An Agent when it must be. An Asset when it should be.*

---

## Two Postures, One Codebase

Vanguard runs in two postures from the same codebase:

- **Agent** — Vanguard owns local mission reasoning and platform execution onboard,
  keeping the platform sensing, deciding, acting, and reporting when the link to the
  operator does not survive.
- **Asset** — Vanguard executes intent from an external mission system on the local
  platform, integrating into an existing command architecture.

In both postures, Vanguard retains local **Platform Authority**: the safety and execution
boundary that prevents external *or onboard* mission logic from bypassing vehicle
readiness, command-path health, and platform constraints.

---

## What Vanguard Does

- **Mission reasoning on a doctrinal spine**
  Missions follow an F2T2EA (Find–Fix–Track–Target–Engage–Assess) structure with
  per-phase capability contracts, decomposed from published doctrine.

- **Platform execution**
  PX4 flight integration and vehicle-state publication, payload and gimbal discovery
  and control, and launch–transit–land lifecycle management.

- **Onboard sensing**
  GPU visual perception with hardware-accelerated inference, an RF collection and
  investigation lane, and an onboard media registry presenting live video.

- **Honest task reporting**
  Admission, progress, completion, cancellation, and failure are first-class typed
  outcomes — completion is evidence-backed, never inferred.

- **Operator visibility**
  A browser operator UI covering vehicle state, task state, service health, media, and
  live behavior-tree and decision inspection.

---

## From Simulation to Field

One workflow drives deterministic behavior-development simulation, full
software-in-the-loop simulation with photoreal rendering, and deployment to NVIDIA
Jetson mission computers — with the same production behavior reused in simulation,
replay, and live operation.

---

## What Vanguard Is Not

Vanguard is **not**:

- A ground control station or fleet C2 system — that is [Echelon](/products/echelon/)
- A flight controller — it commands the autopilot; it does not replace it
- A replacement for human command authority

Operators define intent and constraints. Vanguard executes within those bounds.
