import os
import json
from pathlib import Path
from app.seed_data import SCHEMES_DATA, GLOSSARY_DATA
from app.seed_data_departments.education import EDUCATION_SCHEMES
from app.seed_data_departments.agriculture import AGRICULTURE_SCHEMES
from app.seed_data_departments.labour import LABOUR_SCHEMES
from app.seed_data_departments.glossary import ADDITIONAL_GLOSSARY_DATA

all_schemes = SCHEMES_DATA + EDUCATION_SCHEMES + AGRICULTURE_SCHEMES + LABOUR_SCHEMES
all_glossary = GLOSSARY_DATA + ADDITIONAL_GLOSSARY_DATA

out = []
out.append('-- ==============================================================================')
out.append('-- Urimai AI — Complete Production Scheme & Glossary Seed Data')
out.append('-- Target: Supabase SQL Editor (Project: vabchcklkasdxjjdxomw)')
out.append('-- ==============================================================================\n')

# 1. Glossary
out.append('-- 1. Seed Glossary Terms')
for g in all_glossary:
    t = g['tamil_term'].replace("'", "''")
    e = g['english_equivalent'].replace("'", "''")
    n = (g.get('notes') or '').replace("'", "''")
    out.append(f"INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('{t}', '{e}', '{n}') ON CONFLICT DO NOTHING;")

out.append('\n-- 2. Seed Schemes and Eligibility Rules')
for s in all_schemes:
    code = s['scheme_code'].replace("'", "''")
    name_en = s['name_english'].replace("'", "''")
    name_ta = s['name_tamil'].replace("'", "''")
    translit = s['name_transliteration'].replace("'", "''")
    dept = s['department'].replace("'", "''")
    cat = s['category'].replace("'", "''")
    desc_en = s['description_english'].replace("'", "''")
    desc_ta = s['description_tamil'].replace("'", "''")
    benefit = s['benefit_amount'].replace("'", "''")
    url = (s.get('source_url') or '').replace("'", "''")
    v_date = str(s['last_verified_date'])
    docs_json = json.dumps(s.get('required_documents', []), ensure_ascii=False).replace("'", "''")
    office = s.get('application_office', 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்').replace("'", "''")
    app_mode = (s.get('application_mode').value if hasattr(s.get('application_mode'), 'value') else str(s.get('application_mode') or 'both')).replace("'", "''")
    online_url = s.get('online_application_url') or ''
    clean_online_url = online_url.replace("'", "''")
    online_sql = f"'{clean_online_url}'" if online_url else "NULL"
    proc_time = s.get('processing_time_estimate', '15 முதல் 30 நாட்கள்').replace("'", "''")

    out.append(f"""
DO $$
DECLARE
    v_scheme_id UUID;
BEGIN
    INSERT INTO schemes (
        scheme_code, name_english, name_tamil, name_transliteration,
        department, category, description_english, description_tamil,
        benefit_amount, source_url, last_verified_date, is_active,
        required_documents, application_office, application_mode,
        online_application_url, processing_time_estimate
    ) VALUES (
        '{code}', '{name_en}', '{name_ta}', '{translit}',
        '{dept}', '{cat}', '{desc_en}', '{desc_ta}',
        '{benefit}', '{url}', '{v_date}', true,
        '{docs_json}'::jsonb, '{office}', '{app_mode}',
        {online_sql}, '{proc_time}'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;""")

    for r in s.get('rules', []):
        fn = r['field_name'].replace("'", "''")
        op = (r['operator'].value if hasattr(r['operator'], 'value') else str(r['operator'])).replace("'", "''")
        val = str(r['value']).replace("'", "''")
        app = (r['applies_to'].value if hasattr(r['applies_to'], 'value') else str(r['applies_to'])).replace("'", "''")
        out.append(f"        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, '{fn}', '{op}', '{val}', '{app}');")

    out.append("    END IF;")
    out.append("END $$;")

target_file = Path(__file__).resolve().parent.parent / "migrations" / "seed_schemes_data.sql"
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print(f"Successfully generated {target_file} with {len(all_schemes)} schemes and {len(all_glossary)} glossary terms!")
