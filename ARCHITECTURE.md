# Urimai AI (உரிமை AI) — System Architecture

This document provides a technical overview of Urimai AI's multi-agent architecture, data flows, security design, and the strict firewall boundary between deterministic logic and LLM-assisted guidance.

---

## 1. High-Level System Architecture

```mermaid
flowchart TD
    Citizen([🧑‍🌾 Citizen / Volunteer]) -->|Tamil Voice / Text| Frontend[💻 Next.js Frontend (App Router)]
    Frontend -->|JWT / Secure Cookies| APIGateway[🛡️ FastAPI Gateway + Rate Limiter]

    subgraph Backend Core
        APIGateway --> IntakeAgent[🤖 LangGraph Intake Agent]
        APIGateway --> MatchingEngine[⚙️ Deterministic Eligibility Engine]
        APIGateway --> GuidanceAgent[🧭 Grounded Guidance Agent]
        APIGateway --> FollowupAgent[📬 Follow-up & Freshness Pipeline]
    end

    subgraph Knowledge & Persistence
        IntakeAgent --> DB[(PostgreSQL / Supabase RLS)]
        MatchingEngine --> DB
        GuidanceAgent --> DB
        GuidanceAgent --> Pinecone[(🌲 Pinecone Vector Index)]
        GuidanceAgent --> Gemini[🧠 Google Gemini LLM]
        FollowupAgent --> DB
    end
```

---

## 2. The Strict Rules-Engine vs LLM Boundary (The "Eligibility Firewall")

A core architectural tenet of Urimai AI is that **an LLM is never permitted to decide whether a citizen qualifies for a welfare scheme**. Government benefits involve legal rights, strict financial thresholds, and official Government Orders (GOs). Hallucination in qualification is unacceptable.

```
                    ┌────────────────────────────────────────────────────────┐
                    │           DETERMINISTIC ELIGIBILITY LAYER              │
                    │  (Pure Mathematical Logic / SQLAlchemy Query Engine)   │
                    └──────────────────────────┬─────────────────────────────┘
                                               │
                        [Strict Firewall: Verified Qualification Data Only]
                                               │
                                               ▼
                    ┌────────────────────────────────────────────────────────┐
                    │           GENERATIVE GUIDANCE LAYER (RAG)              │
                    │   • Translates verified rules into friendly Tamil      │
                    │   • Formulates step-by-step application roadmaps       │
                    │   • Retrieves official GO citations from Pinecone      │
                    │   • Cannot add or remove schemes from eligible list    │
                    └────────────────────────────────────────────────────────┘
```

### Boundary Guarantees:
1. **Deterministic Rule Evaluator**: Every `ELIGIBILITY_RULE` evaluates attributes strictly (e.g. `age >= 60`, `total_household_income <= 120000`, `land_holding_acres <= 5.0`).
2. **Deterministic Fallback**: If Gemini or Pinecone is unreachable, the system automatically falls back to pre-compiled, verified structured guidance templates in Tamil with zero service degradation.
3. **Immutability of Results**: The Guidance Agent only receives pre-filtered lists of `eligible_schemes` and `partially_eligible_schemes`. It has no database mutation access and cannot alter matching verdicts.

---

## 3. Multi-Agent Lifecycle & Flow

### A. Conversational Intake Agent (LangGraph)
- **State Machine Nodes**:
  - `greet_and_start`: Detects new vs returning citizen; initial greeting.
  - `collect_family_info`: Gathers household composition, district, taluk, ration card color, and monthly income.
  - `collect_person_info`: Loops through family members. Features **adaptive branching** (e.g., asking land/crop questions only when `occupation = farmer`, asking disability category only when `disability_status = true`).
  - `confirm_and_summarize`: Reads back all extracted information in conversational Tamil for citizen confirmation or correction.
  - `save_to_database`: Writes confirmed data to `families` and `persons` tables.
- **State Persistence**: Supports resuming uncompleted intake turns via `/intake/resume`.

### B. Deterministic Eligibility Engine
- Evaluates individual rules (`applies_to = 'person'`) and household rules (`applies_to = 'family'`).
- Produces three distinct outcomes:
  - **Fully Eligible**: All rules satisfied.
  - **Partially Eligible**: Some conditions met, along with detailed diagnosis of failed rules (e.g. `Age is 45, requires >= 60`).
  - **Ineligible**: Categorically outside the scheme scope.

### C. Guidance Agent (Pinecone RAG + Gemini)
- Transforms eligibility results into an actionable citizen package:
  - Concise Tamil explanation of monetary and non-monetary benefits.
  - Official required document checklist (e.g. குடும்ப அட்டை, ஆதார் அட்டை, வருமானச் சான்றிதழ்).
  - Physical office location routing (VAO, Taluk Office, Agriculture Extension Center).
  - Step-by-step numbered instructions.
  - Freshness verification badge and staleness disclaimer if the scheme has not been re-verified within 180 days.

### D. Application Tracking & Freshness Maintenance
- **Application Lifecycle**: Tracks statuses (`not_started`, `documents_pending`, `submitted`, `under_review`, `approved`, `rejected`, `renewal_due`).
- **Follow-up Agent**: Periodically inspects stuck applications (`documents_pending` > 7 days) and generates targeted Tamil reminders listing only the missing documents.
- **Freshness Review Queue**: Flags schemes older than 180 days for manual human review by administrators. **Zero silent automated modifications** of government rules.

---

## 4. Security & Privacy Architecture

- **Row Level Security (RLS)**: Enforced via PostgreSQL policies in Supabase. Users can only select/insert/update family and person records where `user_id = auth.uid()` or `created_by = auth.uid()`.
- **Authentication**: Phone OTP flow returning signed HS256 JWT tokens, delivered via secure `httpOnly` cookies.
- **Rate Limiting**: In-memory token bucket sliding window protects against OTP spamming and eligibility scraping.
- **Brute-Force Lockout**: 5 failed OTP attempts trigger an automatic 10-minute lockout.
- **Input Sanitization**: Cleans free-text inputs of HTML tags, script handlers, and prompt injection signatures.
- **Error Consistency**: Standardized error response shape with bilingual English and citizen-safe Tamil messages.

---

## 5. API Endpoint Registry

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/phone/send-otp` | Request 6-digit OTP to mobile phone |
| `POST` | `/auth/phone/verify-otp` | Verify OTP and issue JWT session token |
| `GET` | `/auth/me` | Retrieve authenticated profile and managed family IDs |
| `POST` | `/auth/logout` | Clear authentication cookies |
| `POST` | `/families` | Register a new family household |
| `GET` | `/families/{id}` | Fetch family details and members |
| `PATCH` | `/families/{id}` | Update family household attributes |
| `POST` | `/families/{id}/persons` | Add an individual member to a family |
| `GET` | `/families/{id}/persons` | List all persons in a family |
| `GET` | `/persons/{id}` | Fetch individual person record |
| `PATCH` | `/persons/{id}` | Update person details |
| `GET` | `/schemes` | List welfare schemes with department/category filters |
| `GET` | `/schemes/{id_or_code}` | Fetch scheme details and attached eligibility rules |
| `GET` | `/glossary` | Search bilingual Tamil-English scheme glossary terms |
| `GET` | `/persons/{id}/eligibility` | Deterministic eligibility check for an individual |
| `GET` | `/families/{id}/eligibility` | Deterministic eligibility check for an entire household |
| `GET` | `/persons/{id}/guidance` | Generate step-by-step guidance action plan in Tamil |
| `GET` | `/families/{id}/guidance` | Generate household-wide guidance plans |
| `POST` | `/intake/message` | Process conversational intake turn in Tamil |
| `GET` | `/intake/resume` | Resume incomplete conversational intake session |
| `GET` | `/intake/logs` | Audit conversational extraction accuracy logs |
| `POST` | `/applications` | Create or update application tracking record |
| `GET` | `/persons/{id}/applications`| List application statuses for an individual |
| `PATCH` | `/applications/{id}` | Update application status or pending documents |
| `GET` | `/admin/freshness/review-queue` | Admin: List schemes flagged for staleness review |
| `POST` | `/admin/freshness/run-check` | Admin: Trigger automated freshness scan |
| `POST` | `/admin/freshness/verify/{id}` | Admin: Resolve stale scheme review |
| `POST` | `/admin/applications/trigger-followups` | Admin: Trigger follow-up reminder agent cycle |
| `GET` | `/admin/notifications` | Admin: View dispatched citizen notification logs |
| `GET` | `/admin/security/audit` | Admin: Verify database RLS policies and table security |
| `GET` | `/health` | Health and diagnostics check |
