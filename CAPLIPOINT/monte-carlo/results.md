# Caplin Point Laboratories — Monte Carlo Simulation

**Date:** 16 August 2026 | **Ticker:** CAPLIPOINT
**Current Price:** ₹2,480 | **TTM EPS:** ₹87.53 | **Current P/E:** 28.3x

---

## 1. Methodology

A two-factor Monte Carlo simulates the forward stock price by jointly drawing:

1. **EPS growth** (earnings driver)
2. **Terminal P/E multiple** (valuation driver)

Price at horizon = **EPS_terminal × P/E_terminal + accumulated dividends** (₹8/share/yr).

`50,000` iterations were run for a **1-year** and a **2-year** horizon (seed `20260816` for reproducibility).

### 1.1 Earnings Growth Model

```
Annual EPS growth ~ Normal(μ = 16%, σ = 10%), clipped to [-10%, +40%]
```

| Calibration | Value | Rationale |
|---|---|---|
| Mean 16% | below 5-yr (22%) and 3-yr (20%) CAGR | reflects the observed deceleration |
| Std 10% | covers FY21's 12.7% → FY18's 51% | realistic dispersion |
| Min −10% | allows genuine **degrowth** | downside tail |
| Max +40% | allows a **breakout** year | upside tail |

Historical EPS growth: FY18 +51%, FY19 +22%, FY20 +22%, FY21 +13%, FY22 +24%, FY23 +25%, FY24 +21%, FY25 +17%, FY26 +20%.

### 1.2 P/E Multiple Model

The terminal P/E is **lognormal**, anchored at a median of **26x** (between the current 28.3x and the long-run geometric mean), and is **correlated with realized EPS growth** (higher growth → higher multiple), with a mild mean-reversion pull toward the historical mean.

```
ln(P/E) = ln(26) + N(0, 0.30)          ← base spread
        + 0.90 × (g − 16%)/10% × 0.30  ← growth linkage
        − 2yr × 0.03 × (P/E − 18.6)/18.6 ← mild mean reversion
```

### 1.3 Historical P/E (calibration anchor)

Company's trailing P/E at fiscal year-end (wisesheets.io):

| FY | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| P/E | 30.7 | 30.7 | 17.3 | 9.9 | 12.6 | 17.1 | 12.0 | 22.8 | 28.0 |

- **Geometric mean ≈ 18.6x**, log-std ≈ 0.40
- **10-yr range:** 9.7x (Dec 2019) to 36.7x (Sep 2017)
- **5-yr median ≈ 17x**, peak 28.4x (Mar 2025)

The current **28.3x sits above the ~18.6x long-run mean**, so the model applies a *mild* downward mean-reversion (P/E median drifts to ~25x by year 2) — this is the main reason the simulated median return is below the naive "EPS growth only" estimate.

---

## 2. Results

### 2.1 1-Year Horizon

| Statistic | EPS Growth | Terminal P/E | Terminal Price | Total Return |
|---|---|---|---|---|
| **Mean** | 16.0% | 27.6x | ₹2,866 | +15.9% |
| **p5** | −0.5% | 13.4x | ₹1,212 | −50.8% |
| **p25** | 9.3% | 19.7x | ₹1,908 | −22.7% |
| **Median** | 16.0% | 25.6x | ₹2,596 | +5.0% |
| **p75** | 22.8% | 33.4x | ₹3,533 | +42.8% |
| **p95** | 32.4% | 48.6x | ₹5,431 | +119% |

- Probability of positive return: **54%**
- Probability of beating Nifty (12%): **44%**
- Probability of >20% loss: **28%**
- Probability of >2x return: **8%**

### 2.2 2-Year Horizon (primary)

| Statistic | EPS Growth (CAGR) | Terminal P/E | Terminal EPS | Terminal Price | CAGR | Total Return |
|---|---|---|---|---|---|---|
| **Mean** | 15.8% | 26.6x | ₹117.8 | ₹3,207 | +11.6% | +30.0% |
| **p5** | 4.2% | 14.5x | ₹95.0 | ₹1,475 | −22.5% | −39.9% |
| **p25** | 11.0% | 20.1x | ₹107.9 | ₹2,224 | −5.0% | −9.7% |
| **Median** | 15.8% | 25.2x | ₹117.4 | ₹2,951 | +9.4% | +19.6% |
| **p75** | 20.6% | 31.6x | ₹127.2 | ₹3,913 | +25.9% | +58.4% |
| **p95** | 27.3% | 43.7x | ₹141.9 | ₹5,809 | +53.3% | +134.9% |

- **Median 2-year return: +19.6% (~9.4% CAGR)**
- Probability of positive return: **67%**
- Probability of beating Nifty (12%/yr): **45%**
- Probability of >20% loss: **17%**
- Probability of >2x return: **11%**
- Probability EPS growth <5% (near-degrowth): **6%**

### 2.3 Scenario Probabilities (2-Year)

**P/E regime:**

| Regime | Probability |
|---|---|
| Severe de-rate (P/E < 18x) | ~18% |
| Moderate (18–26x) | ~36% |
| Status quo (26–32x) | ~29% |
| Re-rate (32–38x) | ~12% |
| Strong re-rate (> 38x) | ~5% |

**Return regime (2-year):**

| Regime | Probability |
|---|---|
| Loss < −20% | ~17% |
| −20% to 0% | ~16% |
| 0 to +25% | ~22% |
| +25% to +60% | ~23% |
| > +60% | ~22% |

---

## 3. Sensitivity — Effect of the EPS Growth Assumption (2-yr)

Holding the P/E model constant, varying the assumed mean EPS growth:

| EPS Growth Mean | Median Price (2yr) | Median CAGR | Prob. Beat Nifty (12%) |
|---|---|---|---|
| 8% (bear) | ₹2,062 | −8.5% | 17% |
| 12% | ₹2,465 | 0.0% | 29% |
| **16% (base)** | **₹2,947** | **+9.3%** | **45%** |
| 20% | ₹3,510 | +19.2% | 62% |
| 24% (bull) | ₹4,163 | +29.8% | 77% |

The model is **highly sensitive to the earnings-growth assumption** — more so than to the P/E assumption. Growth is the dominant driver; the P/E re-rating is a secondary, correlated amplifier.

---

## 4. Interpretation

1. **Median outcome is modest (≈9–10% CAGR) but positive.** The mean is pulled up to ~11.6% CAGR by the right tail. The model is *not* pricing in the bull case by default — it assumes P/E mildly de-rates from 28x to ~25x (mean reversion toward the ~18.6x long-run average).

2. **The distribution is wide and positively skewed.** A 22% chance of >+60% return in 2 years, but a 17% chance of >20% loss. This is characteristic of a high-multiple, high-growth small-cap where the market re-prices the multiple aggressively in both directions.

3. **Growth, not the multiple, is what matters most.** The sensitivity table shows that if Caplin delivers its ~16% EPS growth, you earn ~9% CAGR even with a *de-rating* P/E; if growth slips to ~8%, you lose money even though P/E barely moves.

4. **Reconciling with the fundamental thesis.** The prior fundamental analysis argued a 15–20% CAGR was achievable if earnings compound at 18–20% *and* P/E re-rates to 32–35x. This simulation shows that outcome sits in the **upper quartile** (p75 ≈ +26% CAGR), i.e., it requires the bull case on *both* earnings and the multiple. The median path (earnings ~16%, P/E ~25x) is ~9% CAGR.

---

## 5. Key Inputs & Caveats

| Parameter | Value |
|---|---|
| Current price | ₹2,480 |
| TTM EPS | ₹87.53 |
| Dividend | ₹8/share/yr |
| EPS growth μ / σ | 16% / 10% |
| EPS growth range | −10% to +40% |
| P/E base median | 26x |
| P/E log-σ | 0.30 |
| Growth→P/E beta | 0.90 |
| Mean-reversion rate | 3%/yr |

**Caveats:**
- Historical P/E is used to *calibrate* the spread, but the simulation assumes a somewhat *higher* base (26x) than the long-run mean (18.6x), on the view that the current growth/quality profile justifies a structural premium. If the market reverts fully to ~18x, the downside is more severe than the median shown here.
- The model does not distinguish the "capacity-fill / FY28 inflection" scenario explicitly — that upside is captured only through the wide growth and P/E tails.
- Single-stock outcomes are dominated by idiosyncratic events (FDA actions, tender wins, LatAm macro) that a lognormal model can only approximate.

---

## 6. Files

- `simulate.py` — reproducible script (edit parameters at top, re-run with `python simulate.py`)
- `simulation.png` — 6-panel chart (price distributions, CAGR, P/E, growth-vs-P/E scatter, scenario table)

*Data sources: screener.in financials, wisesheets.io / pocketful.in historical P/E, devyara/stockpricearchive price history, company earnings presentations & transcripts.*
