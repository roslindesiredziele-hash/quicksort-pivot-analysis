import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("./data/data.csv")

# =====================================================
# VERY SMALL INPUTS (5-50)
# =====================================================

very_small = df[
    (df["Size"] >= 5) &
    (df["Size"] <= 50)
]

plt.figure(figsize=(10, 6))

plt.plot(
    very_small["Size"],
    very_small["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    very_small["Size"],
    very_small["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.title(
    "Quick Sort Pivot Comparison - Very Small Inputs (5-50)"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")

plt.xticks([
    5, 10, 15, 20, 25,
    30, 35, 40, 45, 50
])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/very_small_inputs.png",
    dpi=300
)

plt.close()

# =====================================================
# SMALL INPUTS (50-300)
# =====================================================

small = df[
    (df["Size"] >= 50) &
    (df["Size"] <= 300)
]

plt.figure(figsize=(10, 6))

plt.plot(
    small["Size"],
    small["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    small["Size"],
    small["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.title(
    "Quick Sort Pivot Comparison - Small Inputs (50-300)"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")

plt.xticks([
    50,
    100,
    150,
    200,
    300
])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/small_inputs.png",
    dpi=300
)

plt.close()

# =====================================================
# MEDIUM INPUTS (300-1000)
# =====================================================

medium = df[
    (df["Size"] >= 300) &
    (df["Size"] <= 1000)
]

plt.figure(figsize=(10, 6))

plt.plot(
    medium["Size"],
    medium["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    medium["Size"],
    medium["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.title(
    "Quick Sort Pivot Comparison - Medium Inputs (300-1000)"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")

plt.xticks([
    300,
    400,
    500,
    1000
])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/medium_inputs.png",
    dpi=300
)

plt.close()

# =====================================================
# LARGE INPUTS (1000-5000)
# =====================================================

large = df[
    (df["Size"] >= 1000) &
    (df["Size"] <= 5000)
]

plt.figure(figsize=(10, 6))

plt.plot(
    large["Size"],
    large["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    large["Size"],
    large["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.title(
    "Quick Sort Pivot Comparison - Large Inputs (1000-5000)"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")

plt.xticks([
    1000,
    2000,
    3000,
    4000,
    5000
])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/large_inputs.png",
    dpi=300
)

plt.close()

# =====================================================
# VERY LARGE INPUTS (5000-100000)
# =====================================================

very_large = df[
    (df["Size"] >= 5000) &
    (df["Size"] <= 100000)
]

plt.figure(figsize=(10, 6))

plt.plot(
    very_large["Size"],
    very_large["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    very_large["Size"],
    very_large["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.title(
    "Quick Sort Pivot Comparison - Very Large Inputs (5000-100000)"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")

plt.xticks([
    5000,
    10000,
    20000,
    50000,
    100000
])

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/very_large_inputs.png",
    dpi=300
)

plt.close()

# =====================================================
# LOGARITHMIC COMPARISON
# SMALL (5-100)
# LARGE (100-100000)
# =====================================================

plt.figure(figsize=(12, 7))

plt.plot(
    df["Size"],
    df["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot"
)

plt.plot(
    df["Size"],
    df["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot"
)

plt.xscale("log")
plt.yscale("log")

plt.axvline(
    100,
    color="gray",
    linestyle="--",
    linewidth=2,
    alpha=0.7
)

ypos = min(df["DualPivotMs"]) * 4

plt.text(
    20,
    ypos,
    "Small Inputs\n(5-100)"
)

plt.text(
    3000,
    ypos,
    "Full Benchmark\n(100-100000)"
)

plt.title(
    "Quick Sort Pivot Comparison (Log-Log Scale)"
)

plt.xlabel(
    "Input Size (Log Scale)"
)

plt.ylabel(
    "Execution Time (ms, Log Scale)"
)

plt.legend()

plt.grid(
    True,
    which="both",
    linestyle="--",
    alpha=0.6
)

plt.tight_layout()

plt.savefig(
    "./report/runtime_logarithmic.png",
    dpi=300
)

plt.close()

print("\nGenerated:")
print("  report/very_small_inputs.png")
print("  report/small_inputs.png")
print("  report/medium_inputs.png")
print("  report/large_inputs.png")
print("  report/very_large_inputs.png")
print("  report/runtime_logarithmic.png")