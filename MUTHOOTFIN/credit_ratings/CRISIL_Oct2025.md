Here's a thinking process that leads to the structured markdown report:

1.  **Understand the Goal:** The user wants me to act as an equity analyst and extract a credit rating report from the provided raw text (which is scraped HTML content). I need to structure this into a specific markdown format with defined sections: Rating Action, Detailed Rationale, Key Rating Drivers (Strengths/Weaknesses), Liquidity, Outlook & Sensitivity, Key Financial Indicators, Bank Facilities, and Company & Subsidiaries.

2.  **Analyze the Source Text:** I'll scan the raw text to locate information corresponding to each required section.

    *   *Header Info:* "October 28, 2025 | Mumbai", "Muthoot Finance Limited", "Crisil AA+/Stable". Agency Name: Crisil Ratings Limited.
    *   *Rating Action:* There's a long list of facilities with amounts and ratings (Assigned, Reaffirmed, Withdrawn). I need to summarize the total or list them clearly. The prompt asks for "total facilities rated" and a list.
    *   *Detailed Rationale:* There's a paragraph under "Detailed Rationale" explaining the assignment/reaffirmation and business overview.
    *   *Key Rating Drivers — Strengths:* Section explicitly titled "Key Rating Drivers - Strengths". Contains: Established track record, Strong capitalisation, Profitability.
    *   *Key Rating Drivers — Weaknesses:* Section explicitly titled "Key Rating Drivers - Weaknesses". Contains: Geographical concentration/Non-gold presence, Asset quality in non-gold segments.
    *   *Liquidity:* Section explicitly titled "Liquidity". Mentions liquidity balance, coverage, cash accruals, bank limits (implied via fund raising).
    *   *Outlook & Rating Sensitivity:* Section explicitly titled "Outlook" and "Ratings sensitivity factors".
    *   *Key Financial Indicators:* Tables exist for Standalone and Consolidated indicators (Assets, Income, PAT, Gearing, RoMA).
    *   *Bank Facilities:* The prompt asks for this. I need to check the Annexures. Scanning... The raw text contains "Annexure - Details of Instrument(s)" and "Annexure - List of Entities Consolidated". Wait, looking closely at the raw text, there isn't a specific *Bank Facilities* table listed like there is for Instruments. However, the "Liquidity" section mentions "existing term loans, un-utilized portion of Cash Credit and Working Capital Demand Loans". Usually, bank facilities are detailed in an annexure not fully pasted here, or I might find it in the "Details of Rating Withdrawn" or general text. Actually, scanning again, I don't see a specific table listing *Banks* and their *Facilities*. I will note that specific bank breakup is mentioned as existing but the detailed table is likely in the full report/Annexure not fully extracted, OR I should look for the closest match.
        *Correction:* Looking at the "Liquidity" section, it mentions "liquidity balance of Rs 10,714.6 crore... excluding un-utilized portion of existing term loans...". It doesn't list specific banks. I will state "Not explicitly detailed in source text" or synthesize based on available data if possible. However, strict adherence to the prompt implies organizing what's there. Since there is no bank-wise breakup table in the provided text, I will mention the available liquidity details but note the absence of the specific bank-wise table found in the document provided. *Self-Correction:* I will check if there's any hidden data. No. I will populate the section with the Liquidity info available or mark as N/A regarding specific banks if the data is missing. Better yet, since the instruction says "Organize it...", if data is missing, I state what is available. I'll focus on the Liquidity assessment provided in the text.
    *   *Company & Subsidiaries:* "About the Company", "Annexure - List of Entities Consolidated".

3.  **Drafting the Content - Section by Section:**

    *   **Rating Action:**
        *   Date: October 28, 2025
        *   Agency: Crisil Ratings Limited
        *   Company: Muthoot Finance Limited
        *   Facilities: Need to list the main ones categorized by action (Assigned, Reaffirmed, Withdrawn, Enhanced, Reduced).
        *   Total Facilities Count: I won't count every single debenture ISIN if it's too granular, but rather summarize the actions. The prompt asks for "total facilities rated". I can count the distinct instruments listed in the "Rating Action" header section + Reaffirmed list. Let's group them.
        *   New Ratings Assigned: Subordinated Debt (800cr), NCD (10,000cr) [Text mentions 10,000 cr NCD and 800 cr sub debt].
        *   Reaffirmed: Various NCDs, CP (9000cr), Sub Debts, PPMLDs.
        *   Withdrawn: Redeemed Secured NCDs (805cr), Sub Debts, PPMLDs.
        *   *Refinement:* The "Rating Action" section lists many items. I will summarize the key ones (Assigned vs Reaffirmed) and mention the withdrawal.
        *   *Wait, one discrepancy:* The header says "Rs.800 Crore Subordinated Debt... Assigned", "Rs.200 Crore NCD... Assigned", "Rs.9800 Crore NCD... Assigned". Later in Detailed Rationale it says "assigned its 'Crisil AA+/Stable' to Rs 10,000 crore non-convertible debentures and Rs 800 crore subordinated debt".
        *   *Decision:* Use the Detailed Rationale summary for the core new assignment, and the Rating Action list for the specific breakdown of reaffirmations and other transactions.

    *   **Detailed Rationale:** Extract the summary paragraph. Focus on the decision logic (scaling gold loan, financial risk profile, market position, offsetting risks). Include AUM growth stats.

    *   **Strengths:**
        *   Track Record/Brand (85 years, 7413 branches).
        *   Capitalization (Net worth ~30k cr, Gearing < 4x).
        *   Profitability (RoMA ~4.7-5.6%, margins high).

    *   **Weaknesses:**
        *   Geographical Concentration (South India 58% branches, portfolio concentration reduced but still a factor).
        *   Non-Gold Asset Quality (MFIs ~4.44% GNPA, Housing finance weak profile).

    *   **Liquidity:**
        *   Balance: 10,714.6 Cr (Sep 30, 2025).
        *   Coverage: 1.5x (2 months).
        *   Fundraising: 35,175 Cr raised since April 2025.
        *   *Note on Bank Limits:* The text doesn't give a bank-wise table. I will mention the liquidity status instead.

    *   **Outlook:** Stable. Upward: Market position, profitability > 5%. Downward: Asset quality deterioration, Tier I < 15%.

    *   **Key Financial Indicators:** Create tables for Standalone and Consolidated using the data provided (Jun-25, Mar-25, Mar-24).

    *   **Bank Facilities:** As noted, specific bank names aren't in the text. I will create a placeholder stating "Data not explicitly detailed in provided text" but include the Liquidity line item context if relevant. Actually, looking at the "Key Financial Indicators" there is no mention of specific bank credit limits either. I will leave this section noting the information is summarized in the Liquidity section or unavailable in the specific snippet. *Better approach:* Just state "Not applicable / Not provided in excerpt" for specific bank breakup, but acknowledge the funding capacity mentioned in Liquidity.

    *   **Company & Subsidiaries:**
        *   Parent: Muthoot Finance Ltd (NBFC, est 1997, public 2008).
        *   Subsidiaries: Muthoot Homefin, Belstar Microfinance, Muthoot Money.

4.  **Formatting:** Use Markdown headers (`##`, `###`), bullet points, and tables as requested. Ensure currency formatting (Rs Crore) is consistent. Check dates carefully (Text uses future dates like Oct 2025, June 2025 - treat as factual content of the report provided).

5.  **Review against Constraints:**
    *   Did I miss the Bank Facilities table? The text has an Annexure - Details of Instrument(s) which lists ISINs, Coupon, Maturity, etc., but NOT Bank Facilities specifically (like Bank X: Limit Y, Utilized Z). It lists Debt Instruments. I must be honest. I will indicate that Bank-wise facility details are typically found in a separate schedule not fully included in this text, though liquidity metrics are present.
    *   Did I capture all Strengths/Weaknesses? Yes.
    *   Did I get the Financials right? Yes, transcribed from tables.
    *   Did I include the ESG section? The text has an ESG section. I should probably include relevant highlights under Strengths or create a small note, but the prompt didn't explicitly ask for an "ESG" section header, so I will integrate them into Strengths (as the text does link them to credit risk support) or keep it in D&R. The text puts ESG after Liquidity. I'll put it under a relevant strength or just omit if not requested. To stay true to the text, I'll add a brief note under Strengths or Rationale. Actually, the prompt asks for specific sections. I will stick to the requested structure. I will incorporate ESG highlights into the strengths section ("Governance/ESF Profile") or simply mention they support the credit profile in the Rationale. Let's add it to Strengths as it supports the profile.

6.  **Final Polish:** Check for consistency in numbers (e.g., Networth Rs 30,355 Cr vs 29,367 Cr - use latest Jun-25 for current snapshot). Ensure distinction between Consolidated and Standalone in financial tables.

    *(Self-Correction on Bank Facilities)*: In credit reports, "Bank Facilities" usually refers to Term Loans/Cash Credits. The text says "excluding un-utilized portion of existing term loans...". It doesn't list the banks. I will explicitly state "Bank-wise breakup data not available in the provided excerpt." to be accurate.

    *(Self-Correction on Rating Action)*: There are many items. I will categorize them to make it readable.

    *(Date Check)*: Report date is October 28, 2025. Data is as of March 2025 and June 2025. This is a "future-dated" or hypothetical scenario in the text provided, or simply the text provided treats these as current. I will reproduce the data exactly as written in the source text.

7.  **Construction:** Assemble the Markdown.

**(Final Check of Prompt Requirements):**
- Structure into well-organized markdown report.
- Sections: Rating Action, Detailed Rationale, Key Rating Drivers — Strengths, Key Rating Drivers — Weaknesses, Liquidity, Outlook & Rating Sensitivity, Key Financial Indicators, Bank Facilities, Company & Subsidiaries.

Let's build it.cw
</think>

# Credit Rating Report: Muthoot Finance Limited
**Agency:** Crisil Ratings Limited  
**Date:** October 28, 2025  
**Location:** Mumbai  

---

## Rating Action

**Company:** Muthoot Finance Limited  
**Overall Corporate Rating:** `Crisil AA+/Stable`

**Rating Decisions:**
*   **Assigned:** `Crisil AA+/Stable` to Rs. 800 Crore Subordinated Debt and Rs. 10,000 Crore Non-Convertible Debentures.
*   **Reaffirmed:** `Crisil AA+/Stable`, `Crisil PPMLD AA+/Stable`, and `Crisil A1+` on various outstanding debt instruments including Commercial Papers (Enhanced to Rs. 9,000 Cr), Subordinated Debt, NCDs, and PPMLDs.
*   **Withdrawn:** Ratings on redeemed/deceased instruments totaling approx. Rs. 805 Cr NCDs, Rs. 18.72 Cr Subordinated Debt, and Rs. 216.8 Cr PPMLDs.

**Total Facilities Rated:** Multiple debt instruments ranging across Short-Term (Commercial Paper) and Long-Term (Debentures, Subordinated Debt).

---

## Detailed Rationale

**Summary of Decision:**
Crisil Ratings has assigned its `Crisil AA+/Stable` rating to fresh issues of subordinated debt and non-convertible debentures and reaffirmed ratings on existing debt instruments at `Crisil AA+/Stable`. The rating reflects Muthoot Finance's demonstrated ability to profitably scale its core gold loan business while maintaining a strong financial risk profile. The rating considers the company's strong market position bolstered by promoter experience. These strengths are partially offset by geographical concentration in operations, low market share in non-gold loan segments, and asset quality challenges within those non-gold segments.

**Financial Performance Overview:**
*   **Fiscal 2025 Growth:** Consolidated AUM grew ~37% YoY to Rs. 1,22,181 Crore (March 31, 2025). Flagship gold loans grew ~41% to Rs. 1,02,956 Crore.
*   **Asset Mix:** As of June 2025, Gold Loans accounted for ~88% of Consolidated AUM; Non-Gold loans (Microfinance ~5%, Housing Finance ~2%) accounted for ~12%.
*   **Q1 FY2026:** Return on Managed Assets (RoMA) stood at 5.6% (consolidated), driven by high interest margins and efficiency.

---

## Key Rating Drivers — Strengths

*   **Established Track Record and Brand:**
    *   Supported by an 85-year track record of the promoter family.
    *   Extensive operational base: Over 7,413 branches across India (4,877 offering gold loans).
    *   Leadership position among NBFCs in gold financing.
    *   Customer Base: Active borrowers crossed 64.6 lakhs (June 2025); Loan accounts increased to 1.04 Crore.
*   **Strong Capitalisation:**
    *   **Consolidated Net Worth:** Rs. 30,355 Crore as of June 30, 2025 (increased from Rs. 29,367 Cr on Mar 31, 2025).
    *   **Gearing:** Remained low at 3.5 times (Consolidated) as of June 2025; standalone gearing below 4x historically.
    *   **Capital Adequacy:** Standalone Tier I capital adequacy ratio was 21.96% (June 30, 2025); above 20% over recent years.
*   **Profitability Among Best in Industry:**
    *   **RoMA:** Healthy levels maintained. Fiscal 2025: 4.7%; Q1 FY2026: 5.6%.
    *   **Margins:** High interest margins with controlled operating expenses.
    *   **Credit Costs:** Under control (Stage III assets reduced to 2.6% as of June 30, 2025). Negligible write-offs due to liquid security (Gold).

---

## Key Rating Drivers — Weaknesses

*   **Geographical Concentration:**
    *   Operations concentrated in South India (~58% of branches as of June 30, 2025).
    *   Risk exposure to regional economic/social disruptions.
    *   **Mitigation:** Reduction in portfolio concentration in South region (dropped from 86% in FY2007 to 48% in June 2025).
*   **Low Market Presence in Non-Gold Businesses:**
    *   Primary revenue focus remains Gold Loans (>85% of portfolio).
    *   Non-gold loan growth is gradual; segmental concentration remains a monitorable.
*   **Asset Quality Challenges in Non-Gold Segments:**
    *   **Microfinance:** Gross NPAs (90+ dpd) at 4.44% (June 30, 2025). Vulnerable to external shocks (elections, calamities, regulations).
    *   **Housing Finance:** Operates in affordable sector catering to self-employed/unorganized customers with volatile income profiles.
    *   **Vehicle Finance:** Halted fresh lending due to asset quality issues post-pandemic; shifting focus back to gold loans.

---

## Liquidity

*   **Assessment:** Strong
*   **Cash Accruals & Balance:**
    *   Standalone Liquidity Balance: **Rs. 10,714.6 Crore** (as on September 30, 2025).
    *   Liquidity Cover for next 2 months debt obligations: **1.5 times**.
    *   Maintenance: Maintains 5-8% of balance sheet as liquidity balance over last 4-5 quarters.
*   **Fundraising Capacity:**
    *   Raised **Rs. 35,175 Crore** since April 2025 from various avenues.
    *   Able to roll over existing capital lines and raise incremental funds at competitive rates.
*   **Bank Facilities:**
    *   *Note: Specific bank-wise facility breakup tables were not included in the provided text excerpt.*
    *   Available liquidity covers debt obligations and working capital needs without reliance solely on immediate rollovers.

---

## Outlook & Rating Sensitivity

**Outlook:** **Stable**
*   **Expectation:** Sustained strong capitalisation and healthy profitability. Sound asset quality in gold loans supported by liquid collateral (gold jewelry). Non-gold asset quality remains monitorable.

**Upward Factors:**
*   Continued strong market position in gold finance.
*   Increasing diversity in Loan AUM and geographical reach.
*   Sustenance of profitability with RoMA > 5% steady state.

**Downward Factors:**
*   Significant and sustained deterioration in asset quality of non-gold businesses affecting earnings.
*   Moderation in capital position (Tier I capital adequacy declining below 15%).

---

## Key Financial Indicators

### Consolidated Basis (Rs. Crore)
| Indicator | As On/For Jun-25 | As On/For Mar-25 | As On/For Mar-24 |
| :--- | :--- | :--- | :--- |
| **Total Managed Assets** | 148,716 | 132,860 | 96,469 |
| **Total Income** | 6,485 | 20,324 | 15,163 |
| **Profit After Tax** | 1,974 | 5,352 | 4,468 |
| **Gearing** | 3.5 Times | 3.4 Times | 2.7 Times |
| **Return on Managed Assets** | 5.6%* | 4.7% | 5.1% |

*(*) Annualised basis*

### Standalone Basis (Rs. Crore)
| Indicator | As On/For Jun-25 | As On/For Mar-25 | As On/For Mar-24 |
| :--- | :--- | :--- | :--- |
| **Total Managed Assets** | 136,120 | 121,248 | 85,028 |
| **Total Income** | 5,720 | 17,156 | 12,694 |
| **Profit After Tax** | 2,046 | 5,200 | 4,050 |
| **Gross NPA** | 2.6% | 3.4% | 3.3% |
| **Gearing** | 3.5 Times | 3.2 Times | 2.4 Times |
| **Return on Managed Assets** | 6.4%* | 5.1% | 5.1% |

*(*) Annualised basis*

---

## Bank Facilities

*Information regarding specific bank-wise facility breakup and utilization percentages was not explicitly detailed in the provided text excerpt. Refer to the "Annexure - Details of Instrument(s)" for debt instrument specifics.*

**Available Financing Highlights (From Liquidity Section):**
*   **Term Loans & CC/WCDL:** Un-utilized portions exist and contribute to liquidity balance calculation.
*   **Recent Capital Line Rollover:** Successful rolling over of capital lines observed.

---

## Company & Subsidiaries

**Company Information:**
*   **Name:** Muthoot Finance Limited
*   **Status:** NBFC (Originally Pvt Ltd 1997, Public Ltd Nov 2008).
*   **Promoter History:** Family involved in business since 1939 (~85 years).
*   **Core Business:** Finance against household gold jewellery.

**Consolidated Entities:**
Crisil Ratings combined business and financial risk profiles with the following subsidiaries (Full Consolidation):

| Entity Name | Type | Rationale |
| :--- | :--- | :--- |
| **Muthoot Homefin (India) Ltd** | Subsidiary | Full Consolidation |
| **Belstar Microfinance Private Ltd** | Subsidiary | Full Consolidation |
| **Muthoot Money Limited** | Subsidiary | Full Consolidation |

**Group Diversification:**
Beyond the flagship gold loan business, the group operates in hospitality, healthcare, education, IT, foreign exchange, insurance distribution, and money transfer.