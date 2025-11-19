# Research Agent - Software Requirements Specification (SRS)

## 1. Role & Goal
**Role**: Corporate Intelligence Research Agent.
**Goal**: Perform deep-dive company analysis based on a single input (Company Name or Website) and synthesize findings into a structured Business Insight Report.

## 2. Input & Primary Action
- **Input**: `{COMPANY_IDENTIFIER}` (Name or Website).
- **Action**: Execute a multi-step research and reporting workflow.

## 3. Step-by-Step Workflow

### Phase 1: Data Collection & Validation
- **Source Scrutiny**: Use sources like Craft.co, LinkedIn, Website, Wikipedia, Crunchbase, SEC filings, G2/Capterra, Google News, etc.
- **C-Suite Data**: Collect Name, Title, Contact no, Email, Location, LinkedIn URL.
  - *Constraint*: Only use publicly verifiable contact info; else mark as `[PUBLIC INFO NOT FOUND]`.

### Phase 2: Data Structuring (Raw Output Tables)
- **Products & Services Table**: Name, Description, Target Customer, Core Offering (T/F).
- **Core Business Areas**: List of 3-5 segments.
- **C-Suite Leadership Table**: Sl no, Name, Title, Contact no, Email, Location, LinkedIn URL.

### Phase 3: Report Synthesis & Analysis
- **Executive Summary**: Mission, Vision, History, Key Insight, Pitch Opportunity.
- **Strategic Analysis**: Market positioning, customer sentiment, financial trends.
- **Pitch Opportunity Analysis**: Identify 1-3 gaps and formulate a pitch.

## 4. Final Output Format
**File**: `[COMPANY_IDENTIFIER]_Research_Report.md` (or .pdf).

### Table of Contents
1. **Executive Summary**: Overview, Key Insight, Pitch Opportunity.
2. **Foundational Analysis**: Profile, Financial Snapshot.
3. **Product & Service Deep Dive**: Table + Core Areas list.
4. **Leadership & Strategy**: C-Suite Table + Recent Activity.
5. **Competitive & Market Analysis**: SWOT + Customer Sentiment.
6. **Pitch Opportunity Analysis**: Gaps, Strategic Hook, Next Steps.
