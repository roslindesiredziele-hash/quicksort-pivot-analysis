# Dangerous Quickminds

An empirical comparison of Single-Pivot and Dual-Pivot Quick Sort implementations in C++. The project investigates how the number of pivots affects sorting performance and analyzes the practical relationship between pivot selection and execution time.

## Overview

Quick Sort is one of the most widely used comparison-based sorting algorithms.

Traditional Quick Sort partitions an array around a single pivot element and recursively sorts the resulting subarrays. Modern variants may use multiple pivots to improve partitioning efficiency and reduce practical running time.

This project compares:

- Single-Pivot Quick Sort
- Dual-Pivot Quick Sort

through experimental benchmarking on randomly generated datasets ranging from very small to very large input sizes.

---

## Problem Statement

Investigate the relationship between:

```text
Number of Pivots
```

and:

```text
Sorting Runtime
```

by comparing the performance of:

```text
Single-Pivot Quick Sort
```

and:

```text
Dual-Pivot Quick Sort
```

over multiple input-size ranges.

---

## Algorithms

### Single-Pivot Quick Sort

The Single-Pivot implementation selects a random pivot and partitions the array into two regions:

```text
Elements <= Pivot
Elements > Pivot
```

After partitioning, the algorithm recursively sorts both subarrays.

Implementation:

```cpp
int p = rand() % n;
int P = arr[p];
```

Average-case complexity:

```text
O(n log n)
```

Worst-case complexity:

```text
O(n²)
```

---

### Dual-Pivot Quick Sort

The Dual-Pivot implementation uses two pivot elements:

```text
Pivot 1
Pivot 2
```

The array is partitioned into three regions:

```text
< Pivot 1

Pivot 1 <= x <= Pivot 2

> Pivot 2
```

This generally produces more balanced partitions and can reduce practical running time.

Average-case complexity:

```text
O(n log n)
```

Worst-case complexity:

```text
O(n²)
```

---

## Benchmarking Methodology

Execution time was measured using:

```cpp
QueryPerformanceCounter()
```

from the Windows API.

Input sizes:

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

### Fair Comparison

For every benchmark repetition:

1. A random array was generated.
2. The array was duplicated.
3. Single-Pivot Quick Sort sorted one copy.
4. Dual-Pivot Quick Sort sorted the other copy.

This ensured that both algorithms always processed identical input data.

---

## Complexity Analysis

Let:

```text
n
```

be the number of elements.

### Single-Pivot Quick Sort

Average Case:

```text
O(n log n)
```

Worst Case:

```text
O(n²)
```

Space Complexity:

```text
O(log n)
```

average recursion depth.

---

### Dual-Pivot Quick Sort

Average Case:

```text
O(n log n)
```

Worst Case:

```text
O(n²)
```

Space Complexity:

```text
O(log n)
```

average recursion depth.

---

## Complexity Discussion

The theoretical complexity of both algorithms is identical:

```text
O(n log n)
```

Therefore, increasing the number of pivots does not improve asymptotic complexity.

Instead, performance improvements come from:

- More efficient partitioning.
- Better partition balance.
- Reduced practical constant factors.

The objective of this investigation is therefore not to improve Big-O complexity, but to evaluate real-world execution time.

---

## Experimental Results

### Benchmark Results

| Size | Single Pivot (ms) | Dual Pivot (ms) |
|------:|------:|------:|
| 5 | 0.00015 | 0.00013 |
| 50 | 0.00322 | 0.00196 |
| 100 | 0.00772 | 0.00451 |
| 500 | 0.04058 | 0.02702 |
| 1000 | 0.09128 | 0.06416 |
| 5000 | 0.52581 | 0.36881 |
| 10000 | 1.11442 | 0.79344 |
| 50000 | 6.87260 | 4.82085 |
| 100000 | 13.80490 | 9.59887 |

### Key Observation

Dual-Pivot Quick Sort outperformed Single-Pivot Quick Sort for every tested input size.

For the largest dataset:

```text
100000 elements
```

Single-Pivot Quick Sort required:

```text
13.80 ms
```

whereas Dual-Pivot Quick Sort required:

```text
9.60 ms
```

representing an improvement of approximately:

```text
30%
```

---

## Generated Figures

### Very Small Inputs (5–50)

```text
report/very_small_inputs.png
```

The benchmark demonstrates that Dual-Pivot Quick Sort already performs slightly better on very small arrays. However, the absolute execution times remain extremely small.

---

### Small Inputs (50–300)

```text
report/small_inputs.png
```

The advantage of Dual-Pivot Quick Sort becomes more visible as the input size increases. Both algorithms remain extremely efficient.

---

### Medium Inputs (300–1000)

```text
report/medium_inputs.png
```

The performance gap continues to widen. Both implementations exhibit similar growth behavior, but Dual-Pivot Quick Sort consistently requires less execution time.

---

### Large Inputs (1000–5000)

```text
report/large_inputs.png
```

The runtime difference becomes clearly measurable. Dual-Pivot Quick Sort maintains a noticeable performance advantage while preserving identical asymptotic complexity.

---

### Very Large Inputs (5000–100000)

```text
report/very_large_inputs.png
```

The advantage of Dual-Pivot Quick Sort remains consistent across all large datasets, demonstrating improved practical efficiency.

---

### Logarithmic Runtime Comparison

```text
report/runtime_logarithmic.png
```

The logarithmic graph provides the clearest view of algorithm growth.

The two curves remain nearly parallel throughout the benchmark, showing that both implementations exhibit:

```text
O(n log n)
```

average-case behavior.

The consistently lower position of the Dual-Pivot curve demonstrates improved practical performance due to better partitioning rather than superior asymptotic complexity.

---

## Build

Compile:

```bash
g++ src/main.cpp src/QuickSorts.cpp -o benchmark
```

---

## Usage

Run:

```bash
./benchmark.exe
```

The program:

1. Generates random arrays.
2. Creates identical copies.
3. Sorts one copy using Single-Pivot Quick Sort.
4. Sorts the other copy using Dual-Pivot Quick Sort.
5. Measures execution times.
6. Exports benchmark results.

---

## Output Dataset

Benchmark data is exported to:

```text
data/data.csv
```

Format:

```csv
Size,SinglePivotMs,DualPivotMs
5,...
10,...
...
100000,...
```

---

## Generate Graphs

Install dependencies:

```bash
py -3.13 -m pip install pandas matplotlib
```

Run:

```bash
py -3.13 report/graph.py
```

Generated files:

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

This project investigated the effect of increasing the number of pivots in Quick Sort.

Both algorithms exhibited the expected:

```text
O(n log n)
```

average-case complexity, as confirmed by the logarithmic benchmark graph.

However, Dual-Pivot Quick Sort consistently achieved lower execution times across all tested input sizes. The benchmark results indicate that increasing the number of pivots from one to two improves practical performance by reducing constant factors while preserving the same asymptotic complexity.

The results demonstrate that algorithmic design choices affecting partition quality can significantly influence real-world performance even when theoretical complexity remains unchanged.

---

## Author

**Desire Roslin Dziele**  
Computer Science Student  
University of Łódź