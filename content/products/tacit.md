+++
title = "Tacit"
slug = "tacit"
weight = 30

[extra]
group = "connect"
hero_title = "Tacit"
hero_subtitle = "A quiet datalink for contested spectrum"
card = "A low-probability-of-detection radio control plane linking vehicles with authenticated, reliable delivery at the minimum RF footprint the moment allows."
epigraph = "The link is the first casualty."
related = ["vanguard"]
masthead = "/images/backgrounds/bg-connect.svg"
+++

<!-- synced from Thyraen-Robotics/.github; do not edit here -->

**Tacit** is a quiet ship-to-ship datalink: a low-rate, high-reliability,
low-probability-of-detection (LPD) radio link that serves as the vehicle-to-vehicle
control plane for Vanguard.

Tacit carries command-and-control, telemetry, position reports, and mission-state sync
between platforms in contested spectrum, with no supporting infrastructure.

> *The link is the first casualty.* Tacit is built to be hard to notice, hard to
> localize, hard to jam — and able to walk itself out of a degraded channel without
> operator intervention.

---

## Design Principles

- **Minimum RF footprint**
  Closed-loop power backoff, airtime discipline with terse send-on-change frames, and
  the lowest data rate that closes the link. The adaptive link architecture drives
  power, modulation, channel, and medium access from local evidence — SNR, missed
  acknowledgments, and observed noise floor.

- **Authenticated, reliable delivery**
  Authenticated encryption on every frame, acknowledged unicast with bounded retry,
  and at-most-once delivery with replay protection.

- **Built for losable hardware**
  Session keys ratchet from a root secret rather than a flat pre-shared key, debug
  ports are locked, and keys live in RAM with a zeroize path.

- **Provable before it radiates**
  A deterministic, no-heap protocol core with statically bounded resources — the same
  compiled code runs in the firmware, the desktop simulator, and the property-based
  test suite.

---

## Hardware

Tacit runs on compact commercial LoRa hardware (Nordic nRF52840 + Semtech SX1262),
speaking raw sub-GHz PHY — deliberately not LoRaWAN or Meshtastic. Regulatory
constraints (channel plan, dwell, power caps) enter as a swappable compile-time
profile.

The host platform talks to Tacit as a simple serial device through a compact framed
protocol — the vehicle never needs to understand radio, hopping, or cryptography.

---

## What Tacit Is Not

Tacit is **not**:

- A high-throughput data pipe — it is a control plane, engineered for reliability and
  quiet operation rather than bandwidth
- A mesh-networking hobbyist stack
- A guarantee of invisibility against dedicated wide-band collection — detectability is
  minimized within the physics of the radio, and claims stop where the silicon does
