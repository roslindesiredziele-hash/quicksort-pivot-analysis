import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/benchmark.csv")

# =====================================================
# Runtime Comparison
# =====================================================

plt.figure(figsize=(12, 7))

plt.plot(
    df["Size"],
    df["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot Quick Sort"
)

plt.plot(
    df["Size"],
    df["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot Quick Sort"
)

plt.axvspan(5, 50, alpha=0.15, color="green")
plt.axvspan(50, 300, alpha=0.15, color="blue")
plt.axvspan(300, 1000, alpha=0.15, color="orange")
plt.axvspan(1000, 100000, alpha=0.15, color="red")

ypos = max(df["SinglePivotMs"]) * 0.15

plt.text(
    25,
    ypos,
    "Very Small\n(5-50)",
    ha="center"
)

plt.text(
    175,
    ypos,
    "Small\n(50-300)",
    ha="center"
)

plt.text(
    650,
    ypos,
    "Medium\n(300-1000)",
    ha="center"
)

plt.text(
    50000,
    ypos,
    "Large\n(1000-100000)",
    ha="center"
)

plt.title(
    "Single-Pivot vs Dual-Pivot Quick Sort Runtime"
)

plt.xlabel(
    "Input Size"
)

plt.ylabel(
    "Execution Time (ms)"
)

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "./report/runtime_comparison.png",
    dpi=300
)

plt.close()

# =====================================================
# Logarithmic Comparison
# =====================================================

plt.figure(figsize=(12, 7))

plt.plot(
    df["Size"],
    df["SinglePivotMs"],
    marker="o",
    linewidth=2,
    label="Single Pivot Quick Sort"
)

plt.plot(
    df["Size"],
    df["DualPivotMs"],
    marker="o",
    linewidth=2,
    label="Dual Pivot Quick Sort"
)

plt.xscale("log")
plt.yscale("log")

plt.axvline(
    100,
    color="gray",
    linestyle="--",
    alpha=0.7
)

plt.text(
    30,
    min(df["DualPivotMs"]) * 3,
    "Small Inputs\n(5-100)"
)

plt.text(
    3000,
    min(df["DualPivotMs"]) * 3,
    "Large Inputs\n(100-100000)"
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

print("Generated:")
print("  report/runtime_comparison.png")
print("  report/runtime_logarithmic.png")