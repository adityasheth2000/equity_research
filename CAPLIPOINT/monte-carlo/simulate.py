#!/usr/bin/env python3
"""
Caplin Point Laboratories — Monte Carlo Stock Price Simulation
==============================================================

Models 1-year and 2-year forward stock price using:
  1. EPS growth: Normal(μ=16%, σ=10%), clipped [-10%, +40%]
  2. P/E multiple: lognormal with median anchored at 26, correlated with growth
  3. Dividends: ₹8/share/year

50,000 iterations per horizon. All figures in ₹.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
from textwrap import dedent

# ── Reproduction ──────────────────────────────────────────────────────────
np.random.seed(20260816)
N = 50_000
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ── Current State ─────────────────────────────────────────────────────────
CURRENT_PRICE  = 2480.0
TTM_EPS        = 87.53       # TTM (screener TTM column: ₹87.53)
CURRENT_PE     = CURRENT_PRICE / TTM_EPS  # ≈ 28.3
DIVIDEND_PER_YEAR = 8.0     # ₹4 interim + ₹4 final (FY26 pattern)

# ── Historical P/E (FY-end trailing, wisesheets.io) ───────────────────────
HIST_PE = np.array([30.70, 30.74, 17.30, 9.94,  12.60,
                    17.12, 12.01, 22.79, 28.02])
HIST_PE_MEAN_GEOM = np.exp(np.mean(np.log(HIST_PE)))  # ≈ 18.6
HIST_PE_LOG_STD   = np.std(np.log(HIST_PE), ddof=0)   # ≈ 0.41

print(f"Historical P/E: geometric mean = {HIST_PE_MEAN_GEOM:.1f}, "
      f"log-std = {HIST_PE_LOG_STD:.3f}")
print(f"Current TTM P/E = {CURRENT_PE:.1f}")

# ── Model Parameters ──────────────────────────────────────────────────────
# EPS growth per annum: Normal, clipped for extreme tails
EPS_GROWTH_MEAN = 0.16      # below 5yr 22% / 3yr 20%, above recent 14-15%
EPS_GROWTH_STD  = 0.10
EPS_GROWTH_MIN  = -0.10     # worst case: mild degrowth
EPS_GROWTH_MAX  = 0.40      # best case: breakout

# P/E distribution (lognormal) — base parameters
PE_MEDIAN       = 26.0       # between current 28.3 and long-run ~18.6
PE_LOG_SIGMA    = 0.30       # tighter than historical 0.41 (current PE is known)
PE_GROWTH_BETA  = 0.90       # P/E sensitivity to growth  (per % above/below 16%)

# Mean-reversion toward long-run PE (slight gravitational pull)
# Over H years, expected log drift = -H * reversion_rate
PE_REVERSION_RATE = 0.03     # ~3% log-drift per year toward historical mean

# ── Helpers ───────────────────────────────────────────────────────────────
def draw_eps_growth(size):
    g = np.random.normal(EPS_GROWTH_MEAN, EPS_GROWTH_STD, size=size)
    return np.clip(g, EPS_GROWTH_MIN, EPS_GROWTH_MAX)

def draw_terminal_pe(g_avg, horizon_years, size):
    """Terminal P/E: lognormal base + growth linkage + mild reversion."""
    # Base log-PE
    ln_pe_base = np.log(PE_MEDIAN) + PE_LOG_SIGMA * np.random.normal(0, 1, size=size)

    # Growth linkage: higher growth → higher PE
    growth_adj = PE_GROWTH_BETA * (g_avg - EPS_GROWTH_MEAN) / EPS_GROWTH_STD * PE_LOG_SIGMA

    # Mean-reversion tilt
    reversion_adj = -horizon_years * PE_REVERSION_RATE * (np.exp(ln_pe_base) - HIST_PE_MEAN_GEOM) / HIST_PE_MEAN_GEOM

    ln_pe = ln_pe_base + growth_adj + reversion_adj
    return np.exp(ln_pe)

def simulate(horizon_years, size=N):
    """Run N simulations for given horizon (1 or 2 years)."""
    # EPS growth per year
    if horizon_years == 1:
        g1 = draw_eps_growth(size)
        g2 = np.zeros(size)  # dummy
        g_avg = g1
        eps_terminal = TTM_EPS * (1 + g1)
    else:
        g1 = draw_eps_growth(size)
        g2 = draw_eps_growth(size)
        g_avg = np.exp((np.log(1 + g1) + np.log(1 + g2)) / 2) - 1
        eps_terminal = TTM_EPS * (1 + g1) * (1 + g2)

    # Terminal P/E
    pe_terminal = draw_terminal_pe(g_avg, horizon_years, size)

    # Price and dividend
    cum_dividend = DIVIDEND_PER_YEAR * horizon_years
    price_terminal = eps_terminal * pe_terminal
    total_return = (price_terminal + cum_dividend) / CURRENT_PRICE - 1
    cagr = (1 + total_return) ** (1 / horizon_years) - 1

    return {
        "eps_growth_avg": g_avg,
        "eps_terminal":  eps_terminal,
        "pe_terminal":   pe_terminal,
        "price":         price_terminal,
        "total_return":  total_return,
        "cagr":          cagr,
    }

def stats(arr, label, pct=False):
    """Print percentile summary."""
    p05, p25, p50, p75, p95 = np.percentile(arr, [5, 25, 50, 75, 95])
    mean = np.mean(arr)
    fmt = "{:>7.1f}" if pct else "{:>8.1f}"
    suffix = "%" if pct else ""
    print(f"  {label:22s}: mean={fmt.format(mean)}{suffix}  "
          f"p5={fmt.format(p05)}{suffix}  p25={fmt.format(p25)}{suffix}  "
          f"p50={fmt.format(p50)}{suffix}  p75={fmt.format(p75)}{suffix}  "
          f"p95={fmt.format(p95)}{suffix}")

# ── Run Simulations ────────────────────────────────────────────────────────
print("\nRunning 1-year Monte Carlo...")
res1 = simulate(1)
print("Running 2-year Monte Carlo...")
res2 = simulate(2)

# ── Print Summary ──────────────────────────────────────────────────────────
def summarize(name, res, horizon):
    print(f"\n{'='*60}")
    print(f"  {name} ({horizon} year{'s' if horizon > 1 else ''}, {N:,.0f} iterations)")
    print(f"{'='*60}")
    stats(res["eps_growth_avg"] * 100, "EPS Growth (CAGR)", pct=True)
    stats(res["pe_terminal"],  "Terminal P/E")
    stats(res["eps_terminal"], "Terminal EPS (Rs)")
    stats(res["price"],        "Terminal Price (Rs)")
    stats(res["cagr"] * 100,   "Return CAGR", pct=True)
    total_ret = res["total_return"]
    stats(total_ret * 100,     "Total Return", pct=True)

    nifty_hurdle = 1.12 ** horizon - 1  # 12% CAGR
    prob_positive = np.mean(total_ret > 0)
    prob_beat_nifty = np.mean(total_ret > nifty_hurdle)
    prob_drawdown_20 = np.mean(total_ret < -0.20)
    prob_above_2x = np.mean(total_ret > 1.0)
    prob_degrowth = np.mean(res["eps_growth_avg"] < 0.05)  # <5% growth = near degrowth

    print(f"\n  Probability positive return:      {prob_positive*100:.1f}%")
    print(f"  Probability beating Nifty (12%/yr): {prob_beat_nifty*100:.1f}%")
    print(f"  Probability of >20% loss:          {prob_drawdown_20*100:.1f}%")
    print(f"  Probability of >100% return (2x):  {prob_above_2x*100:.1f}%")
    print(f"  Probability EPS growth < 5%:       {prob_degrowth*100:.1f}%")

summarize("1-YEAR HORIZON",  res1, 1)
summarize("2-YEAR HORIZON",  res2, 2)

# ── Charts ─────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.30)

# Color palette
BLUE   = "#2196F3"
ORANGE = "#FF9800"
RED    = "#F44336"
GREEN  = "#4CAF50"
GREY   = "#9E9E9E"

def add_ref_lines(ax, current, hist_range=True):
    ax.axvline(current, color=RED, linestyle="--", linewidth=1.5, label=f"Current: ₹{current:,.0f}")
    if hist_range:
        for p, ls, lab in [(27, ":", "Long-run mean ~20x"), (12, ":", "")]:
            pass

# --- 1. 1-year price distribution ---
ax = fig.add_subplot(gs[0, 0])
bins = np.linspace(np.percentile(res1["price"], 0.5), np.percentile(res1["price"], 99.5), 80)
ax.hist(res1["price"], bins=bins, color=BLUE, alpha=0.7, edgecolor="white", linewidth=0.3)
ax.axvline(CURRENT_PRICE, color=RED, linestyle="--", linewidth=1.5, label=f"Current: ₹{CURRENT_PRICE:,.0f}")
p50_1 = np.percentile(res1["price"], 50)
ax.axvline(p50_1, color=GREEN, linestyle="-", linewidth=1.5, label=f"Median: ₹{p50_1:,.0f}")
ax.set_title(f"1-Year Price Distribution\n(Median: ₹{p50_1:,.0f})", fontweight="bold")
ax.set_xlabel("Stock Price (₹)")
ax.set_ylabel("Frequency")
ax.legend(fontsize=8)

# --- 2. 2-year price distribution ---
ax = fig.add_subplot(gs[0, 1])
bins = np.linspace(np.percentile(res2["price"], 0.5), np.percentile(res2["price"], 99.5), 80)
ax.hist(res2["price"], bins=bins, color=ORANGE, alpha=0.7, edgecolor="white", linewidth=0.3)
ax.axvline(CURRENT_PRICE, color=RED, linestyle="--", linewidth=1.5, label=f"Current: ₹{CURRENT_PRICE:,.0f}")
p50_2 = np.percentile(res2["price"], 50)
ax.axvline(p50_2, color=GREEN, linestyle="-", linewidth=1.5, label=f"Median: ₹{p50_2:,.0f}")
ax.set_title(f"2-Year Price Distribution\n(Median: ₹{p50_2:,.0f})", fontweight="bold")
ax.set_xlabel("Stock Price (₹)")
ax.set_ylabel("Frequency")
ax.legend(fontsize=8)

# --- 3. CAGR distribution (2-year) ---
ax = fig.add_subplot(gs[0, 2])
cagrs = res2["cagr"] * 100
bins = np.linspace(np.percentile(cagrs, 0.5), np.percentile(cagrs, 99.5), 80)
ax.hist(cagrs, bins=bins, color=GREEN, alpha=0.7, edgecolor="white", linewidth=0.3)
p50_c = np.percentile(cagrs, 50)
ax.axvline(p50_c, color=RED, linestyle="--", linewidth=1.5, label=f"Median: {p50_c:.1f}%")
ax.axvline(12, color=GREY, linestyle=":", linewidth=1.5, label="Nifty hurdle: 12%")
ax.set_title(f"2-Year CAGR Distribution\n(Median: {p50_c:.1f}%)", fontweight="bold")
ax.set_xlabel("CAGR (%)")
ax.set_ylabel("Frequency")
ax.legend(fontsize=8)

# --- 4. Terminal P/E distribution (2-year) ---
ax = fig.add_subplot(gs[1, 0])
pe_vals = res2["pe_terminal"]
bins = np.linspace(np.percentile(pe_vals, 0.5), np.percentile(pe_vals, 99.5), 80)
ax.hist(pe_vals, bins=bins, color="purple", alpha=0.7, edgecolor="white", linewidth=0.3)
ax.axvline(CURRENT_PE, color=RED, linestyle="--", linewidth=1.5, label=f"Current: {CURRENT_PE:.1f}x")
p50_pe = np.percentile(pe_vals, 50)
ax.axvline(p50_pe, color=GREEN, linestyle="-", linewidth=1.5, label=f"Median: {p50_pe:.1f}x")
ax.axvline(HIST_PE_MEAN_GEOM, color=GREY, linestyle=":", linewidth=1.5, label=f"Hist mean: {HIST_PE_MEAN_GEOM:.1f}x")
ax.set_title(f"Terminal P/E Distribution (2yr)\n(Median: {p50_pe:.1f}x)", fontweight="bold")
ax.set_xlabel("P/E Ratio")
ax.set_ylabel("Frequency")
ax.legend(fontsize=7)

# --- 5. EPS growth / P/E scatter (2-year) ---
ax = fig.add_subplot(gs[1, 1])
# Downsample for plotting
idx = np.random.choice(N, min(8000, N), replace=False)
ax.scatter(res2["eps_growth_avg"][idx] * 100, res2["pe_terminal"][idx],
           alpha=0.15, s=3, color=BLUE, edgecolors="none")
ax.axhline(CURRENT_PE, color=RED, linestyle="--", linewidth=1, alpha=0.7)
ax.axvline(EPS_GROWTH_MEAN * 100, color=GREY, linestyle=":", linewidth=1, alpha=0.7)
ax.set_title("EPS Growth vs Terminal P/E (2yr)\n", fontweight="bold")
ax.set_xlabel("Avg Annual EPS Growth (%)")
ax.set_ylabel("Terminal P/E")
ax.text(0.98, 0.98, f"ρ = {np.corrcoef(res2['eps_growth_avg'], res2['pe_terminal'])[0,1]:.2f}",
        transform=ax.transAxes, ha="right", va="top", fontsize=9, color=GREY)

# --- 6. Scenario probability table ---
ax = fig.add_subplot(gs[1, 2])
ax.axis("off")
price2 = res2["price"]
total_ret_2 = res2["total_return"]
scenarios = [
    ("Severe De-rate\n(P/E < 18x)",     np.mean(res2["pe_terminal"] < 18),   "red"),
    ("Moderate\n(P/E 18-26x)",          np.mean((res2["pe_terminal"] >= 18) & (res2["pe_terminal"] < 26)), "orange"),
    ("Status Quo\n(P/E 26-32x)",        np.mean((res2["pe_terminal"] >= 26) & (res2["pe_terminal"] < 32)), "blue"),
    ("Re-rate\n(P/E 32-38x)",           np.mean((res2["pe_terminal"] >= 32) & (res2["pe_terminal"] < 38)), "green"),
    ("Strong Re-rate\n(P/E > 38x)",     np.mean(res2["pe_terminal"] >= 38),   "darkgreen"),
]
scenarios_return = [
    ("Loss <-20%",   np.mean(total_ret_2 < -0.20),   "red"),
    ("-20% to 0%",   np.mean((total_ret_2 >= -0.20) & (total_ret_2 < 0)), "orange"),
    ("0-25% return", np.mean((total_ret_2 >= 0) & (total_ret_2 < 0.25)), "yellow"),
    ("25-60% return",np.mean((total_ret_2 >= 0.25) & (total_ret_2 < 0.60)), "blue"),
    (">60% return",  np.mean(total_ret_2 >= 0.60),   "green"),
]

table_data = []
table_data.append(["P/E REGIME (2yr)", "Prob"])
for s, p, _ in scenarios:
    table_data.append([s, f"{p*100:.1f}%"])
table_data.append(["", ""])
table_data.append(["RETURN REGIME (2yr)", "Prob"])
for s, p, _ in scenarios_return:
    table_data.append([s, f"{p*100:.1f}%"])

table = ax.table(cellText=table_data, cellLoc="center", loc="center",
                 colWidths=[0.45, 0.25])
table.auto_set_font_size(False)
table.set_fontsize(8)
for (row, col), cell in table.get_celld().items():
    if row == 0 or row == len(scenarios) + 2:
        cell.set_facecolor("#E0E0E0")
        cell.set_fontsize(9)
    if col == 0:
        cell.get_text().set_ha("left")
ax.set_title("Scenario Probabilities (2yr)\n", fontweight="bold", y=0.98)

fig.suptitle("Caplin Point Laboratories — Monte Carlo Simulation\n"
             f"{N:,} iterations | EPS growth μ={EPS_GROWTH_MEAN*100:.0f}% | "
             f"P/E median base={PE_MEDIAN:.0f}x | Dividends ₹{DIVIDEND_PER_YEAR:.0f}/year",
             fontsize=11, y=1.01)

plt.savefig(os.path.join(OUT_DIR, "simulation.png"), dpi=150, bbox_inches="tight")
plt.close()
print(f"\nCharts saved: {os.path.join(OUT_DIR, 'simulation.png')}")

# ── Sensitivity: Vary EPS growth mean ─────────────────────────────────────
print(f"\n{'='*60}")
print("  SENSITIVITY: Effect of changing EPS growth assumption (2yr)")
print(f"{'='*60}")
for mu in [0.08, 0.12, 0.16, 0.20, 0.24]:
    # Quick re-run with modified mean
    np.random.seed(20260816)
    def draw_g_sens(size):
        g = np.random.normal(mu, EPS_GROWTH_STD, size=size)
        return np.clip(g, EPS_GROWTH_MIN, EPS_GROWTH_MAX)
    g1s = draw_g_sens(N)
    g2s = draw_g_sens(N)
    g_avg_s = np.exp((np.log(1+g1s) + np.log(1+g2s)) / 2) - 1
    pe_s = draw_terminal_pe(g_avg_s, 2, N)
    eps_s = TTM_EPS * (1+g1s) * (1+g2s)
    price_s = eps_s * pe_s
    cagr_s = (1 + (price_s + DIVIDEND_PER_YEAR*2) / CURRENT_PRICE - 1) ** 0.5 - 1
    print(f"  EPS mean={mu*100:3.0f}% -> "
          f"Price p50=₹{np.percentile(price_s, 50):,.0f}   "
          f"CAGR p50={np.percentile(cagr_s*100, 50):.1f}%   "
          f"Prob beat Nifty={np.mean(price_s + DIVIDEND_PER_YEAR*2 > CURRENT_PRICE*1.2544)*100:.0f}%")