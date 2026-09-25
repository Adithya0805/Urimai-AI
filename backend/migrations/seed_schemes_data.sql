-- ==============================================================================
-- Urimai AI — Complete Production Scheme & Glossary Seed Data
-- Target: Supabase SQL Editor (Project: vabchcklkasdxjjdxomw)
-- ==============================================================================

-- 1. Seed Glossary Terms
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('அந்தியோதயா அன்ன யோஜனா அட்டை (PHH-AAY)', 'Antyodaya Anna Yojana Card (Poorest of the poor)', 'Issued to the most destitute families, entitled to 35 kg of free rice per month under TNPDS.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('முன்னுரிமை குடும்ப அட்டை (PHH)', 'Priority Household Card (Rice Card)', 'Green smart card issued to low-income families entitled to rice and subsidized essential commodities.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('முன்னுரிமையற்ற சர்க்கரை அட்டை (NPHH-S)', 'Non-Priority Household - Sugar Card', 'White smart card holders who opted for additional sugar in lieu of rice.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பொருளற்ற அட்டை (NPHH-NC)', 'No Commodity Card', 'White smart card serving purely as an official proof of residence and identity; no commodities issued.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('காவல்துறை குடும்ப அட்டை (Khaki Card)', 'Police Personnel Ration Card', 'Special card issued to serving police personnel for essential commodities at subsidized rates.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ஆதிதிராவிடர் / பட்டியல் சாதியினர் (SC)', 'Scheduled Caste (SC)', 'Official category in Tamil Nadu encompassing Adi Dravidar and Arundhathiyar communities.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பழங்குடியினர் (ST)', 'Scheduled Tribe (ST)', 'Indigenous tribal communities recognized under the Constitution of India.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பிற்படுத்தப்பட்டோர் (BC)', 'Backward Classes (BC)', 'State backward classes eligible for specific welfare quotas and scholarships.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மிகவும் பிற்படுத்தப்பட்டோர் (MBC)', 'Most Backward Classes (MBC)', 'Socio-economically disadvantaged communities distinct from BC.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சீர்மரபினர் (DNC)', 'De-Notified Communities (DNC)', 'Historical denotified tribes eligible for specialized welfare board schemes in Tamil Nadu.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பொதுப்பிரிவு (General / OC)', 'General Category / Open Category', 'Applicants not belonging to SC/ST/BC/MBC/DNC reservations.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சமூக நலம் மற்றும் மகளிர் உரிமைத்துறை', 'Social Welfare & Women Empowerment Department', 'Main state department managing women, children, elderly pensions, marriage, and empowerment schemes.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மாற்றுத்திறனாளிகள் நலத்துறை', 'Differently Abled Welfare Department', 'Oversees maintenance allowance, assistive devices, and rehabilitation for persons with disabilities.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('வருவாய்த்துறை (சமூகப் பாதுகாப்புத் திட்டங்கள்)', 'Revenue and Disaster Management Department (Social Security Schemes)', 'Disburses monthly pensions such as OAP, Destitute Widow, and Deserted Wives pensions.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ஆதரவற்ற விதவை', 'Destitute Widow', 'A widowed woman lacking independent financial support or property exceeding limits, certified by revenue authorities.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('முதியோர் ஓய்வூதியம் (OAP)', 'Old Age Pension', 'Monthly social security allowance for destitute senior citizens aged 60 and above.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கணவனால் கைவிடப்பட்ட பெண்', 'Deserted Wife', 'A woman legally divorced or separated from husband for over 5 years without alimony or maintenance.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('திருமாங்கல்யத்திற்கு தங்கம்', 'Gold for Thirumangalyam', '1 sovereign (8 grams) of 22k gold given along with cash assistance in marriage schemes.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('உரிமைத்தொகை', 'Entitlement / Rightful Grant', 'Direct bank transfer grant, e.g., Kalaignar Magalir Urimai Thogai (KMUT) ₹1,000/month for women heads.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பராமரிப்பு உதவித்தொகை', 'Maintenance Allowance', 'Monthly grant for severely disabled, mentally challenged, or muscular dystrophy patients.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மாற்றுத்திறனாளி அடையாள அட்டை (UDID)', 'Unique Disability ID (UDID)', 'Standard national identity card indicating disability percentage required for all welfare benefits.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('இணைப்புச் சக்கரம் பொருத்தப்பட்ட வாகனம்', 'Retrofitted Motorized Vehicle', 'Motor scooter adapted with two rear support wheels for orthopaedically challenged individuals.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('இலவச தையல் இயந்திரம்', 'Free Sewing Machine', 'Livelihood support provided under Sathiyavani Muthu Ammaiyar scheme for trained women and persons with disabilities.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கல்வி உதவித்தொகை', 'Scholarship', 'Financial grant awarded to students by government departments based on caste, merit, or income.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('முதல் தலைமுறை பட்டதாரி', 'First Generation Graduate', 'An applicant who is the first person in their family to complete an undergraduate degree.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('போஸ்ட் மெட்ரிக்', 'Post-Matric', 'Educational stage after passing class 10, covering Plus Two, ITI, Diploma, and College courses.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ப்ரீ-மெட்ரிக்', 'Pre-Matric', 'School education stage prior to class 10 (classes 1 through 10).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கல்விக் கட்டண விலக்கு', 'Tuition Fee Exemption', 'Full or partial waiver of tuition and admission fees for eligible reserved category students.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சிறு விவசாயி', 'Small Farmer', 'Farmer holding more than 2.5 acres and up to 5.0 acres of dry land (or up to 2.5 acres of wet land).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('குறு விவசாயி', 'Marginal Farmer', 'Farmer holding up to 2.5 acres of dry land (or up to 1.25 acres of wet land).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பட்டா', 'Patta (Land Title Deed)', 'Official legal revenue document proving ownership of land issued by Tamil Nadu Government.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சிட்டா', 'Chitta (Land Holding Extract)', 'Revenue record specifying land classification (wet/dry), survey number, area, and owner name.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('அடங்கல்', 'Adangal (Crop Cultivation Register)', 'Village administrative record (Register No. 2) recording actual crop cultivated in each survey number.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சொட்டு நீர்ப்பாசனம்', 'Drip Irrigation', 'Micro-irrigation system delivering water and nutrients directly to plant roots at low pressure.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பயிர் காப்பீடு', 'Crop Insurance', 'Financial protection scheme against crop failure due to weather perils and natural calamities (PMFBY).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('உழவர் பாதுகாப்பு அட்டை', 'Farmers Social Security Card', 'Identity card issued to agricultural workers and small farmers under Chief Minister''s Uzhavar Pathukappu Thittam.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மானாவாரி நிலம்', 'Rainfed / Dry Land (Punjai)', 'Agricultural land cultivated depending entirely on seasonal rainfall without perennial canal/well irrigation.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கட்டுமான நல வாரியம்', 'Construction Workers Welfare Board', 'Statutory board in Tamil Nadu providing social security, pensions, and accident relief to construction labourers.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('அமைப்புசாரா தொழிலாளர்', 'Unorganized Worker', 'Daily wage or self-employed labourer not covered by formal pension or provident fund schemes.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('வேலைவாய்ப்பற்றோர் உதவித்தொகை', 'Unemployment Assistance Allowance', 'Monthly cash stipend provided by Tamil Nadu employment exchanges to registered long-term job seekers.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ஈமச்சடங்கு உதவி', 'Funeral Assistance', 'Immediate ex-gratia financial grant paid upon the death of an enrolled welfare board worker.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மகப்பேறு உதவி', 'Maternity Benefit', 'Financial assistance paid to registered female workers for delivery and postnatal care.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கல்வி உதவித்தொகை', 'Scholarship', 'Financial grant awarded to students by government departments based on caste, merit, or income.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('முதல் தலைமுறை பட்டதாரி', 'First Generation Graduate', 'An applicant who is the first person in their family to complete an undergraduate degree.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('போஸ்ட் மெட்ரிக்', 'Post-Matric', 'Educational stage after passing class 10, covering Plus Two, ITI, Diploma, and College courses.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ப்ரீ-மெட்ரிக்', 'Pre-Matric', 'School education stage prior to class 10 (classes 1 through 10).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கல்விக் கட்டண விலக்கு', 'Tuition Fee Exemption', 'Full or partial waiver of tuition and admission fees for eligible reserved category students.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சிறு விவசாயி', 'Small Farmer', 'Farmer holding more than 2.5 acres and up to 5.0 acres of dry land (or up to 2.5 acres of wet land).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('குறு விவசாயி', 'Marginal Farmer', 'Farmer holding up to 2.5 acres of dry land (or up to 1.25 acres of wet land).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பட்டா', 'Patta (Land Title Deed)', 'Official legal revenue document proving ownership of land issued by Tamil Nadu Government.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சிட்டா', 'Chitta (Land Holding Extract)', 'Revenue record specifying land classification (wet/dry), survey number, area, and owner name.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('அடங்கல்', 'Adangal (Crop Cultivation Register)', 'Village administrative record (Register No. 2) recording actual crop cultivated in each survey number.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('சொட்டு நீர்ப்பாசனம்', 'Drip Irrigation', 'Micro-irrigation system delivering water and nutrients directly to plant roots at low pressure.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('பயிர் காப்பீடு', 'Crop Insurance', 'Financial protection scheme against crop failure due to weather perils and natural calamities (PMFBY).') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('உழவர் பாதுகாப்பு அட்டை', 'Farmers Social Security Card', 'Identity card issued to agricultural workers and small farmers under Chief Minister''s Uzhavar Pathukappu Thittam.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மானாவாரி நிலம்', 'Rainfed / Dry Land (Punjai)', 'Agricultural land cultivated depending entirely on seasonal rainfall without perennial canal/well irrigation.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('கட்டுமான நல வாரியம்', 'Construction Workers Welfare Board', 'Statutory board in Tamil Nadu providing social security, pensions, and accident relief to construction labourers.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('அமைப்புசாரா தொழிலாளர்', 'Unorganized Worker', 'Daily wage or self-employed labourer not covered by formal pension or provident fund schemes.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('வேலைவாய்ப்பற்றோர் உதவித்தொகை', 'Unemployment Assistance Allowance', 'Monthly cash stipend provided by Tamil Nadu employment exchanges to registered long-term job seekers.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('ஈமச்சடங்கு உதவி', 'Funeral Assistance', 'Immediate ex-gratia financial grant paid upon the death of an enrolled welfare board worker.') ON CONFLICT DO NOTHING;
INSERT INTO scheme_term_glossary (tamil_term, english_equivalent, notes) VALUES ('மகப்பேறு உதவி', 'Maternity Benefit', 'Financial assistance paid to registered female workers for delivery and postnatal care.') ON CONFLICT DO NOTHING;

-- 2. Seed Schemes and Eligibility Rules

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
        'TN-SW-OAP', 'Indira Gandhi National Old Age Pension Scheme / State Old Age Pension', 'இந்திரா காந்தி தேசிய முதியோர் ஓய்வூதியத் திட்டம் / மாநில முதியோர் ஓய்வூதியம்', 'Indira Gandhi Desiya Mudhiyor Oivoodhiya Thittam',
        'Social Welfare & Women Empowerment', 'pension', 'Monthly financial assistance provided to destitute senior citizens aged 60 and above belonging to below poverty line households with no other source of livelihood.', 'வாழ்வாதாரமற்ற, வறுமைக் கோட்டிற்கு கீழ் உள்ள 60 வயது மற்றும் அதற்கு மேற்பட்ட முதியோர்களுக்கு வழங்கப்படும் மாதாந்திர ஓய்வூதிய உதவி.',
        '₹1,000/month', 'https://www.tnesevai.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை (Ration Card)", "வயதுச் சான்றிதழ் (Age Proof)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)", "வருமானச் சான்றிதழ் (Income Certificate)"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் (சமூகப் பாதுகாப்புத் திட்டம்) / அருகிலுள்ள இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'destitute', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '10000', 'family');
    END IF;
END $$;

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
        'TN-SW-DWP', 'Destitute Widow Pension Scheme (DWPS)', 'ஆதரவற்ற விதவை ஓய்வூதியத் திட்டம்', 'Aadharavatra Vidhavai Oivoodhiya Thittam',
        'Social Welfare & Women Empowerment', 'pension', 'Monthly social security pension for destitute widows aged 18 and above who have no regular income or support.', 'வருமானம் மற்றும் ஆதரவற்ற 18 வயதுக்கு மேற்பட்ட விதவைப் பெண்களுக்கு வழங்கப்படும் மாதாந்திர சமூகப் பாதுகாப்பு ஓய்வூதியம்.',
        '₹1,000/month', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை (Ration Card)", "கணவரின் இறப்புச் சான்றிதழ் (Husband''s Death Certificate)", "ஆதரவற்ற விதவை சான்றிதழ் (Destitute Widow Certificate)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் (Taluk Office) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'widowed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'destitute', 'person');
    END IF;
END $$;

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
        'TN-SW-DDWP', 'Destitute Deserted Wives Pension Scheme (DDWPS)', 'ஆதரவற்ற கணவனால் கைவிடப்பட்ட பெண்கள் ஓய்வூதியத் திட்டம்', 'Aadharavatra Kanavanal Kaividapatta Pengal Oivoodhiya Thittam',
        'Social Welfare & Women Empowerment', 'pension', 'Financial pension for women aged 30 and above who are deserted/separated from their husbands and destitute.', 'கணவனால் கைவிடப்பட்டு, ஆதரவற்ற நிலையில் உள்ள 30 வயதுக்கு மேற்பட்ட பெண்களுக்கு வழங்கப்படும் மாதாந்திர ஓய்வூதியம்.',
        '₹1,000/month', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை (Ration Card)", "விவாகரத்து ஆணை அல்லது பிரிந்து வாழும் சான்றிதழ் (Separation Proof from VAO)", "வட்டாட்சியர் வருமானச் சான்று", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'divorced', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '30', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'destitute', 'person');
    END IF;
END $$;

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
        'TN-SW-UPIWP', 'Unmarried Poor Incapacitated Women Pension Scheme', '50 வயதுக்கு மேற்பட்ட ஆதரவற்ற திருமணமாகாத ஏழைப் பெண்கள் ஓய்வூதியத் திட்டம்', 'Thirumanamagaadha Ezhai Pengal Oivoodhiya Thittam',
        'Social Welfare & Women Empowerment', 'pension', 'Monthly pension for unmarried, destitute women aged 50 and above who have no family livelihood support.', 'குடும்ப ஆதரவு இல்லாத 50 வயதுக்கு மேற்பட்ட ஆதரவற்ற திருமணமாகாத ஏழைப் பெண்களுக்கு வழங்கப்படும் ஓய்வூதியம்.',
        '₹1,000/month', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை (Ration Card)", "வயதுச் சான்றிதழ் (50 வயதுக்கு மேல்)", "திருமணமாகாதவர் சான்று (Unmarried Certificate)", "வருமானச் சான்றிதழ்"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'single', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '50', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'destitute', 'person');
    END IF;
END $$;

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
        'TN-SW-DAP', 'Maintenance Allowance / Pension for Differently Abled Persons', 'மாற்றுத்திறனாளிகளுக்கான பராமரிப்பு உதவித்தொகை / ஓய்வூதியத் திட்டம்', 'Maatruthranali Paramarippu Udhavithogai Thittam',
        'Differently Abled Welfare', 'disability_support', 'Monthly financial maintenance allowance for destitute differently abled persons with benchmark disability.', 'மாற்றுத்திறனாளிகளுக்கு அவர்களின் வாழ்வாதாரத்திற்காகவும் பராமரிப்பிற்காகவும் வழங்கப்படும் மாதாந்திர உதவித்தொகை.',
        '₹1,500/month', 'https://www.scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "மருத்துவச் சான்றிதழ் (Medical Certificate - 40%+ disability)", "ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை (Ration Card)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO) / மாவட்ட ஆட்சியரகம்', 'both',
        'https://www.scd.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-SW-KMUT', 'Kalaignar Magalir Urimai Thittam (KMUT)', 'கலைஞர் மகளிர் உரிமைத் திட்டம்', 'Kalaignar Magalir Urimai Thittam',
        'Social Welfare & Women Empowerment', 'social_security', 'Monthly financial entitlement for eligible women heads of households with annual family income below ₹2.5 lakh, electricity consumption below 3600 units, and land holding limits.', 'ஆண்டு குடும்ப வருமானம் ₹2.5 லட்சத்திற்குள் உள்ள தகுதியான குடும்பத் தலைவிகளுக்கு மாதம் ₹1,000 வழங்கும் முதன்மை உரிமைத் திட்டம்.',
        '₹1,000/month', 'https://kmut.tn.gov.in/', '2026-08-01', true,
        '["குடும்ப அட்டை (Smart Ration Card)", "ஆதார் அட்டை (Aadhaar Card)", "குடும்ப தலைவியின் வங்கி பாஸ்புக்", "மின்சார இணைப்பு நுகர்வோர் எண் (Electricity Consumer Number)"]'::jsonb, 'வட்ட வழங்கல் அலுவலகம் / சிறப்பு முகாம்கள் / இ-சேவை மையம்', 'both',
        'https://kmut.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '21', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '20833', 'family');
    END IF;
END $$;

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
        'TN-SW-PUDHUMAI-PENN', 'Moovalur Ramamirtham Ammaiyar Higher Education Assurance Scheme (Pudhumai Penn)', 'மூவலூர் ராமாமிர்தம் அம்மையார் உயர்கல்வி உறுதித் திட்டம் (புதுமைப் பெண் திட்டம்)', 'Moovalur Ramamirtham Ammaiyar Pudhumai Penn Thittam',
        'Social Welfare & Women Empowerment', 'education_assistance', 'Monthly financial aid to female students pursuing higher education (degrees/diplomas) who studied from classes 6 to 12 in Tamil Nadu government schools.', 'அரசுப் பள்ளிகளில் 6 முதல் 12 ஆம் வகுப்பு வரை படித்து உயர்கல்வி பயிலும் மாணவிகளுக்கு மாதம் ₹1,000 வழங்கும் திட்டம்.',
        '₹1,000/month', 'https://pudhumaipenn.tn.gov.in/', '2026-08-01', true,
        '["6 முதல் 12 ஆம் வகுப்பு அரசுப் பள்ளி பயின்ற சான்றிதழ் (EMIS School Certificate)", "கல்லூரி சேர்க்கை அடையாள அட்டை (College ID / Bonafide)", "மாணவியின் ஆதார் அட்டை", "வங்கி கணக்கு புத்தகம்", "10, 12 ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்"]'::jsonb, 'கல்லூரி முதல்வர் அலுவலகம் / கல்லூரி நோடல் அலுவலர்', 'online',
        'https://pudhumaipenn.tn.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-SW-SEWING-MACHINE', 'Sathiyavani Muthu Ammaiyar Ninaivu Free Supply of Sewing Machine Scheme', 'சத்தியவாணி முத்து அம்மையார் நினைவு இலவச தையல் இயந்திரம் வழங்கும் திட்டம்', 'Sathiyavani Muthu Ammaiyar Ninaivu Ilavasa Thaiyal Iyandhira Thittam',
        'Social Welfare & Women Empowerment', 'livelihood_support', 'Free supply of sewing machine with accessories to destitute women, widows, deserted wives, and differently abled persons aged 20-40 with annual family income up to ₹72,000 who possess tailoring skills.', 'தையல் கலை தெரிந்த 20 முதல் 40 வயதுடைய ஆதரவற்ற பெண்கள், விதவைகள், கணவனால் கைவிடப்பட்டோர் மற்றும் மாற்றுத்திறனாளிகளுக்கு இலவச தையல் இயந்திரம் வழங்கும் திட்டம்.',
        '1 Free Sewing Machine with accessories', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["தையல் கலை பயின்றதற்கான சான்றிதழ் (Tailoring Course Certificate)", "வருமானச் சான்றிதழ் (ஆண்டு வருமானம் ₹72,000-க்குள்)", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை", "வயதுச் சான்று (20-40 வயது)", "விதவை/ஆதரவற்றோர்/மாற்றுத்திறனாளி சான்றிதழ் (பொருந்துமாயின்)"]'::jsonb, 'வட்டார வளர்ச்சி அலுவலகம் (BDO Office) / மாவட்ட சமூக நல அலுவலகம் (DSWO)', 'both',
        'https://www.tnsocialwelfare.tn.gov.in/', '45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '20', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '6000', 'family');
    END IF;
END $$;

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
        'TN-SW-WIDOW-REMARRIAGE', 'Dr. Dharmambal Ammaiyar Ninaivu Widow Remarriage Assistance Scheme', 'டாக்டர் தர்மாம்பாள் அம்மையார் நினைவு விதவை மறுமண நிதியுதவித் திட்டம்', 'Dr Dharmambal Ammaiyar Ninaivu Vidhavai Marumana Thittam',
        'Social Welfare & Women Empowerment', 'marriage_assistance', 'Financial grant and gold coin for Thirumangalyam provided to encourage widow remarriage. Bride must be aged 20 or above.', 'விதவைப் பெண்கள் மறுமணம் செய்து கொள்வதை ஊக்குவிக்க திருமாங்கல்யத்திற்கான தங்க நாணயம் மற்றும் நிதியுதவி வழங்கும் திட்டம்.',
        '₹25,000 to ₹50,000 + 8g Gold Coin', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["முதல் கணவரின் இறப்புச் சான்றிதழ் (First Husband Death Certificate)", "மறுமண அழைப்பிதழ் / திருமண பதிவுச் சான்றிதழ்", "மணமகள், மணமகன் வயதுச் சான்று மற்றும் ஆதார் அட்டை", "பட்டதாரி சான்றிதழ் (திட்டம்-II எனில்)"]'::jsonb, 'மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'widowed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '20', 'person');
    END IF;
END $$;

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
        'TN-SW-POOR-WIDOW-DAUGHTER', 'E.V.R. Maniammaiyar Ninaivu Marriage Assistance Scheme for Daughters of Poor Widows', 'ஈ.வெ.ரா. மணியம்மையார் நினைவு ஏழை விதவைகளின் மகள்கள் திருமண நிதியுதவித் திட்டம்', 'EVR Maniammaiyar Ninaivu Ezhai Vidhavaigalin Magalgal Thirumana Thittam',
        'Social Welfare & Women Empowerment', 'marriage_assistance', 'Marriage financial assistance and 8g gold coin to poor widows to perform the marriage of their daughters (bride aged 18+, annual income limit ₹72,000).', 'ஏழை விதவைகளின் மகள்களின் திருமணத்தை நடத்துவதற்கு வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.',
        '₹25,000 to ₹50,000 + 8g Gold Coin', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["தாய் விதவை என்பதற்கான இறப்புச் சான்றிதழ்", "குடும்ப வருமானச் சான்றிதழ் (₹72,000-க்குள்)", "திருமண அழைப்பிதழ்", "மணமகள் 10-ஆம் வகுப்பு / பட்டதாரி சான்றிதழ்", "ஆதார் மற்றும் ரேஷன் கார்டு"]'::jsonb, 'மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'single', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '6000', 'family');
    END IF;
END $$;

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
        'TN-SW-ORPHAN-GIRL-MARRIAGE', 'Annai Teresa Ninaivu Marriage Assistance Scheme for Orphan Girls', 'அன்னை தெரசா நினைவு ஆதரவற்ற பெண் குழந்தைகள் திருமண நிதியுதவித் திட்டம்', 'Annai Teresa Ninaivu Aadharavatra Pengal Thirumana Thittam',
        'Social Welfare & Women Empowerment', 'marriage_assistance', 'Marriage financial assistance and 8g gold coin for orphan girls (who have lost both parents) aged 18 and above. No income ceiling applies.', 'தாய், தந்தை இருவரையும் இழந்த ஆதரவற்ற பெண்களின் திருமணத்திற்காக வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.',
        '₹25,000 to ₹50,000 + 8g Gold Coin', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["தாய் மற்றும் தந்தை இருவரின் இறப்புச் சான்றிதழ்கள் (Death Certificates of parents)", "அனாதை / ஆதரவற்ற பெண் சான்றிதழ் (Orphan Certificate from MP/MLA/Tahsildar)", "திருமண அழைப்பிதழ்", "மணமகள் வயதுச் சான்று மற்றும் ஆதார் அட்டை"]'::jsonb, 'மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'single', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'orphan', 'person');
    END IF;
END $$;

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
        'TN-SW-INTERCASTE-MARRIAGE', 'Dr. Muthulakshmi Reddy Ninaivu Inter-Caste Marriage Assistance Scheme', 'டாக்டர் முத்துலட்சுமி ரெட்டி நினைவு கலப்புத் திருமண நிதியுதவித் திட்டம்', 'Dr Muthulakshmi Reddy Ninaivu Kalappu Thirumana Thittam',
        'Social Welfare & Women Empowerment', 'marriage_assistance', 'Financial grant and gold coin to encourage inter-caste marriages (Category I: SC/ST with other communities; Category II: Forward communities with BC/MBC). No income ceiling.', 'சாதி பாகுபாடுகளைக் களைய கலப்புத் திருமணம் செய்து கொள்ளும் தம்பதியருக்கு வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.',
        '₹25,000 to ₹50,000 + 8g Gold Coin', 'https://www.tnsocialwelfare.tn.gov.in/', '2026-08-01', true,
        '["திருமண பதிவுச் சான்றிதழ் (Marriage Registration Certificate)", "மணமகன் மற்றும் மணமகள் இருவரின் சாதிச் சான்றிதழ்கள் (Community Certificates)", "வயதுச் சான்றிதழ் மற்றும் ஆதார் அட்டைகள்", "கல்வி சான்றிதழ் (திட்டம்-II எனில்)"]'::jsonb, 'மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'single', 'person');
    END IF;
END $$;

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
        'TN-SW-GIRL-CHILD-1', 'Chief Minister''s Girl Child Protection Scheme (Scheme I)', 'முதலமைச்சரின் பெண் குழந்தை பாதுகாப்புத் திட்டம் (திட்டம்-I)', 'Mudalamaicharin Penn Kuzhandhai Paadhukaappu Thittam',
        'Social Welfare & Women Empowerment', 'child_welfare', 'Fixed deposit of ₹50,000 with annual educational incentive of ₹1,800 from 6th year for families with only one girl child and no male children, parental sterilization before age 40, and annual income within ₹72,000.', 'ஒரே ஒரு பெண் குழந்தை மட்டும் உள்ள ஏழைக் குடும்பங்களுக்கு ₹50,000 நிலையான வைப்பு நிதி மற்றும் ஆண்டு கல்வி உதவித்தொகை வழங்கும் திட்டம்.',
        '₹50,000 Fixed Deposit + ₹1,800/year incentive', 'https://www.tnsocialwelfare.tn.gov.in/', '2025-08-01', true,
        '["பெண் குழந்தையின் பிறப்புச் சான்றிதழ் (Birth Certificate)", "பெற்றோர் குடும்பக் கட்டுப்பாடு சான்றிதழ் (Sterilization Certificate before age 40)", "குடும்ப வருமானச் சான்று (₹72,000-க்குள்)", "ஆண் குழந்தை இல்லை என்பதற்கான சான்று (No male child certificate from VAO)"]'::jsonb, 'வட்டார வளர்ச்சி அலுவலகம் (BDO) / மாவட்ட சமூக நல அலுவலகம் (DSWO)', 'offline',
        NULL, '45 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '3', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '6000', 'family');
    END IF;
END $$;

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
        'TN-SW-DA-MOTOR-VEHICLE', 'Retrofitted Motorized Vehicles for Differently Abled Persons', 'மாற்றுத்திறனாளிகளுக்கு இணைப்புச் சக்கரங்கள் பொருத்தப்பட்ட மோட்டார் வாகனம் வழங்கும் திட்டம்', 'Inaippu Sakkarangal Poruthapatta Motor Vaaganam Thittam',
        'Differently Abled Welfare', 'disability_support', 'Free retrofitted petrol scooter with side wheels provided to locomotor-disabled persons (both legs affected) aged 18 and above who are studying or working.', 'இரு கால்களும் பாதிக்கப்பட்ட 18 வயதுக்கு மேற்பட்ட மாற்றுத்திறனாளி மாணவர்கள் மற்றும் உழைக்கும் நபர்களுக்கு இலவச மோட்டார் வாகனம்.',
        '1 Free Retrofitted Motor Scooter', 'https://www.scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "இரு கால்களும் பாதிக்கப்பட்ட மருத்துவச் சான்றிதழ்", "ஓட்டுநர் உரிமம் (Driving License / LLR for invalid carriage)", "வேலை அல்லது கல்லூரி பயில்வதற்கான சான்று", "ஆதார் மற்றும் குடும்ப அட்டை"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO)', 'both',
        'https://www.scd.tn.gov.in/', '60 முதல் 90 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-SW-DA-AIDS-APPLIANCES', 'Free Supply of Assistive Devices (Tricycles, Wheelchairs, Hearing Aids)', 'மாற்றுத்திறனாளிகளுக்கு உதவி உபகரணங்கள் (முச்சக்கர வண்டி, சக்கர நாற்காலி, காதொலிக் கருவி) வழங்கும் திட்டம்', 'Maatruthranali Udhavi Ubakaranangal Ilavasa Vazhangum Thittam',
        'Differently Abled Welfare', 'disability_support', 'Free assistive aids including tricycles, manual and battery wheelchairs, crutches, calipers, hearing aids, and Braille watches for verified differently abled beneficiaries.', 'தகுதியுடைய மாற்றுத்திறனாளிகளுக்கு முச்சக்கர வண்டிகள், சக்கர நாற்காலிகள், காதொலிக் கருவிகள் மற்றும் பிரெய்லி கடிகாரங்கள் இலவசமாக வழங்குதல்.',
        'Free assistive devices as per medical prescription', 'https://www.scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி அடையாள அட்டை (UDID)", "மருத்துவ அதிகாரியின் உபகரண பரிந்துரை சீட்டு", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை", "புகைப்படம் (முழு உருவப்படம்)"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO) / சிறப்பு முகாம்கள்', 'both',
        'https://www.scd.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
    END IF;
END $$;

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
        'TN-SW-DA-MARRIAGE', 'Marriage Assistance Scheme for Normal Persons Marrying Differently Abled Persons', 'மாற்றுத்திறனாளிகளை திருமணம் செய்து கொள்வோருக்கான திருமண நிதியுதவித் திட்டம்', 'Maatruthranali Thirumana Udhavithogai Thittam',
        'Differently Abled Welfare', 'marriage_assistance', 'Financial assistance of ₹25,000/₹50,000 along with an 8g gold coin to encourage normal individuals to marry visually, hearing, or locomotor impaired persons.', 'மாற்றுத்திறனாளிகளை மணம் முடிக்கும் இயல்பான நபர்களை ஊக்குவிக்க வழங்கப்படும் திருமண உதவித்தொகை மற்றும் 8 கிராம் தங்க நாணயம்.',
        '₹25,000 to ₹50,000 + 8g Gold Coin', 'https://www.scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி துணைவரின் அடையாள அட்டை (UDID) மற்றும் மருத்துவச் சான்றிதழ்", "திருமண அழைப்பிதழ் / திருமண பதிவுச் சான்றிதழ்", "இருவரின் வயதுச் சான்று மற்றும் ஆதார் அட்டை", "முன்மணம் செய்யாததற்கான சான்றிதழ்"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO)', 'both',
        'https://www.scd.tn.gov.in/', '45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'single', 'person');
    END IF;
END $$;

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
        'TN-EDU-POST-MATRIC-SC', 'Post-Matric Scholarship Scheme for SC and ST Students', 'பட்டியலினம் மற்றும் பழங்குடியினர் மாணவர்களுக்கான போஸ்ட் மெட்ரிக் கல்வி உதவித்தொகை', 'Post-Matric Kalvi Uvithogai SC ST',
        'Education', 'scholarship', '100% compulsory tuition fee waiver, maintenance allowance, and book grant for SC and ST students pursuing Higher Secondary and College degree courses.', '11, 12-ஆம் வகுப்பு மற்றும் கல்லூரி உயர்கல்வி பயிலும் பட்டியலினம் (SC) மற்றும் பழங்குடியினர் (ST) மாணவர்களுக்கான முழு கல்விக் கட்டண விலக்கு மற்றும் உதவித்தொகை.',
        '₹10,000 to ₹50,000/year (100% Fee Waiver)', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "மதிப்பெண் சான்றிதழ் (Marksheet)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)", "கல்லூரி சேர்க்கை சான்று (College Bonafide Certificate)"]'::jsonb, 'கல்லூரி முதல்வர் அலுவலகம் / மாவட்ட ஆதிதிராவிடர் நல அலுவலகம்', 'online',
        'https://adwscholarship.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '20833', 'family');
    END IF;
END $$;

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
        'TN-EDU-PRE-MATRIC-SC', 'Pre-Matric Scholarship Scheme for SC and ST Students (Classes 9 & 10)', 'பட்டியலினம் மற்றும் பழங்குடியின 9, 10-ஆம் வகுப்பு மாணவர்களுக்கான ப்ரீ-மெட்ரிக் கல்வி உதவித்தொகை', 'Pre-Matric Kalvi Uvithogai SC ST',
        'Education', 'scholarship', 'Annual educational assistance and book grant provided to SC and ST day-scholars and hostellers studying in classes 9 and 10.', '9 மற்றும் 10-ஆம் வகுப்பு பயிலும் பட்டியலினம் மற்றும் பழங்குடியின பள்ளி மாணவர்களுக்கான வருடாந்திர கல்வி உதவித்தொகை.',
        '₹3,500/year', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'online',
        'https://adwscholarship.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '17', 'person');
    END IF;
END $$;

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
        'TN-EDU-POST-MATRIC-BC-MBC', 'Post-Matric Scholarship for BC, MBC, and DNC Students', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் மாணவர்களுக்கான போஸ்ட் மெட்ரிக் கல்வி உதவித்தொகை', 'Post-Matric Kalvi Uvithogai BC MBC',
        'Education', 'scholarship', 'Tuition fees, special fees, and maintenance grant for BC, MBC, and DNC students in polytechnic, arts, science, and professional colleges.', 'கல்லூரி மற்றும் பாலிடெக்னிக் பயிலும் பிற்படுத்தப்பட்டோர், மிகவும் பிற்படுத்தப்பட்டோர் மற்றும் சீர்மரபினர் மாணவர்களுக்கான உதவித்தொகை.',
        '₹4,000 to ₹15,000/year', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "கல்லூரி அடையாள அட்டை மற்றும் கட்டண ரசீது", "வங்கி கணக்கு விவரம் (Aadhaar Seeded Bank Account)"]'::jsonb, 'கல்லூரி முதல்வர் / மாவட்ட பிற்படுத்தப்பட்டோர் நல அலுவலகம்', 'online',
        'https://bcbmcmw.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-EDU-FREE-EDUCATION-BC-DEGREE', 'Free Education Scheme for BC, MBC, and DNC 3-Year Undergraduate Degree Students', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் பட்டப்படிப்பு மாணவர்களுக்கான இலவசக் கல்வித் திட்டம்', 'Ilavasa Kalvi Thittam BC MBC Degree',
        'Education', 'scholarship', 'Complete exemption from tuition fees and special fees for BC, MBC, and DNC students pursuing 3-year undergraduate arts and science degrees in government and aided colleges.', 'அரசு மற்றும் அரசு உதவிபெறும் கலை, அறிவியல் கல்லூரிகளில் 3 ஆண்டு இளங்கலை பயிலும் BC/MBC/DNC மாணவர்களுக்கு முழு கல்விக் கட்டண விலக்கு.',
        'முழு கல்விக் கட்டண விலக்கு (Full Tuition Fee Exemption)', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (வருமானம் ₹1,00,000-க்குள்)", "12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "குடும்ப அட்டை நகல்"]'::jsonb, 'கல்லூரி அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://bcbmcmw.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '10000', 'family');
    END IF;
END $$;

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
        'TN-EDU-TAMIL-PUDHALVAN', 'Tamil Pudhalvan Higher Education Assurance Scheme for Boys', 'தமிழ்ப்புதல்வன் திட்டம் (அரசுப் பள்ளி மாணவர்கள் உயர்கல்வி உதவி)', 'Tamil Pudhalvan Thittam',
        'Education', 'monthly_allowance', 'Monthly financial assistance of ₹1,000 directly credited to bank accounts of male students from government schools pursuing undergraduate degrees, diplomas, and ITI courses.', 'அரசுப் பள்ளிகளில் (6 முதல் 12 வரை) படித்து உயர்கல்வி சேரும் மாணவர்களுக்கு மாதம் ₹1,000 உதவித்தொகை வழங்கும் திட்டம்.',
        '₹1,000/month', 'https://tamilpudhalvan.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "அரசுப் பள்ளி பயின்ற சான்றிதழ் (EMIS School Study Certificate)", "கல்லூரி சேர்க்கை அடையாள அட்டை", "மாணவர் பெயரிலான ஆதார் இணைக்கப்பட்ட வங்கிக் கணக்கு புத்தகம்"]'::jsonb, 'கல்லூரி இணையதள ஒருங்கிணைப்பாளர் / போர்ட்டல்', 'online',
        'https://tamilpudhalvan.tn.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'male', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'graduate,postgraduate,higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '17', 'person');
    END IF;
END $$;

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
        'TN-EDU-FIRST-GRADUATE-FEE-CONCESSION', 'First Generation Graduate Tuition Fee Concession Scheme', 'முதல் தலைமுறை பட்டதாரி கல்விக் கட்டணச் சலுகைத் திட்டம்', 'Mudhal Thalaimurai Pattadhari Katana Salugai',
        'Education', 'tuition_concession', 'Full tuition fee waiver for students who are the first graduates in their family admitted through single-window counseling in professional degree courses (Engineering, Medical, Agri).', 'குடும்பத்தில் முதல் பட்டதாரியாக பொறியியல், மருத்துவம், வேளாண்மை உள்ளிட்ட தொழில்முறை பட்டப்படிப்பில் சேரும் மாணவர்களுக்கு முழுக் கல்விக் கட்டணச் சலுகை.',
        '₹20,000 to ₹40,000/year Tuition Waiver', 'https://tnesevai.tn.gov.in/', '2026-08-01', true,
        '["வட்டாட்சியர் வழங்கும் முதல் பட்டதாரி சான்றிதழ் (First Graduate Certificate)", "குடும்ப உறுப்பினர்களின் கல்விச் சான்றிதழ்கள் அல்லது உறுதிமொழிப் படிவம்", "ஒற்றைச் சாளர சேர்க்கை ஆணை (Allotment Order)", "குடும்ப அட்டை மற்றும் ஆதார் அட்டை"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம் மற்றும் சேர்க்கை கல்லூரி', 'both',
        'https://tnesevai.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'first_graduate', 'person');
    END IF;
END $$;

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
        'TN-EDU-FREE-LAPTOP', 'Chief Minister''s Free Laptop Scheme for 12th Standard Students', 'முதலமைச்சரின் விலையில்லா மடிக்கணினி திட்டம்', 'Vilayilla Madikanini Thittam',
        'Education', 'education_device', 'Distribution of free laptops to students studying in government and government-aided schools to bridge the digital divide and encourage digital literacy.', 'அரசு மற்றும் அரசு உதவிபெறும் பள்ளிகளில் பயிலும் மேல்நிலைக் கல்வி (12-ஆம் வகுப்பு) மாணவர்களுக்கு வழங்கப்படும் இலவச மடிக்கணினி.',
        'இலவச மடிக்கணினி (Free Laptop Computer)', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["பள்ளி அடையாள அட்டை (School ID Card)", "ஆதார் அட்டை (Aadhaar Card)", "மாணவர் EMIS எண்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'கல்வியாண்டு விநியோக அட்டவணைப்படி'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '16', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '19', 'person');
    END IF;
END $$;

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
        'TN-EDU-FREE-BICYCLE', 'Free Bicycle Scheme for Class 11 Government and Aided School Students', 'அரசு மற்றும் அரசு உதவிபெறும் பள்ளி 11-ஆம் வகுப்பு மாணவர்களுக்கான விலையில்லா மிதிவண்டி திட்டம்', 'Vilayilla Midhivandi Thittam 11th Std',
        'Education', 'welfare_grant', 'Provision of free bicycles to all boys and girls studying in class 11 in government and government-aided schools to facilitate easy commuting.', 'பள்ளிக்கு எளிதாக சென்று வர அரசு மற்றும் அரசு உதவிபெறும் பள்ளிகளில் 11-ஆம் வகுப்பு பயிலும் மாணவ-மாணவிகளுக்கு இலவச மிதிவண்டி வழங்கப்படுகிறது.',
        'இலவச மிதிவண்டி (Free Bicycle)', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["பள்ளி மாணவர் சேர்க்கை சான்று (School Bonafide)", "ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை நகல்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'பள்ளி மூலமாக வழங்கப்படும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '15', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-EDU-CHIEF-MINISTER-BREAKFAST', 'Chief Minister''s Breakfast Scheme for Primary School Children (Classes 1-5)', 'முதலமைச்சரின் காலை உணவுத் திட்டம் (தொடக்கப் பள்ளி 1 முதல் 5 வகுப்புகள்)', 'Mudhalamaicharin Kaalai Unavu Thittam',
        'Education', 'nutrition_support', 'Hot, hygienic, nutritious breakfast provided to all children studying in classes 1 to 5 in government primary schools across Tamil Nadu on all school working days.', 'அரசு தொடக்கப் பள்ளிகளில் 1 முதல் 5-ஆம் வகுப்பு வரை பயிலும் அனைத்து குழந்தைகளுக்கும் பள்ளிகளில் வழங்கப்படும் இலவச சத்தான காலை உணவு.',
        'இலவச காலை சத்தான உணவு', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["அரசு தொடக்கப் பள்ளி மாணவர் சேர்க்கை பதிவு"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'சேர்க்கையின் போதே உடனடியாக பொருந்தும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'primary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '5', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '11', 'person');
    END IF;
END $$;

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
        'TN-EDU-SPECIAL-INCENTIVE-SC-GIRLS', 'Special Incentive Scheme for SC/ST Girl Students studying in 10th to 12th Standard', 'பட்டியலினம் மற்றும் பழங்குடியின 10 முதல் 12-ஆம் வகுப்பு பெண் குழந்தைகளுக்கான சிறப்பு ஊக்கத்தொகை', 'SC ST Pengal Sirappu Ookkathogai 10-12',
        'Education', 'scholarship', 'Special incentive to arrest dropout rates among Scheduled Caste and Scheduled Tribe girl students in secondary and higher secondary education.', 'பள்ளி இடைநிற்றலைத் தடுக்க 10, 11, மற்றும் 12-ஆம் வகுப்பு பயிலும் பட்டியலினம் மற்றும் பழங்குடியின மாணவிகளுக்கு வழங்கப்படும் சிறப்பு ஊக்கத்தொகை.',
        '₹1,500 to ₹2,000/year', 'https://adw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "மாணவி பெயரிலான வங்கி கணக்கு புத்தகம்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'secondary,higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-PERIYAR-AWARD-GIRL-STUDENTS', 'Thanthai Periyar Memorial Award for BC/MBC Girl Students in Higher Secondary', 'தந்தை பெரியார் நினைவு பிற்படுத்தப்பட்டோர் மாணவியர் கல்வி ஊக்க விருது', 'Thanthai Periyar Ninaivu Ninaivu Virudhu',
        'Education', 'merit_award', 'Cash prize and certificate awarded to BC, MBC, and DNC girl students scoring top marks in 10th and 12th public examinations at district levels.', '10 மற்றும் 12-ஆம் வகுப்பு பொதுத்தேர்வில் மாவட்ட அளவில் அதிக மதிப்பெண் பெறும் BC, MBC, DNC மாணவிகளுக்கு வழங்கப்படும் தந்தை பெரியார் நினைவு விருது.',
        '₹5,000 one-time', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (BC/MBC/DNC Community Certificate)", "10-ஆம் அல்லது 12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ் (Marksheet)", "பள்ளி மாற்றுச் சான்றிதழ் (TC) மற்றும் ஆதார் அட்டை"]'::jsonb, 'மாவட்ட பிற்படுத்தப்பட்டோர் நல அலுவலகம் / முதன்மைக் கல்வி அலுவலர் (CEO)', 'offline',
        NULL, 'முடிவுகள் வெளியான பின் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-SPECIAL-SCHOLARSHIP-DISABILITY', 'Special Higher Education Scholarship for Differently Abled Students', 'மாற்றுத்திறனாளி மாணவர்களுக்கான சிறப்பு உயர்கல்வி உதவித்தொகை', 'Maatru Thiranaali Kalvi Uvithogai',
        'Education', 'scholarship', 'Scholarship grant and scribe allowance for visually challenged, hearing impaired, and locomotor disabled students pursuing higher secondary and undergraduate courses.', 'பார்வையற்றோர், காதுகேளாதோர் உள்ளிட்ட மாற்றுத்திறனாளி மாணவர்கள் மேல்நிலைக் கல்வி மற்றும் கல்லூரி படிப்பைத் தொடர வழங்கப்படும் சிறப்பு உதவித்தொகை.',
        '₹6,000 to ₹7,000/year', 'https://scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "கல்வி நிறுவன சேர்க்கை சான்றிதழ் (Bonafide Certificate)", "வங்கி கணக்கு புத்தகம்", "ஆதார் அட்டை"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDWO)', 'both',
        'https://scd.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
    END IF;
END $$;

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
        'TN-EDU-BOARDING-GRANT-BC-MBC', 'Free Boarding Grant for BC/MBC/DNC Students in Hostels', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் தங்கும் விடுதி உணவுக் கட்டண மானியம்', 'Vidhuthi Unavu Maaniyam BC MBC',
        'Education', 'hostel_grant', 'Free boarding and lodging provided to rural poor BC, MBC, and DNC students admitted to department college and school hostels.', 'கிராமப்புற ஏழை BC, MBC, DNC மாணவர்கள் தங்கிப் படிக்க அரசு நலத்துறை விடுதிகளில் இலவச உணவு மற்றும் தங்குமிட வசதி.',
        'இலவச தங்குமிடம் மற்றும் உணவு (Free Boarding & Lodging)', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "பள்ளி/கல்லூரி சேர்க்கை சான்றிதழ்", "இருப்பிடச் சான்றிதழ் (வருவாய்த்துறை)"]'::jsonb, 'மாவட்ட பிற்படுத்தப்பட்டோர் மற்றும் சிறுபான்மையினர் நல அலுவலகம்', 'online',
        'https://bcbmcmw.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '8333', 'family');
    END IF;
END $$;

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
        'TN-EDU-CLEANING-OCCUPATION-CHILDREN', 'Pre-Matric Scholarship to Children of Parents engaged in Unclean and Hazardous Occupations', 'தூய்மைப் பணியில் ஈடுபட்டுள்ள பெற்றோரின் குழந்தைகளுக்கு வழங்கப்படும் கல்வி உதவித்தொகை', 'Thooymai Paniyaalar Kuzhanthaigal Kalvi Uvithogai',
        'Education', 'scholarship', 'Special scholarship without caste or income ceiling for children whose parents are involved in hazardous cleaning and sanitation occupations.', 'சாதி மற்றும் வருமான வரம்பின்றி, தூய்மை மற்றும் சுகாதாரப் பணிகளில் ஈடுபட்டுள்ள பெற்றோரின் குழந்தைகளுக்கு வழங்கப்படும் பள்ளிக் கல்வி உதவித்தொகை.',
        '₹3,500 to ₹8,000/year', 'https://adw.tn.gov.in/', '2026-08-01', true,
        '["பெற்றோர் தூய்மைப் பணியாளர் என்பதற்கான உள்ளாட்சி அமைப்பு சான்றிதழ்", "பள்ளி பயிலும் சான்றிதழ் (School Study Certificate)", "மாணவர் பெயரிலான வங்கிக் கணக்கு புத்தகம்", "ஆதார் அட்டை"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம் / மாவட்ட ஆதிதிராவிடர் நல அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'primary,secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unclean_occupation_parent,sanitation_worker_family', 'person');
    END IF;
END $$;

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
        'TN-EDU-CHIEF-MINISTER-MERIT-AWARD-SC', 'Chief Minister''s Merit Award Scheme for SC and ST Students', 'முதலமைச்சரின் ஆதிதிராவிடர் மற்றும் பழங்குடியினர் சிறந்த மாணவர் தகுதி விருது', 'Chief Minister Merit Award SC ST',
        'Education', 'merit_award', 'Cash incentive of ₹3,000 per year awarded for up to 6 years for one boy and one girl from SC and ST communities in each district scoring highest in Plus Two exams.', '12-ஆம் வகுப்பு பொதுத்தேர்வில் மாவட்ட அளவில் முதலிடம் பெறும் ஆதிதிராவிடர், பழங்குடியின மாணவ-மாணவியருக்கு ஆண்டுக்கு ₹3,000 வீதம் 6 ஆண்டுகளுக்கு வழங்கப்படும் விருது.',
        '₹3,000/year for 6 years', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["12-ஆம் வகுப்பு அரசு பொதுத்தேர்வு மதிப்பெண் சான்றிதழ்", "சாதிச் சான்றிதழ் (SC/ST Community Certificate)", "தொடர்ந்து உயர்கல்வி பயில்வதற்கான கல்லூரி சேர்க்கை சான்று", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட ஆதிதிராவிடர் மற்றும் பழங்குடியினர் நல அலுவலகம்', 'offline',
        NULL, '45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-PM-YASASVI-OBC', 'PM YASASVI Pre-Matric Scholarship for OBC, EBC, and DNT Students (Classes 9 & 10)', 'பிஎம் யசஸ்வி இதர பிற்படுத்தப்பட்டோர் மற்றும் சீர்மரபினர் பள்ளி கல்வி உதவித்தொகை', 'PM YASASVI Pre-Matric Scholarship',
        'Education', 'scholarship', 'Centrally sponsored scholarship scheme implemented by Tamil Nadu government for meritorious OBC, EBC, and DNT students in classes 9 and 10 with annual family income up to ₹2.5 Lakhs.', 'ஆண்டு குடும்ப வருமானம் ₹2.5 லட்சத்திற்குள் உள்ள BC, MBC, DNC 9 மற்றும் 10-ஆம் வகுப்பு மாணவர்களுக்கான மத்திய-மாநில அரசின் பிஎம் யசஸ்வி கல்வி உதவித்தொகை.',
        '₹4,000/year', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate - வருமானம் ₹2.5 லட்சத்திற்குள்)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம் / தேசிய கல்வி உதவித்தொகை போர்ட்டல் (NSP)', 'online',
        'https://bcbmcmw.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '20833', 'family');
    END IF;
END $$;

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
        'TN-AGRI-PM-KISAN', 'Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) Direct Income Support', 'பிரதமர் கிசான் சம்மான் நிதி (PM-KISAN) விவசாயிகளுக்கான நேரடி வருவாய் உதவி', 'PM Kisan Samman Nidhi Vivasayigal Uvithogai',
        'Agriculture and Farmers Welfare', 'farmer_income_support', 'Direct income support of ₹6,000 per year in three equal installments of ₹2,000 every four months to all landholding farmer families across Tamil Nadu.', 'விவசாய நிலம் வைத்துள்ள விவசாய குடும்பங்களுக்கு ஆண்டுக்கு ₹6,000 (4 மாதங்களுக்கு ஒருமுறை ₹2,000 வீதம்) நேரடியாக வங்கிக் கணக்கில் வழங்கும் திட்டம்.',
        '₹6,000/year (₹2,000 every 4 months)', 'https://pmkisan.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card with e-KYC)", "நிலப் பட்டா / சிட்டா (Patta / Chitta document)", "நில ஆவணம் மற்றும் அடங்கல் (Land Adangal)", "ஆதார் இணைக்கப்பட்ட வங்கி கணக்கு புத்தகம் (NPCI Aadhar Seeded Bank Account)"]'::jsonb, 'வட்டார வேளாண்மை உதவி இயக்குநர் அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://pmkisan.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-KURUVAI-PACKAGE', 'Kuruvai Cultivation Special Package Scheme for Delta Paddy Farmers', 'டெல்டா குறுவை சாகுபடி சிறப்பு தொகுப்புத் திட்டம் (இலவச உரம் & விதைகள்)', 'Delta Kuruvai Sagubadi Sirappu Thoguppu',
        'Agriculture and Farmers Welfare', 'input_subsidy', 'Special agricultural input package providing 100% subsidy on certified paddy seeds, urea, DAP, and potash to delta district farmers taking up Kuruvai season paddy cultivation.', 'காவிரி டெல்டா மற்றும் பாசனப் பகுதிகளில் குறுவை நெல் சாகுபடி செய்யும் விவசாயிகளுக்கு 100% மானியத்தில் சான்று பெற்ற விதைகள், யூரியா, டிஏபி, பொட்டாஷ் வழங்கும் திட்டம்.',
        '100% Subsidy on Seeds and Fertilizers (₹4,000/acre value)', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["உழவர் பதிவு எண் (Uzhavar Registration ID / AGRISNET)", "சிட்டா / பட்டா நகல் (Patta / Chitta)", "கிராம நிர்வாக அலுவலர் (VAO) வழங்கும் குறுவை சாகுபடி சான்றிதழ் / அடங்கல்", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை நகல்"]'::jsonb, 'வேளாண் விரிவாக்க மையம் (Agricultural Extension Centre) / உழவர் அலுவலர்', 'both',
        'https://tnagrisnet.tn.gov.in/', '7 முதல் 15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'paddy', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-MICRO-IRRIGATION-MIF', 'Micro Irrigation Scheme (Drip and Sprinkler Subsidy under PMKSY)', 'நுண்ணீர்ப் பாசனத் திட்டம் (சிறு/குறு விவசாயிகளுக்கு 100% மானியத்தில் சொட்டு நீர்ப்பாசனம்)', 'Nunneer Paasana Thittam Sottuneer Paasanam',
        'Agriculture and Farmers Welfare', 'irrigation_subsidy', '100% subsidy for small and marginal farmers (up to 5 acres) and 75% subsidy for other farmers to install drip and sprinkler irrigation systems to conserve ground water.', 'பாசன நீரை சேமிக்க சிறு மற்றும் குறு விவசாயிகளுக்கு 100% மானியத்திலும், இதர விவசாயிகளுக்கு 75% மானியத்திலும் சொட்டுநீர் மற்றும் தெளிப்பு நீர்ப்பாசன கருவிகள் அமைத்தல்.',
        '100% Subsidy for Small/Marginal Farmers, 75% for other farmers', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["சிறு/குறு விவசாயி சான்றிதழ் (வட்டாட்சியர்/VAO சான்றிதழ்)", "நில உரிமை பட்டா, சிட்டா மற்றும் நில வரைபடம் (FMB sketch)", "கிணறு / ஆழ்துளை கிணறு பாசன நீர் ஆதாரம் இருப்பதற்கான சான்று", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார தோட்டக்கலை / வேளாண்மை உதவி இயக்குநர் அலுவலகம்', 'online',
        'https://tnhorticulture.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-UZHAVAR-PATHUKAPPU-PENSION', 'Chief Minister''s Farmers Social Security Scheme (Uzhavar Pathukappu Thittam) Monthly Pension', 'முதலமைச்சரின் உழவர் பாதுகாப்புத் திட்டம் - முதியோர் ஓய்வூதியம்', 'Uzhavar Pathukappu Thittam Mudhiyor Oivoodhiyam',
        'Agriculture and Farmers Welfare', 'pension', 'Monthly pension of ₹1,000 provided to aged small, marginal, and tenant farmers and agricultural labourers aged 60 and above registered under Uzhavar Pathukappu Thittam.', 'உழவர் பாதுகாப்புத் திட்டத்தில் பதிவுசெய்த 60 வயது பூர்த்தியடைந்த சிறு, குறு, குத்தகை விவசாயிகள் மற்றும் விவசாயத் தொழிலாளர்களுக்கு மாதம் ₹1,000 ஓய்வூதியம்.',
        '₹1,000/month', 'https://www.tnesevai.tn.gov.in/', '2026-08-01', true,
        '["முதலமைச்சரின் உழவர் பாதுகாப்பு அட்டை (Uzhavar Card)", "வயதுச் சான்றிதழ் (Age Proof - 60 வயது பூர்த்தி)", "வருமானச் சான்றிதழ் (Income Certificate)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் (சமூகப் பாதுகாப்புத் திட்டம்) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '2.5', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '10000', 'family');
    END IF;
END $$;

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
        'TN-AGRI-CROP-INSURANCE-PMFBY', 'Pradhan Mantri Fasal Bima Yojana (PMFBY) Crop Insurance Scheme', 'பிரதம மந்திரி பயிர் காப்பீட்டுத் திட்டம் (PMFBY)', 'PM Fasal Bima Yojana Payir Kaapeedu',
        'Agriculture and Farmers Welfare', 'crop_insurance', 'Comprehensive crop insurance protection covering yield loss due to non-preventable risks (natural drought, floods, inundation, pests, and unseasonal rainfall) at nominal farmer premium rates (1.5% to 2%).', 'வறட்சி, வெள்ளம், பூச்சித் தாக்குதல் போன்ற இயற்கை இடர்பாடுகளால் ஏற்படும் பயிர் இழப்புகளுக்கு குறைந்த பிரீமியம் விகிதத்தில் முழு நிதி இழப்பீடு வழங்கும் பயிர் காப்பீட்டுத் திட்டம்.',
        'Full Sum Insured on Crop Loss due to drought/flood', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பயிர் சாகுபடி அடங்கல் (Adangal from VAO / e-Adangal)", "பட்டா / சிட்டா நகல் (Patta / Chitta document)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)", "ஆதார் அட்டை (Aadhaar Card)"]'::jsonb, 'தொடக்க வேளாண்மை கூட்டுறவு கடன் சங்கம் (PACCS) / பொது இ-சேவை மையம்', 'both',
        'https://pmfby.gov.in/', 'பயிர் அறுவடை பரிசோதனை முடிவுகளுக்குப் பின்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-MILLETS-MISSION', 'Tamil Nadu Millet Mission Cultivation Incentive and Seed Subsidy', 'தமிழ்நாடு சிறுதானிய இயக்கம் - சாகுபடி மானியம் மற்றும் விதைகள்', 'Tamil Nadu Sirudhaaniya Iyakkam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Financial incentive of ₹5,000 per hectare along with free bio-fertilizers and quality seeds for farmers cultivating millets like ragi, kambu, thinai, and varagu.', 'கேழ்வரகு, கம்பு, தினை, வரகு உள்ளிட்ட சிறுதானியங்களை சாகுபடி செய்யும் விவசாயிகளுக்கு ஹெக்டேருக்கு ₹5,000 மானியம் மற்றும் சான்று பெற்ற விதைகள் வழங்கும் திட்டம்.',
        '₹5,000/hectare Input Subsidy', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["சிறுதானிய சாகுபடி அடங்கல் (Adangal proof for Millets)", "பட்டா / சிட்டா நகல்", "உழவர் பதிவு அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'both',
        'https://tnagrisnet.tn.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'millets', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-SOLAR-PUMP-SUBSIDY', 'Standalone Solar Powered Pumping System Subsidy Scheme (PM-KUSUM Component-B)', 'விவசாயிகளுக்கு 70% மானியத்தில் தனித்து இயங்கும் சூரியசக்தி பம்புசெட்டுகள் அமைத்தல்', 'Sooriya Sakthi Pumbset Maaniyam',
        'Agriculture and Farmers Welfare', 'solar_irrigation', 'Provision of standalone AC/DC solar agricultural pumping systems (up to 10 HP) with 70% capital subsidy from Central and State Governments.', 'மின் இணைப்பு இல்லாத விவசாய நிலங்களுக்கு 70% மானியத்தில் 5 முதல் 10 குதிரைத்திறன் கொண்ட சூரியசக்தி பம்புசெட்டுகள் அமைக்கும் திட்டம்.',
        '70% Subsidy on Solar Pump System (up to ₹2,00,000)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["பட்டா / சிட்டா மற்றும் நில உரிமை ஆவணம்", "கிணறு / ஆழ்துளை கிணறு நிலத்தடி நீர் கிடைக்கும் சான்றிதழ்", "விவசாயி பங்குத் தொகை செலுத்துவதற்கான உறுதிமொழி", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை"]'::jsonb, 'வேளாண் பொறியியல் துறை உதவி செயற்பொறியாளர் அலுவலகம்', 'online',
        'https://aed.tn.gov.in/', '45 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '1.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-FARM-MACHINERY-SUBSIDY', 'Subsidized Agricultural Machinery & Power Tillers Scheme (SMAM)', 'வேளாண் இயந்திரமயமாக்கல் திட்டம் - பவர்டில்லர் மற்றும் கருவிகள் மானியம்', 'Velan Iyandhiramayamakkal Thittam',
        'Agriculture and Farmers Welfare', 'machinery_subsidy', 'Capital subsidy of up to 50% for SC, ST, women, and small/marginal farmers for purchasing power tillers, rotavators, weeders, and paddy transplanters.', 'பவர்டில்லர், களை எடுக்கும் கருவி, நெல் நடவு இயந்திரம் உள்ளிட்ட வேளாண் கருவிகள் வாங்க சிறு, குறு, பெண் விவசாயிகளுக்கு 50% வரை மானியம்.',
        '50% Subsidy for SC/ST/Women/Small Farmers (up to ₹1,00,000)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["சிறு/குறு விவசாயி சான்றிதழ் (Small Farmer Certificate)", "பட்டா மற்றும் சிட்டா நகல்", "விவசாய இயந்திர விலைப்பட்டியல் (Quotation from approved dealer)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வேளாண் பொறியியல் துறை அலுவலகம்', 'online',
        'https://aed.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-KALAIGNAR-ALL-VILLAGE', 'Kalaignar All Village Integrated Agriculture Development Programme (KAVIADP)', 'கலைஞரின் அனைத்து கிராம ஒருங்கிணைந்த வேளாண் வளர்ச்சித் திட்டம்', 'Kalaignarin Anaithu Grama Oringinaindha Velan Thittam',
        'Agriculture and Farmers Welfare', 'integrated_development', 'Holistic village-level mission providing free coconut saplings, vegetable seed kits, hand sprayers, and horticulture saplings to bring fallow lands under cultivation.', 'கிராமப் பஞ்சாயத்துகளில் தரிசு நிலங்களை சாகுபடிக்கு கொண்டு வர இலவச தென்னங்கன்றுகள், காய்கறி விதை பெட்டகங்கள், கைத்தெளிப்பான்கள் வழங்கும் திட்டம்.',
        'Free Coconut Seedlings, Fruit Plants and Hand Sprayers', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["குடும்ப அட்டை நகல்", "ஆதார் அட்டை நகல்", "கிராம பஞ்சாயத்து இருப்பிடச் சான்று"]'::jsonb, 'கிராம ஊராட்சி மன்ற அலுவலகம் / வேளாண் விரிவாக்க மையம்', 'offline',
        NULL, 'கிராம முகாம்களில் உடனடியாக வழங்கப்படும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-PULSES-PRODUCTION-MISSION', 'National Food Security Mission - Pulses Production and Quality Seed Distribution', 'தேசிய உணவுப் பாதுகாப்பு இயக்கம் - பருப்பு வகை பயிர்கள் ஊக்கத்தொகை', 'Paruppu Vagaigal Saagubadi Maaniyam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Incentive support and 50% subsidy on certified blackgram and greengram seeds to promote pulses cultivation as bund crops and rice-fallows.', 'உளுந்து, பாசிப்பயறு உள்ளிட்ட பருப்பு வகை பயிர்களை வரப்புப் பயிராகவும் நெல் தரிசிலும் சாகுபடி செய்ய 50% விதை மானியம் மற்றும் ஊக்கத்தொகை.',
        '₹3,000/hectare Input Incentive', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["நிலப் பட்டா / சிட்டா நகல்", "பயிர் அடங்கல் (Adangal proof for Pulses)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண்மை விரிவாக்க மையம்', 'both',
        'https://tnagrisnet.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'pulses', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-ORGANIC-FARMING-SUBSIDY', 'Paramparagat Krishi Vikas Yojana (PKVY) Organic Farming Promotion', 'பாரம்பரிய இயற்கை விவசாய மேம்பாட்டுத் திட்டம் - இடுபொருட்கள் மானியம்', 'Iyarkai Vivasaayam PKVY Maaniyam',
        'Agriculture and Farmers Welfare', 'organic_farming', 'Financial assistance of ₹15,000 per hectare over 3 years for organic inputs, vermicompost units, bio-fertilizers, and organic certification.', 'இயற்கை மற்றும் இயற்கை உரம் சார்ந்த சாகுபடியை ஊக்குவிக்க 3 ஆண்டுகளில் ஹெக்டேருக்கு ₹15,000 இடுபொருள் மானியம் மற்றும் சான்றளிப்பு உதவி.',
        '₹15,000/hectare over 3 years', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பட்டா, சிட்டா நகல்", "இயற்கை விவசாயக் குழுவில் (Organic Cluster) உறுப்பினர் சான்று", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-OILSEEDS-EXPANSION', 'Oilseeds Production Expansion and Groundnut Seed Subsidy Scheme', 'எண்ணெய் வித்துக்கள் சாகுபடி பரப்பு விரிவாக்கம் மற்றும் விதை மானியம்', 'Ennai Vithukkal Nilakkadalai Maaniyam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Distribution of certified groundnut, sesame, and sunflower seeds at 50% subsidy to expand edible oilseed production in dry and rainfed tracts.', 'நிலக்கடலை, எள், சூரியகாந்தி உள்ளிட்ட எண்ணெய் வித்துக்கள் பயிரிடும் விவசாயிகளுக்கு 50% மானியத்தில் சான்று பெற்ற விதைகள் வழங்கும் திட்டம்.',
        '50% Subsidy on Certified Oilseeds', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பட்டா மற்றும் சிட்டா நகல்", "விவசாயி அடையாள அட்டை", "ஆதார் அட்டை"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம்', 'both',
        'https://tnagrisnet.tn.gov.in/', '7 முதல் 15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'oilseeds', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-DRYLAND-DEVELOPMENT-MISSION', 'Mission on Sustainable Dryland Agriculture (MSDA) for Rainfed Farmers', 'நீடித்த நிலையான மானாவாரி வேளாண்மை இயக்கம் (MSDA)', 'Maanavaari Velanmai Iyakkam MSDA',
        'Agriculture and Farmers Welfare', 'dryland_mission', 'Cluster-based soil health improvement, deep summer ploughing subsidy, and drought-tolerant seed distribution for rainfed and dryland farmers.', 'மழை நம்பி விவசாயம் செய்யும் மானாவாரி நிலங்களில் கோடை உழவு மானியம், மண்வள மேலாண்மை மற்றும் வறட்சியைத் தாங்கும் பயிர் விதைகள் வழங்கும் திட்டம்.',
        'Free Soil Health Management and Agronomic Inputs', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["மானாவாரி நிலப் பட்டா மற்றும் அடங்கல்", "ஆதார் அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'offline',
        NULL, '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-HORTICULTURE-PLANTING-MATERIAL', 'National Horticulture Mission - Subsidized Fruit Plants and Shade Net Polyhouses', 'தோட்டக்கலை பயிர்கள் நடவு மற்றும் பசுமை குடில் அமைக்கும் மானியத் திட்டம்', 'Thottakallai Payirgal Pasumai Kudil Maaniyam',
        'Agriculture and Farmers Welfare', 'horticulture_subsidy', '40% to 50% subsidy on high yielding fruit saplings (Mango, Guava, Acid Lime) and protected cultivation shade nets to boost horticulture income.', 'மா, கொய்யா, எலுமிச்சை உள்ளிட்ட பழ மரக்கன்றுகள் நடவு செய்வதற்கும் பசுமை நிழல்வலை குடில் அமைப்பதற்கும் 40% முதல் 50% வரை மானியம்.',
        '40% to 50% Capital Subsidy on Planting Material', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["தோட்டக்கலை நில பட்டா, சிட்டா மற்றும் வரைபடம்", "சிறு/குறு விவசாயி சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'வட்டார தோட்டக்கலை உதவி இயக்குநர் அலுவலகம்', 'online',
        'https://tnhorticulture.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'horticulture', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-FARM-POND-SUBSIDY', 'Rainwater Harvesting Farm Ponds Construction Subsidy for Dryland Farmers', 'மானாவாரி விவசாய நிலங்களில் பண்ணைக் குட்டைகள் அமைக்க 100% மானியத் திட்டம்', 'Pannai Kuttaigal Amaikka 100% Maaniyam',
        'Agriculture and Farmers Welfare', 'water_conservation', '100% grant (up to ₹1,00,000) for excavation of rainwater harvesting farm ponds (dimensions 30m x 30m x 1.5m) in drylands to store runoff water.', 'மழைநீரை நிலத்தில் சேமித்து பாசனத்திற்கு பயன்படுத்த விவசாய நிலத்தில் பண்ணைக்குட்டை அமைக்க 100% முழு மானியம் (ரூ.1,00,000 வரை).',
        '100% Subsidy (up to ₹1,00,000 for pond excavation)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["நிலப் பட்டா, சிட்டா மற்றும் அடங்கல்", "பண்ணைக்குட்டை அமைக்க உத்தேசித்துள்ள இடத்தின் வரைபடம்", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை"]'::jsonb, 'வேளாண் பொறியியல் துறை உதவி செயற்பொறியாளர் அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '1.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-COCONUT-DEVELOPMENT', 'Integrated Coconut Development Scheme (Seedling Distribution & Pest Management)', 'ஒருங்கிணைந்த தென்னை வளர்ச்சித் திட்டம் - கன்றுகள் மற்றும் பூச்சி மேலாண்மை', 'Oringinaindha Thennai Valarchi Thittam',
        'Agriculture and Farmers Welfare', 'crop_incentive', '50% subsidy on hybrid coconut seedlings, organic manure, and biological control agents for coconut rhinoceros beetle and red palm weevil management.', 'வீரிய ஒட்டு தென்னங்கன்றுகள் வாங்குவதற்கும், காண்டாமிருக வண்டு தாக்குதலைக் கட்டுப்படுத்தவும் தென்னை விவசாயிகளுக்கு 50% மானியம்.',
        '50% Subsidy on Hybrid Seedlings', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["தென்னை சாகுபடி பட்டா மற்றும் சிட்டா", "விவசாயி அடையாள அட்டை", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார தோட்டக்கலை அலுவலர் அலுவலகம்', 'both',
        'https://tnhorticulture.tn.gov.in/', '15 முதல் 20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'coconut', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-GRADUATE', 'Unemployment Assistance Scheme for Graduate and Post-Graduate Job Seekers', 'வேலைவாய்ப்பற்ற பட்டதாரி இளைஞர்களுக்கான மாதாந்திர உதவித்தொகை திட்டம்', 'Velai Vaaippatra Pattadhari Maadhathira Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Monthly financial allowance provided for up to 3 years to unemployed graduates and post-graduates registered continuously for at least 5 years in employment exchanges.', 'வேலைவாய்ப்பு அலுவலகத்தில் 5 ஆண்டுகளுக்கு மேல் தொடர்ந்து பதிவு செய்து காத்திருக்கும் பட்டதாரி மற்றும் முதுகலை இளைஞர்களுக்கு வழங்கப்படும் மாதாந்திர உதவித்தொகை.',
        '₹600/month (₹1,800/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு அலுவலக பதிவு அடையாள அட்டை (Employment Card)", "பட்டப்படிப்பு / முதுகலை சான்றிதழ் (Degree Certificate)", "வருமானச் சான்றிதழ் (ஆண்டு வருமானம் ₹2,00,000-க்குள்)", "வேலையில்லை என்பதற்கான சுய அறிவிப்புப் படிவம்", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு மற்றும் தொழில்நெறி வழிகாட்டும் மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '20', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-HSC', 'Unemployment Assistance Scheme for Higher Secondary (12th Passed) Job Seekers', '12-ஆம் வகுப்பு தேர்ச்சி பெற்ற வேலைவாய்ப்பற்ற இளைஞர்களுக்கான உதவித்தொகை', '12th Muditha Velai Vaaippatra Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Financial allowance of ₹400 per month given for up to 3 years to unemployed Plus Two candidates registered continuously with employment exchanges for 5 years.', 'மேல்நிலைக் கல்வி (12-ஆம் வகுப்பு) முடித்து 5 ஆண்டுகள் வேலைவாய்ப்பு அலுவலகத்தில் பதிவு செய்து காத்திருக்கும் இளைஞர்களுக்கு மாதம் ₹400 உதவி.',
        '₹400/month (₹1,200/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு அலுவலக பதிவு அட்டை (Employment Card)", "12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "வருமானச் சான்றிதழ் (வட்டாட்சியர் அலுவலகம்)", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு மற்றும் தொழில்நெறி வழிகாட்டும் மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-SSLC', 'Unemployment Assistance Scheme for SSLC (10th Passed) Job Seekers', 'பத்தாம் வகுப்பு தேர்ச்சி பெற்ற வேலைவாய்ப்பற்றோருக்கான உதவித்தொகை', '10th Muditha Velai Vaaippatra Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Quarterly assistance of ₹900 (₹300/month) for up to 3 years to unemployed SSLC candidates registered for 5 continuous years in employment exchanges.', '10-ஆம் வகுப்பு தேர்ச்சி பெற்று 5 ஆண்டுகள் வேலைவாய்ப்பு அலுவலகத்தில் பதிவு செய்து காத்திருக்கும் நபர்களுக்கு மாதம் ₹300 வீதம் காலாண்டுக்கு ₹900 உதவி.',
        '₹300/month (₹900/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு பதிவு அடையாள அட்டை", "10-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "வருமானச் சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு அலுவலகம் / இ-சேவை மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-DISABLED', 'Special Unemployment Assistance for Differently Abled Job Seekers', 'மாற்றுத்திறனாளி வேலைவாய்ப்பற்றோருக்கான சிறப்பு உதவித்தொகை', 'Maatru Thiranaali Velai Vaaippatra Sirappu Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Enhanced monthly unemployment allowance without upper age limit for differently abled job seekers registered continuously for at least 1 year in employment exchanges.', 'வேலைவாய்ப்பு அலுவலகத்தில் 1 ஆண்டு பதிவு செய்துள்ள மாற்றுத்திறனாளி வேலை தேடுவோருக்கு மாதம் ₹600 முதல் ₹1,000 வரை வழங்கப்படும் சிறப்பு உதவித்தொகை.',
        '₹600 to ₹1,000/month', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "வேலைவாய்ப்பு பதிவு அட்டை (Employment Registration Card)", "கல்விச் சான்றிதழ்கள்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு அலுவலகம்', 'both',
        'https://employmentexchange.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-PENSION', 'Tamil Nadu Construction Workers Welfare Board Monthly Pension Scheme (Age 60+)', 'தமிழ்நாடு கட்டுமானத் தொழிலாளர்கள் நல வாரிய முதியோர் ஓய்வூதியம்', 'Kattumana Thozhilaalar Nala Vaariya Oivoodhiyam',
        'Labour and Employment', 'pension', 'Monthly pension of ₹1,000 provided to registered building and construction workers who have reached 60 years of age and completed at least 5 years of registration in the board.', 'கட்டுமானத் தொழிலாளர்கள் நல வாரியத்தில் 5 ஆண்டுகளுக்கு மேல் பதிவு செய்து 60 வயது பூர்த்தியடைந்த தொழிலாளர்களுக்கு மாதம் ₹1,000 ஓய்வூதியம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கட்டுமான நல வாரிய உறுப்பினர் அடையாள அட்டை (TNUWWB Smart Card)", "வயதுச் சான்றிதழ் (ஆதார் / வாக்காளர் அட்டை - 60 வயது பூர்த்தி)", "வாரிய சந்தா செலுத்திய ரசீது / புதுப்பித்தல் விவரம்", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'தொழிலாளர் உதவி ஆணையர் (சமூகப் பாதுகாப்புத் திட்டம்) அலுவலகம் / TNUWWB போர்ட்டல்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-ACCIDENT-RELIEF', 'Tamil Nadu Construction Workers Welfare Board Accidental Death and Disability Relief', 'கட்டுமானத் தொழிலாளர்கள் விபத்து மரணம் மற்றும் ஊன நிவாரண நிதி', 'Kattumana Thozhilaalar Vibathu Nivarana Nidhi',
        'Labour and Employment', 'accident_relief', 'Ex-gratia financial assistance of ₹5,00,000 in case of accidental death at worksite or ₹1,00,000 to ₹5,00,000 for permanent total disability for registered construction workers.', 'பணியிட விபத்தில் உயிரிழக்கும் பதிவு பெற்ற கட்டுமானத் தொழிலாளர்களின் குடும்பத்திற்கு ₹5,00,000 மற்றும் நிரந்தர ஊனத்திற்கு ₹1,00,000 முதல் ₹5,00,000 வரை நிவாரணம்.',
        '₹5,00,000 for accidental death', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாரிய உறுப்பினர் அட்டை (TNUWWB Registration Card)", "முதல் தகவல் அறிக்கை (FIR) மற்றும் பிரேத பரிசோதனை அறிக்கை (Postmortem Report)", "இறப்புச் சான்றிதழ் மற்றும் வாரிசுச் சான்றிதழ்", "வாரிசுதாரர் ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'தொழிலாளர் உதவி ஆணையர் (சமூகப் பாதுகாப்புத் திட்டம்) அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '60', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-MARRIAGE-ASSISTANCE', 'Tamil Nadu Construction Workers Welfare Board Marriage Financial Assistance', 'கட்டுமானத் தொழிலாளர்கள் நல வாரிய திருமண நிதி உதவி', 'Kattumana Thozhilaalar Thirumana Nidhi Uvithogai',
        'Labour and Employment', 'marriage_assistance', 'Marriage financial assistance of ₹5,000 for male workers and ₹7,000 for female workers (or their children) provided by the Construction Workers Welfare Board.', 'பதிவு பெற்ற கட்டுமானத் தொழிலாளி அல்லது அவர்களின் மகன்/மகள் திருமணத்திற்கு ₹5,000 (ஆண்) மற்றும் ₹7,000 (பெண்) திருமண நிதி உதவி.',
        '₹5,00,0 (Men) / ₹7,000 (Women)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கட்டுமான நல வாரிய உறுப்பினர் அட்டை", "திருமண அழைப்பிதழ் மற்றும் திருமணப் பதிவுச் சான்றிதழ் (Marriage Certificate)", "மணமகன் மற்றும் மணமகள் வயதுச் சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'TNUWWB இணையதளம் / மாவட்ட தொழிலாளர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'married', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-MATERNITY', 'Maternity Financial Assistance for Registered Female Construction Workers', 'பதிவுபெற்ற பெண் கட்டுமானத் தொழிலாளர்களுக்கான மகப்பேறு உதவித்தொகை', 'Pen Kattumana Thozhilaalar Magapperu Uvithogai',
        'Labour and Employment', 'maternity_benefit', 'Maternity assistance of ₹6,000 (₹3,000 on delivery and ₹3,000 after 30 days) and miscarriage assistance of ₹3,000 for registered female construction workers.', 'வாரியத்தில் பதிவுபெற்ற பெண் கட்டுமானத் தொழிலாளர்களுக்கு குழந்தை பிறப்பின் போது ₹6,000 மகப்பேறு உதவித்தொகை வழங்கும் திட்டம்.',
        '₹6,000 (₹3,000 on delivery, ₹3,000 post-delivery)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாரிய உறுப்பினர் அடையாள அட்டை (TNUWWB ID)", "அரசு மருத்துவமனை குழந்தை பிறப்புச் சான்றிதழ் (Birth Certificate)", "தாய் சேய் நல அட்டை (RCH ID card)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'தொழிலாளர் நல வாரிய போர்ட்டல் / தொழிலாளர் உதவி ஆணையர்', 'online',
        'https://tnuwwb.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '19', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-EDUCATION', 'Educational Assistance Scheme for Children of Registered Construction Workers', 'கட்டுமானத் தொழிலாளர்களின் குழந்தைகளுக்கு வழங்கப்படும் கல்வி உதவித்தொகை', 'Kattumana Thozhilaalar Kuzhanthaigal Kalvi Uvithogai',
        'Labour and Employment', 'education_assistance', 'Annual educational scholarship ranging from ₹1,000 to ₹12,000 per year for children of registered construction workers studying from 10th to Post Graduate and professional degrees.', '10-ஆம் வகுப்பு முதல் தொழிற்கல்வி, பட்டப்படிப்பு வரை பயிலும் கட்டுமானத் தொழிலாளர்களின் குழந்தைகளுக்கு ஆண்டுதோறும் ₹1,000 முதல் ₹12,000 வரை கல்வி உதவி.',
        '₹1,000 to ₹12,000/year', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["பெற்றோரின் கட்டுமான நல வாரிய உறுப்பினர் அட்டை", "மாணவர் பயிலும் சான்றிதழ் (Bonafide Certificate)", "கடந்த ஆண்டு மதிப்பெண் சான்றிதழ்", "மாணவர் பெயரிலான வங்கி கணக்கு புத்தகம்"]'::jsonb, 'TNUWWB போர்ட்டல் / தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'secondary,higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'construction_worker_child', 'person');
    END IF;
END $$;

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
        'TN-LAB-UNORGANIZED-WORKERS-PENSION', 'Tamil Nadu Unorganized Workers Welfare Board Monthly Pension Scheme', 'தமிழ்நாடு அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் நல வாரிய ஓய்வூதியம்', 'Amaippusaara Thozhilaalar Oivoodhiyam',
        'Labour and Employment', 'pension', 'Monthly social security pension of ₹1,000 provided to manual and unorganized workers aged 60 and above registered under the Tamil Nadu Manual Workers Welfare Board.', 'அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் நல வாரியத்தில் பதிவு செய்து 60 வயது பூர்த்தியடைந்த தொழிலாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["அமைப்புசாரா தொழிலாளர் நல வாரிய உறுப்பினர் அட்டை (TNUWWB Card)", "வயதுச் சான்றிதழ் (60 வயது பூர்த்தி)", "ஆதார் அட்டை (Aadhaar Card)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'மாவட்ட தொழிலாளர் சமூகப் பாதுகாப்புத் திட்ட அலுவலகம் / TNUWWB போர்ட்டல்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unorganized_worker', 'person');
    END IF;
END $$;

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
        'TN-LAB-MANUAL-WORKERS-ACCIDENT-RELIEF', 'Manual Workers Social Security Scheme - Natural Death and Funeral Relief', 'அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் இயற்கை மரணம் & ஈமச்சடங்கு நிதி', 'Udaluzhaippu Thozhilaalar Eemachadangu Nidhi',
        'Labour and Employment', 'death_relief', 'Financial grant of ₹20,000 for natural death and ₹5,000 for funeral expenses provided to nominees of registered manual workers in unorganized sectors.', 'அமைப்புசாரா தொழிலாளர்கள் இயற்கை மரணமடைந்தால் குடும்பத்தினருக்கு ₹20,000 மற்றும் உடனடியாக ₹5,000 ஈமச்சடங்கு உதவித்தொகை வழங்கும் திட்டம்.',
        '₹25,000 (Natural Death Relief + Funeral Assistance)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["இறந்த தொழிலாளியின் நல வாரிய அட்டை", "இறப்புச் சான்றிதழ் (Death Certificate)", "வாரிசுச் சான்றிதழ் (Legal Heir Certificate)", "வாரிசுதாரர் ஆதார் மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் அலுவலகம் / TNUWWB', 'both',
        'https://tnuwwb.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unorganized_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-DRIVER-BOARD-VEHICLE-ASSISTANCE', 'Tamil Nadu Auto Rickshaws and Taxi Drivers Welfare Board Welfare Scheme', 'தமிழ்நாடு ஆட்டோ மற்றும் வாடகை வாகன ஓட்டுநர்கள் நல வாரிய உதவி', 'Auto Vaadagai Vaagana Ottunargal Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Comprehensive welfare benefits including accidental relief (₹5,00,000), pension, marriage aid, and spectacles assistance for auto and taxi drivers.', 'ஆட்டோ மற்றும் வாடகை வாகன ஓட்டுநர்கள் நல வாரியத்தில் பதிவு பெற்ற ஓட்டுநர்களுக்கு விபத்து நிவாரணம், திருமணம், கல்வி மற்றும் கண் கண்ணாடி உதவித்தொகை.',
        'Accident Relief (₹5,00,000) & Welfare Grants', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாகன ஓட்டுநர் நல வாரிய அட்டை", "செல்லத்தக்க ஓட்டுநர் உரிமம் (Commercial Driving License with Badge)", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'in_list', 'self_employed,private_employee,daily_wage', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'auto_taxi_driver,driver_license', 'person');
    END IF;
END $$;

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
        'TN-LAB-TAILORING-BOARD-ASSISTANCE', 'Tamil Nadu Tailoring Workers Welfare Board Maternity and Spectacles Assistance', 'தமிழ்நாடு தையல் தொழிலாளர்கள் நல வாரிய மகப்பேறு & மூக்குக்கண்ணாடி உதவி', 'Thaiyal Thozhilaalar Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Spectacles purchase reimbursement of ₹500, maternity assistance of ₹6,000, and pension benefits for registered tailoring and garment workers.', 'தையல் தொழிலாளர் நல வாரிய உறுப்பினர்களுக்கு கண் பார்வைக் குறைபாட்டிற்கு கண்ணாடி வாங்க ₹500 மற்றும் மகப்பேறு உதவித்தொகை ₹6,000 வழங்கும் திட்டம்.',
        '₹500 for Spectacles, ₹6,000 Maternity Assistance', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["தையல் தொழிலாளர் நல வாரிய உறுப்பினர் அட்டை", "கண் மருத்துவப் பரிசோதனைச் சீட்டு / ரசீது", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட தொழிலாளர் அலுவலகம் / TNUWWB', 'online',
        'https://tnuwwb.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'tailoring_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-DOMESTIC-WORKERS-WELFARE', 'Tamil Nadu Domestic Workers Welfare Board Social Security Assistance', 'தமிழ்நாடு வீட்டுப் பணியாளர்கள் நல வாரிய சமூகப் பாதுகாப்பு உதவி', 'Veettu Paniyaalargal Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Accident insurance, maternity benefit, pension (₹1,000/month), and education assistance for registered female domestic maids, cooks, and cleaners.', 'வீட்டு வேலை செய்யும் பெண் தொழிலாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம், விபத்து நிவாரணம் மற்றும் குழந்தைகள் கல்வி உதவித்தொகை.',
        '₹1,000/month Pension (Age 60+), Marriage & Education Aid', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வீட்டுப் பணியாளர் நல வாரிய அடையாள அட்டை", "பணிபுரியும் குடியிருப்பு உரிமையாளர் அல்லது குடியிருப்போர் நல சங்க சான்று", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'both',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'domestic_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-SKILL-TRAINING-TNSDC', 'Tamil Nadu Skill Development Corporation (TNSDC) Free Youth Skill Training with Stipend', 'தமிழ்நாடு திறன் மேம்பாட்டுக் கழகம் (நான் முதல்வன்) இளைஞர் இலவச திறன் பயிற்சி', 'Naan Mudhalvan Thiran Membattu Payirchi',
        'Labour and Employment', 'skill_training', 'Free market-aligned technical and vocational skill training courses with industry certification, placement assistance, and ₹1,000/month stipend for unemployed youth.', 'வேலையில்லாத இளைஞர்களுக்கு தொழில் துறை சார்ந்த இலவச தொழில்நுட்ப திறன் பயிற்சி, மாதம் ₹1,000 உதவித்தொகை மற்றும் வேலைவாய்ப்பு ஏற்பாடு.',
        'Free Certification Training + ₹1,000/month Stipend', 'https://naanmudhalvan.tn.gov.in/', '2026-08-01', true,
        '["கல்வித் தகுதிச் சான்றிதழ் (10th/12th/Diploma/Degree Marksheet)", "ஆதார் அட்டை (Aadhaar Card)", "பாஸ்போர்ட் அளவு புகைப்படம்", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட திறன் பயிற்சி அலுவலகம் / நான் முதல்வன் போர்ட்டல்', 'online',
        'https://naanmudhalvan.tn.gov.in/', 'பயிற்சி தொகுதி தொடங்கும் போது'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '35', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'in_list', 'unemployed,student', 'person');
    END IF;
END $$;

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
        'TN-LAB-HANDLOOM-WEAVERS-PENSION', 'Tamil Nadu Handloom Weavers Social Security and Pension Scheme', 'தமிழ்நாடு கைத்தறி நெசவாளர் முதியோர் ஓய்வூதியத் திட்டம்', 'Kaithari Nesavaalar Oivoodhiya Thittam',
        'Labour and Employment', 'pension', 'Monthly old age pension of ₹1,000 provided to aged handloom and powerloom weavers who have reached 60 years of age and are unable to earn livelihood.', '60 வயது பூர்த்தியடைந்த, நலிவடைந்த கைத்தறி மற்றும் விசைத்தறி நெசவாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம் வழங்கும் திட்டம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கைத்தறி கூட்டுறவு சங்க உறுப்பினர் அட்டை", "நெசவாளர் அடையாள அட்டை", "வயதுச் சான்றிதழ் (60 வயது பூர்த்தி)", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'கைத்தறி மற்றும் துணிநூல் துறை உதவி இயக்குநர் அலுவலகம் / கூட்டுறவு சங்கம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'handloom_weaver', 'person');
    END IF;
END $$;

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
        'TN-EDU-POST-MATRIC-SC', 'Post-Matric Scholarship Scheme for SC and ST Students', 'பட்டியலினம் மற்றும் பழங்குடியினர் மாணவர்களுக்கான போஸ்ட் மெட்ரிக் கல்வி உதவித்தொகை', 'Post-Matric Kalvi Uvithogai SC ST',
        'Education', 'scholarship', '100% compulsory tuition fee waiver, maintenance allowance, and book grant for SC and ST students pursuing Higher Secondary and College degree courses.', '11, 12-ஆம் வகுப்பு மற்றும் கல்லூரி உயர்கல்வி பயிலும் பட்டியலினம் (SC) மற்றும் பழங்குடியினர் (ST) மாணவர்களுக்கான முழு கல்விக் கட்டண விலக்கு மற்றும் உதவித்தொகை.',
        '₹10,000 to ₹50,000/year (100% Fee Waiver)', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "மதிப்பெண் சான்றிதழ் (Marksheet)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)", "கல்லூரி சேர்க்கை சான்று (College Bonafide Certificate)"]'::jsonb, 'கல்லூரி முதல்வர் அலுவலகம் / மாவட்ட ஆதிதிராவிடர் நல அலுவலகம்', 'online',
        'https://adwscholarship.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '20833', 'family');
    END IF;
END $$;

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
        'TN-EDU-PRE-MATRIC-SC', 'Pre-Matric Scholarship Scheme for SC and ST Students (Classes 9 & 10)', 'பட்டியலினம் மற்றும் பழங்குடியின 9, 10-ஆம் வகுப்பு மாணவர்களுக்கான ப்ரீ-மெட்ரிக் கல்வி உதவித்தொகை', 'Pre-Matric Kalvi Uvithogai SC ST',
        'Education', 'scholarship', 'Annual educational assistance and book grant provided to SC and ST day-scholars and hostellers studying in classes 9 and 10.', '9 மற்றும் 10-ஆம் வகுப்பு பயிலும் பட்டியலினம் மற்றும் பழங்குடியின பள்ளி மாணவர்களுக்கான வருடாந்திர கல்வி உதவித்தொகை.',
        '₹3,500/year', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'online',
        'https://adwscholarship.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '17', 'person');
    END IF;
END $$;

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
        'TN-EDU-POST-MATRIC-BC-MBC', 'Post-Matric Scholarship for BC, MBC, and DNC Students', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் மாணவர்களுக்கான போஸ்ட் மெட்ரிக் கல்வி உதவித்தொகை', 'Post-Matric Kalvi Uvithogai BC MBC',
        'Education', 'scholarship', 'Tuition fees, special fees, and maintenance grant for BC, MBC, and DNC students in polytechnic, arts, science, and professional colleges.', 'கல்லூரி மற்றும் பாலிடெக்னிக் பயிலும் பிற்படுத்தப்பட்டோர், மிகவும் பிற்படுத்தப்பட்டோர் மற்றும் சீர்மரபினர் மாணவர்களுக்கான உதவித்தொகை.',
        '₹4,000 to ₹15,000/year', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "கல்லூரி அடையாள அட்டை மற்றும் கட்டண ரசீது", "வங்கி கணக்கு விவரம் (Aadhaar Seeded Bank Account)"]'::jsonb, 'கல்லூரி முதல்வர் / மாவட்ட பிற்படுத்தப்பட்டோர் நல அலுவலகம்', 'online',
        'https://bcbmcmw.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-EDU-FREE-EDUCATION-BC-DEGREE', 'Free Education Scheme for BC, MBC, and DNC 3-Year Undergraduate Degree Students', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் பட்டப்படிப்பு மாணவர்களுக்கான இலவசக் கல்வித் திட்டம்', 'Ilavasa Kalvi Thittam BC MBC Degree',
        'Education', 'scholarship', 'Complete exemption from tuition fees and special fees for BC, MBC, and DNC students pursuing 3-year undergraduate arts and science degrees in government and aided colleges.', 'அரசு மற்றும் அரசு உதவிபெறும் கலை, அறிவியல் கல்லூரிகளில் 3 ஆண்டு இளங்கலை பயிலும் BC/MBC/DNC மாணவர்களுக்கு முழு கல்விக் கட்டண விலக்கு.',
        'முழு கல்விக் கட்டண விலக்கு (Full Tuition Fee Exemption)', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (வருமானம் ₹1,00,000-க்குள்)", "12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "குடும்ப அட்டை நகல்"]'::jsonb, 'கல்லூரி அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://bcbmcmw.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '10000', 'family');
    END IF;
END $$;

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
        'TN-EDU-TAMIL-PUDHALVAN', 'Tamil Pudhalvan Higher Education Assurance Scheme for Boys', 'தமிழ்ப்புதல்வன் திட்டம் (அரசுப் பள்ளி மாணவர்கள் உயர்கல்வி உதவி)', 'Tamil Pudhalvan Thittam',
        'Education', 'monthly_allowance', 'Monthly financial assistance of ₹1,000 directly credited to bank accounts of male students from government schools pursuing undergraduate degrees, diplomas, and ITI courses.', 'அரசுப் பள்ளிகளில் (6 முதல் 12 வரை) படித்து உயர்கல்வி சேரும் மாணவர்களுக்கு மாதம் ₹1,000 உதவித்தொகை வழங்கும் திட்டம்.',
        '₹1,000/month', 'https://tamilpudhalvan.tn.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card)", "அரசுப் பள்ளி பயின்ற சான்றிதழ் (EMIS School Study Certificate)", "கல்லூரி சேர்க்கை அடையாள அட்டை", "மாணவர் பெயரிலான ஆதார் இணைக்கப்பட்ட வங்கிக் கணக்கு புத்தகம்"]'::jsonb, 'கல்லூரி இணையதள ஒருங்கிணைப்பாளர் / போர்ட்டல்', 'online',
        'https://tamilpudhalvan.tn.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'male', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'graduate,postgraduate,higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '17', 'person');
    END IF;
END $$;

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
        'TN-EDU-FIRST-GRADUATE-FEE-CONCESSION', 'First Generation Graduate Tuition Fee Concession Scheme', 'முதல் தலைமுறை பட்டதாரி கல்விக் கட்டணச் சலுகைத் திட்டம்', 'Mudhal Thalaimurai Pattadhari Katana Salugai',
        'Education', 'tuition_concession', 'Full tuition fee waiver for students who are the first graduates in their family admitted through single-window counseling in professional degree courses (Engineering, Medical, Agri).', 'குடும்பத்தில் முதல் பட்டதாரியாக பொறியியல், மருத்துவம், வேளாண்மை உள்ளிட்ட தொழில்முறை பட்டப்படிப்பில் சேரும் மாணவர்களுக்கு முழுக் கல்விக் கட்டணச் சலுகை.',
        '₹20,000 to ₹40,000/year Tuition Waiver', 'https://tnesevai.tn.gov.in/', '2026-08-01', true,
        '["வட்டாட்சியர் வழங்கும் முதல் பட்டதாரி சான்றிதழ் (First Graduate Certificate)", "குடும்ப உறுப்பினர்களின் கல்விச் சான்றிதழ்கள் அல்லது உறுதிமொழிப் படிவம்", "ஒற்றைச் சாளர சேர்க்கை ஆணை (Allotment Order)", "குடும்ப அட்டை மற்றும் ஆதார் அட்டை"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம் மற்றும் சேர்க்கை கல்லூரி', 'both',
        'https://tnesevai.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'first_graduate', 'person');
    END IF;
END $$;

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
        'TN-EDU-FREE-LAPTOP', 'Chief Minister''s Free Laptop Scheme for 12th Standard Students', 'முதலமைச்சரின் விலையில்லா மடிக்கணினி திட்டம்', 'Vilayilla Madikanini Thittam',
        'Education', 'education_device', 'Distribution of free laptops to students studying in government and government-aided schools to bridge the digital divide and encourage digital literacy.', 'அரசு மற்றும் அரசு உதவிபெறும் பள்ளிகளில் பயிலும் மேல்நிலைக் கல்வி (12-ஆம் வகுப்பு) மாணவர்களுக்கு வழங்கப்படும் இலவச மடிக்கணினி.',
        'இலவச மடிக்கணினி (Free Laptop Computer)', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["பள்ளி அடையாள அட்டை (School ID Card)", "ஆதார் அட்டை (Aadhaar Card)", "மாணவர் EMIS எண்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'கல்வியாண்டு விநியோக அட்டவணைப்படி'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '16', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '19', 'person');
    END IF;
END $$;

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
        'TN-EDU-FREE-BICYCLE', 'Free Bicycle Scheme for Class 11 Government and Aided School Students', 'அரசு மற்றும் அரசு உதவிபெறும் பள்ளி 11-ஆம் வகுப்பு மாணவர்களுக்கான விலையில்லா மிதிவண்டி திட்டம்', 'Vilayilla Midhivandi Thittam 11th Std',
        'Education', 'welfare_grant', 'Provision of free bicycles to all boys and girls studying in class 11 in government and government-aided schools to facilitate easy commuting.', 'பள்ளிக்கு எளிதாக சென்று வர அரசு மற்றும் அரசு உதவிபெறும் பள்ளிகளில் 11-ஆம் வகுப்பு பயிலும் மாணவ-மாணவிகளுக்கு இலவச மிதிவண்டி வழங்கப்படுகிறது.',
        'இலவச மிதிவண்டி (Free Bicycle)', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["பள்ளி மாணவர் சேர்க்கை சான்று (School Bonafide)", "ஆதார் அட்டை (Aadhaar Card)", "குடும்ப அட்டை நகல்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'பள்ளி மூலமாக வழங்கப்படும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '15', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-EDU-CHIEF-MINISTER-BREAKFAST', 'Chief Minister''s Breakfast Scheme for Primary School Children (Classes 1-5)', 'முதலமைச்சரின் காலை உணவுத் திட்டம் (தொடக்கப் பள்ளி 1 முதல் 5 வகுப்புகள்)', 'Mudhalamaicharin Kaalai Unavu Thittam',
        'Education', 'nutrition_support', 'Hot, hygienic, nutritious breakfast provided to all children studying in classes 1 to 5 in government primary schools across Tamil Nadu on all school working days.', 'அரசு தொடக்கப் பள்ளிகளில் 1 முதல் 5-ஆம் வகுப்பு வரை பயிலும் அனைத்து குழந்தைகளுக்கும் பள்ளிகளில் வழங்கப்படும் இலவச சத்தான காலை உணவு.',
        'இலவச காலை சத்தான உணவு', 'https://tnschools.gov.in/', '2026-08-01', true,
        '["அரசு தொடக்கப் பள்ளி மாணவர் சேர்க்கை பதிவு"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, 'சேர்க்கையின் போதே உடனடியாக பொருந்தும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'primary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '5', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '11', 'person');
    END IF;
END $$;

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
        'TN-EDU-SPECIAL-INCENTIVE-SC-GIRLS', 'Special Incentive Scheme for SC/ST Girl Students studying in 10th to 12th Standard', 'பட்டியலினம் மற்றும் பழங்குடியின 10 முதல் 12-ஆம் வகுப்பு பெண் குழந்தைகளுக்கான சிறப்பு ஊக்கத்தொகை', 'SC ST Pengal Sirappu Ookkathogai 10-12',
        'Education', 'scholarship', 'Special incentive to arrest dropout rates among Scheduled Caste and Scheduled Tribe girl students in secondary and higher secondary education.', 'பள்ளி இடைநிற்றலைத் தடுக்க 10, 11, மற்றும் 12-ஆம் வகுப்பு பயிலும் பட்டியலினம் மற்றும் பழங்குடியின மாணவிகளுக்கு வழங்கப்படும் சிறப்பு ஊக்கத்தொகை.',
        '₹1,500 to ₹2,000/year', 'https://adw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "மாணவி பெயரிலான வங்கி கணக்கு புத்தகம்"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'secondary,higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-PERIYAR-AWARD-GIRL-STUDENTS', 'Thanthai Periyar Memorial Award for BC/MBC Girl Students in Higher Secondary', 'தந்தை பெரியார் நினைவு பிற்படுத்தப்பட்டோர் மாணவியர் கல்வி ஊக்க விருது', 'Thanthai Periyar Ninaivu Ninaivu Virudhu',
        'Education', 'merit_award', 'Cash prize and certificate awarded to BC, MBC, and DNC girl students scoring top marks in 10th and 12th public examinations at district levels.', '10 மற்றும் 12-ஆம் வகுப்பு பொதுத்தேர்வில் மாவட்ட அளவில் அதிக மதிப்பெண் பெறும் BC, MBC, DNC மாணவிகளுக்கு வழங்கப்படும் தந்தை பெரியார் நினைவு விருது.',
        '₹5,000 one-time', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (BC/MBC/DNC Community Certificate)", "10-ஆம் அல்லது 12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ் (Marksheet)", "பள்ளி மாற்றுச் சான்றிதழ் (TC) மற்றும் ஆதார் அட்டை"]'::jsonb, 'மாவட்ட பிற்படுத்தப்பட்டோர் நல அலுவலகம் / முதன்மைக் கல்வி அலுவலர் (CEO)', 'offline',
        NULL, 'முடிவுகள் வெளியான பின் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-SPECIAL-SCHOLARSHIP-DISABILITY', 'Special Higher Education Scholarship for Differently Abled Students', 'மாற்றுத்திறனாளி மாணவர்களுக்கான சிறப்பு உயர்கல்வி உதவித்தொகை', 'Maatru Thiranaali Kalvi Uvithogai',
        'Education', 'scholarship', 'Scholarship grant and scribe allowance for visually challenged, hearing impaired, and locomotor disabled students pursuing higher secondary and undergraduate courses.', 'பார்வையற்றோர், காதுகேளாதோர் உள்ளிட்ட மாற்றுத்திறனாளி மாணவர்கள் மேல்நிலைக் கல்வி மற்றும் கல்லூரி படிப்பைத் தொடர வழங்கப்படும் சிறப்பு உதவித்தொகை.',
        '₹6,000 to ₹7,000/year', 'https://scd.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "கல்வி நிறுவன சேர்க்கை சான்றிதழ் (Bonafide Certificate)", "வங்கி கணக்கு புத்தகம்", "ஆதார் அட்டை"]'::jsonb, 'மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDWO)', 'both',
        'https://scd.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'higher_secondary,graduate,postgraduate', 'person');
    END IF;
END $$;

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
        'TN-EDU-BOARDING-GRANT-BC-MBC', 'Free Boarding Grant for BC/MBC/DNC Students in Hostels', 'பிற்படுத்தப்பட்டோர் மற்றும் மிகவும் பிற்படுத்தப்பட்டோர் தங்கும் விடுதி உணவுக் கட்டண மானியம்', 'Vidhuthi Unavu Maaniyam BC MBC',
        'Education', 'hostel_grant', 'Free boarding and lodging provided to rural poor BC, MBC, and DNC students admitted to department college and school hostels.', 'கிராமப்புற ஏழை BC, MBC, DNC மாணவர்கள் தங்கிப் படிக்க அரசு நலத்துறை விடுதிகளில் இலவச உணவு மற்றும் தங்குமிட வசதி.',
        'இலவச தங்குமிடம் மற்றும் உணவு (Free Boarding & Lodging)', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate)", "பள்ளி/கல்லூரி சேர்க்கை சான்றிதழ்", "இருப்பிடச் சான்றிதழ் (வருவாய்த்துறை)"]'::jsonb, 'மாவட்ட பிற்படுத்தப்பட்டோர் மற்றும் சிறுபான்மையினர் நல அலுவலகம்', 'online',
        'https://bcbmcmw.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '8333', 'family');
    END IF;
END $$;

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
        'TN-EDU-CLEANING-OCCUPATION-CHILDREN', 'Pre-Matric Scholarship to Children of Parents engaged in Unclean and Hazardous Occupations', 'தூய்மைப் பணியில் ஈடுபட்டுள்ள பெற்றோரின் குழந்தைகளுக்கு வழங்கப்படும் கல்வி உதவித்தொகை', 'Thooymai Paniyaalar Kuzhanthaigal Kalvi Uvithogai',
        'Education', 'scholarship', 'Special scholarship without caste or income ceiling for children whose parents are involved in hazardous cleaning and sanitation occupations.', 'சாதி மற்றும் வருமான வரம்பின்றி, தூய்மை மற்றும் சுகாதாரப் பணிகளில் ஈடுபட்டுள்ள பெற்றோரின் குழந்தைகளுக்கு வழங்கப்படும் பள்ளிக் கல்வி உதவித்தொகை.',
        '₹3,500 to ₹8,000/year', 'https://adw.tn.gov.in/', '2026-08-01', true,
        '["பெற்றோர் தூய்மைப் பணியாளர் என்பதற்கான உள்ளாட்சி அமைப்பு சான்றிதழ்", "பள்ளி பயிலும் சான்றிதழ் (School Study Certificate)", "மாணவர் பெயரிலான வங்கிக் கணக்கு புத்தகம்", "ஆதார் அட்டை"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம் / மாவட்ட ஆதிதிராவிடர் நல அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'primary,secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unclean_occupation_parent,sanitation_worker_family', 'person');
    END IF;
END $$;

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
        'TN-EDU-CHIEF-MINISTER-MERIT-AWARD-SC', 'Chief Minister''s Merit Award Scheme for SC and ST Students', 'முதலமைச்சரின் ஆதிதிராவிடர் மற்றும் பழங்குடியினர் சிறந்த மாணவர் தகுதி விருது', 'Chief Minister Merit Award SC ST',
        'Education', 'merit_award', 'Cash incentive of ₹3,000 per year awarded for up to 6 years for one boy and one girl from SC and ST communities in each district scoring highest in Plus Two exams.', '12-ஆம் வகுப்பு பொதுத்தேர்வில் மாவட்ட அளவில் முதலிடம் பெறும் ஆதிதிராவிடர், பழங்குடியின மாணவ-மாணவியருக்கு ஆண்டுக்கு ₹3,000 வீதம் 6 ஆண்டுகளுக்கு வழங்கப்படும் விருது.',
        '₹3,000/year for 6 years', 'https://adwscholarship.tn.gov.in/', '2026-08-01', true,
        '["12-ஆம் வகுப்பு அரசு பொதுத்தேர்வு மதிப்பெண் சான்றிதழ்", "சாதிச் சான்றிதழ் (SC/ST Community Certificate)", "தொடர்ந்து உயர்கல்வி பயில்வதற்கான கல்லூரி சேர்க்கை சான்று", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட ஆதிதிராவிடர் மற்றும் பழங்குடியினர் நல அலுவலகம்', 'offline',
        NULL, '45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'SC,ST', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'graduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
    END IF;
END $$;

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
        'TN-EDU-PM-YASASVI-OBC', 'PM YASASVI Pre-Matric Scholarship for OBC, EBC, and DNT Students (Classes 9 & 10)', 'பிஎம் யசஸ்வி இதர பிற்படுத்தப்பட்டோர் மற்றும் சீர்மரபினர் பள்ளி கல்வி உதவித்தொகை', 'PM YASASVI Pre-Matric Scholarship',
        'Education', 'scholarship', 'Centrally sponsored scholarship scheme implemented by Tamil Nadu government for meritorious OBC, EBC, and DNT students in classes 9 and 10 with annual family income up to ₹2.5 Lakhs.', 'ஆண்டு குடும்ப வருமானம் ₹2.5 லட்சத்திற்குள் உள்ள BC, MBC, DNC 9 மற்றும் 10-ஆம் வகுப்பு மாணவர்களுக்கான மத்திய-மாநில அரசின் பிஎம் யசஸ்வி கல்வி உதவித்தொகை.',
        '₹4,000/year', 'https://bcbmcmw.tn.gov.in/', '2026-08-01', true,
        '["சாதிச் சான்றிதழ் (Community Certificate)", "வருமானச் சான்றிதழ் (Income Certificate - வருமானம் ₹2.5 லட்சத்திற்குள்)", "பள்ளி சேர்க்கை சான்று (School Bonafide)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு"]'::jsonb, 'பள்ளி தலைமை ஆசிரியர் அலுவலகம் / தேசிய கல்வி உதவித்தொகை போர்ட்டல் (NSP)', 'online',
        'https://bcbmcmw.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'caste_category', 'in_list', 'BC,MBC,DNC', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '20833', 'family');
    END IF;
END $$;

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
        'TN-AGRI-PM-KISAN', 'Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) Direct Income Support', 'பிரதமர் கிசான் சம்மான் நிதி (PM-KISAN) விவசாயிகளுக்கான நேரடி வருவாய் உதவி', 'PM Kisan Samman Nidhi Vivasayigal Uvithogai',
        'Agriculture and Farmers Welfare', 'farmer_income_support', 'Direct income support of ₹6,000 per year in three equal installments of ₹2,000 every four months to all landholding farmer families across Tamil Nadu.', 'விவசாய நிலம் வைத்துள்ள விவசாய குடும்பங்களுக்கு ஆண்டுக்கு ₹6,000 (4 மாதங்களுக்கு ஒருமுறை ₹2,000 வீதம்) நேரடியாக வங்கிக் கணக்கில் வழங்கும் திட்டம்.',
        '₹6,000/year (₹2,000 every 4 months)', 'https://pmkisan.gov.in/', '2026-08-01', true,
        '["ஆதார் அட்டை (Aadhaar Card with e-KYC)", "நிலப் பட்டா / சிட்டா (Patta / Chitta document)", "நில ஆவணம் மற்றும் அடங்கல் (Land Adangal)", "ஆதார் இணைக்கப்பட்ட வங்கி கணக்கு புத்தகம் (NPCI Aadhar Seeded Bank Account)"]'::jsonb, 'வட்டார வேளாண்மை உதவி இயக்குநர் அலுவலகம் / இ-சேவை மையம்', 'both',
        'https://pmkisan.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-KURUVAI-PACKAGE', 'Kuruvai Cultivation Special Package Scheme for Delta Paddy Farmers', 'டெல்டா குறுவை சாகுபடி சிறப்பு தொகுப்புத் திட்டம் (இலவச உரம் & விதைகள்)', 'Delta Kuruvai Sagubadi Sirappu Thoguppu',
        'Agriculture and Farmers Welfare', 'input_subsidy', 'Special agricultural input package providing 100% subsidy on certified paddy seeds, urea, DAP, and potash to delta district farmers taking up Kuruvai season paddy cultivation.', 'காவிரி டெல்டா மற்றும் பாசனப் பகுதிகளில் குறுவை நெல் சாகுபடி செய்யும் விவசாயிகளுக்கு 100% மானியத்தில் சான்று பெற்ற விதைகள், யூரியா, டிஏபி, பொட்டாஷ் வழங்கும் திட்டம்.',
        '100% Subsidy on Seeds and Fertilizers (₹4,000/acre value)', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["உழவர் பதிவு எண் (Uzhavar Registration ID / AGRISNET)", "சிட்டா / பட்டா நகல் (Patta / Chitta)", "கிராம நிர்வாக அலுவலர் (VAO) வழங்கும் குறுவை சாகுபடி சான்றிதழ் / அடங்கல்", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை நகல்"]'::jsonb, 'வேளாண் விரிவாக்க மையம் (Agricultural Extension Centre) / உழவர் அலுவலர்', 'both',
        'https://tnagrisnet.tn.gov.in/', '7 முதல் 15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'paddy', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-MICRO-IRRIGATION-MIF', 'Micro Irrigation Scheme (Drip and Sprinkler Subsidy under PMKSY)', 'நுண்ணீர்ப் பாசனத் திட்டம் (சிறு/குறு விவசாயிகளுக்கு 100% மானியத்தில் சொட்டு நீர்ப்பாசனம்)', 'Nunneer Paasana Thittam Sottuneer Paasanam',
        'Agriculture and Farmers Welfare', 'irrigation_subsidy', '100% subsidy for small and marginal farmers (up to 5 acres) and 75% subsidy for other farmers to install drip and sprinkler irrigation systems to conserve ground water.', 'பாசன நீரை சேமிக்க சிறு மற்றும் குறு விவசாயிகளுக்கு 100% மானியத்திலும், இதர விவசாயிகளுக்கு 75% மானியத்திலும் சொட்டுநீர் மற்றும் தெளிப்பு நீர்ப்பாசன கருவிகள் அமைத்தல்.',
        '100% Subsidy for Small/Marginal Farmers, 75% for other farmers', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["சிறு/குறு விவசாயி சான்றிதழ் (வட்டாட்சியர்/VAO சான்றிதழ்)", "நில உரிமை பட்டா, சிட்டா மற்றும் நில வரைபடம் (FMB sketch)", "கிணறு / ஆழ்துளை கிணறு பாசன நீர் ஆதாரம் இருப்பதற்கான சான்று", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார தோட்டக்கலை / வேளாண்மை உதவி இயக்குநர் அலுவலகம்', 'online',
        'https://tnhorticulture.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-UZHAVAR-PATHUKAPPU-PENSION', 'Chief Minister''s Farmers Social Security Scheme (Uzhavar Pathukappu Thittam) Monthly Pension', 'முதலமைச்சரின் உழவர் பாதுகாப்புத் திட்டம் - முதியோர் ஓய்வூதியம்', 'Uzhavar Pathukappu Thittam Mudhiyor Oivoodhiyam',
        'Agriculture and Farmers Welfare', 'pension', 'Monthly pension of ₹1,000 provided to aged small, marginal, and tenant farmers and agricultural labourers aged 60 and above registered under Uzhavar Pathukappu Thittam.', 'உழவர் பாதுகாப்புத் திட்டத்தில் பதிவுசெய்த 60 வயது பூர்த்தியடைந்த சிறு, குறு, குத்தகை விவசாயிகள் மற்றும் விவசாயத் தொழிலாளர்களுக்கு மாதம் ₹1,000 ஓய்வூதியம்.',
        '₹1,000/month', 'https://www.tnesevai.tn.gov.in/', '2026-08-01', true,
        '["முதலமைச்சரின் உழவர் பாதுகாப்பு அட்டை (Uzhavar Card)", "வயதுச் சான்றிதழ் (Age Proof - 60 வயது பூர்த்தி)", "வருமானச் சான்றிதழ் (Income Certificate)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டாட்சியர் அலுவலகம் (சமூகப் பாதுகாப்புத் திட்டம்) / இ-சேவை மையம்', 'both',
        'https://www.tnesevai.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '2.5', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '10000', 'family');
    END IF;
END $$;

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
        'TN-AGRI-CROP-INSURANCE-PMFBY', 'Pradhan Mantri Fasal Bima Yojana (PMFBY) Crop Insurance Scheme', 'பிரதம மந்திரி பயிர் காப்பீட்டுத் திட்டம் (PMFBY)', 'PM Fasal Bima Yojana Payir Kaapeedu',
        'Agriculture and Farmers Welfare', 'crop_insurance', 'Comprehensive crop insurance protection covering yield loss due to non-preventable risks (natural drought, floods, inundation, pests, and unseasonal rainfall) at nominal farmer premium rates (1.5% to 2%).', 'வறட்சி, வெள்ளம், பூச்சித் தாக்குதல் போன்ற இயற்கை இடர்பாடுகளால் ஏற்படும் பயிர் இழப்புகளுக்கு குறைந்த பிரீமியம் விகிதத்தில் முழு நிதி இழப்பீடு வழங்கும் பயிர் காப்பீட்டுத் திட்டம்.',
        'Full Sum Insured on Crop Loss due to drought/flood', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பயிர் சாகுபடி அடங்கல் (Adangal from VAO / e-Adangal)", "பட்டா / சிட்டா நகல் (Patta / Chitta document)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)", "ஆதார் அட்டை (Aadhaar Card)"]'::jsonb, 'தொடக்க வேளாண்மை கூட்டுறவு கடன் சங்கம் (PACCS) / பொது இ-சேவை மையம்', 'both',
        'https://pmfby.gov.in/', 'பயிர் அறுவடை பரிசோதனை முடிவுகளுக்குப் பின்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-MILLETS-MISSION', 'Tamil Nadu Millet Mission Cultivation Incentive and Seed Subsidy', 'தமிழ்நாடு சிறுதானிய இயக்கம் - சாகுபடி மானியம் மற்றும் விதைகள்', 'Tamil Nadu Sirudhaaniya Iyakkam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Financial incentive of ₹5,000 per hectare along with free bio-fertilizers and quality seeds for farmers cultivating millets like ragi, kambu, thinai, and varagu.', 'கேழ்வரகு, கம்பு, தினை, வரகு உள்ளிட்ட சிறுதானியங்களை சாகுபடி செய்யும் விவசாயிகளுக்கு ஹெக்டேருக்கு ₹5,000 மானியம் மற்றும் சான்று பெற்ற விதைகள் வழங்கும் திட்டம்.',
        '₹5,000/hectare Input Subsidy', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["சிறுதானிய சாகுபடி அடங்கல் (Adangal proof for Millets)", "பட்டா / சிட்டா நகல்", "உழவர் பதிவு அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'both',
        'https://tnagrisnet.tn.gov.in/', '15 முதல் 30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'millets', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-SOLAR-PUMP-SUBSIDY', 'Standalone Solar Powered Pumping System Subsidy Scheme (PM-KUSUM Component-B)', 'விவசாயிகளுக்கு 70% மானியத்தில் தனித்து இயங்கும் சூரியசக்தி பம்புசெட்டுகள் அமைத்தல்', 'Sooriya Sakthi Pumbset Maaniyam',
        'Agriculture and Farmers Welfare', 'solar_irrigation', 'Provision of standalone AC/DC solar agricultural pumping systems (up to 10 HP) with 70% capital subsidy from Central and State Governments.', 'மின் இணைப்பு இல்லாத விவசாய நிலங்களுக்கு 70% மானியத்தில் 5 முதல் 10 குதிரைத்திறன் கொண்ட சூரியசக்தி பம்புசெட்டுகள் அமைக்கும் திட்டம்.',
        '70% Subsidy on Solar Pump System (up to ₹2,00,000)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["பட்டா / சிட்டா மற்றும் நில உரிமை ஆவணம்", "கிணறு / ஆழ்துளை கிணறு நிலத்தடி நீர் கிடைக்கும் சான்றிதழ்", "விவசாயி பங்குத் தொகை செலுத்துவதற்கான உறுதிமொழி", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை"]'::jsonb, 'வேளாண் பொறியியல் துறை உதவி செயற்பொறியாளர் அலுவலகம்', 'online',
        'https://aed.tn.gov.in/', '45 முதல் 60 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '1.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-FARM-MACHINERY-SUBSIDY', 'Subsidized Agricultural Machinery & Power Tillers Scheme (SMAM)', 'வேளாண் இயந்திரமயமாக்கல் திட்டம் - பவர்டில்லர் மற்றும் கருவிகள் மானியம்', 'Velan Iyandhiramayamakkal Thittam',
        'Agriculture and Farmers Welfare', 'machinery_subsidy', 'Capital subsidy of up to 50% for SC, ST, women, and small/marginal farmers for purchasing power tillers, rotavators, weeders, and paddy transplanters.', 'பவர்டில்லர், களை எடுக்கும் கருவி, நெல் நடவு இயந்திரம் உள்ளிட்ட வேளாண் கருவிகள் வாங்க சிறு, குறு, பெண் விவசாயிகளுக்கு 50% வரை மானியம்.',
        '50% Subsidy for SC/ST/Women/Small Farmers (up to ₹1,00,000)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["சிறு/குறு விவசாயி சான்றிதழ் (Small Farmer Certificate)", "பட்டா மற்றும் சிட்டா நகல்", "விவசாய இயந்திர விலைப்பட்டியல் (Quotation from approved dealer)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வேளாண் பொறியியல் துறை அலுவலகம்', 'online',
        'https://aed.tn.gov.in/', '30 முதல் 45 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-KALAIGNAR-ALL-VILLAGE', 'Kalaignar All Village Integrated Agriculture Development Programme (KAVIADP)', 'கலைஞரின் அனைத்து கிராம ஒருங்கிணைந்த வேளாண் வளர்ச்சித் திட்டம்', 'Kalaignarin Anaithu Grama Oringinaindha Velan Thittam',
        'Agriculture and Farmers Welfare', 'integrated_development', 'Holistic village-level mission providing free coconut saplings, vegetable seed kits, hand sprayers, and horticulture saplings to bring fallow lands under cultivation.', 'கிராமப் பஞ்சாயத்துகளில் தரிசு நிலங்களை சாகுபடிக்கு கொண்டு வர இலவச தென்னங்கன்றுகள், காய்கறி விதை பெட்டகங்கள், கைத்தெளிப்பான்கள் வழங்கும் திட்டம்.',
        'Free Coconut Seedlings, Fruit Plants and Hand Sprayers', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["குடும்ப அட்டை நகல்", "ஆதார் அட்டை நகல்", "கிராம பஞ்சாயத்து இருப்பிடச் சான்று"]'::jsonb, 'கிராம ஊராட்சி மன்ற அலுவலகம் / வேளாண் விரிவாக்க மையம்', 'offline',
        NULL, 'கிராம முகாம்களில் உடனடியாக வழங்கப்படும்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-PULSES-PRODUCTION-MISSION', 'National Food Security Mission - Pulses Production and Quality Seed Distribution', 'தேசிய உணவுப் பாதுகாப்பு இயக்கம் - பருப்பு வகை பயிர்கள் ஊக்கத்தொகை', 'Paruppu Vagaigal Saagubadi Maaniyam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Incentive support and 50% subsidy on certified blackgram and greengram seeds to promote pulses cultivation as bund crops and rice-fallows.', 'உளுந்து, பாசிப்பயறு உள்ளிட்ட பருப்பு வகை பயிர்களை வரப்புப் பயிராகவும் நெல் தரிசிலும் சாகுபடி செய்ய 50% விதை மானியம் மற்றும் ஊக்கத்தொகை.',
        '₹3,000/hectare Input Incentive', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["நிலப் பட்டா / சிட்டா நகல்", "பயிர் அடங்கல் (Adangal proof for Pulses)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண்மை விரிவாக்க மையம்', 'both',
        'https://tnagrisnet.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'pulses', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-ORGANIC-FARMING-SUBSIDY', 'Paramparagat Krishi Vikas Yojana (PKVY) Organic Farming Promotion', 'பாரம்பரிய இயற்கை விவசாய மேம்பாட்டுத் திட்டம் - இடுபொருட்கள் மானியம்', 'Iyarkai Vivasaayam PKVY Maaniyam',
        'Agriculture and Farmers Welfare', 'organic_farming', 'Financial assistance of ₹15,000 per hectare over 3 years for organic inputs, vermicompost units, bio-fertilizers, and organic certification.', 'இயற்கை மற்றும் இயற்கை உரம் சார்ந்த சாகுபடியை ஊக்குவிக்க 3 ஆண்டுகளில் ஹெக்டேருக்கு ₹15,000 இடுபொருள் மானியம் மற்றும் சான்றளிப்பு உதவி.',
        '₹15,000/hectare over 3 years', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பட்டா, சிட்டா நகல்", "இயற்கை விவசாயக் குழுவில் (Organic Cluster) உறுப்பினர் சான்று", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-OILSEEDS-EXPANSION', 'Oilseeds Production Expansion and Groundnut Seed Subsidy Scheme', 'எண்ணெய் வித்துக்கள் சாகுபடி பரப்பு விரிவாக்கம் மற்றும் விதை மானியம்', 'Ennai Vithukkal Nilakkadalai Maaniyam',
        'Agriculture and Farmers Welfare', 'crop_incentive', 'Distribution of certified groundnut, sesame, and sunflower seeds at 50% subsidy to expand edible oilseed production in dry and rainfed tracts.', 'நிலக்கடலை, எள், சூரியகாந்தி உள்ளிட்ட எண்ணெய் வித்துக்கள் பயிரிடும் விவசாயிகளுக்கு 50% மானியத்தில் சான்று பெற்ற விதைகள் வழங்கும் திட்டம்.',
        '50% Subsidy on Certified Oilseeds', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["பட்டா மற்றும் சிட்டா நகல்", "விவசாயி அடையாள அட்டை", "ஆதார் அட்டை"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம்', 'both',
        'https://tnagrisnet.tn.gov.in/', '7 முதல் 15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'oilseeds', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-DRYLAND-DEVELOPMENT-MISSION', 'Mission on Sustainable Dryland Agriculture (MSDA) for Rainfed Farmers', 'நீடித்த நிலையான மானாவாரி வேளாண்மை இயக்கம் (MSDA)', 'Maanavaari Velanmai Iyakkam MSDA',
        'Agriculture and Farmers Welfare', 'dryland_mission', 'Cluster-based soil health improvement, deep summer ploughing subsidy, and drought-tolerant seed distribution for rainfed and dryland farmers.', 'மழை நம்பி விவசாயம் செய்யும் மானாவாரி நிலங்களில் கோடை உழவு மானியம், மண்வள மேலாண்மை மற்றும் வறட்சியைத் தாங்கும் பயிர் விதைகள் வழங்கும் திட்டம்.',
        'Free Soil Health Management and Agronomic Inputs', 'https://tnagrisnet.tn.gov.in/', '2026-08-01', true,
        '["மானாவாரி நிலப் பட்டா மற்றும் அடங்கல்", "ஆதார் அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார வேளாண் விரிவாக்க மையம் (AEC)', 'offline',
        NULL, '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'less_or_equal', '5.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-HORTICULTURE-PLANTING-MATERIAL', 'National Horticulture Mission - Subsidized Fruit Plants and Shade Net Polyhouses', 'தோட்டக்கலை பயிர்கள் நடவு மற்றும் பசுமை குடில் அமைக்கும் மானியத் திட்டம்', 'Thottakallai Payirgal Pasumai Kudil Maaniyam',
        'Agriculture and Farmers Welfare', 'horticulture_subsidy', '40% to 50% subsidy on high yielding fruit saplings (Mango, Guava, Acid Lime) and protected cultivation shade nets to boost horticulture income.', 'மா, கொய்யா, எலுமிச்சை உள்ளிட்ட பழ மரக்கன்றுகள் நடவு செய்வதற்கும் பசுமை நிழல்வலை குடில் அமைப்பதற்கும் 40% முதல் 50% வரை மானியம்.',
        '40% to 50% Capital Subsidy on Planting Material', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["தோட்டக்கலை நில பட்டா, சிட்டா மற்றும் வரைபடம்", "சிறு/குறு விவசாயி சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'வட்டார தோட்டக்கலை உதவி இயக்குநர் அலுவலகம்', 'online',
        'https://tnhorticulture.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'horticulture', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.5', 'person');
    END IF;
END $$;

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
        'TN-AGRI-FARM-POND-SUBSIDY', 'Rainwater Harvesting Farm Ponds Construction Subsidy for Dryland Farmers', 'மானாவாரி விவசாய நிலங்களில் பண்ணைக் குட்டைகள் அமைக்க 100% மானியத் திட்டம்', 'Pannai Kuttaigal Amaikka 100% Maaniyam',
        'Agriculture and Farmers Welfare', 'water_conservation', '100% grant (up to ₹1,00,000) for excavation of rainwater harvesting farm ponds (dimensions 30m x 30m x 1.5m) in drylands to store runoff water.', 'மழைநீரை நிலத்தில் சேமித்து பாசனத்திற்கு பயன்படுத்த விவசாய நிலத்தில் பண்ணைக்குட்டை அமைக்க 100% முழு மானியம் (ரூ.1,00,000 வரை).',
        '100% Subsidy (up to ₹1,00,000 for pond excavation)', 'https://aed.tn.gov.in/', '2026-08-01', true,
        '["நிலப் பட்டா, சிட்டா மற்றும் அடங்கல்", "பண்ணைக்குட்டை அமைக்க உத்தேசித்துள்ள இடத்தின் வரைபடம்", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை"]'::jsonb, 'வேளாண் பொறியியல் துறை உதவி செயற்பொறியாளர் அலுவலகம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '1.0', 'person');
    END IF;
END $$;

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
        'TN-AGRI-COCONUT-DEVELOPMENT', 'Integrated Coconut Development Scheme (Seedling Distribution & Pest Management)', 'ஒருங்கிணைந்த தென்னை வளர்ச்சித் திட்டம் - கன்றுகள் மற்றும் பூச்சி மேலாண்மை', 'Oringinaindha Thennai Valarchi Thittam',
        'Agriculture and Farmers Welfare', 'crop_incentive', '50% subsidy on hybrid coconut seedlings, organic manure, and biological control agents for coconut rhinoceros beetle and red palm weevil management.', 'வீரிய ஒட்டு தென்னங்கன்றுகள் வாங்குவதற்கும், காண்டாமிருக வண்டு தாக்குதலைக் கட்டுப்படுத்தவும் தென்னை விவசாயிகளுக்கு 50% மானியம்.',
        '50% Subsidy on Hybrid Seedlings', 'https://tnhorticulture.tn.gov.in/', '2026-08-01', true,
        '["தென்னை சாகுபடி பட்டா மற்றும் சிட்டா", "விவசாயி அடையாள அட்டை", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'வட்டார தோட்டக்கலை அலுவலர் அலுவலகம்', 'both',
        'https://tnhorticulture.tn.gov.in/', '15 முதல் 20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'farmer', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'crop_type', 'equals', 'coconut', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'land_holding_acres', 'greater_than', '0.0', 'person');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-GRADUATE', 'Unemployment Assistance Scheme for Graduate and Post-Graduate Job Seekers', 'வேலைவாய்ப்பற்ற பட்டதாரி இளைஞர்களுக்கான மாதாந்திர உதவித்தொகை திட்டம்', 'Velai Vaaippatra Pattadhari Maadhathira Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Monthly financial allowance provided for up to 3 years to unemployed graduates and post-graduates registered continuously for at least 5 years in employment exchanges.', 'வேலைவாய்ப்பு அலுவலகத்தில் 5 ஆண்டுகளுக்கு மேல் தொடர்ந்து பதிவு செய்து காத்திருக்கும் பட்டதாரி மற்றும் முதுகலை இளைஞர்களுக்கு வழங்கப்படும் மாதாந்திர உதவித்தொகை.',
        '₹600/month (₹1,800/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு அலுவலக பதிவு அடையாள அட்டை (Employment Card)", "பட்டப்படிப்பு / முதுகலை சான்றிதழ் (Degree Certificate)", "வருமானச் சான்றிதழ் (ஆண்டு வருமானம் ₹2,00,000-க்குள்)", "வேலையில்லை என்பதற்கான சுய அறிவிப்புப் படிவம்", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு மற்றும் தொழில்நெறி வழிகாட்டும் மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '20', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-HSC', 'Unemployment Assistance Scheme for Higher Secondary (12th Passed) Job Seekers', '12-ஆம் வகுப்பு தேர்ச்சி பெற்ற வேலைவாய்ப்பற்ற இளைஞர்களுக்கான உதவித்தொகை', '12th Muditha Velai Vaaippatra Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Financial allowance of ₹400 per month given for up to 3 years to unemployed Plus Two candidates registered continuously with employment exchanges for 5 years.', 'மேல்நிலைக் கல்வி (12-ஆம் வகுப்பு) முடித்து 5 ஆண்டுகள் வேலைவாய்ப்பு அலுவலகத்தில் பதிவு செய்து காத்திருக்கும் இளைஞர்களுக்கு மாதம் ₹400 உதவி.',
        '₹400/month (₹1,200/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு அலுவலக பதிவு அட்டை (Employment Card)", "12-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "வருமானச் சான்றிதழ் (வட்டாட்சியர் அலுவலகம்)", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு மற்றும் தொழில்நெறி வழிகாட்டும் மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'higher_secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-SSLC', 'Unemployment Assistance Scheme for SSLC (10th Passed) Job Seekers', 'பத்தாம் வகுப்பு தேர்ச்சி பெற்ற வேலைவாய்ப்பற்றோருக்கான உதவித்தொகை', '10th Muditha Velai Vaaippatra Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Quarterly assistance of ₹900 (₹300/month) for up to 3 years to unemployed SSLC candidates registered for 5 continuous years in employment exchanges.', '10-ஆம் வகுப்பு தேர்ச்சி பெற்று 5 ஆண்டுகள் வேலைவாய்ப்பு அலுவலகத்தில் பதிவு செய்து காத்திருக்கும் நபர்களுக்கு மாதம் ₹300 வீதம் காலாண்டுக்கு ₹900 உதவி.',
        '₹300/month (₹900/quarter)', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["வேலைவாய்ப்பு பதிவு அடையாள அட்டை", "10-ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்", "வருமானச் சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு அலுவலகம் / இ-சேவை மையம்', 'online',
        'https://employmentexchange.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'equals', 'secondary', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'total_household_income', 'less_or_equal', '16666', 'family');
    END IF;
END $$;

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
        'TN-LAB-UNEMPLOYMENT-ASSISTANCE-DISABLED', 'Special Unemployment Assistance for Differently Abled Job Seekers', 'மாற்றுத்திறனாளி வேலைவாய்ப்பற்றோருக்கான சிறப்பு உதவித்தொகை', 'Maatru Thiranaali Velai Vaaippatra Sirappu Uvithogai',
        'Labour and Employment', 'unemployment_assistance', 'Enhanced monthly unemployment allowance without upper age limit for differently abled job seekers registered continuously for at least 1 year in employment exchanges.', 'வேலைவாய்ப்பு அலுவலகத்தில் 1 ஆண்டு பதிவு செய்துள்ள மாற்றுத்திறனாளி வேலை தேடுவோருக்கு மாதம் ₹600 முதல் ₹1,000 வரை வழங்கப்படும் சிறப்பு உதவித்தொகை.',
        '₹600 to ₹1,000/month', 'https://employmentexchange.tn.gov.in/', '2026-08-01', true,
        '["மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)", "வேலைவாய்ப்பு பதிவு அட்டை (Employment Registration Card)", "கல்விச் சான்றிதழ்கள்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட வேலைவாய்ப்பு அலுவலகம்', 'both',
        'https://employmentexchange.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'unemployed', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'disability_status', 'equals', 'true', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-PENSION', 'Tamil Nadu Construction Workers Welfare Board Monthly Pension Scheme (Age 60+)', 'தமிழ்நாடு கட்டுமானத் தொழிலாளர்கள் நல வாரிய முதியோர் ஓய்வூதியம்', 'Kattumana Thozhilaalar Nala Vaariya Oivoodhiyam',
        'Labour and Employment', 'pension', 'Monthly pension of ₹1,000 provided to registered building and construction workers who have reached 60 years of age and completed at least 5 years of registration in the board.', 'கட்டுமானத் தொழிலாளர்கள் நல வாரியத்தில் 5 ஆண்டுகளுக்கு மேல் பதிவு செய்து 60 வயது பூர்த்தியடைந்த தொழிலாளர்களுக்கு மாதம் ₹1,000 ஓய்வூதியம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கட்டுமான நல வாரிய உறுப்பினர் அடையாள அட்டை (TNUWWB Smart Card)", "வயதுச் சான்றிதழ் (ஆதார் / வாக்காளர் அட்டை - 60 வயது பூர்த்தி)", "வாரிய சந்தா செலுத்திய ரசீது / புதுப்பித்தல் விவரம்", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'தொழிலாளர் உதவி ஆணையர் (சமூகப் பாதுகாப்புத் திட்டம்) அலுவலகம் / TNUWWB போர்ட்டல்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-ACCIDENT-RELIEF', 'Tamil Nadu Construction Workers Welfare Board Accidental Death and Disability Relief', 'கட்டுமானத் தொழிலாளர்கள் விபத்து மரணம் மற்றும் ஊன நிவாரண நிதி', 'Kattumana Thozhilaalar Vibathu Nivarana Nidhi',
        'Labour and Employment', 'accident_relief', 'Ex-gratia financial assistance of ₹5,00,000 in case of accidental death at worksite or ₹1,00,000 to ₹5,00,000 for permanent total disability for registered construction workers.', 'பணியிட விபத்தில் உயிரிழக்கும் பதிவு பெற்ற கட்டுமானத் தொழிலாளர்களின் குடும்பத்திற்கு ₹5,00,000 மற்றும் நிரந்தர ஊனத்திற்கு ₹1,00,000 முதல் ₹5,00,000 வரை நிவாரணம்.',
        '₹5,00,000 for accidental death', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாரிய உறுப்பினர் அட்டை (TNUWWB Registration Card)", "முதல் தகவல் அறிக்கை (FIR) மற்றும் பிரேத பரிசோதனை அறிக்கை (Postmortem Report)", "இறப்புச் சான்றிதழ் மற்றும் வாரிசுச் சான்றிதழ்", "வாரிசுதாரர் ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'தொழிலாளர் உதவி ஆணையர் (சமூகப் பாதுகாப்புத் திட்டம்) அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '60', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-MARRIAGE-ASSISTANCE', 'Tamil Nadu Construction Workers Welfare Board Marriage Financial Assistance', 'கட்டுமானத் தொழிலாளர்கள் நல வாரிய திருமண நிதி உதவி', 'Kattumana Thozhilaalar Thirumana Nidhi Uvithogai',
        'Labour and Employment', 'marriage_assistance', 'Marriage financial assistance of ₹5,000 for male workers and ₹7,000 for female workers (or their children) provided by the Construction Workers Welfare Board.', 'பதிவு பெற்ற கட்டுமானத் தொழிலாளி அல்லது அவர்களின் மகன்/மகள் திருமணத்திற்கு ₹5,000 (ஆண்) மற்றும் ₹7,000 (பெண்) திருமண நிதி உதவி.',
        '₹5,00,0 (Men) / ₹7,000 (Women)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கட்டுமான நல வாரிய உறுப்பினர் அட்டை", "திருமண அழைப்பிதழ் மற்றும் திருமணப் பதிவுச் சான்றிதழ் (Marriage Certificate)", "மணமகன் மற்றும் மணமகள் வயதுச் சான்றிதழ்", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'TNUWWB இணையதளம் / மாவட்ட தொழிலாளர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'marital_status', 'equals', 'married', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-MATERNITY', 'Maternity Financial Assistance for Registered Female Construction Workers', 'பதிவுபெற்ற பெண் கட்டுமானத் தொழிலாளர்களுக்கான மகப்பேறு உதவித்தொகை', 'Pen Kattumana Thozhilaalar Magapperu Uvithogai',
        'Labour and Employment', 'maternity_benefit', 'Maternity assistance of ₹6,000 (₹3,000 on delivery and ₹3,000 after 30 days) and miscarriage assistance of ₹3,000 for registered female construction workers.', 'வாரியத்தில் பதிவுபெற்ற பெண் கட்டுமானத் தொழிலாளர்களுக்கு குழந்தை பிறப்பின் போது ₹6,000 மகப்பேறு உதவித்தொகை வழங்கும் திட்டம்.',
        '₹6,000 (₹3,000 on delivery, ₹3,000 post-delivery)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாரிய உறுப்பினர் அடையாள அட்டை (TNUWWB ID)", "அரசு மருத்துவமனை குழந்தை பிறப்புச் சான்றிதழ் (Birth Certificate)", "தாய் சேய் நல அட்டை (RCH ID card)", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'தொழிலாளர் நல வாரிய போர்ட்டல் / தொழிலாளர் உதவி ஆணையர்', 'online',
        'https://tnuwwb.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'registered_construction_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '19', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '40', 'person');
    END IF;
END $$;

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
        'TN-LAB-CONSTRUCTION-BOARD-EDUCATION', 'Educational Assistance Scheme for Children of Registered Construction Workers', 'கட்டுமானத் தொழிலாளர்களின் குழந்தைகளுக்கு வழங்கப்படும் கல்வி உதவித்தொகை', 'Kattumana Thozhilaalar Kuzhanthaigal Kalvi Uvithogai',
        'Labour and Employment', 'education_assistance', 'Annual educational scholarship ranging from ₹1,000 to ₹12,000 per year for children of registered construction workers studying from 10th to Post Graduate and professional degrees.', '10-ஆம் வகுப்பு முதல் தொழிற்கல்வி, பட்டப்படிப்பு வரை பயிலும் கட்டுமானத் தொழிலாளர்களின் குழந்தைகளுக்கு ஆண்டுதோறும் ₹1,000 முதல் ₹12,000 வரை கல்வி உதவி.',
        '₹1,000 to ₹12,000/year', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["பெற்றோரின் கட்டுமான நல வாரிய உறுப்பினர் அட்டை", "மாணவர் பயிலும் சான்றிதழ் (Bonafide Certificate)", "கடந்த ஆண்டு மதிப்பெண் சான்றிதழ்", "மாணவர் பெயரிலான வங்கி கணக்கு புத்தகம்"]'::jsonb, 'TNUWWB போர்ட்டல் / தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'equals', 'student', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'education_level', 'in_list', 'secondary,higher_secondary,graduate,postgraduate', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'construction_worker_child', 'person');
    END IF;
END $$;

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
        'TN-LAB-UNORGANIZED-WORKERS-PENSION', 'Tamil Nadu Unorganized Workers Welfare Board Monthly Pension Scheme', 'தமிழ்நாடு அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் நல வாரிய ஓய்வூதியம்', 'Amaippusaara Thozhilaalar Oivoodhiyam',
        'Labour and Employment', 'pension', 'Monthly social security pension of ₹1,000 provided to manual and unorganized workers aged 60 and above registered under the Tamil Nadu Manual Workers Welfare Board.', 'அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் நல வாரியத்தில் பதிவு செய்து 60 வயது பூர்த்தியடைந்த தொழிலாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["அமைப்புசாரா தொழிலாளர் நல வாரிய உறுப்பினர் அட்டை (TNUWWB Card)", "வயதுச் சான்றிதழ் (60 வயது பூர்த்தி)", "ஆதார் அட்டை (Aadhaar Card)", "வங்கி கணக்கு புத்தகம் (Bank Passbook)"]'::jsonb, 'மாவட்ட தொழிலாளர் சமூகப் பாதுகாப்புத் திட்ட அலுவலகம் / TNUWWB போர்ட்டல்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unorganized_worker', 'person');
    END IF;
END $$;

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
        'TN-LAB-MANUAL-WORKERS-ACCIDENT-RELIEF', 'Manual Workers Social Security Scheme - Natural Death and Funeral Relief', 'அமைப்புசாரா உடலுழைப்புத் தொழிலாளர்கள் இயற்கை மரணம் & ஈமச்சடங்கு நிதி', 'Udaluzhaippu Thozhilaalar Eemachadangu Nidhi',
        'Labour and Employment', 'death_relief', 'Financial grant of ₹20,000 for natural death and ₹5,000 for funeral expenses provided to nominees of registered manual workers in unorganized sectors.', 'அமைப்புசாரா தொழிலாளர்கள் இயற்கை மரணமடைந்தால் குடும்பத்தினருக்கு ₹20,000 மற்றும் உடனடியாக ₹5,000 ஈமச்சடங்கு உதவித்தொகை வழங்கும் திட்டம்.',
        '₹25,000 (Natural Death Relief + Funeral Assistance)', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["இறந்த தொழிலாளியின் நல வாரிய அட்டை", "இறப்புச் சான்றிதழ் (Death Certificate)", "வாரிசுச் சான்றிதழ் (Legal Heir Certificate)", "வாரிசுதாரர் ஆதார் மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் அலுவலகம் / TNUWWB', 'both',
        'https://tnuwwb.tn.gov.in/', '15 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'unorganized_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-DRIVER-BOARD-VEHICLE-ASSISTANCE', 'Tamil Nadu Auto Rickshaws and Taxi Drivers Welfare Board Welfare Scheme', 'தமிழ்நாடு ஆட்டோ மற்றும் வாடகை வாகன ஓட்டுநர்கள் நல வாரிய உதவி', 'Auto Vaadagai Vaagana Ottunargal Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Comprehensive welfare benefits including accidental relief (₹5,00,000), pension, marriage aid, and spectacles assistance for auto and taxi drivers.', 'ஆட்டோ மற்றும் வாடகை வாகன ஓட்டுநர்கள் நல வாரியத்தில் பதிவு பெற்ற ஓட்டுநர்களுக்கு விபத்து நிவாரணம், திருமணம், கல்வி மற்றும் கண் கண்ணாடி உதவித்தொகை.',
        'Accident Relief (₹5,00,000) & Welfare Grants', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வாகன ஓட்டுநர் நல வாரிய அட்டை", "செல்லத்தக்க ஓட்டுநர் உரிமம் (Commercial Driving License with Badge)", "ஆதார் அட்டை மற்றும் குடும்ப அட்டை", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'online',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'in_list', 'self_employed,private_employee,daily_wage', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'auto_taxi_driver,driver_license', 'person');
    END IF;
END $$;

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
        'TN-LAB-TAILORING-BOARD-ASSISTANCE', 'Tamil Nadu Tailoring Workers Welfare Board Maternity and Spectacles Assistance', 'தமிழ்நாடு தையல் தொழிலாளர்கள் நல வாரிய மகப்பேறு & மூக்குக்கண்ணாடி உதவி', 'Thaiyal Thozhilaalar Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Spectacles purchase reimbursement of ₹500, maternity assistance of ₹6,000, and pension benefits for registered tailoring and garment workers.', 'தையல் தொழிலாளர் நல வாரிய உறுப்பினர்களுக்கு கண் பார்வைக் குறைபாட்டிற்கு கண்ணாடி வாங்க ₹500 மற்றும் மகப்பேறு உதவித்தொகை ₹6,000 வழங்கும் திட்டம்.',
        '₹500 for Spectacles, ₹6,000 Maternity Assistance', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["தையல் தொழிலாளர் நல வாரிய உறுப்பினர் அட்டை", "கண் மருத்துவப் பரிசோதனைச் சீட்டு / ரசீது", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'மாவட்ட தொழிலாளர் அலுவலகம் / TNUWWB', 'online',
        'https://tnuwwb.tn.gov.in/', '20 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'tailoring_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-DOMESTIC-WORKERS-WELFARE', 'Tamil Nadu Domestic Workers Welfare Board Social Security Assistance', 'தமிழ்நாடு வீட்டுப் பணியாளர்கள் நல வாரிய சமூகப் பாதுகாப்பு உதவி', 'Veettu Paniyaalargal Nala Vaariya Uvithogai',
        'Labour and Employment', 'welfare_grant', 'Accident insurance, maternity benefit, pension (₹1,000/month), and education assistance for registered female domestic maids, cooks, and cleaners.', 'வீட்டு வேலை செய்யும் பெண் தொழிலாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம், விபத்து நிவாரணம் மற்றும் குழந்தைகள் கல்வி உதவித்தொகை.',
        '₹1,000/month Pension (Age 60+), Marriage & Education Aid', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["வீட்டுப் பணியாளர் நல வாரிய அடையாள அட்டை", "பணிபுரியும் குடியிருப்பு உரிமையாளர் அல்லது குடியிருப்போர் நல சங்க சான்று", "ஆதார் அட்டை மற்றும் வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட தொழிலாளர் உதவி ஆணையர் அலுவலகம்', 'both',
        'https://tnuwwb.tn.gov.in/', '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'gender', 'equals', 'female', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'domestic_worker', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
    END IF;
END $$;

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
        'TN-LAB-SKILL-TRAINING-TNSDC', 'Tamil Nadu Skill Development Corporation (TNSDC) Free Youth Skill Training with Stipend', 'தமிழ்நாடு திறன் மேம்பாட்டுக் கழகம் (நான் முதல்வன்) இளைஞர் இலவச திறன் பயிற்சி', 'Naan Mudhalvan Thiran Membattu Payirchi',
        'Labour and Employment', 'skill_training', 'Free market-aligned technical and vocational skill training courses with industry certification, placement assistance, and ₹1,000/month stipend for unemployed youth.', 'வேலையில்லாத இளைஞர்களுக்கு தொழில் துறை சார்ந்த இலவச தொழில்நுட்ப திறன் பயிற்சி, மாதம் ₹1,000 உதவித்தொகை மற்றும் வேலைவாய்ப்பு ஏற்பாடு.',
        'Free Certification Training + ₹1,000/month Stipend', 'https://naanmudhalvan.tn.gov.in/', '2026-08-01', true,
        '["கல்வித் தகுதிச் சான்றிதழ் (10th/12th/Diploma/Degree Marksheet)", "ஆதார் அட்டை (Aadhaar Card)", "பாஸ்போர்ட் அளவு புகைப்படம்", "வங்கி கணக்கு புத்தகம்"]'::jsonb, 'மாவட்ட திறன் பயிற்சி அலுவலகம் / நான் முதல்வன் போர்ட்டல்', 'online',
        'https://naanmudhalvan.tn.gov.in/', 'பயிற்சி தொகுதி தொடங்கும் போது'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '18', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'less_or_equal', '35', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'occupation', 'in_list', 'unemployed,student', 'person');
    END IF;
END $$;

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
        'TN-LAB-HANDLOOM-WEAVERS-PENSION', 'Tamil Nadu Handloom Weavers Social Security and Pension Scheme', 'தமிழ்நாடு கைத்தறி நெசவாளர் முதியோர் ஓய்வூதியத் திட்டம்', 'Kaithari Nesavaalar Oivoodhiya Thittam',
        'Labour and Employment', 'pension', 'Monthly old age pension of ₹1,000 provided to aged handloom and powerloom weavers who have reached 60 years of age and are unable to earn livelihood.', '60 வயது பூர்த்தியடைந்த, நலிவடைந்த கைத்தறி மற்றும் விசைத்தறி நெசவாளர்களுக்கு மாதம் ₹1,000 முதியோர் ஓய்வூதியம் வழங்கும் திட்டம்.',
        '₹1,000/month', 'https://tnuwwb.tn.gov.in/', '2026-08-01', true,
        '["கைத்தறி கூட்டுறவு சங்க உறுப்பினர் அட்டை", "நெசவாளர் அடையாள அட்டை", "வயதுச் சான்றிதழ் (60 வயது பூர்த்தி)", "ஆதார் அட்டை மற்றும் வங்கி பாஸ்புக்"]'::jsonb, 'கைத்தறி மற்றும் துணிநூல் துறை உதவி இயக்குநர் அலுவலகம் / கூட்டுறவு சங்கம்', 'offline',
        NULL, '30 நாட்கள்'
    )
    ON CONFLICT (scheme_code) DO UPDATE SET
        name_english = EXCLUDED.name_english,
        name_tamil = EXCLUDED.name_tamil,
        benefit_amount = EXCLUDED.benefit_amount,
        last_verified_date = EXCLUDED.last_verified_date,
        required_documents = EXCLUDED.required_documents
    RETURNING id INTO v_scheme_id;

    IF v_scheme_id IS NOT NULL THEN
        DELETE FROM eligibility_rules WHERE scheme_id = v_scheme_id;
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'age', 'greater_or_equal', '60', 'person');
        INSERT INTO eligibility_rules (scheme_id, field_name, operator, value, applies_to) VALUES (v_scheme_id, 'special_flags', 'in_list', 'handloom_weaver', 'person');
    END IF;
END $$;