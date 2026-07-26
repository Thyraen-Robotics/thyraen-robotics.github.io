+++
title = "Dissident"
slug = "dissident"
weight = 40

[extra]
group = "connect"
hero_title = "Dissident"
hero_subtitle = "Vendor-free drone video, from goggles to the tactical map"
card = "Captures encoded live drone video without vendor apps or firmware modification and republishes it as RTSP and Cursor-on-Target for ATAK and TAKX."
epigraph = "From goggles to the tactical map — no vendor software in the loop."
related = ["echelon"]
masthead = "/images/backgrounds/bg-connect.svg"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Dissident** is an open, cross-platform receiver stack for encoded drone video: it
captures live video from commodity hardware without any vendor application, SDK, or
firmware modification, and republishes it to the tools operators already use.

From goggles to the tactical map — with no vendor software in the loop.

---

## What Dissident Does

- **Vendor-free acquisition**
  Discovers and authorizes the video source over Bluetooth, joins its network, and
  maintains the live-view session directly — no vendor app, no vendor SDK, and no
  firmware modification. The current source adapter targets the DJI Goggles 3
  live-view stream over BLE + Wi-Fi or USB.

- **Portable protocol core**
  A sans-I/O Rust core owns framing, session protocol, and loss-aware H.264
  reassembly, so every platform frontend wraps the same proven code.

- **Local decode and display**
  Hardware-accelerated decode and display on Android and desktop, tolerant of
  late-join streams.

- **Republication to the tactical map**
  The received video is republished as RTSP/RTP alongside Cursor-on-Target video
  announcements, delivered to ATAK and TAKX as self-contained plugins — each embedding
  the full receiver runtime with no separate daemon to install.

- **Protocol lab tooling**
  A streaming CLI inspects captures, extracts elementary streams, and generates video
  announcements for integration testing.

---

## Verified on Real Hardware

Both the wireless and USB acquisition paths are verified end to end against real
hardware, on Android and directly on Linux, at 1080p60.

Targets include Ubuntu x86_64, Android, Raspberry Pi, and NVIDIA Jetson.

---

## What Dissident Is Not

Dissident is **not**:

- A vendor SDK wrapper — it contains no vendor code and modifies no firmware
- A video pipeline tied to one ecosystem — the protocol core is deliberately portable
  and the source-adapter boundary is designed for additional devices
