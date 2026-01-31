+++
title = "Echelon"
slug = "echelon"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

# Echelon

**Echelon** is the mission autonomy and mission command-and-control (C2) capability within the Thyraen Robotics ecosystem. It translates intent into coordinated tasks, maintains shared mission state, and enables autonomous agents to operate coherently under human authority.

---

## Role in the Thyraen Ecosystem

Echelon serves as the **mission reasoning and coordination layer** that binds
autonomous activity into coherent mission execution.

It is responsible for:
- Representing shared mission state
- Translating intent into executable tasks
- Coordinating activity across agents and systems
- Providing mission-level visibility and control to operators

Other Thyraen capabilities, such as Breacher, are tasked and coordinated through
Echelon rather than operating independently.

---

## What Echelon Does

Echelon focuses on four core functions:

- **Mission state representation**  
  Maintaining a shared representation of entities, tasks, objectives, and constraints
  across participating agents and systems.

- **Tasking and coordination**  
  Creating, assigning, tracking, and managing mission tasks across single platforms
  and coordinated teams.

- **Mission adaptation**  
  Supporting task reallocation and execution adjustment in response to changing
  conditions, within defined constraints.

- **Mission C2 interaction**  
  Providing operators with situational awareness, task visibility, and mechanisms
  for intervention without micromanagement.

These functions operate at the mission layer rather than at the level of vehicle control.

---

## Autonomy and Deployment

Echelon supports multiple operational configurations depending on mission needs and
operating conditions.

It may:
- Execute onboard autonomous agents as a headless mission autonomy service
- Operate across multiple distributed nodes coordinating peer activity
- Function as a centralized mission coordination node when appropriate

These configurations may coexist within a single mission and do not require a fixed
deployment topology.

---

## Human Interaction

Echelon integrates humans as **mission authorities**.

Human operators:
- Define mission intent and objectives
- Establish constraints, priorities, and policies
- Supervise mission execution
- Intervene or approve actions as required

Echelon focuses on execution and coordination within those bounds, not on replacing
human command authority.

---

## What Echelon Is Not

Echelon is **not**:
- A flight controller or platform autonomy stack
- A vehicle-specific mission planner
- A requirement for centralized command
- A replacement for human decision-making

It is a mission-level autonomy and C2 capability designed to integrate with platform
autonomy systems and human operators.

---

## Relationship to Detailed Documentation

Operational concepts, deployment considerations, and implementation details are
maintained with the Echelon product documentation.
