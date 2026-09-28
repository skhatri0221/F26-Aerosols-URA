import os
import re
import glob
import matplotlib.pyplot as plt
import pandas as pd
# from scipy.interpolate import make_interp_spline
import numpy as np

# ============================================================
# USER CONFIGURATION
# ============================================================

# Change this to the folder you want to process
FOLDER_NAME = "0_3Lam"

# Time window
t_start = 0.0
t_end = 30.0


# ============================================================
# FIND FILES
# ============================================================

phi_files = glob.glob(
    os.path.join(FOLDER_NAME, "*_phi.dat")
)

print(f"Found {len(phi_files)} phi files.")


# ============================================================
# PROCESS EACH PARTICLE SIZE
# ============================================================

results = []
steady_state_results = []

for phi_file in phi_files:

    # --------------------------------------------------------
    # Find matching phiT file
    # --------------------------------------------------------

    phiT_file = phi_file.replace("_phi.dat", "_phiT.dat")

    if not os.path.exists(phiT_file):
        print(f"WARNING: No matching phiT file for {phi_file}")
        continue

    # Get filename only
    filename = os.path.basename(phi_file)

    #print(f"Processing: {filename}")

    # --------------------------------------------------------
    # Extract particle size
    #
    # Example:
    # 0_3Lam_225Up_phi.dat
    #
    # Extracts:
    #              225
    # --------------------------------------------------------

    match = re.search(r"_(\d+)Up_phi\.dat$", filename)

    if match:
        particle_size = int(match.group(1))
    else:
        print(f"WARNING: Could not extract particle size from {filename}")
        particle_size = filename

    # --------------------------------------------------------
    # Read data
    # --------------------------------------------------------

    df_phiT = pd.read_csv(
        phiT_file,
        sep=r"\s+",
        comment="#"
    )

    df_phi = pd.read_csv(
        phi_file,
        sep=r"\s+",
        comment="#"
    )

    # --------------------------------------------------------
    # Extract columns
    # --------------------------------------------------------

    time_col = df_phiT.columns[0]

    df = pd.DataFrame({
        "Raw_Time": df_phiT[time_col],
        "phiT": df_phiT[df_phiT.columns[1]],
        "phi": df_phi[df_phi.columns[1]]
    })

    # --------------------------------------------------------
    # Calculate T = phiT / phi
    # --------------------------------------------------------

    df["T"] = df["phiT"] / df["phi"]

    # Remove invalid values
    df = df.replace([float("inf"), -float("inf")], pd.NA)
    df = df.dropna(subset=["T"])

    # --------------------------------------------------------
    # Normalize by maximum concentration
    # --------------------------------------------------------

    max_T = df["T"].max()

    if pd.isna(max_T) or max_T == 0:
        max_T = 1.0

    df["Normalized_T"] = df["T"] / max_T

    # --------------------------------------------------------
    # Shift time so it starts at zero
    # --------------------------------------------------------

    min_time = df["Raw_Time"].min()

    df["Elapsed_Time"] = df["Raw_Time"] - min_time

    # --------------------------------------------------------
    # Apply time window
    # --------------------------------------------------------

    df = df[
        (df["Elapsed_Time"] >= t_start) &
        (df["Elapsed_Time"] <= t_end) &
        (df["Normalized_T"] >= 0)
    ].copy()

    # Store result
    results.append({
        "particle_size": particle_size,
        "filename": filename,
        "data": df
    })
    # --------------------------------------------------------
    # Steady-state value
    # --------------------------------------------------------

    steady_state_T = df["T"].max()

    print(f"Particle size: {particle_size} nm")
    print(f"Steady-state phiT/phi: {steady_state_T:.6e}")

    steady_state_results.append({"particle_size": particle_size, "steady_state_T": steady_state_T})

# ============================================================
# SORT BY PARTICLE SIZE
# ============================================================

results.sort(
    key=lambda x: x["particle_size"]
    if isinstance(x["particle_size"], (int, float))
    else float("inf")
)

# ============================================================
# INDIVIDUAL PARTICLE SIZE PLOTS
# ============================================================

# ============================================================
# INDIVIDUAL PARTICLE SIZE SUBPLOTS
# ============================================================

# ============================================================
# INDIVIDUAL PARTICLE SIZE SUBPLOTS
# ============================================================

import numpy as np
import math

tau = 3.62

n_particles = len(results)

# 2 columns
ncols = 2
nrows = math.ceil(n_particles / ncols)

fig, axes = plt.subplots(
    nrows,
    ncols,
    figsize=(12, 3.2 * nrows),
    sharex=False,
    sharey=True
)
fig.subplots_adjust(hspace=0.1)

axes = np.atleast_1d(axes).flatten()


for i, result in enumerate(results):

    df = result["data"]
    particle_size = result["particle_size"]

    ax = axes[i]

    # --------------------------------------------------------
    # Analytical curve
    # --------------------------------------------------------

    t_analytical = np.linspace(
        t_start,
        t_end,
        500
    )

    t_safe = np.maximum(
        t_analytical,
        1e-10
    )

    T_analytical = (
        1 - tau**2 / (4 * t_safe**2)
    )

    T_analytical = np.maximum(
        T_analytical,
        0
    )

    # --------------------------------------------------------
    # CFD
    # --------------------------------------------------------

    ax.plot(
        df["Elapsed_Time"],
        df["Normalized_T"],
        linewidth=2.0,
        label="CFD"
    )

    # --------------------------------------------------------
    # Analytical
    # --------------------------------------------------------

    ax.plot(
        t_analytical,
        T_analytical,
        linestyle="--",
        linewidth=1.7,
        label="Analytical"
    )

    # --------------------------------------------------------
    # tau
    # --------------------------------------------------------

    ax.axvline(
        x=tau,
        linestyle=":",
        linewidth=1.2,
        label="$\\tau = 3.62$ s"
    )

    # --------------------------------------------------------
    # Axes
    # --------------------------------------------------------

    ax.set_xlim(t_start, t_end)
    ax.set_ylim(-0.05, 1.05)

    # Smaller subplot title
    ax.set_title(
        f"{particle_size} nm",
        fontsize=11,
        fontweight="bold",
        pad=5
    )

    ax.grid(
        True,
        linestyle="--",
        linewidth=0.5,
        alpha=0.7
    )

    ax.legend(
        loc="lower right",
        fontsize=8,
        frameon=True,
        edgecolor="black"
    )


# ============================================================
# COMMON LABELS
# ============================================================

fig.supxlabel(
    "Time, $t$ [s]",
    fontsize=12,
    fontweight="bold"
)

fig.supylabel(
    "$\\tilde{N}(t)$ at outlet [-]",
    fontsize=12,
    fontweight="bold"
)

fig.suptitle(
    "Normalized step-down response at tube outlet at 0.3 L/min",
    fontsize=14,
    fontweight="bold"
)


# Hide unused subplot
for j in range(n_particles, len(axes)):
    axes[j].set_visible(False)


# Spacing between subplots
plt.tight_layout(
    rect=[0.03, 0.04, 1, 0.94],
    h_pad=1.5,
    w_pad=1.5
)

# ============================================================
# PLOT
# ============================================================

plt.figure(figsize=(7, 6))

for result in results:

    df = result["data"]
    particle_size = result["particle_size"]

    # Legend label
    label = f"{particle_size} nm"

    plt.plot(
        df["Elapsed_Time"],
        df["Normalized_T"],
        linewidth=2.5,
        label=label
    )


# ============================================================
# AXES / FORMATTING
# ============================================================

plt.xlim(t_start, t_end)
plt.ylim(-0.05, 1.05)

plt.xlabel(
    "Time, $t$ [s]",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "$\\tilde{N}(t)$ at outlet [-]",
    fontsize=12,
    fontweight="bold"
)

plt.title(
    "Tube D = 4.9mm, L = 960mm",
    fontsize=13,
    fontweight="bold"
)

plt.grid(
    True,
    linestyle="--",
    linewidth=0.5,
    alpha=0.7
)

plt.axvline(
    x=3.62,
    linestyle="--",
    linewidth=1.5,
    label="$t = 3.62$ s"
)

plt.legend(
    loc="lower right",
    frameon=True,
    edgecolor="black"
)

plt.tight_layout()

# ============================================================
# STEADY-STATE TRANSMISSION vs PARTICLE DIAMETER
# ============================================================

steady_state_results.sort(
    key=lambda x: x["particle_size"]
)

particle_sizes = [
    x["particle_size"] for x in steady_state_results
]

steady_state_values = [
    x["steady_state_T"] for x in steady_state_results
]

plt.figure(figsize=(7, 6))

plt.title(
    "Transmission efficiency at tube outlet",
    fontsize=13,
    fontweight="bold"
)

plt.plot(
    particle_sizes,
    steady_state_values,
    marker="o",
    linewidth=2.5
)

plt.xlabel(
    "Particle diameter [nm]",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "$\\phi_T/\\phi$ [-]",
    fontsize=12,
    fontweight="bold"
)



plt.grid(
    True,
    linestyle="--",
    linewidth=0.5,
    alpha=0.7
)

plt.figure(figsize=(7, 6))

for result in results:

    df = result["data"]
    particle_size = result["particle_size"]

    # Make sure time is sorted
    df = df.sort_values("Elapsed_Time")

    t = df["Elapsed_Time"].to_numpy()
    T = df["T"].to_numpy()

    # Remove t = 0 to avoid problems with dT/dln(t)
    mask = t > 0

    t = t[mask]
    T = T[mask]

    # --------------------------------------------------------
    # Standard RTD: E(t) = dT/dt
    # --------------------------------------------------------

    dT_dt = np.gradient(T, t)

    # --------------------------------------------------------
    # Log-time RTD:
    #
    # dT/d(ln t) = t * dT/dt
    # --------------------------------------------------------

    RTD_log = t * dT_dt

    # --------------------------------------------------------
    # Plot
    # --------------------------------------------------------

    plt.plot(
        t,
        RTD_log,
        linewidth=2.0,
        label=f"{particle_size} nm"
    )


plt.xscale("log")

plt.xlabel(
    "Time, $t$ [s]",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "$dT/d\\ln(t)$ [-]",
    fontsize=12,
    fontweight="bold"
)

plt.title(
    "Residence Time Distribution",
    fontsize=13,
    fontweight="bold"
)

plt.grid(
    True,
    linestyle="--",
    linewidth=0.5,
    alpha=0.7
)

plt.legend(
    frameon=True,
    edgecolor="black"
)

# ============================================================
# RTD: CFD vs ANALYTICAL
# ============================================================

fig, axes = plt.subplots(
    nrows,
    ncols,
    figsize=(12, 3.2 * nrows),
    sharex=False,
    sharey=True
)
fig.subplots_adjust(hspace=0.1)


axes = np.atleast_1d(axes).flatten()

for i, result in enumerate(results):

    df = result["data"]
    particle_size = result["particle_size"]

    ax = axes[i]

    # --------------------------------------------------------
    # CFD RTD
    # --------------------------------------------------------

    df = df.sort_values("Elapsed_Time")

    t_cfd = df["Elapsed_Time"].to_numpy()
    T_cfd = df["Normalized_T"].to_numpy()

    # Remove t = 0
    mask = t_cfd > 0

    t_cfd = t_cfd[mask]
    T_cfd = T_cfd[mask]

    # dT/dt
    dT_dt = np.gradient(T_cfd, t_cfd)

    # dT/d(ln t) = t dT/dt
    RTD_cfd = t_cfd * dT_dt

    # --------------------------------------------------------
    # Analytical RTD
    # --------------------------------------------------------

    t_analytical = np.linspace(
        t_start,
        t_end,
        1000
    )

    # Avoid t = 0
    t_safe = np.maximum(
        t_analytical,
        1e-10
    )

    # Analytical F(t)
    F_analytical = (
        1 - tau**2 / (4 * t_safe**2)
    )

    # Same clipping as your F(t) calculation
    F_analytical = np.maximum(
        F_analytical,
        0
    )

    # --------------------------------------------------------
    # Analytical RTD
    #
    # RTD = dF/d(ln t)
    #
    # dF/dt = tau^2 / (2 t^3)
    #
    # therefore:
    #
    # dF/d(ln t) = t dF/dt
    #            = tau^2 / (2 t^2)
    # --------------------------------------------------------

    RTD_analytical = (
        tau**2 / (2 * t_safe**2)
    )

    # Analytical RTD should be zero before
    # F(t) starts increasing
    RTD_analytical[
        t_safe < tau / 2
    ] = 0

    # --------------------------------------------------------
    # Plot CFD RTD
    # --------------------------------------------------------

    ax.plot(
        t_cfd,
        RTD_cfd,
        linewidth=2.0,
        label="CFD"
    )

    # --------------------------------------------------------
    # Plot analytical RTD
    # --------------------------------------------------------

    ax.plot(
        t_analytical,
        RTD_analytical,
        linestyle="--",
        linewidth=1.7,
        label="Analytical"
    )

    # --------------------------------------------------------
    # Mean residence time
    # --------------------------------------------------------

    ax.axvline(
        x=tau,
        linestyle=":",
        linewidth=1.2,
        label=r"$\tau = 3.62$ s"
    )

    # --------------------------------------------------------
    # Axes
    # --------------------------------------------------------

    ax.set_xlim(t_start, t_end)

    ax.set_title(
        f"{particle_size} nm",
        fontsize=11,
        fontweight="bold",
        pad=5
    )

    ax.grid(
        True,
        linestyle="--",
        linewidth=0.5,
        alpha=0.7
    )

    ax.legend(
        loc="upper right",
        fontsize=8,
        frameon=True,
        edgecolor="black"
    )


# ============================================================
# COMMON LABELS
# ============================================================

fig.supxlabel(
    "Time, $t$ [s]",
    fontsize=12,
    fontweight="bold"
)

fig.supylabel(
    "$dF/d\\ln(t)$ [-]",
    fontsize=12,
    fontweight="bold"
)

fig.suptitle(
    "Residence Time Distribution: CFD vs Analytical",
    fontsize=14,
    fontweight="bold"
)


# ============================================================
# HIDE UNUSED SUBPLOTS
# ============================================================

for j in range(n_particles, len(axes)):
    axes[j].set_visible(False)


# ============================================================
# SPACING
# ============================================================

plt.tight_layout(
    rect=[0.03, 0.04, 1, 0.94],
    h_pad=1.5,
    w_pad=1.5
)

plt.tight_layout()
plt.show()

