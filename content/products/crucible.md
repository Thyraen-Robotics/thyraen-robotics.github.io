+++
title = "Crucible"
slug = "crucible"
weight = 60

[extra]
hero_title = "Crucible"
hero_subtitle = "Raw material in, refined capability out"
card = "A provenance-tracked data foundry turning raw sources into training-ready datasets and hardware-specific perception models with verifiable lineage."
masthead = "/images/mastheads/org-masthead.png"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

# Crucible

**Crucible** is the Thyraen Robotics data foundry: a provenance-tracked repository and
toolchain that turns raw source material into training-ready datasets and deployable
model capability.

Raw material in, refined capability out.

---

## Provenance-First Data Layers

Crucible keeps immutable original sources, curated references, cross-project
interpretations, per-project mappings, and machine-consumable datasets in separate
layers, each bound by stable IDs — so search indexes, data loaders, and downstream
consumers never depend on filenames.

Every dataset carries schema-validated metadata, checksummed assets, and a documented
review status.

---

## What Crucible Does

- **Framework-neutral dataset tooling**
  Validation, asset verification, statistics, record building with split indexes,
  COCO and Pascal VOC interchange, and cross-dataset training mixtures assembled by
  declared weights.

- **Config-driven training**
  A generic training harness where a per-run configuration declares the corpus blend,
  model, and hyperparameters.

- **Offline retrieval assistant**
  A self-contained document-QA tool doing retrieval-augmented generation over the
  datasets — built to run on workstations and embedded GPU hardware without network
  access.

- **Network-amputated labeling**
  A desktop image labeler with the network surface removed entirely, exporting
  standard formats that flow straight back into the dataset pipeline.

- **Deployable perception pipeline**
  A perception track carries data from curation through fine-tuning to
  hardware-specific, hash-qualified TensorRT engines with reviewed deployment
  profiles — the pipeline that produces perception models for
  [Vanguard](/products/vanguard/).

---

## Role in the Ecosystem

Crucible is where operational data becomes capability: imagery becomes detectors,
project documentation becomes searchable knowledge, and every derived artifact traces
back to its sources. Its outputs are consumed downstream with pinned digests and
verified provenance — never as loose files.
