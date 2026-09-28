import matplotlib.pyplot as plt
import pandas as pd

# --- MANUAL TIME WINDOW CONFIGURATION (Elapsed Time) ---
t_start = 0.0   # Starts cleanly at 0 seconds for linear scale
t_end = 30  # Goes up to 1000s

# --- 1. LOAD AND PROCESS DATA ---
phiT_file = "0_3Lam_225Up_phiT.dat"
phi_file = "0_3Lam_225Up_phi.dat"

df_phiT = pd.read_csv(phiT_file, sep=r"\s+", comment="#")
df_phi = pd.read_csv(phi_file, sep=r"\s+", comment="#")

# Extract columns
time_col = df_phiT.columns[0]
df_merged = pd.DataFrame({
    "Raw_Time": df_phiT[time_col],
    "phiT": df_phiT[df_phiT.columns[1]],
    "phi": df_phi[df_phi.columns[1]],
})

# Calculate raw concentration
df_merged["Concentration"] = df_merged["phiT"] / df_merged["phi"]

# Normalize by the steady-state (maximum) concentration
max_concentration = df_merged["Concentration"].max()
if pd.isna(max_concentration) or max_concentration == 0:
    max_concentration = 1.0

df_merged["Normalized_Concentration"] = df_merged["Concentration"] / max_concentration

# SHIFT TIME SO IT STARTS AT 0 (No need to add 1 for linear scale)
min_time = df_merged["Raw_Time"].min()
df_merged["Elapsed_Time"] = df_merged["Raw_Time"] - min_time

# Filter data based on manual variables
df_filtered = df_merged[
    (df_merged["Elapsed_Time"] >= t_start) &
    (df_merged["Elapsed_Time"] <= t_end) &
    (df_merged["Normalized_Concentration"] >= 0)
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

# --- 3. AXES AND FORMATTING (LINEAR) ---
# (Log scale lines are removed here)

# Set limits for linear scale (Time: 0 to 1000, Concentration: slightly below 0 to slightly above 1)
plt.xlim(t_start, t_end)
plt.ylim(-0.05, 1.05)

# Labels and Text Annotations
plt.xlabel("Time, $t$ [s]", fontsize=12, fontweight="bold")
plt.ylabel("$\\tilde{N}(t)$ at outlet [-]", fontsize=12, fontweight="bold")

# Position text box dynamically for linear coordinates
plt.text(
    250, 0.4,
    "TSI 3077A no insert",
    fontsize=11, fontweight="bold",
    bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none")
)

# Grid and Legend
plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
plt.legend(loc="lower right", frameon=True, edgecolor="black") # Moved to lower right since curve rises there

plt.tight_layout()
plt.show()