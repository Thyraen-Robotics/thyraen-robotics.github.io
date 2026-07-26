+++
title = "Devstack"
slug = "devstack"
weight = 80

[extra]
hero_title = "Devstack"
hero_subtitle = "One dashboard for every stack"
card = "The shared engineering platform under every Thyraen repository: supervised process stacks, readiness gates, and fleet-wide dependency policy for humans and coding agents alike."
masthead = "/images/mastheads/org-masthead.png"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

# Devstack

**Devstack** is the shared engineering platform underneath every Thyraen Robotics
repository: one supervisor, one dashboard, one dependency policy across the fleet.

> *One dashboard for every stack. The mechanism is shared. The policy is yours.*

---

## What Devstack Does

- **Process-stack supervision**
  Runs a stack of long-lived development processes under one live terminal dashboard —
  with real process-group teardown, per-process restart, readiness probes, and
  resource monitoring. No orphaned processes, on Linux or Windows.

- **One event model, three surfaces**
  The same run drives a live dashboard for humans, stable plain-text output for CI,
  and a structured JSON event stream for coding agents — so automation reads facts,
  never scrapes prose.

- **Bootstrap and readiness**
  Host package installation, checksum-verified asset fetch, and a doctor/readiness
  model with unambiguous pass/fail verdicts — `cargo xtask bootstrap | doctor | run |
  deps` behaves identically in every repository.

- **Fleet-wide dependency management**
  A single declarative fleet definition and one reviewable lock snapshot pin the
  toolchain, one version per external package, and per-repository internal exports —
  materialized into every repo's native manifests atomically.

- **Shared agent tooling**
  Devstack ships the fleet's coding-agent skills and policy hooks, pinned to the same
  version as the library, so human and agent workflows cannot drift apart.

---

## Why It's a Product

Every Thyraen repository — from onboard autonomy to embedded firmware to knowledge
systems — consumes Devstack for its developer surface. The library carries the
mechanism; each consuming repo supplies only its policy: which commands, which assets,
which processes, which crates.

That separation is what lets a small team run a large fleet of demanding repositories
with consistent quality gates, reproducible environments, and agent-operable tooling
everywhere.
