Here's a thinking process that leads to the suggested output:

1.  **Analyze the Request:**
    *   **Role:** Equity Analyst.
    *   **Task:** Extract credit rating report information from raw text and structure it into a well-organized markdown report.
    *   **Required Sections:** Rating Action, Detailed Rationale, Key Rating Drivers (Strengths & Weaknesses), Liquidity, Outlook & Rating Sensitivity, Key Financial Indicators, Bank Facilities, Company & Subsidiaries.
    *   **Input Data:** A raw text dump from a CRISIL Ratings webpage (Rating Rationale for Kovai Medical Center and Hospital Limited).

2.  **Scan and Extract Information (Section by Section):**

    *   **Header Info:** Date (January 08, 2025), Location (Mumbai), Company Name (Kovai Medical Center and Hospital Limited), Agency (CRISIL Ratings Limited).
    *   **Rating Action:**
        *   Long Term: CRISIL AA-/Stable (Reaffirmed).
        *   Short Term: CRISIL A1+ (Reaffirmed).
        *   Date: January 08, 2025.
        *   Total Bank Loan Facilities Rated: Rs. 500 Crore (Enhanced from Rs. 400 Crore).
        *   Rating Type: Reaffirmed + Enhanced Amount.
    *   **Detailed Rationale:**
        *   Summary: Reaffirmed 'CRISIL AA-/Stable/CRISIL A1+' on bank loan facilities. Reflects long vintage, promoter experience, diversified revenue (healthcare + education), comfortable operating performance, strong financial risk. Offset by geographic concentration and regulatory risks.
    *   **Key Rating Drivers — Strengths:**
        1.  *Long vintage & experience:* Incorporated 1985, ops since 1990. Flagship multispecialty hospital in Coimbatore + satellite centers. Promoters have 40+ years exp.
        2.  *Diversified revenue & operating performance:* Healthcare (~92%) + Education (~8%) of total FY24 revenue. Operating performance 27-29% last 3 years. ROCE >20% in FY24. New cancer treatment IceCure.
        3.  *Strong financial risk profile:* Networth Rs 973 Cr (Sep 30, 2024). Gearing 0.40x. Interest coverage 9.53x (FY24) vs 6.44x (FY23). Net cash accrual to adjusted debt 0.95x (FY24) vs 0.42x. Debt to EBITDA <1x (Mar 31, 2024).
    *   **Key Rating Drivers — Weaknesses:**
        1.  *Geographic concentration:* ~75% revenue from flagship hospital (FY24). ~90% revenue from Coimbatore. Peripheral centers are smaller. Plan for Chennai hospital might reduce this later.
        2.  *Regulatory risk:* Price caps on stents/knee implants impacted past private hospitals. Cash transaction caps challenged liquidity. SC proposal on price standardization monitorable.
    *   **Liquidity:**
        *   Status: Strong.
        *   Cash/Bank/FD: ~Rs 250 Cr (Sep 30, 2024).
        *   Working Capital: Barely used limit due to negative working capital cycle.
        *   Accruals: Over Rs 300 Cr annually sufficient for debt obligations (Rs 30-40 Cr) and capex.
        *   Dividends: Unlikely to pay over medium term; cash flows reinvested.
        *   Flexibility: Low gearing supports flexibility against downturns.
    *   **Outlook & Rating Sensitivity:**
        *   Outlook: Stable. Belief KMCH will benefit from established presence in Coimbatore, healthy efficiency, and financial prudence.
        *   Upward Factors: Steady revenue growth, stable margins (>25%), higher cash accrual, geographical diversification while maintaining financial risk.
        *   Downward Factors: Sluggish growth or margin decline leading to net cash accrual issues. Large debt-funded capex/acquisition weakening metrics (Debt/EBITDA > 2.25x).
    *   **Key Financial Indicators:** (Need table)
        *   Source: "As on / for the period ended March 31" section.
        *   Years: 2024, 2023.
        *   Metrics: Op Income, PAT, PAT Margin, Adj Debt/Adj Networth, Interest Coverage.
    *   **Bank Facilities:** (Need table from "Annexure - Details of Bank Lenders & Facilities")
        *   Columns: Facility Type, Amount (Rs Cr), Name of Lender, Rating.
        *   Note: Some proposed loans list lender as "Not Applicable" in the specific annexure, but I should transcribe exactly what is there. Wait, checking the Annexure table provided in text...
        *   Actually, the text has "Annexure - Details of Bank Lenders & Facilities". It lists facility, amount, lender, rating.
    *   **Company & Subsidiaries:**
        *   Incorporation: 1985.
        *   Operations: 854-bed multispecialty hospital in Coimbatore. Satellite centers (City Center, Sulur, Kovilpalayam, Erode). Medical college (2019-2020).
        *   Promoters: Dr Nalla G Palaniswami and Dr Thavamani Devi Palaniswami.
        *   Listing: Bombay Stock Exchange (BSE).
        *   Consolidated entities: Not explicitly detailed in the text, but mentions "Group" in weaknesses section and "Annexure - Rating History" implies consolidated view usually. The prompt asks for "consolidated entities" if available. The text mentions "KMCH" mostly. It says "The company also started a medical college...". I will extract what is explicitly stated about the entity structure.

3.  **Drafting the Content (Iterative refinement):**

    *   *Formatting:* Use Markdown headers (`##`, `###`), bullet points (`-`), and tables (`|`).
    *   *Accuracy:* Ensure numbers match exactly (e.g., Rs 500 Crore rated amount, 2024 vs 2023 figures).
    *   *Tone:* Professional analyst tone.
    *   *Cleaning:* Remove boilerplate legal disclaimers, contact info, and footer links unless relevant to the specific sections requested (e.g., Agency Name).
    *   *Financial Table:* Align columns properly.
    *   *Bank Facilities Table:* Combine the "Annexure - Details of Instrument(s)" data with "Annexure - Details of Bank Lenders & Facilities" where applicable to make the Bank Facilities section robust. The prompt specifically asks for "Bank-wise breakup as a markdown table". The "Annexure - Details of Bank Lenders & Facilities" is the most direct source for *Bank* breakdown. The other annexure is "Details of Instrument(s)" which includes letters of credit etc. I will prioritize the Bank Lenders annexure for the Bank Facilities section as per instruction.

4.  **Review against Constraints:**
    *   Did I include all required sections? Yes.
    *   Is it markdown? Yes.
    *   Are tables formatted correctly? Yes.
    *   Is the data accurate to the source text? Yes.

5.  **Final Polish:** Check for readability and logical flow. Ensure dates are clear. (Self-Correction: Make sure to distinguish between FY end dates like March 31 vs Reporting dates like Sep 30).

    *   *Correction on Bank Facilities:* The text provides an "Annexure - Details of Bank Lenders & Facilities". I will use that for the Bank Facilities section.
    *   *Correction on Financials:* The table provided in text is clearly under "Key Financial Indicators". I will replicate that.

6.  **Final Output Generation** (Proceed to generate response based on these steps).
</think>

# Credit Rating Report: Kovai Medical Center and Hospital Ltd (KMCH)

**Date:** January 08, 2025  
**Agency:** CRISIL Ratings Limited (A subsidiary of CRISIL Limited, S&P Global)  
**Location:** Mumbai

---

## Rating Action

| Component | Details |
| :--- | :--- |
| **Long-Term Rating** | CRISIL AA- / Stable (**Reaffirmed**) |
| **Short-Term Rating** | CRISIL A1+ (**Reaffirmed**) |
| **Total Bank Loan Facilities Rated** | Rs. 500 Crore *(Enhanced from Rs. 400 Crore)* |
| **Action** | Reaffirmation with enhancement of rated amount |
| **Reporting Date** | January 08, 2025 |

---

## Detailed Rationale

CRISIL Ratings has reaffirmed its ratings on the bank loan facilities of Kovai Medical Center and Hospital Ltd (KMCH). The ratings reflect the company's long operational vintage, extensive industry experience of promoters, diversified revenue streams (healthcare and education), comfortable operating performance, and a strong financial risk profile. These strengths are partially offset by geographic concentration in revenue and exposure to regulatory risks.

---

## Key Rating Drivers — Strengths

*   **Long Vintage and Extensive Industry Experience:**
    *   KMCH was incorporated in 1985 and commenced operations in 1990.
    *   Flagship multispecialty hospital located in Coimbatore.
    *   Satellite centres established in Coimbatore (City Center, Sulur Hospital, Kovilpalayam Hospital) and Erode (Erode Speciality Hospital).
    *   Started a medical college (KMCH Institute of Health Sciences & Research) during 2019-2020.
    *   Promoters (Dr. Nalla G Palaniswami and Dr. Thavamani Devi Palaniswami) possess over four decades of healthcare sector experience.
*   **Diversified Revenue Streams and Operating Performance:**
    *   Revenue split across Healthcare (~92%) and Education (~8%) in Fiscal 2024.
    *   Serviced patients across Tamil Nadu and Kerala.
    *   Recognized as a forerunner in transplant and gynaecology surgeries.
    *   Inaugurated 'IceCure' cancer treatment option in Fiscal 2023 (First in South India).
    *   Operating performance maintained at 27-29% over the last three years.
    *   Return on Capital Employed (ROCE) healthy at >20% in Fiscal 2024.
*   **Strong Financial Risk Profile:**
    *   Sizeable Net Worth: Rs 973 crore (as of September 30, 2024).
    *   Comfortable Gearing: 0.40 times (as of September 30, 2024).
    *   Improved Debt Protection Metrics: Interest Coverage Ratio improved to ~9.53 times in FY24 from ~6.44 times in FY23.
    *   Net Cash Accrual to Adjusted Debt: 0.95 times in FY24 (vs 0.42 times in FY23).
    *   Low Leverage: Total Debt to EBITDA ratio <1 time as on March 31, 2024 (down from 1.64 times in FY23).

---

## Key Rating Drivers — Weaknesses

*   **Geographic Concentration in Revenue:**
    *   High reliance on flagship hospital contributing ~75% of revenue in Fiscal 2024.
    *   Coimbatore accounts for around 90% of total revenue.
    *   While peripheral centers are expanding, the flagship remains the key profitability driver in the medium term due to smaller scale of satellites.
*   **Exposure to Regulatory Risks:**
    *   Vulnerable to government regulations impacting private hospitals (e.g., price caps on cardiac stents and knee implants in late FY2017).
    *   Temporary challenges faced during introduction of cash transaction caps (up to Rs 2 lakh) in FY2018.
    *   Monitoring required on Supreme Court proposals to standardize prices across public and private hospitals.

---

## Liquidity

*   **Assessment:** **Strong**.
*   **Cash Reserves:** Cash, bank balances, and fixed deposits stand at around Rs 250 crore as of September 30, 2024.
*   **Working Capital:** Barely utilized working capital limits over the last 12 months through November 2024 due to a negative working capital cycle.
*   **Cash Accruals:** Annual accrual of over Rs 300 crore is expected to be sufficient to meet debt obligations (Rs 30-40 crore over medium term) and capital expenditure.
*   **Dividend Policy:** Unlikely to declare dividends over the medium term; cash flows expected to be reinvested to fund growth.
*   **Financial Flexibility:** Low gearing supports flexibility to withstand adverse business conditions or downturns.

---

## Outlook & Rating Sensitivity

**Outlook:** Stable

CRISIL Ratings believes KMCH will continue to benefit from its established presence in Coimbatore and healthy operating efficiency. The company is expected to maintain financial prudence and sustain healthy credit metrics while pursuing growth.

### Sensitivity Factors

| Direction | Factors |
| :--- | :--- |
| **Upward** | • Steady revenue growth and stable healthy operating margin (>25%) leading to higher cash accrual.<br>• Geographical diversification in hospital business while maintaining a strong financial risk profile. |
| **Downward** | • Sluggish revenue growth or decline in operating margin leading to reduced net cash accrual.<br>• Addition of large debt-funded capex or acquisition weakening key credit metrics (specifically Debt-to-EBITDA > 2.25 times). |

---

## Key Financial Indicators

| Particulars | Unit | FY 2024 | FY 2023 |
| :--- | :--- | :--- | :--- |
| Operating income | Rs. Crore | 1,219.55 | 1,019.74 |
| Reported profit after tax (PAT) | Rs. Crore | 179.73 | 115.77 |
| PAT margin | % | 14.49 | 11.18 |
| Adjusted debt / Adjusted networth | Times | 0.31 | 0.66 |
| Interest coverage | Times | 9.53 | 6.44 |

*Note: Data as on / for the period ended March 31.*

---

## Bank Facilities

| Facility Type | Amount (Rs. Crore) | Name of Lender | Rating Assigned |
| :--- | :--- | :--- | :--- |
| Bank Guarantee | 15.00 | Indian Bank | CRISIL A1+ |
| Inland/Import Letter of Credit | 100.00 | Indian Bank | CRISIL A1+ |
| Proposed Term Loan | 9.15 | Not Applicable | CRISIL AA-/Stable |
| Proposed Term Loan | 50.00 | Not Applicable | CRISIL AA-/Stable |
| Secured Overdraft Facility | 15.00 | Indian Bank | CRISIL A1+ |
| Term Loan | 119.95 | Indian Overseas Bank | CRISIL AA-/Stable |
| Term Loan | 140.90 | Indian Bank | CRISIL AA-/Stable |
| Term Loan | 50.00 | Indian Bank | CRISIL AA-/Stable |

---

## Company & Subsidiaries

*   **Company Name:** Kovai Medical Center and Hospital Limited
*   **Incorporation Year:** 1985
*   **Commencement of Operations:** 1990
*   **Listing:** Bombay Stock Exchange (BSE)
*   **Promoters:**
    *   Dr. Nalla G Palaniswami
    *   Dr. Thavamani Devi Palaniswami
*   **Operations:**
    *   **Flagship:** 854-bed multispecialty hospital in Coimbatore.
    *   **Satellite Centres:** Coimbatore (City Center, Sulur Hospital, Kovilpalayam Hospital); Erode (Erode Speciality Hospital).
    *   **Education Segment:** KMCH Institute of Health Sciences & Research (started 2019-2020). Offers MBBS degree course with annual intake of 150 students along with a 750-bed medical college hospital.
*   **Consolidated Entities:** The rationale analyzes standalone business and financial risk profiles of KMCH. Specific names of subsidiaries are not listed separately beyond the institute mentioned above, but group level regulatory risks are monitored.