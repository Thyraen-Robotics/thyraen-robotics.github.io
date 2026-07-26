+++
title = "Augur"
slug = "augur"
weight = 70

[extra]
group = "build"
hero_title = "Augur"
hero_subtitle = "The doctrine knowledge substrate"
card = "Decomposes military doctrine into a cited, version-aware knowledge graph and answers doctrine questions with claims resolved to publication and paragraph — or an honest not-found."
epigraph = "Decompose the doctrine we have. Author the doctrine autonomous warfare needs."
related = ["vanguard"]
masthead = "/images/backgrounds/bg-build.svg"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Augur** is the doctrine knowledge substrate: it decomposes the doctrine we have, so we
can author the doctrine autonomous warfare needs.

Augur turns paragraph-numbered military doctrine publications into a version-aware,
provenance-stamped knowledge graph that machines can actually read — every paragraph,
term, concept, task, condition, standard, capability, and effect, each carrying the
literal source span it came from.

---

## What Augur Does

- **Doctrine to knowledge graph, repeatably**
  An offline, stage-by-stage pipeline parses publications, extracts structured
  knowledge, and loads a graph database with vector search — governed by a single
  ontology source of truth.

- **Zero fabrication, enforced by construction**
  Every extracted claim carries a grounding quote verified against the source
  paragraph. Spans that don't appear in the source are rejected and fail the build.
  "No fabrication" is a build property, not a prompt instruction.

- **A cited thought-partner**
  Ask a doctrine question and get back claims resolved to publication, paragraph, and
  version — or an explicit "not found in current doctrine." Never an uncited answer.

- **Supersession-aware retrieval**
  Current-doctrine search is structurally restricted to current publications;
  superseded doctrine cannot leak into current answers, and historical lookup stays
  explicit.

- **Doctrine modernization as graph authoring**
  Hold a task's purpose constant, swap in an autonomous capability set, and re-derive
  its conditions and standards with provable lineage back to the doctrine being
  adapted. Derived doctrine stays permanently distinguishable from source doctrine —
  a consumer always knows "the publication says X" from "Augur proposes X, derived
  from it."

---

## Built for Closed Networks

Augur is airgap-capable by design: a single provider seam swaps hosted language models
for on-premises inference, and the deployable footprint is native binaries, static
frontend assets, and local models — no container stack required on the target.

Analysts work in a single-URL workbench: a doctrine library, a review surface for
derived proposals, a graph lens over the real knowledge graph, and a persistent cited
chat.

---

## Role in the Ecosystem

Autonomy that operates within doctrine has to be able to read it. Augur gives the
Thyraen ecosystem a machine-readable doctrinal foundation — and a disciplined path for
proposing how doctrine should evolve as autonomous capability replaces assumptions
written for manned formations.
