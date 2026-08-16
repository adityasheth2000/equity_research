Here's a thinking process that leads to the suggested markdown report:

1.  **Understand the Goal:** The user wants me to act as an equity analyst and extract specific information from the provided raw text (a credit rating rationale) into a structured markdown report. The structure is predefined with specific sections (Rating Action, Detailed Rationale, Key Rating Drivers, Liquidity, Outlook & Sensitivity, Key Financial Indicators, Bank Facilities, Company & Subsidiaries).

2.  **Analyze the Input Data:** I need to read through the raw text carefully and identify where each piece of information fits according to the required sections.

    *   *Source:* Brickwork Ratings (BWR).
    *   *Date:* 03 Mar 2022.
    *   *Entity:* Ganesh Housing Corporation Limited (GHCL).
    *   *Rating Details:* BWR BB-/Stable vs Previous BWR B-/Negative.
    *   *Amount:* Rs. 31.91 Crs.
    *   *Facilities:* Fund Based (Term Loans).
    *   *Rationale:* Upgrade due to improved financials, debt reduction, sales, cash flows, info cooperation. Removed "Issuer Not Cooperating".
    *   *Strengths:* Leverage ratio improvement, Project details/sales, Operational mix, Location advantage, Management experience, Cash flows from land bank, Industry outlook.
    *   *Weaknesses:* Cyclical industry, Regulatory risk, Geographic concentration.
    *   *Liquidity:* Cash/bank balance, Debt levels, CPLTD.
    *   *Outlook/Sensitivity:* Positive (revenue, debt servicing), Negative (cash flow dilution, performance deterioration).
    *   *Financials:* Standalone table exists for FY20-21 and FY19-20. Consolidated revenue mentioned in narrative.
    *   *Bank Facilities:* Annexure-I lists Karur Vysya, PNB Housing Finance, Tamilnad Mercantile Bank.
    *   *Company Info:* Incorporated 1991, Ahmedabad based, Promoters (Shekhar Patel, Dipakkumar Patel). Subsidiaries: Gatil Properties, Madhukamal Infrastructure.

3.  **Drafting the Sections (Iterative Process):**

    *   **Rating Action:** Need Agency (Brickwork Ratings), Date (03 Mar 2022), Rating (BB-/Stable), Previous (B-/Negative), Amount (Rs. 31.91 Cr), Facilities (Fund Based/Bank Loan).
    *   **Detailed Rationale:** Summarize the upgrade reason. Focus on the shift from "Non-Cooperation" to providing info, debt reduction (663cr -> 225.8cr), and project progress (40% construction done, 91% units sold). Mention NDS provision.
    *   **Key Rating Drivers — Strengths:** Extract the bullet points from "KEY RATING DRIVERS - Credit Strengths". Add specific numbers (Net worth 572 cr, Leverage 0.43x, Inventory sold 95%).
    *   **Key Rating Drivers — Weaknesses:** Extract from "Credit Risks". Mention Cyclicality, Regulation, Geographic Concentration.
    *   **Liquidity:** Check "LIQUIDITY INDICATORS". Cash/Bank = 10.41 crs. Total Debt = 225.8 crs. CPLTD = 78 cr (FY22), 42 cr (FY23). Ratio TDT/TNW = 0.43X.
    *   **Outlook & Rating Sensitivity:** Outlook is Stable. Positive factors: Revenue improvement, timely repayment. Negative factors: Cash flow dilution, operating performance drop.
    *   **Key Financial Indicators:** Use the table at the end titled "KEY FINANCIAL INDICATORS (Standalone)". Note: There is also consolidated data mentioned in narrative (Rev 228 cr, EBITDA 82 cr), but the explicit table is standalone. I should probably include the Standalone table as requested ("Present as a markdown table if tabular data exists"). I will add a note about consolidated figures if they add value, but prioritize the table found.
    *   **Bank Facilities:** Use Annexure-I. Create a table with Bank Name, Type, Long Term, Short Term, Total.
    *   **Company & Subsidiaries:** Incorporate info from "ABOUT THE ENTITY" and "ANNEXURE-III List of entities consolidated".

4.  **Refining and Formatting:**
    *   Ensure Markdown headers match the requested structure (`##`).
    *   Ensure tables are aligned correctly.
    *   Check for clarity and conciseness.
    *   Verify all numbers match the source text (e.g., Rs. 31.91 Crs, 0.43x leverage).
    *   *Self-Correction on Financial Indicators:* The prompt asks for "Key Financial Indicators" as a table. The text provides a table for "KEY FINANCIAL INDICATORS (Standalone)". I will use that. I will also make sure to mention the consolidated context briefly in the company section or rationale since the analysis is consolidated.
    *   *Self-Correction on Date:* The text header says "03Mar2022".
    *   *Self-Correction on Rating:* Current is "BWR BB - /Negative to Stable" (Upgrade from BWR B-/Negative). Actually, looking closely at the text: "The company has... rating continues to derive support...". Wait, under Rating Action it says "upgrade the rating to BWR BB-/Stable from BWR B-/Negative". Under the table "Previous Present" columns show "BWR B-/Negative" and "BWR BB - /Negative to Stable". It seems the decision is Upgrade to BB- and Outlook change to Stable. I will state the *current* status clearly as BB-/Stable.

5.  **Final Review against Constraints:**
    *   Markdown format? Yes.
    *   All sections present? Yes.
    *   Accurate extraction? Yes.
    *   Tone: Professional Equity Analyst style.

6.  **Constructing the Output:** (Proceeding to generate the response based on the thought process).

    *   *Note on Table Data:* The financial indicators table has some empty cells or dashes. I will render them as blank or `NA` where appropriate for cleanliness.
    *   *Note on Bank Facilities:* Annexure shows "Others" with 0.00 amount. I will focus on the banks with active ratings/funds.
    *   *Note on Currency:* Keep as "Rs. Crs." or "Crs." for consistency.

    *(Self-Correction during drafting)*: The "Rating History" section in the text has complex dates. I only need the current action summary for the "Rating Action" section unless specifically asked for history. I will stick to the current action to keep it clean, but maybe reference the previous one for comparison.

    *(Check Bank Facilities)*:
    1. Karur Vysya: 0.93
    2. Others: 0.00
    3. PNB Housing: 11.08
    4. TN Mercantile: 19.90
    5. Yes Bank: 0.00
    Total: 31.91

    *(Check Subsidiaries)*:
    1. Gatil Properties Private Limited (71.09%)
    2. Madhukamal Infrastructure Private Limited (100%)

    Let's assemble.

7.  **Final Polish:** Check bolding for emphasis on key metrics. Ensure the distinction between Standalone and Consolidated financials is clear where data conflicts (Text says Analysis is Consolidated, but Table is Standalone). I will label the table explicitly.

    *Wait, one detail check:* The text says "BWR BB - /Negative to Stable" in the table, but the narrative says "upgrade the rating to BWR BB-/Stable". Usually, this means the final decision is BB-/Stable. The `/Negative to Stable` likely indicates the transition event. I will simplify to the resulting state: BWR BB- / Stable.

    *Another detail:* "ISSUER NOT COOPERATING*" was removed. This is crucial for the Rationale section regarding why the outlook changed.

    Okay, ready to write.cw
</think>

# Credit Rating Report: Ganesh Housing Corporation Limited

**Date:** 03 March 2022  
**Agency:** Brickwork Ratings (BWR)

---

## Rating Action

| Parameter | Details |
| :--- | :--- |
| **Issuing Entity** | Ganesh Housing Corporation Limited (GHCL) |
| **Facility Rated** | Bank Loan Facilities (Fund Based) |
| **Total Facilities Amount** | ₹31.91 Crores |
| **Current Rating** | BWR BB- |
| **Current Outlook** | Stable |
| **Previous Rating** | BWR B- |
| **Previous Outlook** | Negative |
| **Decision** | Upgrade & Outlook Revision |
| **Issue Status** | Issuer Not Cooperating (Removed) |

---

## Detailed Rationale

Brickwork Ratings (BWR) has upgraded the bank loan facilities of Ganesh Housing Corporation Limited (GHCL) to **BWR BB-** with a **Stable** outlook from **BWR B-** with a **Negative** outlook. 

This revision reflects significant improvements in the company's financial profile, including a substantial reduction in total debt from ₹663 crores (March 2019) to ₹225.8 crores (September 2021). Improved leverage metrics (gearing ratio reduced to 0.43x) were achieved through the monetization of the land bank and receipt of customer advances totaling ₹72 crores from running projects. 

Previously, the Negative outlook and "Issuer Not Cooperating" tag were assigned due to non-submission of necessary surveillance data. These issues have been rectified; the company has now provided the Necessary Disclosure Statement (NDS) and requisite information for review. Visibility on project execution is now clear, with over 40% construction completion on running projects and 91% unit sales achievement.

---

## Key Rating Drivers — Strengths

*   **Improved Financial Leverage:** Tangible net worth stood at ₹572 crores (FY2021). Debt reduction improved the Gearing Ratio to 0.43x (Sep 2021) from 0.81x (March 2019).
*   **Strong Sales & Inventory Position:** Total saleable area of ~2.5 million sq ft. The company has sold approximately 95% of its inventory. Two ongoing projects (Malabar County III & Malabar Exotica) have seen 91% of units already booked.
*   **Operational Diversification:** Ongoing projects are at various stages of construction (advanced vs. nascent), which helps balance cash flows efficiently.
*   **Experienced Management:** GHCL has nearly four decades of experience (since 1991) in the Ahmedabad real estate sector. Chairman Mr. Dipakkumar Patel has over three decades of industry experience.
*   **Land Bank & Liquidity:** Regular sale of land parcels supports cash flows alongside operating cash flows.
*   **Location Advantage:** Projects are located in strategic areas of Ahmedabad with good connectivity, expected to fetch better prices in a positive real estate market.
*   **Listed Status:** Company is listed on both BSE and NSE.

---

## Key Rating Drivers — Weaknesses

*   **Geographic Concentration:** Operations are heavily concentrated in Ahmedabad city. A downturn in this specific region could adversely impact cash flows.
*   **Industry Cyclicality:** Exposure to economic downturns impacts sales realization and revenues.
*   **Regulatory Risk:** The real estate sector faces increased regulatory requirements which may affect timely project execution and increase costs.

---

## Liquidity

*   **Assessment:** Adequate.
*   **Cash & Bank Balance:** ₹10.41 Crores (as of Sep 2021).
*   **Debt Levels:** Reduced to ₹225.8 Crores (Sep 2021) from ₹663 Crores (March 2019).
*   **Commitment to Principal/Long Term Debt (CPLTD):** 
    *   FY2022: ₹78 Crores
    *   FY2023: ₹42 Crores
    *   *Plan:* Expected to be serviced via operating cash flows and other inflows.

---

## Outlook & Rating Sensitivity

**Outlook:** **Stable**
*(Revised from Negative)*

| Factor Category | Drivers |
| :--- | :--- |
| **Positive Factors** | • Improvement in revenue and timely servicing of scheduled debt repayments.<br>• Overall improvement in operating performance.<br>• Continued visibility on project execution and sales realization. |
| **Negative Factors** | • Dilution in expected cash flows.<br>• Deterioration in operating performance.<br>• Regulatory changes impacting project timelines. |

---

## Key Financial Indicators (Standalone)

| Key Parameters | Units | FY 20-21 (Audited) | FY 19-20 (Audited) |
| :--- | :--- | :--- | :--- |
| Operating Revenue | Rs. Crs. | 4.22 | 1.71 |
| EBITDA | Rs. Crs. | -9.83 | -23.76 |
| PAT | Rs. Crs. | -46.92 | -63.28 |
| Tangible Net Worth | Rs. Crs. | 654.11 | 700.99 |
| Total Debt / TNW | Times | 0.43 | 0.46 |
| Current Ratio | Times | 2.47 | 2.88 |

*> Note: While standalone figures above are provided in the report, the entity is analyzed on a consolidated basis.*

---

## Bank Facilities

| Sl. No. | Bank/Lender | Type of Facility | Tenure | Amount (Rs. Crs.) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Karur Vysya Bank | Term Loan | Long Term | 0.93 |
| 2 | PNBE Housing Finance Ltd. | Term Loan | Long Term | 11.08 |
| 3 | Tamilnad Mercantile Bank Ltd. | Term Loan | Long Term | 19.90 |
| 4 | Yes Bank | Term Loan | Long Term | 0.00 |
| **Total** | **Consolidated** | **-** | **-** | **31.91** |

---

## Company & Subsidiaries

**Corporate Profile**
*   **Entity:** Ganesh Housing Corporation Ltd (GHCL)
*   **Incorporation:** 1991
*   **Headquarters:** Ahmedabad, Gujarat
*   **Sector:** Real Estate Development (Residential & Commercial)
*   **Promoters:** Mr. Shekhar Patel (Managing Director), Mr. Dipakkumar Patel (Chairman)
*   **Listing:** BSE & NSE
*   **Track Record:** Developed >22 million sq. ft. real estate space; ~29.1 million sq. ft. under development.

**Current Projects**
1.  **Malabar County III:** Launched Feb 2021 (Affordable Housing, Nirma Univ area). 284/288 units booked. Rev est. ₹128 Cr.
2.  **Malabar Exotica:** Launched July 2021 (3.50 BHK, Nirma Univ area). 186/224 units booked. Rev est. ₹165 Cr.
3.  **Pipeline:** Malabar Luxuria, IT SEZ, Smile City (Expected commencement FY2023).

**Consolidated Entities**
| Name of Entity | % Ownership | Extent of Consolidation |
| :--- | :--- | :--- |
| Gatil Properties Private Limited | 71.09% | 100% |
| Madhukamal Infrastructure Private Limited | 100% | 100% |