Thinking Process:

1.  **Analyze the Request:**
    *   **Role:** Equity Analyst.
    *   **Task:** Extract a credit rating report from raw text and structure it into a well-organized markdown report.
    *   **Input Raw Text:** "India Ratings and Research: Credit Rating and Research Agency India Loading..."
    *   **Required Sections:**
        *   ## Rating Action (Rating, outlook, date, agency name, total facilities rated)
        *   ## Detailed Rationale (Summary paragraph)
        *   ## Key Rating Drivers — Strengths (List with data)
        *   ## Key Rating Drivers — Weaknesses (List with data)
        *   ## Liquidity (Assessment, cash, bank limits)
        *   ## Outlook & Rating Sensitivity (Statement, upward/downward factors)
        *   ## Key Financial Indicators (Markdown table if tabular data exists)
        *   ## Bank Facilities (Bank-wise breakup table)
        *   ## Company & Subsidiaries (Company info, consolidated entities)

2.  **Analyze the Input Data:**
    *   The provided raw text is: `India Ratings and Research: Credit Rating and Research Agency India Loading...`
    *   This is essentially a header or a loading screen text from a website. It contains *no* actual credit rating data, financial indicators, company names, facility details, ratings, dates, etc.
    *   It only mentions the agency name ("India Ratings and Research").

3.  **Evaluate Feasibility:**
    *   I cannot fabricate data. As an AI, I must be truthful about the content provided.
    *   The prompt asks me to "extract a credit rating report from raw text".
    *   If the raw text is insufficient, I need to inform the user that the extraction cannot be completed due to lack of information, while still adhering to the requested format as much as possible (e.g., marking sections as "Not Available" or noting the insufficiency).
    *   However, usually, in these types of prompts, if the input is empty/invalid, the correct behavior is to point out the missing information rather than hallucinating content.
    *   Wait, looking closely at the prompt structure: It seems like a test case where the input might be incomplete or intentionally minimal to see how I handle it.
    *   Strategy: I will structure the markdown report according to the requirements but explicitly state that the provided text did not contain sufficient data to populate specific fields beyond the Agency Name. I should not invent numbers.

4.  **Drafting the Response:**
    *   *Header:* Keep the requested sections.
    *   *Content:* Fill in what can be known (Agency Name = India Ratings and Research). Mark everything else as "Information Not Provided in Source Text".
    *   *Tone:* Professional, analytical.

5.  **Refining the Output:**
    *   Actually, providing a template filled with "N/A" might look lazy. But providing fake data is worse (hallucination).
    *   Best approach: Create the structure as requested, fill the known value (Agency), and clearly indicate that the source text was insufficient for the rest of the report.
    *   Let's check if there's any hidden info. "Loading..." implies the page didn't render content.
    *   I will generate the report structure but annotate that data is missing based on the provided snippet.

    *Self-Correction:* If I just output "N/A" everywhere, it might not be helpful. I should explicitly mention *why* (the source text appears to be a page header/loading message without underlying data).

    *Decision:* I will create the report structure. For the sections requiring specific data found *only* in the full report (which isn't here), I will state "Data Not Available in Source Snippet". This fulfills the formatting requirement without lying.

6.  **Final Plan:**
    *   Use the exact headers requested.
    *   Extract "India Ratings and Research" as the Agency.
    *   Set other values to "Not Reported in Source Text" or similar.
    *   Add a note at the beginning or end explaining the limitation.

    *Wait, one more consideration:* Is this a trick? Sometimes users paste partial text expecting the model to know the context or search. I am a text-generation model, I don't browse live web. I must rely *only* on the provided raw text.
    *   Okay, I will proceed with the "Insufficient Data" approach within the required framework.

    *Revised Plan:* To be most helpful, I will present the structure but highlight the missing data clearly.

    *Wait, looking at the instruction again:* "You are an equity analyst extracting a credit rating report from raw text."
    *   If the raw text is just the agency name, I cannot extract a report.
    *   I should probably inform the user that the provided text is insufficient.
    *   However, to follow the "Structure this into a well-organized markdown report" instruction strictly, I will output the structure but mark the fields as unavailable.

    *Actually, the best professional response:* Acknowledge the input limitation while demonstrating the intended output format.

    *Let's try to make it look like a valid report draft with placeholders.*

    *Wait, I need to be careful not to hallucinate.*
    *   I will fill the Agency Name correctly.
    *   I will leave other fields blank or marked as N/A.

    *(Self-Correction during drafting)*: Providing a report full of "N/A" might confuse the user if they expect me to find the info elsewhere. I must state clearly that the *provided text* does not contain the info.

    *Final Decision:* I will produce the Markdown report as requested, populating only the information actually present (Agency Name) and indicating the rest as unavailable based on the provided snippet.

7.  **Constructing the Markdown:**
    *   Header: # Credit Rating Report Summary
    *   Section 1: Rating Action (Date: N/A, Rating: N/A...)
    *   Section 2: Detailed Rationale (Text: N/A)
    *   ...and so on.

    *Wait, I should add a disclaimer.*

    *Okay, let's write it.*

    *Wait, is there any chance I should search?* No, I am a static model instance regarding context window. I must use the provided text.

    *Okay, final plan:*
    1. Acknowledge the limited input.
    2. Present the structured template.
    3. Fill available data (Agency Name).
    4. Mark unavailable data as "Data Not Present in Source Snippet".

    *Wait, one nuance:* The prompt says "The raw text below is scraped...". It implies I should treat it as the source. Since it's basically noise, I must reflect that truthfully.

    Let's go.

    *Wait, checking the prompt again:* "Structure this into a well-organized markdown report."
    If I return a bunch of N/As, is it a "well-organized markdown report"? Yes, structurally.
    Okay, I will do that.

    *Wait, actually, I should check if I can infer anything.* No. "Loading..." means no content loaded.

    *Okay, I will create the report and add a prominent note at the top stating the source text was insufficient.*

    *Wait, looking at the examples of similar tasks:* Usually, if data is missing, the model should say "Unable to extract..."
    But the instruction says "Structure this into...".
    I'll strike a balance. I'll provide the structure, fill what I can, and explain the missing data.

    *Wait, let's look at the instruction:* "You are an equity analyst..."
    An equity analyst wouldn't publish a report with "N/A" everywhere without explanation.
    So I will write a brief introduction stating the limitation, then the formatted report.

    *Actually, better yet:* I will simply output the report sections as requested but with the accurate status of the data.

    *Let's finalize the content:*
    Agency: India Ratings and Research.
    Everything else: Not Available.

    *Wait, I need to make sure I don't violate safety policies.* No issue here.

    *Okay, ready to generate.*

    *Wait, I'll add a polite note at the very beginning.* "Note: The provided raw text appears to be a page header or loading message and lacks specific credit rating details. The following structure reflects the available information with missing data points noted."

    Then the Markdown table/sections.

    *Wait, I need to make sure I don't hallucinate the company name either.* The text doesn't say which company was rated. Just the agency.

    *Okay, proceeding.*

    *Wait, one last thought:* Maybe I should ask the user for the full text? No, the prompt is a task completion task. I need to output the result.

    *Okay, I will output the report structure with the available info.*

    *Wait, I'll check the section requirements again.*
    - Rating Action
    - Detailed Rationale
    - Strengths
    - Weaknesses
    - Liquidity
    - Outlook
    - Financial Indicators
    - Bank Facilities
    - Company & Subsidiaries

    All will be populated with "Not specified in provided text" except Agency Name.

    *Wait, I want to make it look professional.*
    I will use tables where appropriate.

    *Okay, let's write it.*
</think>

> **Analyst Note:** The provided raw text appears to be a website header or loading screen containing only the agency name ("India Ratings and Research"). Specific rating details, financial data, and rationale were not included in the source snippet. The report below has been structured according to your requirements, populating available data and marking missing sections as "Not Specified in Source."

# Credit Rating Report Summary

## Rating Action

| Parameter | Details |
| :--- | :--- |
| **Rating Agency** | India Ratings and Research |
| **Rating** | Not Specified in Source |
| **Outlook** | Not Specified in Source |
| **Effective Date** | Not Specified in Source |
| **Total Facilities Rated** | Not Specified in Source |
| **Issuing Entity** | Not Specified in Source |

## Detailed Rationale

> **Summary:**  
> No detailed rationale or summary paragraph was provided in the source text. Typically, this section would explain the methodology used by the agency and the core reasoning behind the assigned rating and outlook decision.

## Key Rating Drivers — Strengths

*   **Strength 1:** Not Specified in Source
*   **Supporting Data:** Not Specified in Source
*   **Strength 2:** Not Specified in Source
*   **Supporting Data:** Not Specified in Source

## Key Rating Drivers — Weaknesses

*   **Weakness 1:** Not Specified in Source
*   **Supporting Data:** Not Specified in Source
*   **Weakness 2:** Not Specified in Source
*   **Supporting Data:** Not Specified in Source

## Liquidity

*   **Liquidity Assessment:** Not Specified in Source
*   **Cash Accruals:** Not Specified in Source
*   **Bank Limit Utilisation:** Not Specified in Source

## Outlook & Rating Sensitivity

| Component | Status |
| :--- | :--- |
| **Outlook Statement** | Not Specified in Source |
| **Upward Factors** | Not Specified in Source |
| **Downward Factors** | Not Specified in Source |

## Key Financial Indicators

| Metric | FY End [Year] | Previous Year | Change (%) |
| :--- | :--- | :--- | :--- |
| **Revenue** | Not Specified | Not Specified | Not Specified |
| **EBITDA** | Not Specified | Not Specified | Not Specified |
| **Net Profit** | Not Specified | Not Specified | Not Specified |
| **Debt/Equity** | Not Specified | Not Specified | Not Specified |
| **Interest Coverage** | Not Specified | Not Specified | Not Specified |

## Bank Facilities

| Bank Name | Facility Type | Amount (INR Cr) | Utilization (%) |
| :--- | :--- | :--- | :--- |
| Not Specified | Not Specified | Not Specified | Not Specified |
| Not Specified | Not Specified | Not Specified | Not Specified |

## Company & Subsidiaries

| Item | Details |
| :--- | :--- |
| **Company Name** | Not Specified in Source |
| **Sector/Industry** | Not Specified in Source |
| **Consolidated Entities** | Not Specified in Source |