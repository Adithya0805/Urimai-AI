# 🏛️ உரிமை AI (Urimai AI)
### Single-Window Tamil Nadu Government Welfare Discovery & Assistance Platform
[![CI Status](https://img.shields.io/badge/CI-89%20Tests%20Passing-emerald?style=flat-square&logo=githubactions)](https://github.com/urimai-ai/urimai/actions)
[![Next.js](https://img.shields.io/badge/Next.js-16.3.6-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase%20RLS-336791?style=flat-square&logo=postgresql)](https://supabase.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Pro%2FFlash-4285F4?style=flat-square&logo=google)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 📖 Overview

**Urimai AI (உரிமை AI)** is an intelligent, bilingual (Tamil & English) single-window government welfare information counter digitized for the families of Tamil Nadu. Built specifically for citizens navigating government assistance—including elderly individuals, agricultural workers, and first-time smartphone users on low-end Android devices and patchy mobile data—Urimai AI determines household eligibility with **100% deterministic mathematical accuracy** across 5+ government departments, explains complex Government Orders (GOs) in clear spoken Tamil via grounded RAG, and delivers assistance through both a lightweight Web application and an interactive WhatsApp Business channel (`1/2/3` quick-replies).

---

## 📱 Product Experience & Citizen Flows

### 1. Web Counter Flow (Next.js 16)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏛️ உரிமை AI — தமிழ்நாடு அரசு நலத்திட்ட ஒற்றை சாளர உதவி மையம்                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [1] குடும்ப விவரங்கள்      [2] தகுதி கண்டறிதல்       [3] விண்ணப்ப வழிகாட்டி  │
│  ─────────────────────      ───────────────────       ─────────────────────  │
│  • மாவட்டம்: மதுரை           ✅ 4 திட்டங்களுக்கு முழு   📄 தேவையான ஆவணங்கள்:  │
│  • குடும்ப அட்டை: அரிசி அட்டை  தகுதி உள்ளது             - குடும்ப அட்டை நகல் │
│  • தொழில்: விவசாயி (நெல்)                              - கிராம நிர்வாக அலுவலர் │
│                             ⚠️ 2 திட்டங்களுக்கு          சான்றிதழ் (VAO)    │
│  👤 கந்தசாமி (65, ஆண்)        கூடுதல் ஆவணம் தேவை                             │
│                                                       🏢 வட்டாட்சியர்          │
│                                                          அலுவலகம் / இ-சேவை   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. WhatsApp Interactive Flow (`1/2/3` Quick-Replies)
```
[User]     -> வணக்கம்
[Urimai]   -> 🏛️ வணக்கம்! உரிமை AI உதவி மையத்திற்கு நல்வரவு.
              தொடங்க தங்கள் குடும்ப அமைப்பை தேர்வு செய்யவும்:
              1️⃣ தனி நபர் (Single)
              2️⃣ தம்பதியர் (Couple)
              3️⃣ அணு குடும்பம் (Nuclear)
              4️⃣ கூட்டுக் குடும்பம் (Joint)
[User]     -> 3
[Urimai]   -> தங்களின் மாவட்டம் எது?
[User]     -> தஞ்சாவூர்
...
[Urimai]   -> 🎉 நற்செய்தி கந்தசாமி! தங்களுக்கு 4 நலத்திட்டங்கள் கண்டறியப்பட்டன.
              📋 திட்டம் 1: முதலமைச்சரின் உழவர் பாதுகாப்புத் திட்டம்
              💰 பயன்: ₹1,000 / மாதம் + இயற்கை மரண ஈட்டுத்தொகை
              🏢 விண்ணப்பிக்கும் இடம்: வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்
              
              🔔 WhatsApp நினைவூட்டல் சேவையை இயக்க விரும்புகிறீர்களா?
              1️⃣ ஆம் (Yes)  2️⃣ வேண்டாம் (No)
```

---

## ⚡ Key Features

1. **Deterministic Eligibility Engine (Zero Hallucination)**:
   - Rule evaluation is strictly decoupled from LLMs using explicit relational algebra.
   - Covers 65+ verified schemes across Social Welfare, Education, Agriculture, Labour & Employment, and Adi Dravidar/Tribal Welfare.
2. **Conversational Tamil NLU & Adaptive Branching**:
   - Extracts structured criteria (ration cards, land holding acres, crop types, caste, disability, special tags) with graceful regex-first extraction and Gemini fallback.
3. **Cross-Channel Identity & Family Parity**:
   - Seamlessly switch between WhatsApp and the Web App with automatic phone number normalization (`+91XXXXXXXXXX`) and Supabase RLS isolation.
4. **Multi-Day Resume & Gap Handling**:
   - Paused conversations are automatically preserved; returning citizens can resume with one tap (`1. விட்ட இடத்திலிருந்து தொடர`).
5. **Grounded Scheme Guidance (RAG)**:
   - Delivers actionable step-by-step application instructions, required document checklists, and official portal links referenced against verified Tamil Nadu Government Orders.
6. **Proactive Follow-Up Agent**:
   - Automatically tracks pending document deficiencies and scheme renewal deadlines, dispatching 24h-compliant WhatsApp session messages or pre-approved Meta templates.
7. **Admin Review & Freshness Maintenance Dashboard**:
   - Internal dashboard with secure role-based access for scheme freshness audits, rule editing with dry-run verification, and real-time LLM audit logs.

---

## 🏗️ Repository Architecture (Monorepo)

```
Urimai AI/
├── backend/                        # FastAPI Python Backend
│   ├── app/
│   │   ├── api/                    # REST & Webhook Routers (Auth, Intake, Eligibility, WhatsApp, Admin)
│   │   ├── core/                   # Security, Sanitizer, Rate Limiter, Environment Config
│   │   ├── models/                 # SQLAlchemy ORM Models (Family, Person, Scheme, WhatsApp, Tracking)
│   │   ├── schemas/                # Pydantic Schemas & DTOs
│   │   └── services/               # Matching Engine, Guidance RAG, Intake Graph, WhatsApp Adapter
│   ├── migrations/                 # Sequential SQL Migrations (001 -> 010)
│   ├── scripts/                    # Production Migration & Security Verification Scripts
│   ├── tests/                      # 89 Comprehensive Pytest Suites (14 Modules)
│   ├── Dockerfile                  # Production Container Image
│   ├── railway.json                # Railway Deployment Configuration
│   └── requirements.txt            # Python Dependencies
├── frontend/                       # Next.js 16 Frontend (App Router)
│   ├── src/
│   │   ├── app/                    # Citizen UI, Admin Dashboard, Intake, Guidance, Tracker
│   │   ├── components/             # Reusable Tamil Typography & UI Components
│   │   └── lib/                    # API Client with Token Refresh & Retry Backoff
│   ├── public/                     # Static Assets
│   ├── vercel.json                 # Vercel Deployment Configuration
│   └── package.json                # Node Dependencies
├── .github/
│   └── workflows/
│       ├── ci.yml                  # GitHub Actions CI (Backend 89 Tests + Frontend Build)
│       └── deploy.yml              # Continuous Deployment Hooks
├── .gitignore                      # Strict Secret & Cache Exclusions
├── ARCHITECTURE.md                 # Complete Architectural Specification
├── LICENSE                         # MIT License
└── README.md                       # Project Documentation
```

---

## 🚀 Quickstart for Developers

### Prerequisites
- **Python**: 3.12+
- **Node.js**: 20.x+
- **PostgreSQL / Supabase**: Optional for local dev (defaults to local SQLite `urimai_local.db` if `DATABASE_URL` is omitted)

---

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate Python virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env to set your JWT_SECRET, GOOGLE_API_KEY (optional for LLM), etc.

# Run database migrations (or use default local SQLite)
python -m scripts.migrate_production

# Start development server
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
API Documentation will be available at: `http://127.0.0.1:8000/docs`

---

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Configure environment variables
cp .env.example .env.local
# Set NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000

# Start development server
npm run dev
```
Web app will be available at: `http://localhost:3000`

---

### 3. Running Tests & Security Audit

```bash
cd backend

# Run the complete test suite (89 tests across all 14 modules)
pytest -v

# Run migration sequence validation
pytest tests/test_migration_sequence.py -v

# Run production security & RLS verification
python scripts/verify_production_security.py
```

---

## 🔒 Security & Environment Separation

- **Strict Environment Isolation**: Production, Staging, and Development use isolated Supabase databases and API keys.
- **Row-Level Security (RLS)**: Enforced directly at the PostgreSQL catalog level on all critical tables (`families`, `persons`, `application_status`, `whatsapp_sessions`, `whatsapp_message_logs`).
- **Rate Limiting & Anti-Abuse**: In-memory token bucket rate limiting on `/auth/phone/send-otp` (3/min, 5 failed attempts lockout) and `/intake/chat` (20/min).
- **XSS & Injection Sanitization**: All incoming free-text is sanitized before entering ORM models or LLM prompts.
- **Zero Committed Secrets**: All secrets reside strictly in deployment environment stores (Vercel / Railway Secret Managers).

---

## 🌐 Deployed Environments

| Service | Environment | Provider | URL |
| :--- | :--- | :--- | :--- |
| **Frontend Web App** | Production | Vercel | `https://urimai.tn.gov.in` / `https://urimai-app.vercel.app` |
| **Backend REST API** | Production | Railway | `https://api.urimai.tn.gov.in` / `https://urimai-api.up.railway.app` |
| **Database** | Production | Supabase | Managed PostgreSQL with RLS (`ap-south-1`) |
| **WhatsApp Channel** | Production | Meta / Twilio | `+91 94441 99999` (`POST /whatsapp/webhook`) |

---

## 🤝 Contributing & Branch Protection

1. **Branch Protection**: The `main` branch requires all status checks to pass before merging:
   - `Backend Test Suite & Security Audit` (All 89 Pytest suites)
   - `Frontend Build & Typecheck` (`npm run build`)
2. **Pull Request Process**:
   - Create a feature branch (`git checkout -b feature/scheme-updates`).
   - Ensure all tests pass locally (`pytest`).
   - Open a PR against `main` for automated CI validation.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
