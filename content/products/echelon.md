+++
title = "Echelon"
slug = "echelon"
weight = 20

[extra]
group = "operate"
hero_title = "Echelon"
hero_subtitle = "Situational awareness and tasking for heterogeneous autonomous platforms"
card = "A contract-driven mission C2 control plane: canonical entities and tasks, strict reject-only validation, adapters for vehicles and tactical data feeds, and a 3D operator portal."
epigraph = "Aligned with the Army’s Next Generation C2 architecture."
related = ["vanguard", "dissident"]
masthead = "/images/mastheads/org-masthead.png"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Echelon** is a contract-driven situational awareness and tasking control plane for
heterogeneous robotic and autonomy platforms, aligned with the U.S. Army's Next
Generation C2 (NGC2) architecture.

Echelon ingests operational data from external mission runtimes, validates it against a
canonical domain model, maintains a coherent operational picture, and routes task
assignments to the runtimes that execute them.

Rather than centralizing autonomy, Echelon treats autonomy systems as external runtimes
and supplies the layer they lack: state validation, task routing, situational awareness,
and hard integration boundaries between dissimilar systems.

---

## Canonical Entities and Tasks

Everything Echelon knows is expressed as two canonical objects:

- **Entities** — observed world state
- **Tasks** — intent and execution state, with an authoritative lifecycle from
  assignment through acknowledgment, execution, and terminal status

Validation is strictly **reject-only**: invalid input is refused, never repaired,
normalized, or inferred. Undocumented behavior is undefined by design.

---

## Integration Through Adapters

External systems reach Echelon only through adapters, which enforce the contract
boundary:

- **Vanguard** vehicles publishing canonical entity, task, and media state
- **TAK** streaming Cursor-on-Target over TCP, UDP, or verified TLS
- **ADS-B** aircraft tracking
- **AIS** maritime traffic

An SDK provides scaffolding and canonical types for building new adapters against the
same contract.

---

## Operator Portal

The Echelon portal is a presentation-only 3D map workspace:

- Cesium-based globe with military symbology
- Capability-gated tasking — task UI appears only for entities that truthfully publish
  a task catalog
- Task queue and detail views
- Live video from platform sensors, resolved deterministically and delivered to the
  browser over WebRTC

The UI never owns or mutates system truth.

---

## Deployment Topologies

Echelon runs centrally on a control workstation, onboard a vehicle, or fully distributed
across peer nodes that exchange canonical Entities and Tasks — with each node enforcing
contracts independently.

---

## What Echelon Is Not

Echelon is **not**:

- A flight controller or platform autonomy stack — that is [Vanguard](/products/vanguard/)
- A mission planner or autonomy reasoning engine
- A requirement for centralized command
- A replacement for human decision-making
