
#  ChaCha20 Encryption Internship Project

This repository contains the deliverables for the internship project titled **"ChaCha20: A Modern Encryption Method and Implementation in Python"** under the supervision of **Dr. Mohamed Samir**.

##  Overview

ChaCha20 is a fast and secure stream cipher designed by Daniel J. Bernstein. This project explores its structure, implementation, and performance in Python, both manually and using cryptographic libraries.

##  Project Structure

```
 ChaCha20-Internship/
├── report/                       
│   └── ChaCha20_Report.pdf
├── src/
│   ├── Manual Implementation.py     
│   └── Simplified Implementation.py       
├── test/
│   ├── testing_file.txt        
│   ├── encrypted_manual_output.bin
│   └── encrypted_library_output.bin
│   └── encrypted_manual_optimized.bin
└── README.md
```

## 🛠 Implementations

### 1. Manual ChaCha20
- Built entirely from scratch using ARX operations (Add, Rotate, XOR)
- Full control of quarter rounds, state matrix, and keystream generation
- Contains benchmarking for encryption time

### 2. Cryptography Library Version
- Uses `cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20`
- Extremely fast and production-ready

##  Performance

| Implementation          | Time (ms)    |
|-------------------------|--------------|
| Manual (Original)       | 4038.99 ms   |
| Manual (Optimized)      | 2276.56 ms   |
| Library (`cryptography`)| 1.61 ms      |

> Optimized version is **1.77× faster** than the original manual code.

##  How to Test

Run any of the implementations with the sample file:

```bash
python src/Manual Implementation.py
python src/Simplified Implementation.py
```

Make sure `testing_file.txt` is present in the working directory. It will be encrypted and saved as `.bin`.

##  Final Report

A detailed report written in LaTeX can be found in the `/report/` folder. It covers:

- History and use cases of ChaCha20
- State matrix explanation
- ARX operations
- Manual and library implementation
- Side-channel attack resistance
- Performance benchmarking
- Optimization strategies

##  Authors

- Abdelaleem Baher  
- Mazen Ahmed  

Supervised by: **Dr. Mohamed Samir**

---

© 2025 | For academic and learning purposes only
