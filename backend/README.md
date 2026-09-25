# Urimai AI — Backend

FastAPI service for **Urimai AI**, the Tamil Nadu government scheme eligibility platform.

## Architecture

- **Framework**: FastAPI (Python 3.12+)
- **Database**: Supabase / PostgreSQL (with SQLite support for isolated testing)
- **ORM / Migrations**: SQLAlchemy 2.0 & Alembic
- **Validation**: Pydantic v2
- **Testing**: Pytest & HTTPX TestClient

---

## Data Model

### `FAMILY`
- `id` (UUID, Primary Key)
- `composition_type` (Enum: `single`, `couple`, `nuclear`, `joint`)
- `district` (Text)
- `taluk` (Text)
- `address` (Text)
- `ration_card_type` (Enum: `none`, `green` [Rice], `white` [Sugar/No-commodity], `khaki` [Police], `phh_aay` [AAY], `orange`, `yellow`, `other`)
- `total_household_income` (Numeric, monthly)
- `created_at`, `updated_at` (Timestamps with timezone)

### `PERSON`
- `id` (UUID, Primary Key)
- `family_id` (UUID, FK -> `families.id` ON DELETE CASCADE)
- `name` (Text)
- `age` (Integer, validation: `age > 0`)
- `gender` (Enum: `male`, `female`, `transgender`, `other`)
- `education_level` (Enum: `none`, `primary`, `secondary`, `higher_secondary`, `graduate`, `postgraduate`, `dropout`)
- `occupation` (Enum: `farmer`, `daily_wage`, `self_employed`, `govt_employee`, `private_employee`, `unemployed`, `student`, `homemaker`, `retired`, `other`)
- `occupation_detail` (Text, nullable)
- `marital_status` (Enum: `single`, `married`, `widowed`, `divorced`)
- `caste_category` (Enum: `SC`, `ST`, `BC`, `MBC`, `DNC`, `General`)
- `disability_status` (Boolean, default `False`)
- `disability_type` (Text, nullable)
- `special_flags` (JSON / Text Array: `widow`, `destitute`, `folk_artist`, `journalist`, `registered_construction_worker`, `orphan`, `ex_serviceman`, etc.)
- `created_at`, `updated_at` (Timestamps with timezone)

### `SCHEME` (Phase 2)
- `id` (UUID, Primary Key)
- `scheme_code` (Text, Unique Short Code, e.g. `TN-SW-OAP`)
- `name_english` (Text)
- `name_tamil` (Text)
- `name_transliteration` (Text)
- `department` (Text)
- `category` (Text: `pension`, `marriage_assistance`, `disability_support`, `child_welfare`, `education_assistance`, `livelihood_support`, etc.)
- `description_english` (Text)
- `description_tamil` (Text)
- `benefit_amount` (Text: e.g. `₹1,000/month`, `₹50,000 + 8g Gold Coin`)
- `source_url` (Text, verified official government portal link)
- `last_verified_date` (Date)
- `is_active` (Boolean, default `True`)

### `ELIGIBILITY_RULE` (Phase 2)
- `id` (UUID, Primary Key)
- `scheme_id` (UUID, FK -> `schemes.id` ON DELETE CASCADE)
- `field_name` (Text, matches `Person` or `Family` column name)
- `operator` (Enum: `equals`, `not_equals`, `greater_than`, `less_than`, `greater_or_equal`, `less_or_equal`, `in_list`)
- `value` (Text)
- `applies_to` (Enum: `person`, `family`)

### `SCHEME_TERM_GLOSSARY` (Phase 2)
- `id` (UUID, Primary Key)
- `tamil_term` (Text)
- `english_equivalent` (Text)
### `INTAKE_EXTRACTION_LOG` (Phase 4)
- `id` (UUID, Primary Key)
- `session_id` (Text, indexed)
- `raw_tamil_input` (Text)
- `target_field` (Text)
- `extracted_value` (Text)
- `confirmed_value` (Text, nullable)
- `is_valid` (Boolean)
- `error_message` (Text, nullable)
- `created_at` (Timestamp with timezone)

---

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/families` | Create a new family |
| `GET` | `/families/{id}` | Fetch family details and member list |
| `PATCH` | `/families/{id}` | Update family attributes |
| `POST` | `/families/{id}/persons` | Add a person to a family (validates family exists) |
| `GET` | `/families/{id}/persons` | List all persons in a family |
| `GET` | `/persons/{id}` | Fetch a person by ID |
| `PATCH` | `/persons/{id}` | Update person details (e.g. occupation, marital status) |
| `GET` | `/schemes` | List schemes (filter by `department`, `category`, `is_active`) |
| `GET` | `/schemes/{id_or_code}` | Fetch full scheme details with attached eligibility rules |
| `GET` | `/glossary` | List bilingual terms (searchable via `?search=...`) |
| `GET` | `/persons/{id}/eligibility` | Evaluate all schemes for an individual (Phase 3) |
| `GET` | `/families/{id}/eligibility` | Evaluate all schemes for entire household (Phase 3) |
| `POST` | `/intake/message` | Process conversational Tamil turn & update LangGraph state (Phase 4) |
| `GET` | `/intake/state/{session_id}` | Retrieve intake session state (Phase 4) |
| `GET` | `/intake/logs` | Audit logs of Tamil input extractions (Phase 4) |
| `GET` | `/intake/chat` | Mobile-friendly interactive Tamil Web Chat UI (Phase 4) |
| `GET` | `/health` | Health check endpoint |
| `GET` | `/docs` | Interactive Swagger API documentation |


---

## Setup & Running

### 1. Create Virtual Environment & Install Dependencies
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Environment Variables
Copy `.env.example` to `.env`:
```powershell
Copy-Item .env.example .env
```
Update `DATABASE_URL` with your Supabase PostgreSQL connection string:
```
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
```

### 3. Migrations
Apply migrations via Alembic:
```powershell
alembic upgrade head
```
Or execute SQL scripts in Supabase SQL Editor:
- `migrations/001_initial_schema.sql` (Phase 1)
- `migrations/002_schemes_schema.sql` (Phase 2)

### 4. Seed Scheme Catalog & Glossary
```powershell
python -m app.seed_data
```

### 5. Start the Server
```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Interactive Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run Tests
```powershell
pytest tests -v
```
