+++
title = "Simulator"
slug = "simulator"
weight = 50

[extra]
group = "build"
hero_title = "Simulator"
hero_subtitle = "Photoreal simulation and testbed for the autonomy stack"
card = "Headless PX4/JSBSim flight truth paired with photoreal Unreal + Cesium sensor simulation, composable scenario registries, and gated validation with flight-log reports."
epigraph = "Fly it a thousand times before it ever leaves the rail."
related = ["vanguard", "crucible"]
masthead = "/images/backgrounds/bg-build.svg"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Simulator** is the shared simulation and testbed environment behind the Thyraen
autonomy stack — the place where thousands of controlled, repeatable flights happen
long before hardware is on a launch rail.

> *Fly it a thousand times before it ever leaves the rail.*

---

## One Source of Flight Truth

Simulator pairs two engines with a strict division of authority:

- A **headless PX4 / JSBSim backend** is the single authoritative source of flight
  truth — vehicle state and flight dynamics live here.
- An **Unreal Engine 5 + Cesium photoreal stack** acts strictly as a visual and sensor
  *follower* of that truth, rendering real-world terrain and feeding co-boresighted EO
  and simulated-IR imagery into the Vanguard perception pipeline.

The renderer never owns physics.

---

## What Simulator Does

- **Photoreal sensor simulation for perception**
  Continuous EO and IR capture lanes off one schedule, with exact-frame,
  capture-correlated ground-truth annotation for perception development and
  evaluation.

- **Composable, reviewable scenarios**
  Registries of maps, vehicles, launchers, payloads, and autopilot profiles compose
  into scenarios — a test configuration is a versioned manifest under review, not a
  hand-built scene.

- **One-command control plane**
  A single front door bootstraps the environment, checks health, materializes
  scenarios, and launches and supervises the full simulation session.

- **Gated, artifact-producing validation**
  Automated flight modes arm, launch, and assert estimator, airspeed, attitude, and
  failsafe health — then emit flight-log-derived reports for vehicle dynamics tuning
  and characterization.

- **Pinned, patched dependencies**
  No engine or autopilot source is vendored blindly: everything is pinned refs,
  checksummed payloads, and documented patch queues, enforced at bootstrap.

---

## Role in the Ecosystem

Simulator is the proving ground for [Vanguard](/products/vanguard/): the same production
autonomy behavior runs against simulated flight truth and photoreal sensor feeds before
it runs on hardware. Scenario definitions, autopilot profiles, and the simulation
contract are owned here, so adding a vehicle or flight engine never requires touching
the autonomy runtime.
