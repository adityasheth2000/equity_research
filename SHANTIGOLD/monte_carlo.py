#!/usr/bin/env python3
"""
Shanti Gold International Ltd — 3-Year Monte Carlo Simulation v2
Stores every sampled variable & generates individual distribution charts.
"""

import numpy as np
from scipy import stats
import json, os

# ── CONFIG ───────────────────────────────────────────────────────────
np.random.seed(42)
N = 10_000
MARKET_CAP = 1605
TAX_RATE = 0.24
GOLD_DRIFT = 0.07
GOLD_VOL = 0.16
GOLD_SPOT = 148000
MONTHS = 36
DT = 1 / 12
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── FACILITIES ───────────────────────────────────────────────────────
facilities = {
    "Andheri": {"cap_kg": 2700, "start_month": 0, "max_util": 0.90, "ramp_dur": (0, 0, 0)},
    "Marol":   {"cap_kg": 4000, "start_month": 2, "max_util": 0.85, "ramp_dur": (24, 36, 48)},
    "Jaipur":  {"cap_kg": 1200, "start_month": 6, "max_util": 0.80, "ramp_dur": (18, 30, 42)},
}

FY_START = [0, 12, 24]
FY_END   = [12, 24, 36]

# ── STORAGE: raw samples + derived ───────────────────────────────────
samples = {
    "ramp_marol_months":     [],   # triangular
    "ramp_jaipur_months":    [],   # triangular
    "vol_elasticity":        [],   # normal (via ppf)
    "cz_pct_fy27": [], "cz_pct_fy28": [], "cz_pct_fy29": [],  # uniform
    "cz_premium":  [], "plain_premium": [],                    # uniform
    "core_margin_fy27": [], "core_margin_fy28": [], "core_margin_fy29": [],  # normal
    "hedge_ratio_fy27": [], "hedge_ratio_fy28": [], "hedge_ratio_fy29": [],  # uniform
    "gold_fy27": [], "gold_fy28": [], "gold_fy29": [],          # GBM path avg
}

outputs = {
    "fy27_pat": [], "fy28_pat": [], "fy29_pat": [],
    "fy27_rev": [], "fy28_rev": [], "fy29_rev": [],
    "fy27_vol": [], "fy28_vol": [], "fy29_vol": [],
    "fy27_pe":  [], "fy28_pe":  [], "fy29_pe":  [],
}

# ── S-CURVE UTIL FOR CHARTING (store sample paths) ──────────────────
sample_util_curves_marol = []   # 100 sample util-vs-month curves
sample_util_curves_jaipur = []

# ── HELPER ──────────────────────────────────────────────────────────
def vol_elasticity_sample(u):
    return stats.norm.ppf(u, loc=-0.25, scale=0.05)

def s_curve(m, s_m, dur, max_u):
    if dur == 0:
        return max_u
    return max_u / (1 + np.exp(-6 * (m - s_m - dur / 2) / max(dur, 1)))

# ── MAIN LOOP ───────────────────────────────────────────────────────
for _ in range(N):
    # 1. Gold GBM path
    gold_path = [GOLD_SPOT]
    for t in range(MONTHS):
        z = np.random.randn()
        gold_path.append(gold_path[-1] * np.exp((GOLD_DRIFT - 0.5 * GOLD_VOL**2) * DT
                                                + GOLD_VOL * np.sqrt(DT) * z))
    gold_at = lambda m: gold_path[m + 1]

    # 2. Ramp durations
    rd_marol  = np.random.triangular(*facilities["Marol"]["ramp_dur"])
    rd_jaipur = np.random.triangular(*facilities["Jaipur"]["ramp_dur"])
    samples["ramp_marol_months"].append(rd_marol)
    samples["ramp_jaipur_months"].append(rd_jaipur)

    # 3. Volume elasticity
    ve = vol_elasticity_sample(np.random.random())
    samples["vol_elasticity"].append(ve)

    # 4. Product mix
    cz27 = np.random.uniform(0.65, 0.80)
    cz28 = np.random.uniform(0.40, 0.60)
    cz29 = np.random.uniform(0.30, 0.50)
    samples["cz_pct_fy27"].append(cz27)
    samples["cz_pct_fy28"].append(cz28)
    samples["cz_pct_fy29"].append(cz29)
    cz_pcts = [cz27, cz28, cz29]

    # 5. Making charge premiums
    cz_p    = np.random.uniform(1.18, 1.22)
    plain_p = np.random.uniform(1.05, 1.08)
    samples["cz_premium"].append(cz_p)
    samples["plain_premium"].append(plain_p)

    # 6. Core PAT margins
    cm = np.random.normal(0.04, 0.004, 3)
    samples["core_margin_fy27"].append(cm[0])
    samples["core_margin_fy28"].append(cm[1])
    samples["core_margin_fy29"].append(cm[2])

    # ── Per-FY computation ──
    for fy_idx in range(3):
        s_m = FY_START[fy_idx]
        e_m = FY_END[fy_idx]
        months_in_fy = list(range(s_m, e_m))

        # Capacity → volume
        total_vol = 0
        for name, f in facilities.items():
            sm = f["start_month"]
            du = 0 if name == "Andheri" else (rd_marol if name == "Marol" else rd_jaipur)
            utils = []
            for m in months_in_fy:
                if m >= sm or du == 0:
                    util = s_curve(m, sm, du, f["max_util"])
                else:
                    util = 0.0
                utils.append(util)
            avg_u = np.mean(utils)
            total_vol += f["cap_kg"] * avg_u

            # Store sample S-curves (100 paths per facility in FY29)
            if _ < 100 and fy_idx == 2:
                if name == "Marol":
                    sample_util_curves_marol.append((du, utils))
                elif name == "Jaipur":
                    sample_util_curves_jaipur.append((du, utils))

        # Gold price & elasticity
        avg_gold = np.mean([gold_at(m) for m in months_in_fy])
        gold_dev = (avg_gold - GOLD_SPOT) / GOLD_SPOT
        adj = np.clip(1 + ve * gold_dev, 0.5, 1.5)
        final_vol = total_vol * adj

        # Gold price storage
        if fy_idx == 0: samples["gold_fy27"].append(avg_gold)
        if fy_idx == 1: samples["gold_fy28"].append(avg_gold)
        if fy_idx == 2: samples["gold_fy29"].append(avg_gold)

        # Revenue
        cz_v   = final_vol * cz_pcts[fy_idx]
        pl_v   = final_vol * (1 - cz_pcts[fy_idx])
        rev = (cz_v * avg_gold * 100 * cz_p + pl_v * avg_gold * 100 * plain_p) / 1e7

        # PAT
        core_pat = rev * cm[fy_idx]
        cost_m = list(range(max(0, s_m - 2), s_m))
        avg_cost = np.mean([gold_at(m) for m in cost_m]) if cost_m else avg_gold
        # Hedging ratio: time-varying
        hedge_map = {0: (0.60, 0.90), 1: (0.85, 1.00), 2: (0.90, 1.00)}
        lo, hi = hedge_map[fy_idx]
        hr = np.random.uniform(lo, hi)
        if fy_idx == 0: samples["hedge_ratio_fy27"].append(hr)
        if fy_idx == 1: samples["hedge_ratio_fy28"].append(hr)
        if fy_idx == 2: samples["hedge_ratio_fy29"].append(hr)
        unhedged = final_vol * (1 - hr)
        gain_per_10g = max(0, avg_gold - avg_cost)
        inv_gain = (unhedged * gain_per_10g * 100) / 1e7 * (1 - TAX_RATE)
        pat = core_pat + inv_gain

        if fy_idx == 0:
            outputs["fy27_pat"].append(pat)
            outputs["fy27_rev"].append(rev)
            outputs["fy27_vol"].append(final_vol)
            outputs["fy27_pe"].append(MARKET_CAP / max(1e-3, pat))
        elif fy_idx == 1:
            outputs["fy28_pat"].append(pat)
            outputs["fy28_rev"].append(rev)
            outputs["fy28_vol"].append(final_vol)
            outputs["fy28_pe"].append(MARKET_CAP / max(1e-3, pat))
        else:
            outputs["fy29_pat"].append(pat)
            outputs["fy29_rev"].append(rev)
            outputs["fy29_vol"].append(final_vol)
            outputs["fy29_pe"].append(MARKET_CAP / max(1e-3, pat))

# ── CONVERT TO ARRAYS ───────────────────────────────────────────────
for k in samples:
    arr = np.array(samples[k], dtype=float)
    if len(arr) == 0:
        print(f"  WARNING: samples['{k}'] is empty — skipping")
        samples[k] = np.array([0.0])
    else:
        samples[k] = arr
for k in outputs:  outputs[k] = np.array(outputs[k])

 # ── SAVE RAW DATA ───────────────────────────────────────────────────
print("\n── Debug: array sizes")
for k, v in sorted(samples.items()):
    print(f"  samples['{k}']: size={v.size} shape={v.shape}")
for k, v in sorted(outputs.items()):
    print(f"  outputs['{k}']: size={v.size} shape={v.shape}")

def safe_stats(arr):
    clean = arr[np.isfinite(arr)]
    if len(clean) == 0:
        return {"mean": 0, "median": 0, "p10": 0, "p90": 0, "std": 0, "min": 0, "max": 0}
    return {"mean": float(np.mean(clean)), "median": float(np.median(clean)),
            "p10": float(np.percentile(clean, 10)), "p90": float(np.percentile(clean, 90)),
            "std": float(np.std(clean)), "min": float(np.min(clean)), "max": float(np.max(clean))}

save_data = {"samples": {}, "outputs": {}}
for k, v in samples.items():
    save_data["samples"][k] = safe_stats(v)
    save_data["samples"][k]["values"] = v[np.isfinite(v)][:500].tolist()
for k, v in outputs.items():
    save_data["outputs"][k] = safe_stats(v)

save_data["probabilities"] = {
    "fy29_pe_below_5x": float(np.mean(np.isfinite(outputs["fy29_pe"]) & (outputs["fy29_pe"] < 5))),
    "fy29_pe_below_3x": float(np.mean(np.isfinite(outputs["fy29_pe"]) & (outputs["fy29_pe"] < 3))),
    "fy29_pe_above_10x": float(np.mean(np.isfinite(outputs["fy29_pe"]) & (outputs["fy29_pe"] > 10))),
    "fy27_pat_below_100": float(np.mean(np.isfinite(outputs["fy27_pat"]) & (outputs["fy27_pat"] < 100))),
    "fy29_pat_above_500": float(np.mean(np.isfinite(outputs["fy29_pat"]) & (outputs["fy29_pat"] > 500))),
}

with open(os.path.join(OUT_DIR, "monte_carlo_data.json"), "w") as f:
    json.dump(save_data, f, indent=2)

# ── CONSOLE OUTPUT ──────────────────────────────────────────────────
print("=" * 80)
print("  SHANTI GOLD — MONTE CARLO  (N=10,000)  |  Raw Variable Distributions")
print("=" * 80)

sections = [
    ("RAMP DURATIONS (Triangular)", [
        ("ramp_marol_months",  "Marol Ramp (mo)"),
        ("ramp_jaipur_months", "Jaipur Ramp (mo)"),
    ]),
    ("VOLUME ELASTICITY (Normal via PPF)", [
        ("vol_elasticity", "Elasticity"),
    ]),
    ("PRODUCT MIX — CZ % (Uniform)", [
        ("cz_pct_fy27", "FY27 CZ%"), ("cz_pct_fy28", "FY28 CZ%"), ("cz_pct_fy29", "FY29 CZ%"),
    ]),
    ("MAKING CHARGE MULTIPLIERS (Uniform)", [
        ("cz_premium",    "CZ Premium (×gold)"),
        ("plain_premium", "Plain Premium (×gold)"),
    ]),
    ("CORE PAT MARGIN (Normal)", [
        ("core_margin_fy27", "FY27 Margin"), ("core_margin_fy28", "FY28 Margin"), ("core_margin_fy29", "FY29 Margin"),
    ]),
    ("HEDGING RATIO (Uniform, tightening bounds)", [
        ("hedge_ratio_fy27", "FY27 Hedged%"), ("hedge_ratio_fy28", "FY28 Hedged%"), ("hedge_ratio_fy29", "FY29 Hedged%"),
    ]),
    ("GOLD PRICE — GBM Path Avg (₹/10g)", [
        ("gold_fy27", "FY27 Avg Gold"), ("gold_fy28", "FY28 Avg Gold"), ("gold_fy29", "FY29 Avg Gold"),
    ]),
]

for section_title, vars_list in sections:
    print(f"\n── {section_title}")
    print(f"  {'Variable':<25} {'Mean':>10} {'Median':>10} {'P10':>10} {'P90':>10} {'Std':>10}  {'Shapiro-Wilk p'}")
    print(f"  {'─'*23}  {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*10}")
    for var_key, var_label in vars_list:
        v = samples[var_key]
        # Shapiro-Wilk normality test (sample up to 5000)
        shuf = np.random.permutation(v)[:min(5000, len(v))]
        try:
            sw_stat, sw_p = stats.shapiro(shuf)
        except Exception:
            sw_p = -1.0
        print(f"  {var_label:<25} {np.mean(v):>10.4f} {np.median(v):>10.4f} {np.percentile(v,10):>10.4f} {np.percentile(v,90):>10.4f} {np.std(v):>10.4f}  {sw_p:<10.4f}")

# ── OUTPUT SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 80)
print("  OUTPUT SUMMARY")
print("=" * 80)
print(f"  {'Metric':<18} {'Mean':>10} {'Median':>10} {'P10':>10} {'P90':>10}")
print(f"  {'─'*16}  {'─'*10} {'─'*10} {'─'*10} {'─'*10}")
for yr in ["fy27", "fy28", "fy29"]:
    for m in ["rev", "pat", "pe"]:
        v = outputs[f"{yr}_{m}"]
        vc = v[np.isfinite(v)]
        unit = "Cr" if m in ("rev","pat") else "x"
        if len(vc) == 0:
            print(f"  FY{yr[2:]} {m.upper():>3} ({unit}){' ':<7} {'--':>10} {'--':>10} {'--':>10} {'--':>10}")
        else:
            print(f"  FY{yr[2:]} {m.upper():>3} ({unit}){' ':<7} {np.mean(vc):>10.1f} {np.median(vc):>10.1f} {np.percentile(vc,10):>10.1f} {np.percentile(vc,90):>10.1f}")

print(f"\n  FY29 P/E < 5x: {np.mean(np.isfinite(outputs['fy29_pe']) & (outputs['fy29_pe']<5))*100:.1f}%  |  < 3x: {np.mean(np.isfinite(outputs['fy29_pe']) & (outputs['fy29_pe']<3))*100:.1f}%")
print(f"  FY29 PAT > ₹500 Cr: {np.mean(np.isfinite(outputs['fy29_pat']) & (outputs['fy29_pat']>500))*100:.1f}%")
print(f"\n  Full data saved → {os.path.join(OUT_DIR, 'monte_carlo_data.json')}")


# ══════════════════════════════════════════════════════════════════════
#  CHARTS — Individual distribution panels
# ══════════════════════════════════════════════════════════════════════

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

plt.rcParams.update({
    "figure.facecolor": "#0d1117", "axes.facecolor": "#161b22",
    "axes.edgecolor": "#30363d", "axes.labelcolor": "#c9d1d9",
    "text.color": "#c9d1d9", "xtick.color": "#8b949e", "ytick.color": "#8b949e",
    "grid.color": "#21262d", "figure.dpi": 150, "font.size": 8,
    "axes.titlesize": 10, "axes.labelsize": 8,
})

def add_stats_box(ax, data, fmt=".2f", pos=(0.97, 0.95)):
    m, med = np.mean(data), np.median(data)
    p10, p90 = np.percentile(data, [10, 90])
    txt = f"μ={m:{fmt}}\nP10={p10:{fmt}}\nP90={p90:{fmt}}"
    ax.text(pos[0], pos[1], txt, transform=ax.transAxes, ha="right", va="top",
            fontsize=6.5, family="monospace",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#0d1117", alpha=0.7))

def hist_plot(ax, data, color, label, bins=60, alpha=0.85, show_median=True):
    ax.hist(data, bins=bins, color=color, alpha=alpha, edgecolor=None, density=True)
    if show_median:
        ax.axvline(np.median(data), color="white", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.set_title(label, fontweight="bold")
    ax.grid(True, alpha=0.15)
    add_stats_box(ax, data)

# ============================
#  CHART 1: INPUT DISTRIBUTIONS (3×3 grid)
# ============================
fig1 = plt.figure(figsize=(18, 15))
gs1 = GridSpec(3, 3, figure=fig1, hspace=0.5, wspace=0.4)

# Row 1: Ramp durations (Triangular) + Volume Elasticity
hist_plot(fig1.add_subplot(gs1[0, 0]), samples["ramp_marol_months"], "#f0883e",
          "Marol Ramp Duration (mo)\nTriangular(24, 36, 48)", bins=50, alpha=0.7)
hist_plot(fig1.add_subplot(gs1[0, 1]), samples["ramp_jaipur_months"], "#f0883e",
          "Jaipur Ramp Duration (mo)\nTriangular(18, 30, 42)", bins=50, alpha=0.7)
hist_plot(fig1.add_subplot(gs1[0, 2]), samples["vol_elasticity"], "#a5d6ff",
          "Volume Elasticity to Gold Price\nN(−0.25, 0.05) via inverse-CDF", bins=60)

# Row 2: Product Mix — CZ % (Uniform)
for i, yr in enumerate(["27", "28", "29"]):
    hist_plot(fig1.add_subplot(gs1[1, i]), samples[f"cz_pct_fy{yr}"], "#56d364",
              f"FY{yr} CZ Studded Mix %\nUniform({['65','40','30'][i]}–{['80','60','50'][i]}%)", bins=40, alpha=0.7)

# Row 3: Core PAT Margin (Normal)
for i, yr in enumerate(["27", "28", "29"]):
    hist_plot(fig1.add_subplot(gs1[2, i]), samples[f"core_margin_fy{yr}"] * 100, "#ff7b72",
              f"FY{yr} Core PAT Margin (%)\nN(4.0%, 0.4%) — sampled independently", bins=80,
              show_median=(i == 1))

fig1.suptitle("Shanti Gold — Monte Carlo: Input Variable Distributions (N=10,000)",
              fontsize=14, fontweight="bold", y=0.99)
fig1.savefig(os.path.join(OUT_DIR, "chart_inputs.png"), dpi=150, bbox_inches="tight",
             facecolor="#0d1117")
print(f"  Chart 1 saved → {os.path.join(OUT_DIR, 'chart_inputs.png')}")


# ============================
#  CHART 2: GOLD & HEDGING (2×3 grid)
# ============================
fig2 = plt.figure(figsize=(18, 10))
gs2 = GridSpec(2, 3, figure=fig2, hspace=0.45, wspace=0.35)

gold_colors = ["#f0c050", "#e0a830", "#d09020"]
hedge_colors = ["#79c0ff", "#56a5ec", "#3388d8"]
for i, yr in enumerate(["27", "28", "29"]):
    hist_plot(fig2.add_subplot(gs2[0, i]), samples[f"gold_fy{yr}"], gold_colors[i],
              f"FY{yr} Avg Gold Price (₹/10g)\nGBM(μ=7%, σ=16%) — {np.mean(samples[f'gold_fy{yr}']):.0f} mean",
              bins=70, alpha=0.7)
    hist_plot(fig2.add_subplot(gs2[1, i]), samples[f"hedge_ratio_fy{yr}"] * 100, hedge_colors[i],
              f"FY{yr} Hedging Ratio (%)\nUniform({['60','85','90'][i]}-{['90','100','100'][i]}%) — tightening",
              bins=40, alpha=0.7)

fig2.suptitle("Shanti Gold — Gold Price Paths & Hedging Transition",
              fontsize=14, fontweight="bold", y=0.99)
fig2.savefig(os.path.join(OUT_DIR, "chart_gold_hedging.png"), dpi=150, bbox_inches="tight",
             facecolor="#0d1117")
print(f"  Chart 2 saved → {os.path.join(OUT_DIR, 'chart_gold_hedging.png')}")


# ============================
#  CHART 3: PREMIUM, S-CURVES, Q-Q PLOTS (3×3 grid)
# ============================
fig3 = plt.figure(figsize=(18, 15))
gs3 = GridSpec(3, 3, figure=fig3, hspace=0.5, wspace=0.4)

# Row 1: Making charge premiums
hist_plot(fig3.add_subplot(gs3[0, 0]), samples["cz_premium"], "#d2a8ff",
          "CZ Studded Premium (× gold value)\nUniform(1.18, 1.22) — 18-22% making charge",
          bins=50, alpha=0.7)
hist_plot(fig3.add_subplot(gs3[0, 1]), samples["plain_premium"], "#d2a8ff",
          "Plain Gold Premium (× gold value)\nUniform(1.05, 1.08) — 5-8% making charge",
          bins=50, alpha=0.7)

# Q-Q Plot: Volume Elasticity vs Normal
ax_qq = fig3.add_subplot(gs3[0, 2])
stats.probplot(samples["vol_elasticity"], dist="norm", plot=ax_qq)
ax_qq.get_lines()[0].set_color("#a5d6ff")
ax_qq.get_lines()[0].set_markersize(2)
ax_qq.get_lines()[0].set_alpha(0.4)
ax_qq.get_lines()[1].set_color("#f0883e")
ax_qq.get_lines()[1].set_linewidth(1.5)
ax_qq.set_title("Q-Q: Vol Elasticity vs Normal", fontweight="bold")
ax_qq.grid(True, alpha=0.15)

# Row 2: S-Curve overlay (Marol & Jaipur) — 100 sample paths
ax_marol = fig3.add_subplot(gs3[1, 0])
for dur, curve in sample_util_curves_marol[:100]:
    ax_marol.plot(curve, alpha=0.08, color="#f0883e", linewidth=0.5)
ax_marol.set_title(f"Marol Ramp S-Curves ({min(100, len(sample_util_curves_marol))} paths)\nFY29 monthly util — Logistic ramp",
                   fontweight="bold")
ax_marol.set_xlabel("Month in FY29")
ax_marol.set_ylabel("Utilization")
ax_marol.set_ylim(0, 1)
ax_marol.grid(True, alpha=0.15)

ax_jai = fig3.add_subplot(gs3[1, 1])
for dur, curve in sample_util_curves_jaipur[:100]:
    ax_jai.plot(curve, alpha=0.08, color="#56d364", linewidth=0.5)
ax_jai.set_title(f"Jaipur Ramp S-Curves ({min(100, len(sample_util_curves_jaipur))} paths)\nFY29 monthly util — Logistic ramp",
                fontweight="bold")
ax_jai.set_xlabel("Month in FY29")
ax_jai.set_ylabel("Utilization")
ax_jai.set_ylim(0, 1)
ax_jai.grid(True, alpha=0.15)

# Q-Q: Core Margin vs Normal
ax_qq2 = fig3.add_subplot(gs3[1, 2])
stats.probplot(samples["core_margin_fy27"] * 100, dist="norm", plot=ax_qq2)
ax_qq2.get_lines()[0].set_color("#ff7b72")
ax_qq2.get_lines()[0].set_markersize(2)
ax_qq2.get_lines()[0].set_alpha(0.4)
ax_qq2.get_lines()[1].set_color("#56d364")
ax_qq2.get_lines()[1].set_linewidth(1.5)
ax_qq2.set_title("Q-Q: Core Margin FY27 vs Normal", fontweight="bold")
ax_qq2.grid(True, alpha=0.15)

# Row 3: Gold price path overlay (sample 50 paths)
ax_gpaths = fig3.add_subplot(gs3[2, :2])

# Re-run a mini-sim to get paths
np.random.seed(999)
for p in range(50):
    gpath = [GOLD_SPOT]
    for t in range(MONTHS):
        z = np.random.randn()
        gpath.append(gpath[-1] * np.exp((GOLD_DRIFT - 0.5 * GOLD_VOL**2) * DT
                                        + GOLD_VOL * np.sqrt(DT) * z))
    ax_gpaths.plot(gpath, alpha=0.12, linewidth=0.5, color="#f0c050")
ax_gpaths.plot([GOLD_SPOT]*37, color="white", alpha=0.2, linewidth=0.5, linestyle=":")
ax_gpaths.set_title("Gold Price GBM — 50 Sample Paths (Monthly)\nS₀=₹1,48,000  μ=7%  σ=16%",
                    fontweight="bold")
ax_gpaths.set_xlabel("Month (0 = Apr'26)")
ax_gpaths.set_ylabel("₹/10g")
ax_gpaths.grid(True, alpha=0.15)

# Distribution comparison: shapes
ax_dist = fig3.add_subplot(gs3[2, 2])

# Overlay key distributions normalized
def norm_dist(arr):
    return (arr - np.mean(arr)) / np.std(arr)

bins = np.linspace(-4, 4, 80)
ax_dist.hist(norm_dist(samples["vol_elasticity"]), bins=bins, alpha=0.4, density=True,
             color="#a5d6ff", label="Vol Elast (Normal)")
ax_dist.hist(norm_dist(samples["ramp_marol_months"]), bins=bins, alpha=0.4, density=True,
             color="#f0883e", label="Ramp Marol (Triangular)")
ax_dist.hist(norm_dist(samples["cz_pct_fy28"]), bins=bins, alpha=0.4, density=True,
             color="#56d364", label="CZ% FY28 (Uniform)")
x = np.linspace(-4, 4, 200)
ax_dist.plot(x, stats.norm.pdf(x), color="white", linewidth=0.8, linestyle="--", alpha=0.6)
ax_dist.set_title("Distribution Shapes Compared\n(Mean-centered, σ-scaled)", fontweight="bold")
ax_dist.legend(fontsize=6, loc="upper right", framealpha=0.3)
ax_dist.grid(True, alpha=0.15)

fig3.suptitle("Shanti Gold — Premiums, S-Curves, GBM Paths & Distribution Shapes",
              fontsize=14, fontweight="bold", y=0.99)
fig3.savefig(os.path.join(OUT_DIR, "chart_curves_and_shapes.png"), dpi=150, bbox_inches="tight",
             facecolor="#0d1117")
print(f"  Chart 3 saved → {os.path.join(OUT_DIR, 'chart_curves_and_shapes.png')}")


# ============================
#  CHART 4: OUTPUT DISTRIBUTIONS (PAT, P/E, Volume — 3×3)
# ============================
fig4 = plt.figure(figsize=(18, 15))
gs4 = GridSpec(3, 3, figure=fig4, hspace=0.45, wspace=0.35)

pat_colors = ["#58a6ff", "#3fb950", "#f0883e"]
pe_colors  = ["#a5d6ff", "#7ee787", "#ffa198"]
vol_colors = ["#79c0ff", "#56d364", "#f78166"]

for i, yr in enumerate(["27", "28", "29"]):
    # PAT
    ax = fig4.add_subplot(gs4[0, i])
    data = outputs[f"fy{yr}_pat"]
    ax.hist(data, bins=80, color=pat_colors[i], alpha=0.8, edgecolor=None, density=True)
    ax.axvline(np.median(data), color="white", linestyle="--", linewidth=1, alpha=0.7)
    ax.set_title(f"FY{yr} PAT (₹ Cr)", fontweight="bold", color=pat_colors[i])
    ax.grid(True, alpha=0.15)
    add_stats_box(ax, data, fmt=".0f")

    # P/E
    ax = fig4.add_subplot(gs4[1, i])
    data = outputs[f"fy{yr}_pe"]
    data = data[np.isfinite(data)]
    data = np.clip(data, 0, 25)
    ax.hist(data, bins=80, color=pe_colors[i], alpha=0.8, edgecolor=None, density=True)
    ax.axvline(np.median(data), color="white", linestyle="--", linewidth=1, alpha=0.7)
    ax.set_title(f"Forward P/E FY{yr}E", fontweight="bold", color=pe_colors[i])
    ax.grid(True, alpha=0.15)
    add_stats_box(ax, data, fmt=".1f")

    # Volume
    ax = fig4.add_subplot(gs4[2, i])
    data = outputs[f"fy{yr}_vol"]
    ax.hist(data, bins=60, color=vol_colors[i], alpha=0.8, edgecolor=None, density=True)
    ax.axvline(np.median(data), color="white", linestyle="--", linewidth=1, alpha=0.7)
    ax.set_title(f"FY{yr} Volume (kg)", fontweight="bold", color=vol_colors[i])
    ax.grid(True, alpha=0.15)
    add_stats_box(ax, data, fmt=".0f")

fig4.suptitle("Shanti Gold — Monte Carlo: Output Distributions (N=10,000)",
              fontsize=14, fontweight="bold", y=0.99)
fig4.savefig(os.path.join(OUT_DIR, "chart_outputs.png"), dpi=150, bbox_inches="tight",
             facecolor="#0d1117")
print(f"  Chart 4 saved → {os.path.join(OUT_DIR, 'chart_outputs.png')}")

print("\n" + "=" * 80)
print("  All charts saved. Simulation complete.")
print("=" * 80)
