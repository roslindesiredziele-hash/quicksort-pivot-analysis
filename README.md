# Dangerous Quickminds

A C++ benchmarking project that compares Single-Pivot Quick Sort and Dual-Pivot Quick Sort to investigate how the number of pivots influences sorting performance.

## Overview

Quick Sort is one of the most widely used comparison-based sorting algorithms.

This project compares:

- Single-Pivot Quick Sort
- Dual-Pivot Quick Sort

using randomly generated datasets ranging from very small inputs to arrays containing 100,000 elements.

The objective is to determine whether increasing the number of pivots improves practical performance while preserving the same theoretical complexity.

---

## Algorithms

### Single-Pivot Quick Sort

Partitions the array around a single randomly selected pivot.

```text
<= Pivot | > Pivot
```

### Dual-Pivot Quick Sort

Partitions the array using two pivots.

```text
< Pivot1

Pivot1 <= x <= Pivot2

> Pivot2
```

This often produces more balanced partitions and improves practical runtime.

---

## Complexity Analysis

Let:

```text
n
```

be the number of elements.

| Algorithm | Average Case | Worst Case | Space |
|-----------|-------------|------------|--------|
| Single-Pivot Quick Sort | O(n log n) | O(n²) | O(log n) |
| Dual-Pivot Quick Sort | O(n log n) | O(n²) | O(log n) |

Both algorithms have identical asymptotic complexity.

The purpose of the benchmark is therefore to measure practical performance differences caused by partitioning strategy and constant factors.

---

## Benchmark Setup

Execution time was measured using:

```cpp
QueryPerformanceCounter()
```

Benchmark sizes:

```text
5
10
15
20
25
30
35
40
45
50
100
150
200
300
400
500
1000
2000
3000
4000
5000
10000
20000
50000
100000
```

For every repetition:

1. A random array was generated.
2. The array was duplicated.
3. Single-Pivot Quick Sort sorted one copy.
4. Dual-Pivot Quick Sort sorted the other copy.

This ensured that both algorithms always processed identical data.

---

## Performance Comparison

| Size | Single Pivot (ms) | Dual Pivot (ms) | Improvement |
|------:|------:|------:|------:|
| 100 | 0.00772 | 0.00451 | 41.6% |
| 1,000 | 0.09128 | 0.06416 | 29.7% |
| 10,000 | 1.11442 | 0.79344 | 28.8% |
| 100,000 | 13.80490 | 9.59887 | 30.5% |

### Key Finding

Dual-Pivot Quick Sort outperformed Single-Pivot Quick Sort for every tested input size.

For arrays containing:

```text
100,000 elements
```

Dual-Pivot Quick Sort completed in:

```text
9.60 ms
```

compared to:

```text
13.80 ms
```

for Single-Pivot Quick Sort.

---

## Generated Figures

### Very Small Inputs (5–50)

```text
report/very_small_inputs.png
```

Compares the algorithms on tiny arrays where overhead dominates execution time.

### Small Inputs (50–300)

```text
report/small_inputs.png
```

Shows the first noticeable performance differences between the two implementations.

### Medium Inputs (300–1000)

```text
report/medium_inputs.png
```

Illustrates the growing advantage of Dual-Pivot Quick Sort.

### Large Inputs (1000–5000)

```text
report/large_inputs.png
```

Highlights increasingly significant runtime differences.

### Very Large Inputs (5000–100000)

```text
report/very_large_inputs.png
```

Demonstrates the practical performance advantage of Dual-Pivot Quick Sort on large datasets.

### Logarithmic Runtime Comparison

```text
report/runtime_logarithmic.png
```

The most important graph in the project.

The nearly parallel curves confirm that both algorithms maintain:

```text
O(n log n)
```

average-case complexity.

The lower position of the Dual-Pivot curve indicates improved practical performance rather than improved asymptotic complexity.

---

## Build

Compile:

```bash
g++ src/main.cpp src/QuickSorts.cpp -o benchmark
```

---

## Run Benchmark

Execute:

```bash
./benchmark.exe
```

This will:

1. Generate benchmark datasets.
2. Measure execution times.
3. Export benchmark results to:

```text
data/data.csv
```

---

## Generate Graphs

Install dependencies:

```bash
py -3.13 -m pip install pandas matplotlib
```

Generate all graphs:

```bash
py -3.13 report/graph.py
```

Output:

```text
report/
├── very_small_inputs.png
├── small_inputs.png
├── medium_inputs.png
├── large_inputs.png
├── very_large_inputs.png
└── runtime_logarithmic.png
```

---

## Project Structure

```text
dangerous-quickminds
│
├── data/
│   └── data.csv
│
├── report/
│   ├── graph.py
│   ├── very_small_inputs.png
│   ├── small_inputs.png
│   ├── medium_inputs.png
│   ├── large_inputs.png
│   ├── very_large_inputs.png
│   └── runtime_logarithmic.png
│
├── src/
│   ├── QuickSorts.h
│   ├── QuickSorts.cpp
│   └── main.cpp
│
├── README.md
└── benchmark.exe
```

---

## Conclusion

Both Single-Pivot and Dual-Pivot Quick Sort exhibited the expected:

```text
O(n log n)
```

average-case complexity.

However, Dual-Pivot Quick Sort consistently achieved lower execution times across all tested input sizes.

The benchmark results demonstrate that increasing the number of pivots from one to two improves practical sorting performance while preserving the same asymptotic complexity.

---

## Author

**Desire Roslin Dziele**  
Computer Science Student  
University of Łódź