import matplotlib.pyplot as plt
import pandas as pd

# --- MANUAL TIME WINDOW CONFIGURATION (Elapsed Time) ---
t_start = 1.0   # Starts at 1s so the log scale opens up properly
t_end = 1000.0  # Goes up to 1000s across multiple log decades

# --- 1. LOAD AND PROCESS DATA ---
phiT_file = "0_3Lam_225Down_phiT.dat"
phi_file = "0_3Lam_225Down_phi.dat"

df_phiT = pd.read_csv(phiT_file, sep=r"\s+", comment="#")
df_phi = pd.read_csv(phi_file, sep=r"\s+", comment="#")

# Extract columns
time_col = df_phiT.columns[0]
df_merged = pd.DataFrame({
    "Raw_Time": df_phiT[time_col],
    "phiT": df_phiT[df_phiT.columns[1]],
    "phi": df_phi[df_phi.columns[1]],
})

# Calculate concentration and normalize
df_merged["Concentration"] = df_merged["phiT"] / df_merged["phi"]
initial_concentration = df_merged["Concentration"].iloc[0]

if pd.isna(initial_concentration) or initial_concentration == 0:
    initial_concentration = 1.0

df_merged["Normalized_Concentration"] = df_merged["Concentration"] / initial_concentration

# SHIFT TIME SO IT STARTS AT 0 (Then add 1 so log scale accepts t_start)
min_time = df_merged["Raw_Time"].min()
df_merged["Elapsed_Time"] = (df_merged["Raw_Time"] - min_time) + 1.0

# Filter data based on manual variables
df_filtered = df_merged[
    (df_merged["Elapsed_Time"] >= t_start) &
    (df_merged["Elapsed_Time"] <= t_end) &
    (df_merged["Normalized_Concentration"] > 0)
].copy()

# --- 2. PLOTTING CONFIGURATION ---
plt.figure(figsize=(7, 6))

# Plot CFD Simulation Line (0.3 L/min in Orange)
plt.plot(
    df_filtered["Elapsed_Time"],
    df_filtered["Normalized_Concentration"],
    color="#ff7f0e",
    linewidth=2.5,
    linestyle="-",
    label="CFD ($0.3\\text{ L min}^{-1}$)"
)

# --- 3. AXES AND FORMATTING ---
plt.xscale("log")
plt.yscale("log")

# Set limits to match multiple log decades ($10^0$ to $10^3$)
plt.xlim(t_start, t_end)
plt.ylim(1e-4, 1.2)

# Labels and Text Annotations
plt.xlabel("Time, $t$ [s]", fontsize=12, fontweight="bold")
plt.ylabel("$\\tilde{N}(t)$ at outlet [-]", fontsize=12, fontweight="bold")

# Position text box dynamically
plt.text(
    250, 5e-1,
    "TSI 3077A no insert",
    fontsize=11, fontweight="bold",
    bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none")
)

# Grid and Legend
plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
plt.legend(loc="lower left", frameon=True, edgecolor="black")

plt.tight_layout()
plt.show()