# NextGen-PQCrypto-Dilithium

> A multi-mode optimized Dilithium post-quantum signature platform for software and embedded systems.

---

## 🚀 Overview

With the rapid development of quantum computing, traditional public-key cryptographic systems face severe security threats. Post-quantum cryptography (PQC) has become a critical direction for future secure systems.

This project is based on the official implementation of **CRYSTALS-Dilithium**, a NIST-standardized post-quantum digital signature scheme. We extend it into a **multi-mode adaptive optimization platform**, targeting real-world deployment scenarios across **resource-constrained embedded devices and high-performance systems**.

---

## 🌐 Toward a Post-Quantum Cryptographic Ecosystem

This project is not just an algorithmic optimization, but an effort to build a **lightweight and practical post-quantum cryptographic ecosystem**, featuring:

- 📦 Precompiled libraries for rapid integration (.so / .a)
- ⚙️ Multi-mode adaptive optimization for diverse hardware environments
- 🔌 Unified API for cross-platform development
- 🧩 Support for all Dilithium security levels (2 / 3 / 5)

By lowering the barrier to adoption, we aim to accelerate the **industrial deployment of post-quantum signature schemes** in real-world systems.

---

## ✨ Key Features

- 🔐 Based on NIST PQC standard **CRYSTALS-Dilithium**
- ⚡ Three optimization modes for different application scenarios
- 💾 Support for both **performance-critical** and **memory-constrained** environments
- 🖥️ Ready-to-use shared libraries (`.so`) and static libraries (`.a`)
- 🔁 Unified interface for:
  - Key Generation
  - Signing
  - Verification

---

## ⚙️ Multi-Mode Optimization

We propose three optimization modes to adapt Dilithium to different system constraints:

### 🔥 Mode 1 — Performance-Optimized

- Introduces **pre-rejection sampling**
- Reduces unnecessary computation in signing
- Achieves up to **~26% speedup in signature generation**

✅ Best for:
- High-performance servers
- Real-time signing systems

---

### 💾 Mode 2 — Memory-Optimized

- Streaming generation of matrix A
- Memory reuse techniques
- On-the-fly computation of constants

- Significantly reduces RAM usage

⚠️ Trade-off:
- Increased computation time

✅ Best for:
- Embedded systems
- IoT devices
- Memory-constrained environments

---

### ⚖️ Mode 3 — Balanced Mode

- Combines:
  - Pre-rejection sampling
  - Memory optimization strategies

- Achieves:
  - ~11% performance improvement
  - ~24% memory reduction

✅ Best for:
- General-purpose deployments
- Edge computing scenarios

---

## 📂 Project Structure

```
NextGen-PQCrypto-Dilithium/
│  api.h
│  README.md
│
├─demo/
│  demo.py
│  libdilithium_mode3.so
│
├─mode1/
│  libdilithium_f407_mode1.a
│  libdilithium_mode1.so
│
├─mode2/
│  libdilithium_f407_mode2.a
│  libdilithium_mode2.so
│
└─mode3/
   libdilithium_f407_mode3.a
   libdilithium_mode3.so
```

---

## 🧪 Supported Functions

All modes provide a unified API covering:

- `KeyGen` — Key pair generation  
- `Sign` — Message signing  
- `Verify` — Signature verification  

Supported security levels:

- Dilithium2  
- Dilithium3  
- Dilithium5  

---

## 🐍 Python Demo (Using .so)

You can directly use the shared library in Python:

```python
import ctypes

lib = ctypes.CDLL("./libdilithium.so")
```

💼 Application Scenarios

This project targets practical deployment of post-quantum signatures in:

🔒 Secure communication systems
🌐 IoT and embedded devices
☁️ Cloud authentication services
🏦 Financial and identity systems
🔗 Blockchain and distributed systems
🧩 Industrial Value

By providing ready-to-use optimized libraries + adaptive modes, this project:

Reduces integration cost for developers
Enables PQC deployment on constrained hardware
Bridges the gap between academic research and real-world systems
Serves as a building block for future post-quantum secure infrastructure

---

📖 Reference

CRYSTALS-Dilithium Official Implementation:
https://github.com/pq-crystals/dilithium

📌 Future Work

Hardware acceleration (ARM / RISC-V)
Integration with TLS / secure protocols
Automatic mode selection based on runtime environment
Extended PQC algorithm support

👥 Acknowledgment

This project is based on the official Dilithium implementation and extends it with engineering-oriented optimizations for real-world deployment.

⭐ If you find this project useful

Give it a star and help promote post-quantum cryptography!
