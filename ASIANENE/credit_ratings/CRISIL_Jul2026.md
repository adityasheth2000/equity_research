Here's a thinking process that leads to the suggested markdown report:

1.  **Analyze the Request:**
    *   **Role:** Equity Analyst extracting a credit rating report from raw text.
    *   **Task:** Structure the provided raw text into a well-organized markdown report.
    *   **Required Sections:**
        *   Rating Action
        *   Detailed Rationale
        *   Key Rating Drivers — Strengths
        *   Key Rating Drivers — Weaknesses
        *   Liquidity
        *   Outlook & Rating Sensitivity
        *   Key Financial Indicators (Markdown table)
        *   Bank Facilities (Bank-wise breakup as a markdown table)
        *   Company & Subsidiaries
    *   **Input Data:** A raw text scrape from a Crisil Ratings website (HTML converted to text).

2.  **Scan and Extract Information (Section by Section):**

    *   **Rating Action:**
        *   Agency: Crisil Ratings Limited
        *   Date: July 29, 2026 (Scraped text says "July 29, 2026 | Mumbai", also mentions dates in future relative to typical real-time, but I must stick to the text provided).
        *   Entity: Asian Energy Services Limited (AESL)
        *   Status: Ratings continue on 'Watch Developing'
        *   Long Term Rating: Crisil BBB+/Watch Developing
        *   Short Term Rating: Crisil A2/Watch Developing
        *   Regulator: RBI
        *   Total Bank Loan Facilities Rated: Rs.317.5 Crore (from "Total Bank Loan Facilities Rated" line)

    *   **Detailed Rationale:**
        *   Context: Continued watch status placed on Sept 09, 2025 due to merger announcement of parent (Oilmax Energy Pvt Ltd - OEPL) into AESL.
        *   Current Status: Board/Stock Exchange/Shareholder approval secured. NCLT final order pending. Hearing scheduled for August 07, 2026.
        *   Monitoring: Progress of merger will be monitored. Rating action post-completion upon gaining clarity on OEPL's performance.
        *   General Assessment: Strengths (presence, technical capability, diversified revenue, financial risk). Offsetting Weaknesses (working capital, regulatory susceptibility).

    *   **Key Rating Drivers — Strengths:**
        *   Longstanding presence, strong technical capabilities: 3-decade experience (Promoter Kapil Garg), reputed clientele (GAIL, ONGC, etc.), Revenue CAGR ~62% for 3 fiscals through 2025. Revenue Rs 453 Cr for 9 months ended Dec 31, 2025. Order book Rs 1,874 crore (Dec 31, 2025).
        *   Diversified revenue base: Moved from seismic to EPC (FY21) to O&M. Acquired Kuiper Group (H1 FY26) for manpower services in West Asia. Topline growth 81% (9M ended Dec 31, 2025 YoY).
        *   Comfortable capital structure: Networth Rs 443 crore (Sep 30, 2025). Gearing 0.24x (Sep 30, 2025). Interest coverage ratio 7.57 times (same period). Debt-funded capex/acquisition done in H1 FY26 but still healthy.

    *   **Key Rating Drivers — Weaknesses:**
        *   Working capital intensive: Gross Current Asset (GCA) Days 293 (Mar 31, 2025). Debtor days 284 (Sep 30, 2025). Inventory days reduced from 79 to 59 (Mar 2025 to Sep 2025). Estimates: Debtor days 170-190 by Mar 31, 2026.
        *   Susceptibility to government policy: Most revenue from oil/gas. Geopolitical/environmental/safety policies impact business risk.
        *   Funding reliance: WC requirements met by creditors and bank lines (Implied risk).

    *   **Liquidity:**
        *   Position: Adequate.
        *   Accruals vs Obligation: Estimated net cash accruals over Rs 84 Cr vs repayment obligations of Rs 24-25 Cr (FY 2027 onwards).
        *   Utilization: Fund-based limit ~56%. Non-fund-based limit ~76.25% (12 months through Feb 2026).
        *   Cash Reserves: Cash/Cash equivalents Rs 157 crore (Mar 31, 2026). Unencumbered portion Rs 92 crore.

    *   **Outlook & Rating Sensitivity:**
        *   Outlook: Watch Developing (Continues on 'Rating Watch with Developing Implications').
        *   Upward Factors: Sustained operation scale increase -> net cash accruals > Rs 80 Cr sustained. Improvement in working capital cycle (debtor days). Sustenance of financial risk profile.
        *   Downward Factors: Decline in scale/margin -> net cash accrual < Rs 50 Cr sustained. Further stretch in receivables (higher GCAs). Large debt-funded capex weakening financial risk profile.

    *   **Key Financial Indicators:**
        *   Source Table: "Key Financial Indicators (consolidated numbers)"
        *   Columns: Unit, 2025, 2024.
        *   Rows: Operating income (465.04, 465.04), PAT (42.04, 42.04), PAT margin (9.04%, 9.04%), Adjusted debt/networth (0.06, 0.06), Interest coverage (20.28, 20.28).
        *   *Correction/Observation:* The table shows identical figures for 2025 and 2024 which seems odd for growth, but I must transcribe what is in the text accurately. Wait, looking closer at the text: "2025 2024". Values are indeed identical in the snippet provided ("Operating income... 465.04 465.04"). This might be a typo in the source text or indicating stability, but as an analyst formatting the report, I should reflect the data provided. However, earlier text mentions revenue CAGR of 62% and growth of 81% in top-line for 9 months. The "Key Financial Indicators" table likely refers to audited numbers for March 31 years, while the rationale discusses specific periods (e.g., 9 months ended Dec 2025). I will use the table data provided under "Key Financial Indicators".

    *   **Bank Facilities:**
        *   Source: "Annexure - Details of Bank Lenders & Facilities"
        *   Need to aggregate by Bank Name.
        *   Union Bank of India: Bank Guarantee 100, Cash Credit 20. Total? Let's list breakdown per facility type per bank as requested "Bank-wise breakup". Or aggregate total per bank. Usually, a table showing Facility Type, Amount, Bank Name is best. Let's look at the instruction: "Bank-wise breakup as a markdown table". I will create a table grouping by Bank Name to show the breakup clearly.
        *   *Data Extraction:*
            *   Union Bank of India: BG 100 + CC 20 = 120
            *   Bank of Maharashtra: BG 20 + BG 40 + CC 10 + LTC 37.5 = 107.5
            *   Kotak Mahindra Bank: CC 10 + SLC 60 = 70
            *   Citi Bank: Fund-Based 15 + Fund-Based 5 = 20
            *   *Wait, check totals:* 120 + 107.5 + 70 + 20 = 317.5. Matches "Total Bank Loan Facilities Rated: Rs.317.5 Crore". Perfect.
            *   Format: Table columns: Bank Name, Facility Type, Amount (Rs. Crore), Rating.

    *   **Company & Subsidiaries:**
        *   Company Info: Asian Energy Services Limited (AESL). Promoter: Dr. Kapil Garg (MD). Listed on BSE & NSE. Activities: Geophysical seismic, drilling, EPC, O&M. Part of Asian group (subsidiary of OEPL).
        *   Consolidated Entities: Huge list in Annexure. I will summarize the main entities mentioned in the "Analytical Approach" section rather than listing every single one in a massive block if possible, but the prompt asks for "Company info, consolidated entities". A summary list or mentioning the count + key examples is better for readability, but ideally, I should capture the "Annexure - List of Entities consolidated" data somewhat concisely or list the main ones if the list is too long. Given the constraint to organize into sections, I will list the primary subsidiaries and mention the JVs/Step-down nature as per the text analysis section, then maybe summarize the Annexure list in a condensed format or list the major ones to keep the report clean, or list them all if strict extraction is required. *Decision:* The prompt says "Company & Subsidiaries - Company info, consolidated entities". I will provide the main description and list the consolidated entities mentioned in the "Analytical Approach" and "Annexure" sections, grouped logically (Main Subsidiaries, Step-down, JVs) to save space while remaining complete. Actually, listing the Annexure table content is probably safer for accuracy. I'll extract the key full consolidation entities from the Annexure table provided in the text.
        *   Wait, the text lists many entities in "Annexure - List of Entities consolidated". I will create a subsection for this within "Company & Subsidiaries".
        *   Joint Ventures listed in Analytical Approach: Zuberi Asian JV, AESL FFIL JV, Asian Indwell JV, Asian Oilmax JV.

3.  **Formatting and Review:**
    *   Use standard Markdown headers (`##`, `###`).
    *   Use tables where appropriate (`| | |`).
    *   Ensure dates and currency symbols are consistent.
    *   Check for any conflicting data (e.g., FY dates). The text uses "Fiscal 2026", "March 31 2025", "September 30 2025". I must preserve these exact labels as they appear in the source text (even if they seem futuristic relative to today's actual date, this is a simulation/scrape context).
    *   Double-check the "Total Facilities Rated" sum against the bank details sum (317.5).
    *   Ensure the distinction between Strengths and Weaknesses is clear.

4.  **Drafting the Content:** (Self-Correction during drafting)
    *   *Note on Dates:* The text explicitly mentions dates like "July 29, 2026". This suggests the text is from the future or a hypothetical scenario. I will not alter the dates, just report them as written.
    *   *Table Construction:* For the Bank Facilities, I need to ensure the math adds up visually or state the breakdown clearly.
    *   *Financial Indicators:* There is a discrepancy between the narrative (Revenue growing 81%) and the table (Operating Income identical 465.04 for 2025 and 2024). I will present the table exactly as shown in the text to maintain fidelity to the "scraped" source, as my role is extraction/formatting, not fact-checking the underlying finance theory.
    *   *Consolidated Entities:* There are too many to list exhaustively without making the report cluttered, but the prompt asks for "Company & Subsidiaries". I will categorize them based on the "Annexure - List of Entities consolidated" section provided in the text. I'll list the Full Subsidiaries separately from Proportionate Subsidiaries.

5.  **Final Polish:** Check markdown syntax. Ensure no HTML tags remain (like `<br>`, `&nbsp;`). Clean up whitespace artifacts (e.g., "step - down" -> "step-down").

**(Self-Correction on Bank Table):** The text lists "Fund-Based Facilities" twice for Citi (15 + 5). I will combine these or list distinct rows. Listing distinct rows per facility type is clearer.
**(Self-Correction on Financials):** The table header says "2025 2024". I will use those headers.

Let's assemble.

*Refining the Bank Breakup Table:*
Instruction: "Bank-wise breakup as a markdown table".
I will group by Bank Name, then list facilities within that bank to make it truly "bank-wise".
Or, simpler: Columns: Bank Name | Facility | Amount | Rating. This allows sorting by bank easily. I'll go with the latter for clarity as a general breakdown, or a summary per bank if "breakup" implies aggregation. I think a detailed list is safer for transparency. Let's do a table with Bank Name, Facility, Amount.

*Refining Companies/Subsidiaries:* I will list the Parent/Group structure first, then the main subsidiaries. I will condense the long list of entities from the annexure into bullet points grouped by region/type to make it readable, while keeping the data points accurate.

*Final check of the "Watch Developing":* The outlook is specifically "Watch Developing". I need to make sure this is prominent in the Rating Action and Outlook sections.

Okay, ready to generate.beat
</think>

# Credit Rating Report: Asian Energy Services Limited

## Rating Action

| Parameter | Details |
| :--- | :--- |
| **Agency** | Crisil Ratings Limited |
| **Date** | July 29, 2026 |
| **Location** | Mumbai |
| **Issuer** | Asian Energy Services Limited (AESL) |
| **Long Term Rating** | **Crisil BBB+** / Watch Developing |
| **Short Term Rating** | **Crisil A2** / Watch Developing |
| **Regulator** | Reserve Bank of India (RBI) |
| **Total Bank Loan Facilities Rated** | **Rs. 317.5 Crore** |
| **Current Status** | Ratings continued on 'Watch with Developing Implications' |

---

## Detailed Rationale

Crisil Ratings has maintained its ratings on the bank facilities of Asian Energy Services Limited (AESL; part of the Asian group) on a **“Watch Developing”** basis. 

The watch status was initially placed on September 09, 2025, following an announcement regarding the merger of AESL’s parent company, Oilmax Energy Pvt Ltd (OEPL), into AESL. While AESL has secured approvals from its Board, the Stock Exchange, and Shareholders, the final National Company Law Tribunal (NCLT) order remains pending, with a hearing scheduled for August 07, 2026. 

The agency will monitor the progress of the merger and intends to resolve the watch with appropriate rating action post-completion once there is clarity on OEPL's performance. The current ratings reflect AESL's longstanding presence, strong technical capabilities, diversified revenue streams, and comfortable financial risk profile. These strengths are partially offset by large working capital requirements and susceptibility to government regulations.

---

## Key Rating Drivers — Strengths

*   **Longstanding Presence & Technical Capabilities:**
    *   Benefits from three-decade experience of promoter Dr. Kapil Garg.
    *   Strong clientele comprising Gail India Ltd, ONGC Ltd, Oil India Ltd, Vedanta Ltd, Heavy Engineering Corporation, Singareni Coalfield Ltd, and Eastern Coalfield Ltd.
    *   **Revenue Growth:** Compound Annual Growth Rate (CAGR) of nearly **62%** for three fiscals through 2025. Group revenue was **Rs 453 Cr** for nine months ended December 31, 2025.
    *   **Order Book:** Healthy unexecuted order book of **Rs 1,874 Crore** as on December 31, 2025, ensuring adequate revenue visibility.
*   **Diversified Revenue Base:**
    *   Expanded beyond the seismic segment into Engineering, Procurement and Construction (EPC) operations (Fiscal 2021) and Operations and Maintenance (O&M).
    *   Acquired the **Kuiper Group** in the first half of Fiscal 2026 to provide manpower services to the West Asia energy sector.
    *   **Growth:** Top-line growth of **81%** during the nine months ended December 31, 2025, compared to the corresponding period last year.
*   **Comfortable Capital Structure:**
    *   Healthy net worth of **Rs 443 Crore** as on September 30, 2025.
    *   Moderate debt levels resulting in a gearing ratio of **0.24 times** as on September 30, 2025, despite debt-funded capex and acquisition activity.
    *   Strong interest coverage ratio at **7.57 times** for the same period.

## Key Rating Drivers — Weaknesses

*   **Working Capital Intensive Nature:**
    *   Reflected in **293 Gross Current Asset (GCA) Days** as on March 31, 2025.
    *   High debtor days stood at **284 days** as on September 30, 2025 (Estimated to reduce to range of 170-190 days by March 31, 2026).
    *   Inventory days reduced from 79 days (March 31, 2025) to 59 days (September 30, 2025).
    *   Working capital requirements are primarily met via creditors and bank lines.
*   **Susceptibility to Government Policy:**
    *   Most revenue generated from the oil and gas segment makes the entity vulnerable to industry changes.
    *   Shifts in geopolitical landscapes, environmental policies, or safety regulations could significantly impact the business risk profile.

---

## Liquidity

*   **Overall Position:** Adequate liquidity position supported by estimated net cash accruals over **Rs 84 Crore**, exceeding repayment obligations of Rs 24-25 Crore for fiscal 2027 onwards.
*   **Limit Utilisation:**
    *   Fund-based limit utilisation: **~56%**
    *   Non-fund-based limit utilisation: **76.25%**
    *   (Period: 12 months through February 2026)
*   **Cash Reserves:** Cash and cash equivalents stood at **Rs 157 Crore** as on March 31, 2026.
    *   **Unencumbered Cash:** **Rs 92 Crore**

---

## Outlook & Rating Sensitivity

**Outlook:** **Watch Developing**
The agency continues to monitor the merger completion with the National Company Law Tribunal and the performance of the merged entity.

| Factor Type | Description |
| :--- | :--- |
| **Upward Factors** | • Sustained increase in scale of operations leading to net cash accruals over Rs 80 Cr on a sustained basis.<br>• Sustained improvement in working capital cycle, particularly driven by improvement in debtor days.<br>• Sustenance of the financial risk profile. |
| **Downward Factors** | • Decline in scale or operating margin resulting in net cash accrual below Rs 50 Cr on a sustained basis.<br>• Further stretch in receivables, leading to higher-than-expected Gross Current Assets (GCAs).<br>• Any large, debt-funded capital expenditure (capex) that weakens the financial risk profile. |

---

## Key Financial Indicators

*(Consolidated Numbers)*

| Indicator | Unit | 2025 | 2024 |
| :--- | :--- | :--- | :--- |
| **Operating Income** | Rs Crore | 465.04 | 465.04 |
| **Reported Profit After Tax (PAT)** | Rs Crore | 42.04 | 42.04 |
| **PAT Margin** | % | 9.04 | 9.04 |
| **Adjusted Debt / Adjusted Networth** | Times | 0.06 | 0.06 |
| **Interest Coverage** | Times | 20.28 | 20.28 |

---

## Bank Facilities

*Bank-wise breakup of rated facilities*

| Rank | Bank Name | Facility Type | Amount (Rs. Crore) | Rating |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Union Bank of India** | Bank Guarantee | 100.00 | Crisil A2/Watch Developing |
| | | Cash Credit | 20.00 | Crisil BBB+/Watch Developing |
| **2** | **Bank of Maharashtra** | Bank Guarantee | 60.00 | Crisil A2/Watch Developing |
| | | Cash Credit | 10.00 | Crisil BBB+/Watch Developing |
| | | Long Term Loan | 37.50 | Crisil BBB+/Watch Developing |
| **3** | **Kotak Mahindra Bank Ltd** | Cash Credit | 10.00 | Crisil BBB+/Watch Developing |
| | | Standby Letter of Credit | 60.00 | Crisil A2/Watch Developing |
| **4** | **Citi Bank** | Fund-Based Facilities | 20.00 | Crisil BBB+/Watch Developing |
| **TOTAL** | | **All Facilities** | **317.50** | |

---

## Company & Subsidiaries

**Company Profile:**
*   **Name:** Asian Energy Services Limited (AESL)
*   **Status:** Listed on BSE Limited and National Stock Exchange of India Limited.
*   **Promoter/MD:** Dr. Kapil Garg (Part of the Asian group, subsidiary of OEPL).
*   **Core Business:** Provides geophysical onshore seismic and drilling services (acquisition, imaging, field evaluation, 2D & 3D seismic data). Also provides EPC and O&M services to oil, gas, mining, and energy sectors.
*   **Analytical Scope:** Considers consolidated numbers of AESL and step-down subsidiaries including global entities in Dubai, Singapore, Malaysia, etc.

**Consolidated Entities Summary:**
The analytical approach consolidates the following entities (Excerpt from Annexure):

| Entity Name | Extent of Consolidation | Role |
| :--- | :--- | :--- |
| Asian Energy Services Limited | Full | Holding Company |
| Asian Oilfield & Energy Services DMCC | Full | Subsidiary |
| AOSL Petroleum Pte. Ltd | Full | Subsidiary |
| AOSL Energy Services Limited | Full | Subsidiary |
| Optimum Oil & Gas Private Limited | Full | Subsidiary |
| Cure Multitrade Private Limited | Proportionate | Subsidiary |
| Ivorene Oil Services Nigeria Ltd | Full | Subsidiary |
| Kuiper Group Limited | Full | Subsidiary (Acquired H1 FY26) |
| OCB Oilfield Services DMCC | Full | Subsidiary |
| Global Resources Management Employment Services LLC | Full | Subsidiary |
| Nexus People Management (KSA) | Full | Subsidiary |
| Maaber for Logistics Services | Full | Subsidiary |
| Offshore International Management (India) Pvt Ltd | Full | Subsidiary |
| Kuiper International Pte Ltd | Full | Subsidiary |
| Kuiper Malaysia Sdn. Bhd | Full | Subsidiary |
| PT Oilfeild Crew Management Ltd | Full | Subsidiary |
| OCB Oilfield Services Limited | Full | Subsidiary |
| Kuiper Holdings Limited | Full | Subsidiary |
| *(Additional Step-down entities in Egypt, Namibia, Qatar, Cyprus, Oman)* | Varies | Subsidiary |

**Joint Ventures Included in Analysis:**
1.  Zuberi Asian joint venture
2.  AESL FFIL joint venture
3.  Asian Indwell joint venture
4.  Asian Oilmax joint venture