Here's a thinking process that leads to the suggested markdown report:

1.  **Understand the Goal:** The user wants me to act as an equity analyst extracting credit rating report information from raw text (which is scraped from an HTML page). I need to structure this into a well-organized Markdown report following specific sections provided in the prompt.

2.  **Analyze the Input Data:**
    *   **Source:** Raw text from a Crisil Ratings credit rating rationale document.
    *   **Subject:** Muthoot Finance Limited.
    *   **Date:** March 24, 2026.
    *   **Key Information Available:** Rating actions (assignments, reaffirmations, withdrawals), financial data (AUM, profitability, gearing, etc.), strengths/weaknesses, liquidity, outlook, subsidiaries, bank facilities (mentioned but details in annexure), ESG info, company background.
    *   **Formatting Issues:** The raw text has some OCR-like errors (e.g., "Rs 1 2 ,000", "Y o Y (%)", broken lines). I need to clean these up while maintaining accuracy.

3.  **Map Input to Required Sections:**

    *   **## Rating Action:** Needs Rating, Outlook, Date, Agency, Total Facilities Rated.
        *   *Agency:* Crisil Ratings.
        *   *Date:* March 24, 2026.
        *   *Rating:* Crisil AA+/Stable (assigned/reaffirmed) for NCDs. A1+ for CP. PPMLD AA+/Stable.
        *   *Facilities:* Need to summarize the total value or list key ones based on the "Details of Instrument" table and summary. The prompt asks for "total facilities rated". Looking at the text, it lists many instruments. I will aggregate the main categories or highlight the largest recent action (Rs. 12,000 Crore NCDs assigned).
    *   **## Detailed Rationale:** Summary paragraph explaining decision.
        *   *Content:* Ability to profitably scale gold loans, strong market position, offset by geographical concentration and non-gold asset quality challenges.
    *   **## Key Rating Drivers — Strengths:** List strengths with data.
        *   *Strengths:* Track record/brand, Strong capitalization, High profitability (RoMA).
        *   *Data:* Branch count, Net worth, Gearing, RoMA % figures.
    *   **## Key Rating Drivers — Weaknesses:** List weaknesses with data.
        *   *Weaknesses:* Geographical concentration, Asset quality in non-gold segments (MF/Housing).
        *   *Data:* South India branch %, NPAs in MF/House finance.
    *   **## Liquidity:** Assessment, cash accruals, bank limits.
        *   *Content:* Standalone liquidity balance Rs 14971 crore (Jan 2026), coverage ratio 1.23x. Fundraising activity mentioned.
    *   **## Outlook & Rating Sensitivity:** Outlook statement, Up/Down factors.
        *   *Outlook:* Stable.
        *   *Factors:* Market position/Growth vs. Non-gold asset quality/Capital erosion.
    *   **## Key Financial Indicators:** Table if tabular data exists.
        *   *Data:* There are two tables (Standalone and Consolidated) covering 9 months FY2026, FY2025, FY2024. I should combine or present them clearly.
    *   **## Bank Facilities:** Bank-wise breakup as a markdown table.
        *   *Note:* The text says "Refer to Annexure for Details of Instruments & Bank Facilities". However, looking closely at the provided text, there is *no* specific table listing bank names and facility amounts in the "Annexure - Details of Instrument(s)" section provided in the prompt. It lists ISINs, Coupon Rates, and Maturity dates. It mentions "Bank loans" generally in the text ("raised around Rs.48,887 crore of funds from bank loans...").
        *   *Action:* Since the specific bank-wise breakup isn't explicitly detailed in the text (only referenced as existing), I must state that specific bank-wise details are not provided in this excerpt or summarize the general fund-raising mention. *Correction:* I should check if I missed a table. Scanning the text... "Annexure - Details of Instrument(s)" has no bank names. "Bank-wise breakup as a markdown table" is a requirement. I cannot invent data. I will note that specific bank-wise details are not detailed in the provided text but summarize the overall fundraising context found under Liquidity. *Wait, re-reading the prompt requirements:* "Structure this into a well-organized markdown report." If the data isn't there, I shouldn't hallucinate. I will create the table header but indicate the specific breakdown is unavailable in the source text, OR simply omit it if strictly forbidden to add external info. Better approach: Summarize the available debt instrument info which acts as the funding mix. Actually, the prompt asks me to extract *from raw text*. If the text doesn't have the bank list, I can't make the table complete. I will add a note or leave it blank with a description.
        *   *Re-evaluation:* The text *mentions* "Refer to Annexure for Details of Instruments & Bank Facilities" but the provided text cuts off or doesn't include a separate bank facility table, only Instrument details. I will populate what is available (Instruments acting as facilities) and add a disclaimer.
        *   *Decision:* I will create a section for Debt Facilities based on the "Annexure - Details of Instrument(s)" since those represent the rated liability facilities.
    *   **## Company & Subsidiaries:** Info + Consolidated entities.
        *   *Info:* NBFC, Est 1997/2008, Gold financing.
        *   *Subsidiaries:* Muthoot Homefin, Belstar Microfinance, Muthoot Money.

4.  **Drafting the Content (Iterative refinement):**

    *   *Cleaning:* Fix "Rs 1 2 ,000" -> "Rs 12,000". Fix "Y o Y" -> "YoY". Fix "20.27% as on December 31, 2025".
    *   *Tables:* Ensure Markdown syntax is correct. Align columns properly.
    *   *Tone:* Professional analyst tone.
    *   *Check Date:* Current date in text is March 2026 (Future date relative to now, but consistent within the text). I will maintain the text's date context.

5.  **Review against Constraints:**
    *   Did I miss any sections? No.
    *   Is it Markdown? Yes.
    *   Are the data points accurate to the text? Yes.
    *   Bank Facilities: Since the text does not contain a specific breakdown of *banks* (HDFC, SBI, etc.) vs just total debt types, I cannot generate a true "Bank-wise breakup" table. I will explicitly state "Not specified in provided text" or use the "Debt Instruments" table as a proxy for funded liabilities if appropriate, but strictly speaking, it's not a bank breakup. I will label the section carefully to reflect the available data (Funded Liabilities/Instruments). *Self-Correction:* The prompt asks me to organize the *provided raw text*. If the raw text lacks the bank names, I shouldn't pretend they are there. I will add a note in that section explaining the limitation based on the input.

6.  **Final Polish:** Check formatting headers, bold text for emphasis, and ensure readability. (Ensure the distinction between Standalone and Consolidated financials is clear).

7.  **Final Output Generation** (Proceeding to generate response based on these steps).
</think>

# Credit Rating Report: Muthoot Finance Limited

## Rating Action

| Detail | Description |
| :--- | :--- |
| **Agency** | Crisil Ratings Limited |
| **Date** | March 24, 2026 |
| **Company** | Muthoot Finance Limited |
| **Primary Rating** | **Crisil AA+/Stable** |
| **Total Facilities Rated** | Multiple debt instruments including Non Convertible Debentures (NCDs), Subordinated Debt, Commercial Papers (CP), and Principal Protected Market Linked Debentures (PPMLDs). |
| **Major Recent Assignment** | Rs. 12,000 Crore NCDs assigned at 'Crisil AA+/Stable'. |
| **Other Active Ratings** | • Rs. 13,200 Crore NCDs (Reaffirmed)<br>• Rs. 9,000 Crore Commercial Paper ('Crisil A1+')<br>• Rs. 76.3 Crore NCDs (Reduced)<br>• Various other NCD and Subordinated Debt tranches reconfirmed. |
| **Withdrawn Instruments** | Several redeemed Secured Redeemable NCDs and PPMLDs withdrawn (Total approx. Rs. 2,181+ Crore). |

---

## Detailed Rationale

Crisil Ratings has assigned its **'Crisil AA+/Stable'** rating to Rs 12,000 crore Non-Convertible Debentures of Muthoot Finance Ltd (Muthoot Finance) and reaffirmed ratings on other debt instruments at **'Crisil AA+/Crisil PPMLD AA+/Stable/Crisil A1+'**. The ratings continue to factor in the company’s demonstrated ability to profitably scale its core gold loan business while maintaining a strong financial risk profile. This assessment is bolstered by the company's strong market position within the Indian gold loan segment, supported by promoter experience spanning over eight decades.

However, these strengths are partially offset by **geographical concentration** in operations (primarily South India) and **asset quality challenges** relating to non-gold loan segments, specifically microfinance. As of December 2025, consolidated loan AUM grew 48% YoY to Rs 1,64,720 Crore. Despite this growth, the management continues to prioritize the gold loan segment (~90% of portfolio) while monitoring the diversification efforts into microfinance and housing finance.

---

## Key Rating Drivers — Strengths

*   **Established Track Record and Brand Name:**
    *   Operates in the gold financing industry for 85 years (promoter family involvement since 1939).
    *   Extensive operational base with **over 7,541 branches across India** (6,007 offering gold loans).
    *   Leadership position among NBFCs in gold lending supported by diverse geographies.
    *   Active borrowers crossed **65.3 lakh** as of Dec 2025; loan accounts increased to **1.06 Crore**.

*   **Strong Capitalisation:**
    *   Consolidated net worth of **Rs 35,624 Crore** as of December 31, 2025.
    *   Low leverage with consolidated gearing at **3.9 times** (Dec 2025).
    *   Standalone Tier I capital adequacy ratio remains comfortable at **20.27%** (Dec 2025).
    *   Internal cash generation supports prudent capitalization of subsidiaries.

*   **Profitability Among the Best in Industry:**
    *   Consolidated Return on Managed Assets (RoMA) stood at **6.1%** for nine months of fiscal 2026 (annualized).
    *   Driven by high interest margins, operational efficiency, and low credit losses.
    *   Stage III assets reduced to **1.6%** as of Dec 31, 2025.
    *   Consolidated credit costs annualized remained within **1.5%**.

---

## Key Rating Drivers — Weaknesses

*   **Geographical Concentration & Low Market Presence in Non-Gold:**
    *   Operations exhibit regional concentration: **57% of branches in South India** (Dec 2025).
    *   Gold loan portfolio concentration in South region reduced to **49%** (from 86% in 2007), but still significant.
    *   Vulnerable to economic/social/political disruptions in the home region.
    *   Share of non-gold loan segments remains low despite diversification attempts.

*   **Asset Quality Challenges in Non-Gold Segments:**
    *   **Microfinance:** Gross NPAs (90+ dpd) stood at **4.93%** as of Dec 31, 2025 (Belstar Microfinance).
    *   **Housing Finance:** Gross NPAs in range of **1.2–2.3%** last 1-2 years. Targets self-employed/unorganised sector clients.
    *   **Vehicle Finance:** Focus shifted back to gold loans due to past asset quality issues.
    *   External risks such as local elections and borrower protests impact the microfinance model.

---

## Liquidity

*   **Assessment:** **Strong**.
*   **Liquidity Balance:** Standalone liquidity balance was **Rs 14,971 Crore** as on January 31, 2026.
*   **Debt Obligation Coverage:** Liquidity cover for debt obligations arising over the following 2 months was at **1.23 times** (excluding rollovers and incremental collections).
*   **Balance Sheet Management:** Maintains about **5-8%** of its balance sheet as a liquidity balance over the last 4-5 quarters.
*   **Fund Raising:** Raised approximately **Rs 48,887 Crore** via bank loans, NCDs, and ECBs since April 2025 at competitive rates.

---

## Outlook & Rating Sensitivity

### Outlook Statement
**Stable**
The stable outlook reflects expectations that Muthoot Finance will sustain its strong capitalisation and healthy profitability. Asset quality in the dominant gold loan business is expected to remain sound due to high liquidity of security and frequent interest collections. Maintenance of asset quality and profitability alongside growth in non-gold segments remains monitorable.

### Rating Sensitivity Factors

| **Upward Factors** | **Downward Factors** |
| :--- | :--- |
| • Continued strong market position in gold finance.<br>• Increasing diversity in Loan AUM and geographical reach.<br>• Sustenance of profitability with RoMA above **5%** on steady state basis. | • Significant/sustained deterioration in asset quality of **non-gold businesses** affecting earnings.<br>• Moderation in capital position: Tier I capital adequacy declining below **15%**. |

---

## Key Financial Indicators

### Consolidated Basis
*(Figures in ₹ Crores unless specified)*

| Parameter | Nine Months FY2026<br>(Dec-25) | Fiscal 2025<br>(Mar-25) | Fiscal 2024<br>(Mar-24) |
| :--- | :--- | :--- | :--- |
| **Total Managed Assets** | 180,234 | 132,860 | 96,469 |
| **Total Income** | 22,057 | 20,324 | 15,163 |
| **Profit After Tax** | 7,209 | 5,352 | 4,468 |
| **Gearing (Times)** | 3.9 | 3.4 | 2.7 |
| **Return on Managed Assets** | 6.1%* | 4.7% | 5.1% |

### Standalone Basis
*(Figures in ₹ Crores unless specified)*

| Parameter | Nine Months FY2026<br>(Dec-25) | Fiscal 2025<br>(Mar-25) | Fiscal 2024<br>(Mar-24) |
| :--- | :--- | :--- | :--- |
| **Total Managed Assets** | 165,584 | 121,248 | 85,028 |
| **Total Income** | 19,444 | 17,156 | 12,694 |
| **Profit After Tax** | 7,048 | 5,200 | 4,050 |
| **Gross NPA (%)** | 1.6% | 3.4% | 3.3% |
| **Gearing (Times)** | 3.7 | 3.2 | 2.4 |
| **Return on Managed Assets** | 6.6%* | 5.1% | 5.1% |

*\*On an annualized basis*

---

## Bank Facilities

*Note: Specific bank-wise breakups are not detailed in the provided text. The following table summarizes the major rated funding instruments disclosed in the Annexure.*

| Instrument Type | Issue Size (₹ Crore) | Complexity Level | Current Rating |
| :--- | :--- | :--- | :--- |
| **Non Convertible Debentures** | 12,000 (Assigned) / Various others (Total > 50k) | Simple / Complex | Crisil AA+/Stable |
| **Commercial Paper** | 9,000 | Simple | Crisil A1+ |
| **Subordinated Debt** | ~700 | Complex | Crisil AA+/Stable |
| **Principal Protected Mkt Linked Deb.** | ~612.7 (Reaffirmed) | Highly Complex | Crisil PPMLD AA+/Stable |

*Additional funds raised post-April 2025 included bank loans and ECBS totaling ~Rs 48,887 Crore.*

---

## Company & Subsidiaries

### Company Overview
*   **Entity:** Muthoot Finance Limited (NBFC).
*   **Setup:** Originally private limited (1997); Public limited (Nov 2008).
*   **Business:** Provides finance against used household gold jewellery.
*   **Promoter History:** Family involved in business since 1939 (over 80 years).
*   **Group Affiliation:** Flagship company of Muthoot Group (operations in hospitality, healthcare, IT, FX, insurance, etc.).

### Consolidated Entities
The analytical approach combines business and financial risk profiles of the following fully consolidated subsidiaries:

| Entity Name | Extent of Consolidation |
| :--- | :--- |
| Muthoot Homefin (India) Ltd | Full Subsidiary |
| Belstar Microfinance Private Limited | Full Subsidiary |
| Muthoot Money Limited | Full Subsidiary |