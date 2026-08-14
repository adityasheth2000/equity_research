Here's a thinking process that leads to the suggested markdown report:

1.  **Analyze the Request:**
    *   **Role:** Equity Analyst.
    *   **Task:** Extract credit rating report from raw text and structure it into a well-organized markdown report.
    *   **Input:** Raw text scraped from a credit rating agency (Crisil Ratings) webpage.
    *   **Required Sections:**
        *   ## Rating Action
        *   ## Detailed Rationale
        *   ## Key Rating Drivers — Strengths
        *   ## Key Rating Drivers — Weaknesses
        *   ## Liquidity
        *   ## Outlook & Rating Sensitivity
        *   ## Key Financial Indicators (Markdown Table)
        *   ## Bank Facilities (Markdown Table)
        *   ## Company & Subsidiaries

2.  **Information Extraction & Categorization:**

    *   **Header Info:**
        *   Date: September 26, 2025
        *   Agency: Crisil Ratings
        *   Company: Kovai Medical Center and Hospital Limited (KMCH)
        *   Location: Mumbai/Coimbatore context.

    *   **Rating Action:**
        *   Long Term: Crisil AA-/Stable (Reaffirmed)
        *   Short Term: Crisil A1+ (Reaffirmed)
        *   Total Facilities Rated: Rs.900 Crore (Enhanced from Rs.500 Crore).
        *   Note on Directors: None participated in rating assignment (standard disclosure).

    *   **Detailed Rationale:**
        *   Summary: Reaffirmed ratings due to long vintage, promoter experience, diversified revenue (healthcare + education), comfortable operating performance, strong financial risk profile.
        *   Offsetting factors: Geographic concentration (Tamil Nadu/Kerala), regulatory risks.

    *   **Strengths:**
        *   Vintage/Experience: Inc. 1985, Ops since 1990. Promoters >40 years exp.
        *   Diversification/Ops: Healthcare (93%) + Education (7%). Flagship hospital Coimbatore + satellite centers. New treatments (IceCure). Operating margins 27-29% over last 3 years. ROCE ~23% (FY25).
        *   Financial Risk: Networth Rs 1086 crore. Gearing 0.35x (Mar 2025). ICR 10.8x (FY25). Debt/EBITDA <1x (Mar 2025).

    *   **Weaknesses:**
        *   Geographic Concentration: 90% revenue from Coimbatore. Flagship contributes 77%. Plan for Chennai to reduce dependency.
        *   Regulatory Risk: Price caps (stents, implants), cash transaction limits, potential standardization of public/private hospital prices.

    *   **Liquidity:**
        *   Assessment: Strong.
        *   Cash/BF/FD: ~Rs. 270 crores (Mar 31, 2025).
        *   Working Capital: Barely utilized. Negative working capital cycle.
        *   Accruals: Rs 330-450 crore annually sufficient for debt obligations (30-60 crore).
        *   Dividends: Unlikely major payouts; reinvested for growth.

    *   **Outlook & Rating Sensitivity:**
        *   Outlook: Stable.
        *   Upward: Steady revenue growth, stable margins >25%, geographical diversification.
        *   Downward: Sluggish growth/margins, debt-funded capex/acquisition leading to Debt/EBITDA > 2.25 times.

    *   **Key Financial Indicators (Table):**
        *   Need to extract FY2024 vs FY2025 data.
        *   Data points: Operating income, PAT, PAT margins, Adjusted Debt/Net worth, Interest coverage.
        *   Source table: "Key Financial Indicators" section.

    *   **Bank Facilities (Table):**
        *   Need to extract facility type, amount, lender, rating.
        *   Source tables: "Annexure - Details of Instrument(s)" AND "Annexure - Details of Bank Lenders & Facilities". The latter is more structured for a bank breakup. Note: Some amounts differ between annexures or represent outstanding vs proposed. I will prioritize the "Details of Bank Lenders & Facilities" table as it explicitly names lenders, but I should check if totals match the Rs 900 Cr mentioned in the header.
        *   Header says Total Bank Loan Facilities Rated Rs 900 Crore.
        *   Lenders table breakdown:
            *   Bank Guarantee: 15
            *   LC: 100
            *   Prop LT Loan: 350
            *   Prop Term: 9.15
            *   Secured OD: 15
            *   Term Loan 1: 119.95
            *   Term Loan 2: 140.9
            *   Term Loan 3: 100
            *   Term Loan 4: 50
            *   Sum: 15+100+350+9.15+15+119.95+140.9+100+50 = 899.95 (approx 900). Perfect match.
        *   Lender: Indian Bank, Indian Overseas Bank, Not Applicable (Proposed).

    *   **Company & Subsidiaries:**
        *   Incorporation: 1985.
        *   Operations: 854-bed multispecialty hospital in Coimbatore.
        *   Satellite Centers: City center, Sulur, Kovilpalayam (Coimbatore); Erode Speciality Hospital.
        *   Education: KMCH Institute of Health Sciences & Research (Medical College).
        *   Promoters: Dr Nalla G Palaniswami, Dr Thavamani Devi Palaniswami.
        *   Listing: BSE.
        *   Subsidiaries/Rating History Annexure mentions Fund Based & Non-Fund Based facilities but doesn't explicitly name separate subsidiary entities other than the college arm mentioned in text. I will list the entities mentioned in the "About the Company" section.

3.  **Drafting the Report (incorporating Markdown formatting):**

    *   *Self-Correction on Dates:* The text says "September 26, 2025". This is future-dated relative to my current training cutoff, but I must stick to the provided text.
    *   *Formatting Tables:* Ensure columns align properly.
    *   *Clarity:* Remove HTML artifacts (like `&nbsp;`, broken lines) found in the raw text (e.g., "Ratings continues to reflect..."). Clean up typos like "weaking", "addit ion".
    *   *Financials:* Ensure units (Rs Crore) are clear.

4.  **Review against Constraints:**
    *   Did I include all specific sections requested? Yes.
    *   Is it in Markdown? Yes.
    *   Are the tables formatted correctly? Yes.
    *   Is the tone professional (Equity Analyst style)? Yes.

5.  **Final Polish:** Check for consistency in terminology (e.g., "Fiscal 2025" vs "Year ended March 31, 2025"). Ensure the distinction between Proposed and Existing facilities is clear in the Bank Facilities table based on the source data. (The source table lumps them under "Facility" with some marked "Not Applicable" for lenders on proposed loans). I will present the data as listed but ensure clarity.

    *Refining Bank Facilities Table:*
    The source "Annexure - Details of Bank Lenders & Facilities" is the best source for the breakup.
    Columns: Facility, Amount (Rs. Cr), Lender, Rating.

    *Refining Financials Table:*
    Columns: Indicator, FY2025, FY2024, Unit.

    *Refining Company Info:*
    Make sure to capture the promoters' names accurately.

6.  **Construct Output:** (Proceeding to generate response based on these steps).
</think>

# Credit Rating Report: Kovai Medical Center and Hospital Limited

**Date:** September 26, 2025  
**Agency:** Crisil Ratings Limited  
**Jurisdiction:** India  

---

## Rating Action

| Parameter | Detail |
| :--- | :--- |
| **Long Term Rating** | **Crisil AA-/Stable** (Reaffirmed) |
| **Short Term Rating** | **Crisil A1+** (Reaffirmed) |
| **Total Facilities Rated** | **Rs. 900 Crore** (Enhanced from Rs. 500 Crore) |
| **Rating Date** | September 26, 2025 |

---

## Detailed Rationale

Crisil Ratings has reaffirmed its `'Crisil AA-/Stable/Crisil A1+'` ratings to the bank facilities of Kovai Medical Center and Hospital Ltd (KMCH). 

The rating reflects the company’s long industry vintage, extensive experience of the promoters, diversified revenue streams (Healthcare and Education), comfortable operating performance, and a strong financial risk profile. These strengths are partially offset by geographic concentration in revenue and exposure to regulatory risks.

**Analytical Approach:** Crisil Ratings has considered the standalone business and financial risk profiles of KMCH.

---

## Key Rating Drivers — Strengths

*   **Long vintage and extensive industry experience of the promoters:** 
    *   Incorporated in 1985; commenced operations in 1990 with flagship multispecialty hospital in Coimbatore.
    *   Setup of satellite centres in Coimbatore (City Center, Sulur Hospital, Kovilpalayam Hospital) and Erode (Erode Speciality Hospital).
    *   Established KMCH Institute of Health Sciences & Research (Medical College) during 2019-2020.
    *   Promoters (Dr Nalla G Palaniswami and Dr Thavamani Devi Palaniswami) possess over four decades of healthcare sector experience.
*   **Diversified revenue streams and comfortable operating performance:** 
    *   Revenue stream diversified across Healthcare (~93%) and Education (~7%) sectors in Fiscal 2025.
    *   Operates for over three decades servicing urban/rural patients in Tamil Nadu and Kerala.
    *   Recognized forerunner in transplant and gynecology surgeries.
    *   Inaugurated IceCure cancer treatment option (3rd in India, 1st in South India) in fiscal 2023.
    *   Operating performance was 27-29% in the last three years ending fiscal 2025; Return on Capital Employed (ROCE) was healthy at ~23% in fiscal 2025.
*   **Strong financial risk profile:** 
    *   Supportive sizeable net worth of **Rs 1086 crore**.
    *   Comfortable gearing of **0.35 times** as on March 31, 2025.
    *   Improved interest coverage ratio of around **10.8 times** in fiscal 2025 (vs 6.44 times in fiscal 2023).
    *   Total Debt to EBITDA less than **1 time** as on March 31, 2025.

---

## Key Rating Drivers — Weaknesses

*   **Geographic concentration in revenue:** 
    *   High reliance on the flagship hospital (contributed **77%** revenue in fiscal 2025).
    *   Revenue from Coimbatore region contributes around **90%**.
    *   Peripheral centers are smaller; dependency on Coimbatore likely remains key driver over the medium term until the planned Chennai hospital expansion reduces it.
*   **Exposure to regulatory risk:** 
    *   Exposure to private hospital regulations impacting pricing (e.g., price caps on cardiac stents/knee implants in FY17).
    *   Challenges regarding cash transaction caps introduced in FY18.
    *   Monitorable risk regarding Supreme Court proposals to standardize prices across public and private hospitals.

---

## Liquidity

*   **Assessment:** **Strong**
*   **Cash Reserves:** Cash, bank balance, and fixed deposits stood at around **Rs. 270 crores** as on March 31, 2025.
*   **Working Capital Cycle:** Healthy liquidity supported by negative working capital cycle; barely used working capital limit for the 12 months through July 2025.
*   **Debt Servicing:** Annual accrual of over **Rs. 330-450 crores** is sufficient to meet debt obligations of Rs. 30-60 crores over the medium term.
*   **Dividend Policy:** Unlikely to pay major dividends over the medium term; cash flow expected to be reinvested to fund growth.
*   **Flexibility:** Low gearing supports flexibility to withstand adverse conditions or downturns.

---

## Outlook & Rating Sensitivity

*   **Outlook:** **Stable**
    *   Crisil believes KMCH will continue to benefit from its established presence in Coimbatore and healthy operating efficiency while maintaining financial prudence.

*   **Upward Factors:**
    *   Steady revenue growth and stable healthy operating margin (>25%) leading to higher cash accrual.
    *   Geographical diversification in the hospital business while maintaining a strong financial risk profile.

*   **Downward Factors:**
    *   Sluggish revenue growth or decline in operating margins leading to lower net cash accrual.
    *   Additional large debt-funded capex or acquisitions weakening key credit metrics (Total Debt to EBITDA ratio exceeding **2.25 times**).

---

## Key Financial Indicators

*(Values in Rs. Crore unless stated otherwise)*

| Key Indicator | FY 2025 (Mar 31) | FY 2024 (Mar 31) |
| :--- | :--- | :--- |
| **Operating Income** | 1,373.52 | 1,223.06 |
| **Reported Profit After Tax** | 208.95 | 179.73 |
| **PAT Margins** | 15.21% | 14.70% |
| **Adjusted Debt / Adjusted Net Worth** | 0.35 Times | 0.31 Times |
| **Interest Coverage Ratio** | 10.80 Times | 9.53 Times |

*Note: Figures are based on Crisil-Adjusted Values.*

---

## Bank Facilities

*(Breakup of Rated Facilities)*

| Facility Type | Amount (Rs. Crore) | Lender | Assigned Rating |
| :--- | :--- | :--- | :--- |
| **Non-Fund Based (ST)** ||||
| Bank Guarantee | 15.00 | Indian Bank | Crisil A1+ |
| Inland/Import Letter of Credit | 100.00 | Indian Bank | Crisil A1+ |
| Secured Overdraft Facility | 15.00 | Indian Bank | Crisil A1+ |
| **Fund Based (LT/ST)** ||||
| Proposed Long Term Bank Loan Facility | 350.00 | Not Applicable | Crisil AA-/Stable |
| Proposed Term Loan | 9.15 | Not Applicable | Crisil AA-/Stable |
| Term Loan | 119.95 | Indian Overseas Bank | Crisil AA-/Stable |
| Term Loan | 140.90 | Indian Bank | Crisil AA-/Stable |
| Term Loan | 100.00 | Indian Bank | Crisil AA-/Stable |
| Term Loan | 50.00 | Indian Bank | Crisil AA-/Stable |
| **Total** | **900.00** | | |

---

## Company & Subsidiaries

*   **Entity Name:** Kovai Medical Center and Hospital Limited (KMCH)
*   **Incorporation:** 1985
*   **Operations Commenced:** 1990
*   **Promoters:** 
    *   Dr Nalla G Palaniswami
    *   Dr Thavamani Devi Palaniswami
*   **Flagship Asset:** 854-bed multispecialty hospital in Coimbatore.
*   **Satellite Centres:**
    *   **Coimbatore:** City Center, Sulur Hospital, Kovilpalayam Hospital
    *   **Erode:** Erode Speciality Hospital
*   **Education Arm:** KMCH Institute of Health Sciences & Research (Established 2019-20). Offers MBBS degree course with annual intake of 150 students alongside a 750-bed medical college hospital.
*   **Listing Status:** Shares listed on the Bombay Stock Exchange (BSE).
*   **Consolidated Entities:** Includes the hospital network and the Medical College entity as described in the "About the Company" section.