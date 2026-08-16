Here's a thinking process that leads to the suggested report:

1.  **Understand the Goal:** The user wants me to act as an equity analyst extracting information from raw text (a credit rating rationale) and structure it into a well-organized markdown report. Specific sections are mandated: Rating Action, Detailed Rationale, Key Rating Drivers (Strengths/Weaknesses), Liquidity, Outlook & Sensitivity, Key Financial Indicators (table), Bank Facilities (table), and Company & Subsidiaries.

2.  **Analyze the Raw Text:** I need to scan the provided text for specific data points corresponding to the required sections.

    *   *Header:* "Rating Rationale", "January 09, 2025 | Mumbai", "Ujjivan Small Finance Bank Limited".
    *   *Rating:* "CRISIL A1+ (Reaffirmed)". Date: January 09, 2025. Agency: CRISIL Ratings Limited. Instrument: Rs.2500 Crore Certificate of Deposits.
    *   *Detailed Rationale:* Look for summary paragraphs explaining *why* the rating was reaffirmed.
        *   Strong presence in microfinance + expansion to other assets.
        *   Adequate capitalization + profitability normalization.
        *   Offset by small retail deposit base + susceptibility of asset quality due to borrower profile.
        *   Growth metrics (Fiscal 2024 gross advances 24%, H1 FY25 moderate growth 2%).
        *   Asset Quality: Improved in FY24 (GNPA 2.1%), moderated in H1 FY25 (GNPA 2.5%, Provisional Dec 2024: 2.7%).
        *   Profitability: RoMA corrected to 3.3% in FY24, moderated to 2.5% in H1 FY25.
        *   Capitalisation: Tier I 21.6%, CAR 23.4% (Sept 30, 2024).
        *   Deposits: Total deposit base Rs 34,070 crore (Sept 30, 2024), Retail deposits 73% (of total). CASA ~25.9%.
    *   *Key Rating Drivers — Strengths:*
        *   Established market position (Microfinance).
        *   Diversification (Affordable housing, SME, etc.).
        *   Geographical diversity (No state >15%).
        *   Adequate capitalization (CAR/Tier I).
        *   Stable profitability (historically, though recent moderation noted).
        *   ESG profile.
    *   *Key Rating Drivers — Weaknesses:*
        *   Small share of CASA/Retail deposits (CASA 25.9%).
        *   Cost of deposits increasing (7.5% Q2 FY25).
        *   Modest credit risk profile of borrowers (over-leveraging, debt waivers, attrition).
        *   Asset quality moderation (GNPA increase H1 FY25).
    *   *Liquidity:*
        *   Strong profile.
        *   Assets maturing > liabilities maturing (1-year): 1.01 times.
        *   SLR excess: 5.4%.
        *   LCR: 122% (Nov 30, 2024).
        *   Access to systemic liquidity (ALF, Call money).
    *   *Outlook & Rating Sensitivity:*
        *   Outlook isn't explicitly stated as "Stable" or "Negative" in the header, but usually reaffirmation implies stability unless specified. However, looking closely at the text: "Rating reaffirmed...". Under "Rating sensitivity factors", it lists Downward factors. It doesn't explicitly name the outlook direction (like 'Positive'/'Negative') in the standard summary block, but often 'Reaffirmed' implies 'Stable'. Wait, looking at the "Annexure - Rating History", it says "Outstanding Amount" -> "Rating". No explicit outlook column there either. In the "Rating Rationale" section: "The rating continues to reflect..." usually implies stability. I will check if there is a specific outlook mentioned.
        *   *Correction:* Scanning again. "Rating reaffirmed at 'CRISIL A1+'". Usually, if no outlook is specified, it defaults to 'Stable' or is omitted. I will look for keywords. Found under "Rating Sensitivity Factors": "Downward factors". No specific upward/outlook statement explicitly labeled "Outlook: [Status]". However, the prompt asks for "Outlook Statement". Given it is a Reaffirmation without a change note, "Stable" is the implied status, but strictly based on text, I should quote the reaffirmation. I will check the Annexure table: "Current 2025 (History)... CRISIL A1+". No Outlook listed there. I will note "Implied Stable / Not Explicitly Stated" or just focus on the Reaffirmation status. Actually, looking at "Rating reaffirmed at 'CRISIL A1+'", I will treat the status as the action and look for any specific outlook text. There isn't one. I will state "Not explicitly stated" or infer based on context (Reaffirmation = Status Quo). Let's stick to what is written: "Rating Action". Under "Outlook & Rating Sensitivity", I will list the sensitivities provided.
    *   *Key Financial Indicators:*
        *   Table needed for Year ended March 31 (2022-2024).
        *   Table needed for Period ended Sept 30 (2022-2024).
        *   Combine or present sequentially. The prompt asks for "a markdown table if tabular data exists". I will combine them or present two tables for clarity.
    *   *Bank Facilities:*
        *   The text mentions "Refer to Annexure for Details of Instruments & Bank Facilities".
        *   Annexure details: "Certificate of Deposits", ISIN NA, Issue Size 2500 Cr.
        *   There is no specific bank-wise breakup table in the text (e.g., HDFC vs ICICI limits). It only mentions the specific instrument being rated (CoD). I must represent what is available.
        *   Wait, is there a bank facility breakdown? "Refers to Annexure for Details...". Annexure shows CD details. It does not show a lender/bank facility breakup like "Axis Bank: X amount". It talks about "Total facilities rated" in the first section instructions. I can put the CD facility info here.
    *   *Company & Subsidiaries:*
        *   Ujjivan Small Finance Bank Ltd.
        *   Holding Entity: Ujjivan Financial Services Limited (UFSL).
        *   Reverse merged with UFSL (NCLT approval April 19, 2024).
        *   Branch network: 752 (Sept 30, 2024).
        *   States: 26.

3.  **Drafting the Content:**

    *   *Header:* Create the Markdown structure.
    *   *Rating Action:* Extract Date, Agency, Rating, Instrument, Amount.
    *   *Detailed Rationale:* Synthesize the "Detailed Rationale" section into a cohesive paragraph.
    *   *Drivers:* Split Strengths and Weaknesses based on the text labels. Use bullet points. Ensure numbers match the text.
    *   *Liquidity:* Summarize the liquidity section (LCR, SLR, Mismatches).
    *   *Outlook:* Since "Outlook" isn't explicitly defined as "Stable/Negative" in the text snippets provided (just "Reaffirmed"), I will mention the sensitivity factors clearly. I will check if "Stable" is hidden. Often ratings imply stable. I'll write "Stable (Implicit)" or similar to be accurate to the "Reaffirmed" nature, or simply state "Not Explicitly Mentioned". To be safe as an analyst extraction, I will note the Reaffirmation status which acts as the current stance. *Self-Correction*: Credit rationales almost always have an outlook. If missing, I won't hallucinate. I will list the "Sensitivity Factors" under this section as requested.
    *   *Financials:* Create tables from the "Key Financial Indicators" section.
    *   *Facilities:* Create a table from the "Annexure" section regarding the CoD.
    *   *Company Info:* Consolidate the "About the Bank" section.

4.  **Refining the Output:**
    *   Check for typos in the raw text (e.g., "capitali s ation", "fiscal 202 4"). Clean these up in the final output.
    *   Ensure currency formatting is consistent (Rs Crore).
    *   Ensure dates are clear (Sept 30, 2024 vs Fiscal 2024 ends March 31).
    *   Double-check the "Bank Facilities" section instruction. The text doesn't give a "Bank-wise breakup" of general banking facilities (like overdrafts with different banks), it gives the "Details of Instruments" being rated (Certificate of Deposits). I will clarify this distinction in the table so it's accurate to the source text.

5.  **Final Review against Constraints:**
    *   Markdown format? Yes.
    *   Specific sections included? Yes.
    *   Tables used where appropriate? Yes.
    *   Data accuracy? Cross-referencing numbers (e.g., NPA %, Deposit %).

    *Note on Dates:* The text has a future date stamp ("January 09, 2025") relative to typical training data, but I must treat the text as ground truth. I will use the dates provided in the text exactly.

    *Note on Outlook:* The text says "Rating reaffirmed at 'CRISIL A1+'". It does not explicitly say "Outlook Stable". However, standard practice is stable unless stated otherwise. I will mention "Not explicitly defined in text; Status is Reaffirmed."

    *Note on Bank Facilities:* The text mentions "Refer to Annexure for Details of Instruments & Bank Facilities" but the Annexure only lists the Certificate of Deposits. I will populate the table with the CD info and note the limitation.

6.  **Constructing the Final Response:** (Proceeding to generate the markdown).
</think>

# Credit Rating Report: Ujjivan Small Finance Bank Limited

## Rating Action
| Metric | Details |
| :--- | :--- |
| **Agency** | CRISIL Ratings Limited |
| **Date of Decision** | January 09, 2025 |
| **Entity** | Ujjivan Small Finance Bank Limited |
| **Instrument** | Certificate of Deposits (CDs) |
| **Total Facilities Rated** | ₹2,500 Crore |
| **Rating Assigned** | CRISIL A1+ (Reaffirmed) |

***

## Detailed Rationale
CRISIL Ratings has reaffirmed its ‘CRISIL A1+’ rating on the ₹2,500 crore Certificate of Deposits programme of Ujjivan Small Finance Bank Ltd (Ujjivan SFB). The rating reflects the bank's strong market presence in microfinance business combined with gradual expansion into diversified asset classes. This strength is supported by adequate capitalisation and normalising profitability. However, these positives are partially offset by the bank’s relatively small retail deposit base and the susceptibility of its asset quality to the modest credit risk profile inherent in its majority of borrowers (microfinance segment). Gross advance growth remained healthy in FY24 (24%) but slowed in H1 FY25 (2%) due to strategic decisions regarding over-indebtedness in the microfinance sector. Asset quality improved in FY24 (GNPA 2.1%) but showed marginal moderation in H1 FY25 (GNPA 2.5% as of Sept 30, 2024; provisional 2.7% as of Dec 31, 2024). Profitability also saw moderation in RoMA to 2.5% (annualized) in H1 FY25 due to higher credit costs and operating expenses.

***

## Key Rating Drivers — Strengths
*   **Established Market Position:** Third largest small finance bank in India with over two decades of track record in microfinance. As of Sept 30, 2024, micro-banking loans constituted 64% of gross advances (down from 72% in FY23), indicating active diversification.
*   **Geographical Diversification:** Well-diversified operational presence with no single state accounting for more than 15% of the loan book. Top states were Tamil Nadu (14%), Karnataka (13%), and West Bengal (12%).
*   **Adequate Capitalisation:** Reported Tier I capital of 21.6% and Overall CAR of 23.4% as on September 30, 2024 (vs 22.6% and 24.7% as on March 31, 2024). Networth stood at ₹5,882 crore.
*   **Profitability Revival:** Despite moderation, profitability has revived since FY22. Return on Managed Assets (RoMA) stood at 3.3% in FY24 before moderating to 2.5% in H1 FY25.
*   **ESG Profile:** Board governance includes 60% independent directors. Gender diversity rate stood at 19.54% as on March 31, 2024. Focus on energy/water reduction and waste management initiatives.

## Key Rating Drivers — Weaknesses
*   **Deposit Franchise Limitations:** Retail deposits (including CASA) constitute 73% of total deposits as of Sept 30, 2024, but the CASA ratio remains modest at 25.9% (lower than peers).
*   **Higher Funding Costs:** Cost of deposits increased to 7.5% in Q2 FY25 from 7.4% in Q2 FY24 and 6.2% in Q2 FY23.
*   **Asset Quality Vulnerabilities:** Portfolio comprises clients with below-average credit risk profiles susceptible to macro disruptions (over-leveraging, debt waivers, election season challenges).
*   **Moderation in Metrics:** GNPA increased from 2.1% (March 31, 2024) to 2.5% (Sept 30, 2024) and provision coverage ratio (PCR) decreased to 78% from 96.1% YoY. Micro-banking portfolio GNPA specifically rose to 2.6% as on Sept 30, 2024.

***

## Liquidity
*   **Assessment:** Strong.
*   **Asset-Liability Matching:** As of September 30, 2024, assets maturing within one year formed 1.01 times the liabilities maturing within the same period.
*   **Statutory Ratios:** Excess Statutory Liquidity Ratio (SLR) of approximately 5.4%; Provisional Liquidity Coverage Ratio (LCR) of 122% as on November 30, 2024.
*   **External Access:** Scheduled Commercial Bank status allows access to liquidity adjustment facilities (ALF) and call money markets. Funds parked in liquid mutual funds and lines sanctioned from development banks available for utilization.

***

## Outlook & Rating Sensitivity
**Outlook Statement:**
The rating is **Reaffirmed**. While an explicit outlook label (e.g., Stable/Negative) is not detailed in the header, the reaffirmation indicates the agency views the risk profile as currently manageable.

**Downward Sensitivities:**
*   Significant deterioration in asset quality and/or profitability causing RoMA to decline materially and remain compressed for a prolonged period.
*   Material weakening in capitalization reflected in Tier I capital to risk assets ratio (CRAR) falling to and remaining below 18% for a prolonged period.
*   Inability to garner retail deposits resulting in the share of CASA as a percentage of total deposits remaining moderate.

***

## Key Financial Indicators

**Year Ended March 31**
| Indicator | Unit | 2024 | 2023 | 2022 |
| :--- | :--- | :--- | :--- | :--- |
| Total Assets | ₹ Crore | 40,422 | 33,317 | 23,612 |
| Total Income | ₹ Crore | 6,464 | 4,754 | 3,173 |
| Profit After Tax | ₹ Crore | 1,281 | 1,100 | (415) |
| Gross NPA | % | 2.1 | 2.6 | 7.1 |
| Overall CAR | % | 24.7 | 25.8 | 19.0 |
| Return on Managed Assets | % | 3.3 | 3.7 | (1.9) |

**Period Ended September 30**
| Indicator | Unit | 2024 | 2023 | 2022 |
| :--- | :--- | :--- | :--- | :--- |
| Total Assets | ₹ Crore | 43,619 | 38,680 | 26,785 |
| Total Income | ₹ Crore | 3,594 | 3,044 | 2,170 |
| Profit After Tax | ₹ Crore | 534 | 652 | 497 |
| Gross NPA | % | 2.5 | 2.2 | 4.4 |
| Overall CAR | % | 23.4 | 25.2 | 26.7 |
| Return on Managed Assets | % | 2.5 | 3.4 | 3.7 |

***

## Bank Facilities
*Note: The provided text details the specific instrument rated under this rationale. General bank facility breakups with external lenders are not explicitly itemized in the text.*

| Instrument Name | Issue Size (₹ Crore) | Rating | Outstanding With Outlook | Complexity Level |
| :--- | :--- | :--- | :--- | :--- |
| Certificate of Deposits | 2,500.00 | CRISIL A1+ | CRISIL A1+ | Simple |

**Additional Facility Details:**
*   **Maturity Duration:** 7–365 Days
*   **Coupon Rate:** Not Applicable (Variable/Market linked)
*   **Issue Size:** ₹2,500 Crore

***

## Company & Subsidiaries
*   **Parent Entity:** Ujjivan Small Finance Bank Limited commenced SFB operations in February 2017 via transfer of assets/liabilities of Ujjivan Financial Services Limited (UFSL).
*   **Corporate Restructuring:** The bank reverse merged with Ujjivan Financial Services following NCLT approval received on April 19, 2024. Paid-up equity capital revised to ₹1,932 crore (from ₹1,959 crore); Preference capital of ₹200 Crores extinguished.
*   **Branch Network:** 752 branches spread across 26 states as of September 30, 2024.
*   **Consolidation:** The entity operates as a standalone banking platform post-merger.