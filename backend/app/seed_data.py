import datetime
from sqlalchemy.orm import Session
from app.models.enums import RuleOperator, RuleAppliesTo, ApplicationMode
from app.models.scheme import Scheme, EligibilityRule, SchemeTermGlossary

SCHEMES_DATA = [
    {
        "scheme_code": "TN-SW-OAP",
        "name_english": "Indira Gandhi National Old Age Pension Scheme / State Old Age Pension",
        "name_tamil": "இந்திரா காந்தி தேசிய முதியோர் ஓய்வூதியத் திட்டம் / மாநில முதியோர் ஓய்வூதியம்",
        "name_transliteration": "Indira Gandhi Desiya Mudhiyor Oivoodhiya Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "pension",
        "description_english": "Monthly financial assistance provided to destitute senior citizens aged 60 and above belonging to below poverty line households with no other source of livelihood.",
        "description_tamil": "வாழ்வாதாரமற்ற, வறுமைக் கோட்டிற்கு கீழ் உள்ள 60 வயது மற்றும் அதற்கு மேற்பட்ட முதியோர்களுக்கு வழங்கப்படும் மாதாந்திர ஓய்வூதிய உதவி.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://www.tnesevai.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "வயதுச் சான்றிதழ் (Age Proof)",
            "வங்கி கணக்கு புத்தகம் (Bank Passbook)",
            "வருமானச் சான்றிதழ் (Income Certificate)",
        ],
        "application_office": "வட்டாட்சியர் அலுவலகம் (சமூகப் பாதுகாப்புத் திட்டம்) / அருகிலுள்ள இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 நாட்கள்",
        "rules": [
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "60",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "special_flags",
                "operator": RuleOperator.IN_LIST,
                "value": "destitute",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "total_household_income",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "10000",
                "applies_to": RuleAppliesTo.FAMILY,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DWP",
        "name_english": "Destitute Widow Pension Scheme (DWPS)",
        "name_tamil": "ஆதரவற்ற விதவை ஓய்வூதியத் திட்டம்",
        "name_transliteration": "Aadharavatra Vidhavai Oivoodhiya Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "pension",
        "description_english": "Monthly social security pension for destitute widows aged 18 and above who have no regular income or support.",
        "description_tamil": "வருமானம் மற்றும் ஆதரவற்ற 18 வயதுக்கு மேற்பட்ட விதவைப் பெண்களுக்கு வழங்கப்படும் மாதாந்திர சமூகப் பாதுகாப்பு ஓய்வூதியம்.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "கணவரின் இறப்புச் சான்றிதழ் (Husband's Death Certificate)",
            "ஆதரவற்ற விதவை சான்றிதழ் (Destitute Widow Certificate)",
            "வங்கி கணக்கு புத்தகம் (Bank Passbook)",
        ],
        "application_office": "வட்டாட்சியர் அலுவலகம் (Taluk Office) / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "widowed",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "special_flags",
                "operator": RuleOperator.IN_LIST,
                "value": "destitute",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DDWP",
        "name_english": "Destitute Deserted Wives Pension Scheme (DDWPS)",
        "name_tamil": "ஆதரவற்ற கணவனால் கைவிடப்பட்ட பெண்கள் ஓய்வூதியத் திட்டம்",
        "name_transliteration": "Aadharavatra Kanavanal Kaividapatta Pengal Oivoodhiya Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "pension",
        "description_english": "Financial pension for women aged 30 and above who are deserted/separated from their husbands and destitute.",
        "description_tamil": "கணவனால் கைவிடப்பட்டு, ஆதரவற்ற நிலையில் உள்ள 30 வயதுக்கு மேற்பட்ட பெண்களுக்கு வழங்கப்படும் மாதாந்திர ஓய்வூதியம்.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "விவாகரத்து ஆணை அல்லது பிரிந்து வாழும் சான்றிதழ் (Separation Proof from VAO)",
            "வட்டாட்சியர் வருமானச் சான்று",
            "வங்கி கணக்கு புத்தகம்",
        ],
        "application_office": "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "divorced",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "30",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "special_flags",
                "operator": RuleOperator.IN_LIST,
                "value": "destitute",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-UPIWP",
        "name_english": "Unmarried Poor Incapacitated Women Pension Scheme",
        "name_tamil": "50 வயதுக்கு மேற்பட்ட ஆதரவற்ற திருமணமாகாத ஏழைப் பெண்கள் ஓய்வூதியத் திட்டம்",
        "name_transliteration": "Thirumanamagaadha Ezhai Pengal Oivoodhiya Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "pension",
        "description_english": "Monthly pension for unmarried, destitute women aged 50 and above who have no family livelihood support.",
        "description_tamil": "குடும்ப ஆதரவு இல்லாத 50 வயதுக்கு மேற்பட்ட ஆதரவற்ற திருமணமாகாத ஏழைப் பெண்களுக்கு வழங்கப்படும் ஓய்வூதியம்.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "வயதுச் சான்றிதழ் (50 வயதுக்கு மேல்)",
            "திருமணமாகாதவர் சான்று (Unmarried Certificate)",
            "வருமானச் சான்றிதழ்",
        ],
        "application_office": "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "single",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "50",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "special_flags",
                "operator": RuleOperator.IN_LIST,
                "value": "destitute",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DAP",
        "name_english": "Maintenance Allowance / Pension for Differently Abled Persons",
        "name_tamil": "மாற்றுத்திறனாளிகளுக்கான பராமரிப்பு உதவித்தொகை / ஓய்வூதியத் திட்டம்",
        "name_transliteration": "Maatruthranali Paramarippu Udhavithogai Thittam",
        "department": "Differently Abled Welfare",
        "category": "disability_support",
        "description_english": "Monthly financial maintenance allowance for destitute differently abled persons with benchmark disability.",
        "description_tamil": "மாற்றுத்திறனாளிகளுக்கு அவர்களின் வாழ்வாதாரத்திற்காகவும் பராமரிப்பிற்காகவும் வழங்கப்படும் மாதாந்திர உதவித்தொகை.",
        "benefit_amount": "₹1,500/month",
        "source_url": "https://www.scd.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)",
            "மருத்துவச் சான்றிதழ் (Medical Certificate - 40%+ disability)",
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "வங்கி கணக்கு புத்தகம் (Bank Passbook)",
        ],
        "application_office": "மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO) / மாவட்ட ஆட்சியரகம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.scd.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 45 நாட்கள்",
        "rules": [
            {
                "field_name": "disability_status",
                "operator": RuleOperator.EQUALS,
                "value": "true",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-KMUT",
        "name_english": "Kalaignar Magalir Urimai Thittam (KMUT)",
        "name_tamil": "கலைஞர் மகளிர் உரிமைத் திட்டம்",
        "name_transliteration": "Kalaignar Magalir Urimai Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "social_security",
        "description_english": "Monthly financial entitlement for eligible women heads of households with annual family income below ₹2.5 lakh, electricity consumption below 3600 units, and land holding limits.",
        "description_tamil": "ஆண்டு குடும்ப வருமானம் ₹2.5 லட்சத்திற்குள் உள்ள தகுதியான குடும்பத் தலைவிகளுக்கு மாதம் ₹1,000 வழங்கும் முதன்மை உரிமைத் திட்டம்.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://kmut.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "குடும்ப அட்டை (Smart Ration Card)",
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப தலைவியின் வங்கி பாஸ்புக்",
            "மின்சார இணைப்பு நுகர்வோர் எண் (Electricity Consumer Number)",
        ],
        "application_office": "வட்ட வழங்கல் அலுவலகம் / சிறப்பு முகாம்கள் / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://kmut.tn.gov.in/",
        "processing_time_estimate": "30 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "21",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "total_household_income",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "20833",
                "applies_to": RuleAppliesTo.FAMILY,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-PUDHUMAI-PENN",
        "name_english": "Moovalur Ramamirtham Ammaiyar Higher Education Assurance Scheme (Pudhumai Penn)",
        "name_tamil": "மூவலூர் ராமாமிர்தம் அம்மையார் உயர்கல்வி உறுதித் திட்டம் (புதுமைப் பெண் திட்டம்)",
        "name_transliteration": "Moovalur Ramamirtham Ammaiyar Pudhumai Penn Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "education_assistance",
        "description_english": "Monthly financial aid to female students pursuing higher education (degrees/diplomas) who studied from classes 6 to 12 in Tamil Nadu government schools.",
        "description_tamil": "அரசுப் பள்ளிகளில் 6 முதல் 12 ஆம் வகுப்பு வரை படித்து உயர்கல்வி பயிலும் மாணவிகளுக்கு மாதம் ₹1,000 வழங்கும் திட்டம்.",
        "benefit_amount": "₹1,000/month",
        "source_url": "https://pudhumaipenn.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "6 முதல் 12 ஆம் வகுப்பு அரசுப் பள்ளி பயின்ற சான்றிதழ் (EMIS School Certificate)",
            "கல்லூரி சேர்க்கை அடையாள அட்டை (College ID / Bonafide)",
            "மாணவியின் ஆதார் அட்டை",
            "வங்கி கணக்கு புத்தகம்",
            "10, 12 ஆம் வகுப்பு மதிப்பெண் சான்றிதழ்",
        ],
        "application_office": "கல்லூரி முதல்வர் அலுவலகம் / கல்லூரி நோடல் அலுவலர்",
        "application_mode": ApplicationMode.ONLINE,
        "online_application_url": "https://pudhumaipenn.tn.gov.in/",
        "processing_time_estimate": "15 முதல் 30 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "education_level",
                "operator": RuleOperator.IN_LIST,
                "value": "higher_secondary,graduate,postgraduate",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "occupation",
                "operator": RuleOperator.EQUALS,
                "value": "student",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-SEWING-MACHINE",
        "name_english": "Sathiyavani Muthu Ammaiyar Ninaivu Free Supply of Sewing Machine Scheme",
        "name_tamil": "சத்தியவாணி முத்து அம்மையார் நினைவு இலவச தையல் இயந்திரம் வழங்கும் திட்டம்",
        "name_transliteration": "Sathiyavani Muthu Ammaiyar Ninaivu Ilavasa Thaiyal Iyandhira Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "livelihood_support",
        "description_english": "Free supply of sewing machine with accessories to destitute women, widows, deserted wives, and differently abled persons aged 20-40 with annual family income up to ₹72,000 who possess tailoring skills.",
        "description_tamil": "தையல் கலை தெரிந்த 20 முதல் 40 வயதுடைய ஆதரவற்ற பெண்கள், விதவைகள், கணவனால் கைவிடப்பட்டோர் மற்றும் மாற்றுத்திறனாளிகளுக்கு இலவச தையல் இயந்திரம் வழங்கும் திட்டம்.",
        "benefit_amount": "1 Free Sewing Machine with accessories",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "தையல் கலை பயின்றதற்கான சான்றிதழ் (Tailoring Course Certificate)",
            "வருமானச் சான்றிதழ் (ஆண்டு வருமானம் ₹72,000-க்குள்)",
            "ஆதார் அட்டை மற்றும் குடும்ப அட்டை",
            "வயதுச் சான்று (20-40 வயது)",
            "விதவை/ஆதரவற்றோர்/மாற்றுத்திறனாளி சான்றிதழ் (பொருந்துமாயின்)",
        ],
        "application_office": "வட்டார வளர்ச்சி அலுவலகம் (BDO Office) / மாவட்ட சமூக நல அலுவலகம் (DSWO)",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "processing_time_estimate": "45 நாட்கள்",
        "rules": [
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "20",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "40",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "total_household_income",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "6000",
                "applies_to": RuleAppliesTo.FAMILY,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-WIDOW-REMARRIAGE",
        "name_english": "Dr. Dharmambal Ammaiyar Ninaivu Widow Remarriage Assistance Scheme",
        "name_tamil": "டாக்டர் தர்மாம்பாள் அம்மையார் நினைவு விதவை மறுமண நிதியுதவித் திட்டம்",
        "name_transliteration": "Dr Dharmambal Ammaiyar Ninaivu Vidhavai Marumana Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "marriage_assistance",
        "description_english": "Financial grant and gold coin for Thirumangalyam provided to encourage widow remarriage. Bride must be aged 20 or above.",
        "description_tamil": "விதவைப் பெண்கள் மறுமணம் செய்து கொள்வதை ஊக்குவிக்க திருமாங்கல்யத்திற்கான தங்க நாணயம் மற்றும் நிதியுதவி வழங்கும் திட்டம்.",
        "benefit_amount": "₹25,000 to ₹50,000 + 8g Gold Coin",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "முதல் கணவரின் இறப்புச் சான்றிதழ் (First Husband Death Certificate)",
            "மறுமண அழைப்பிதழ் / திருமண பதிவுச் சான்றிதழ்",
            "மணமகள், மணமகன் வயதுச் சான்று மற்றும் ஆதார் அட்டை",
            "பட்டதாரி சான்றிதழ் (திட்டம்-II எனில்)",
        ],
        "application_office": "மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 60 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "widowed",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "20",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-POOR-WIDOW-DAUGHTER",
        "name_english": "E.V.R. Maniammaiyar Ninaivu Marriage Assistance Scheme for Daughters of Poor Widows",
        "name_tamil": "ஈ.வெ.ரா. மணியம்மையார் நினைவு ஏழை விதவைகளின் மகள்கள் திருமண நிதியுதவித் திட்டம்",
        "name_transliteration": "EVR Maniammaiyar Ninaivu Ezhai Vidhavaigalin Magalgal Thirumana Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "marriage_assistance",
        "description_english": "Marriage financial assistance and 8g gold coin to poor widows to perform the marriage of their daughters (bride aged 18+, annual income limit ₹72,000).",
        "description_tamil": "ஏழை விதவைகளின் மகள்களின் திருமணத்தை நடத்துவதற்கு வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.",
        "benefit_amount": "₹25,000 to ₹50,000 + 8g Gold Coin",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "தாய் விதவை என்பதற்கான இறப்புச் சான்றிதழ்",
            "குடும்ப வருமானச் சான்றிதழ் (₹72,000-க்குள்)",
            "திருமண அழைப்பிதழ்",
            "மணமகள் 10-ஆம் வகுப்பு / பட்டதாரி சான்றிதழ்",
            "ஆதார் மற்றும் ரேஷன் கார்டு",
        ],
        "application_office": "மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 60 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "single",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "total_household_income",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "6000",
                "applies_to": RuleAppliesTo.FAMILY,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-ORPHAN-GIRL-MARRIAGE",
        "name_english": "Annai Teresa Ninaivu Marriage Assistance Scheme for Orphan Girls",
        "name_tamil": "அன்னை தெரசா நினைவு ஆதரவற்ற பெண் குழந்தைகள் திருமண நிதியுதவித் திட்டம்",
        "name_transliteration": "Annai Teresa Ninaivu Aadharavatra Pengal Thirumana Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "marriage_assistance",
        "description_english": "Marriage financial assistance and 8g gold coin for orphan girls (who have lost both parents) aged 18 and above. No income ceiling applies.",
        "description_tamil": "தாய், தந்தை இருவரையும் இழந்த ஆதரவற்ற பெண்களின் திருமணத்திற்காக வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.",
        "benefit_amount": "₹25,000 to ₹50,000 + 8g Gold Coin",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "தாய் மற்றும் தந்தை இருவரின் இறப்புச் சான்றிதழ்கள் (Death Certificates of parents)",
            "அனாதை / ஆதரவற்ற பெண் சான்றிதழ் (Orphan Certificate from MP/MLA/Tahsildar)",
            "திருமண அழைப்பிதழ்",
            "மணமகள் வயதுச் சான்று மற்றும் ஆதார் அட்டை",
        ],
        "application_office": "மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 60 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "single",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "special_flags",
                "operator": RuleOperator.IN_LIST,
                "value": "orphan",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-INTERCASTE-MARRIAGE",
        "name_english": "Dr. Muthulakshmi Reddy Ninaivu Inter-Caste Marriage Assistance Scheme",
        "name_tamil": "டாக்டர் முத்துலட்சுமி ரெட்டி நினைவு கலப்புத் திருமண நிதியுதவித் திட்டம்",
        "name_transliteration": "Dr Muthulakshmi Reddy Ninaivu Kalappu Thirumana Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "marriage_assistance",
        "description_english": "Financial grant and gold coin to encourage inter-caste marriages (Category I: SC/ST with other communities; Category II: Forward communities with BC/MBC). No income ceiling.",
        "description_tamil": "சாதி பாகுபாடுகளைக் களைய கலப்புத் திருமணம் செய்து கொள்ளும் தம்பதியருக்கு வழங்கப்படும் நிதியுதவி மற்றும் 8 கிராம் தங்க நாணயம்.",
        "benefit_amount": "₹25,000 to ₹50,000 + 8g Gold Coin",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "திருமண பதிவுச் சான்றிதழ் (Marriage Registration Certificate)",
            "மணமகன் மற்றும் மணமகள் இருவரின் சாதிச் சான்றிதழ்கள் (Community Certificates)",
            "வயதுச் சான்றிதழ் மற்றும் ஆதார் அட்டைகள்",
            "கல்வி சான்றிதழ் (திட்டம்-II எனில்)",
        ],
        "application_office": "மாவட்ட சமூக நல அலுவலகம் (DSWO) / இ-சேவை மையம்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.tnesevai.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 60 நாட்கள்",
        "rules": [
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "single",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-GIRL-CHILD-1",
        "name_english": "Chief Minister's Girl Child Protection Scheme (Scheme I)",
        "name_tamil": "முதலமைச்சரின் பெண் குழந்தை பாதுகாப்புத் திட்டம் (திட்டம்-I)",
        "name_transliteration": "Mudalamaicharin Penn Kuzhandhai Paadhukaappu Thittam",
        "department": "Social Welfare & Women Empowerment",
        "category": "child_welfare",
        "description_english": "Fixed deposit of ₹50,000 with annual educational incentive of ₹1,800 from 6th year for families with only one girl child and no male children, parental sterilization before age 40, and annual income within ₹72,000.",
        "description_tamil": "ஒரே ஒரு பெண் குழந்தை மட்டும் உள்ள ஏழைக் குடும்பங்களுக்கு ₹50,000 நிலையான வைப்பு நிதி மற்றும் ஆண்டு கல்வி உதவித்தொகை வழங்கும் திட்டம்.",
        "benefit_amount": "₹50,000 Fixed Deposit + ₹1,800/year incentive",
        "source_url": "https://www.tnsocialwelfare.tn.gov.in/",
        # Older verified date (e.g. 2025-08-01, >6 months ago) to demonstrate the staleness disclaimer functionality
        "last_verified_date": datetime.date(2025, 8, 1),
        "is_active": True,
        "required_documents": [
            "பெண் குழந்தையின் பிறப்புச் சான்றிதழ் (Birth Certificate)",
            "பெற்றோர் குடும்பக் கட்டுப்பாடு சான்றிதழ் (Sterilization Certificate before age 40)",
            "குடும்ப வருமானச் சான்று (₹72,000-க்குள்)",
            "ஆண் குழந்தை இல்லை என்பதற்கான சான்று (No male child certificate from VAO)",
        ],
        "application_office": "வட்டார வளர்ச்சி அலுவலகம் (BDO) / மாவட்ட சமூக நல அலுவலகம் (DSWO)",
        "application_mode": ApplicationMode.OFFLINE,
        "online_application_url": None,
        "processing_time_estimate": "45 முதல் 60 நாட்கள்",
        "rules": [
            {
                "field_name": "gender",
                "operator": RuleOperator.EQUALS,
                "value": "female",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "3",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "total_household_income",
                "operator": RuleOperator.LESS_OR_EQUAL,
                "value": "6000",
                "applies_to": RuleAppliesTo.FAMILY,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DA-MOTOR-VEHICLE",
        "name_english": "Retrofitted Motorized Vehicles for Differently Abled Persons",
        "name_tamil": "மாற்றுத்திறனாளிகளுக்கு இணைப்புச் சக்கரங்கள் பொருத்தப்பட்ட மோட்டார் வாகனம் வழங்கும் திட்டம்",
        "name_transliteration": "Inaippu Sakkarangal Poruthapatta Motor Vaaganam Thittam",
        "department": "Differently Abled Welfare",
        "category": "disability_support",
        "description_english": "Free retrofitted petrol scooter with side wheels provided to locomotor-disabled persons (both legs affected) aged 18 and above who are studying or working.",
        "description_tamil": "இரு கால்களும் பாதிக்கப்பட்ட 18 வயதுக்கு மேற்பட்ட மாற்றுத்திறனாளி மாணவர்கள் மற்றும் உழைக்கும் நபர்களுக்கு இலவச மோட்டார் வாகனம்.",
        "benefit_amount": "1 Free Retrofitted Motor Scooter",
        "source_url": "https://www.scd.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "மாற்றுத்திறனாளி தேசிய அடையாள அட்டை (UDID Card)",
            "இரு கால்களும் பாதிக்கப்பட்ட மருத்துவச் சான்றிதழ்",
            "ஓட்டுநர் உரிமம் (Driving License / LLR for invalid carriage)",
            "வேலை அல்லது கல்லூரி பயில்வதற்கான சான்று",
            "ஆதார் மற்றும் குடும்ப அட்டை",
        ],
        "application_office": "மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO)",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.scd.tn.gov.in/",
        "processing_time_estimate": "60 முதல் 90 நாட்கள்",
        "rules": [
            {
                "field_name": "disability_status",
                "operator": RuleOperator.EQUALS,
                "value": "true",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DA-AIDS-APPLIANCES",
        "name_english": "Free Supply of Assistive Devices (Tricycles, Wheelchairs, Hearing Aids)",
        "name_tamil": "மாற்றுத்திறனாளிகளுக்கு உதவி உபகரணங்கள் (முச்சக்கர வண்டி, சக்கர நாற்காலி, காதொலிக் கருவி) வழங்கும் திட்டம்",
        "name_transliteration": "Maatruthranali Udhavi Ubakaranangal Ilavasa Vazhangum Thittam",
        "department": "Differently Abled Welfare",
        "category": "disability_support",
        "description_english": "Free assistive aids including tricycles, manual and battery wheelchairs, crutches, calipers, hearing aids, and Braille watches for verified differently abled beneficiaries.",
        "description_tamil": "தகுதியுடைய மாற்றுத்திறனாளிகளுக்கு முச்சக்கர வண்டிகள், சக்கர நாற்காலிகள், காதொலிக் கருவிகள் மற்றும் பிரெய்லி கடிகாரங்கள் இலவசமாக வழங்குதல்.",
        "benefit_amount": "Free assistive devices as per medical prescription",
        "source_url": "https://www.scd.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "மாற்றுத்திறனாளி அடையாள அட்டை (UDID)",
            "மருத்துவ அதிகாரியின் உபகரண பரிந்துரை சீட்டு",
            "ஆதார் அட்டை மற்றும் குடும்ப அட்டை",
            "புகைப்படம் (முழு உருவப்படம்)",
        ],
        "application_office": "மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO) / சிறப்பு முகாம்கள்",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.scd.tn.gov.in/",
        "processing_time_estimate": "30 முதல் 45 நாட்கள்",
        "rules": [
            {
                "field_name": "disability_status",
                "operator": RuleOperator.EQUALS,
                "value": "true",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
    {
        "scheme_code": "TN-SW-DA-MARRIAGE",
        "name_english": "Marriage Assistance Scheme for Normal Persons Marrying Differently Abled Persons",
        "name_tamil": "மாற்றுத்திறனாளிகளை திருமணம் செய்து கொள்வோருக்கான திருமண நிதியுதவித் திட்டம்",
        "name_transliteration": "Maatruthranali Thirumana Udhavithogai Thittam",
        "department": "Differently Abled Welfare",
        "category": "marriage_assistance",
        "description_english": "Financial assistance of ₹25,000/₹50,000 along with an 8g gold coin to encourage normal individuals to marry visually, hearing, or locomotor impaired persons.",
        "description_tamil": "மாற்றுத்திறனாளிகளை மணம் முடிக்கும் இயல்பான நபர்களை ஊக்குவிக்க வழங்கப்படும் திருமண உதவித்தொகை மற்றும் 8 கிராம் தங்க நாணயம்.",
        "benefit_amount": "₹25,000 to ₹50,000 + 8g Gold Coin",
        "source_url": "https://www.scd.tn.gov.in/",
        "last_verified_date": datetime.date(2026, 8, 1),
        "is_active": True,
        "required_documents": [
            "மாற்றுத்திறனாளி துணைவரின் அடையாள அட்டை (UDID) மற்றும் மருத்துவச் சான்றிதழ்",
            "திருமண அழைப்பிதழ் / திருமண பதிவுச் சான்றிதழ்",
            "இருவரின் வயதுச் சான்று மற்றும் ஆதார் அட்டை",
            "முன்மணம் செய்யாததற்கான சான்றிதழ்",
        ],
        "application_office": "மாவட்ட மாற்றுத்திறனாளிகள் நல அலுவலகம் (DDAWO)",
        "application_mode": ApplicationMode.BOTH,
        "online_application_url": "https://www.scd.tn.gov.in/",
        "processing_time_estimate": "45 நாட்கள்",
        "rules": [
            {
                "field_name": "age",
                "operator": RuleOperator.GREATER_OR_EQUAL,
                "value": "18",
                "applies_to": RuleAppliesTo.PERSON,
            },
            {
                "field_name": "marital_status",
                "operator": RuleOperator.EQUALS,
                "value": "single",
                "applies_to": RuleAppliesTo.PERSON,
            },
        ],
    },
]

GLOSSARY_DATA = [
    # Ration Card Terminology
    {
        "tamil_term": "அந்தியோதயா அன்ன யோஜனா அட்டை (PHH-AAY)",
        "english_equivalent": "Antyodaya Anna Yojana Card (Poorest of the poor)",
        "notes": "Issued to the most destitute families, entitled to 35 kg of free rice per month under TNPDS.",
    },
    {
        "tamil_term": "முன்னுரிமை குடும்ப அட்டை (PHH)",
        "english_equivalent": "Priority Household Card (Rice Card)",
        "notes": "Green smart card issued to low-income families entitled to rice and subsidized essential commodities.",
    },
    {
        "tamil_term": "முன்னுரிமையற்ற சர்க்கரை அட்டை (NPHH-S)",
        "english_equivalent": "Non-Priority Household - Sugar Card",
        "notes": "White smart card holders who opted for additional sugar in lieu of rice.",
    },
    {
        "tamil_term": "பொருளற்ற அட்டை (NPHH-NC)",
        "english_equivalent": "No Commodity Card",
        "notes": "White smart card serving purely as an official proof of residence and identity; no commodities issued.",
    },
    {
        "tamil_term": "காவல்துறை குடும்ப அட்டை (Khaki Card)",
        "english_equivalent": "Police Personnel Ration Card",
        "notes": "Special card issued to serving police personnel for essential commodities at subsidized rates.",
    },
    # Caste / Social Categories
    {
        "tamil_term": "ஆதிதிராவிடர் / பட்டியல் சாதியினர் (SC)",
        "english_equivalent": "Scheduled Caste (SC)",
        "notes": "Official category in Tamil Nadu encompassing Adi Dravidar and Arundhathiyar communities.",
    },
    {
        "tamil_term": "பழங்குடியினர் (ST)",
        "english_equivalent": "Scheduled Tribe (ST)",
        "notes": "Indigenous tribal communities recognized under the Constitution of India.",
    },
    {
        "tamil_term": "பிற்படுத்தப்பட்டோர் (BC)",
        "english_equivalent": "Backward Classes (BC)",
        "notes": "State backward classes eligible for specific welfare quotas and scholarships.",
    },
    {
        "tamil_term": "மிகவும் பிற்படுத்தப்பட்டோர் (MBC)",
        "english_equivalent": "Most Backward Classes (MBC)",
        "notes": "Socio-economically disadvantaged communities distinct from BC.",
    },
    {
        "tamil_term": "சீர்மரபினர் (DNC)",
        "english_equivalent": "De-Notified Communities (DNC)",
        "notes": "Historical denotified tribes eligible for specialized welfare board schemes in Tamil Nadu.",
    },
    {
        "tamil_term": "பொதுப்பிரிவு (General / OC)",
        "english_equivalent": "General Category / Open Category",
        "notes": "Applicants not belonging to SC/ST/BC/MBC/DNC reservations.",
    },
    # Departments
    {
        "tamil_term": "சமூக நலம் மற்றும் மகளிர் உரிமைத்துறை",
        "english_equivalent": "Social Welfare & Women Empowerment Department",
        "notes": "Main state department managing women, children, elderly pensions, marriage, and empowerment schemes.",
    },
    {
        "tamil_term": "மாற்றுத்திறனாளிகள் நலத்துறை",
        "english_equivalent": "Differently Abled Welfare Department",
        "notes": "Oversees maintenance allowance, assistive devices, and rehabilitation for persons with disabilities.",
    },
    {
        "tamil_term": "வருவாய்த்துறை (சமூகப் பாதுகாப்புத் திட்டங்கள்)",
        "english_equivalent": "Revenue and Disaster Management Department (Social Security Schemes)",
        "notes": "Disburses monthly pensions such as OAP, Destitute Widow, and Deserted Wives pensions.",
    },
    # Scheme Beneficiary & Concept Terms
    {
        "tamil_term": "ஆதரவற்ற விதவை",
        "english_equivalent": "Destitute Widow",
        "notes": "A widowed woman lacking independent financial support or property exceeding limits, certified by revenue authorities.",
    },
    {
        "tamil_term": "முதியோர் ஓய்வூதியம் (OAP)",
        "english_equivalent": "Old Age Pension",
        "notes": "Monthly social security allowance for destitute senior citizens aged 60 and above.",
    },
    {
        "tamil_term": "கணவனால் கைவிடப்பட்ட பெண்",
        "english_equivalent": "Deserted Wife",
        "notes": "A woman legally divorced or separated from husband for over 5 years without alimony or maintenance.",
    },
    {
        "tamil_term": "திருமாங்கல்யத்திற்கு தங்கம்",
        "english_equivalent": "Gold for Thirumangalyam",
        "notes": "1 sovereign (8 grams) of 22k gold given along with cash assistance in marriage schemes.",
    },
    {
        "tamil_term": "உரிமைத்தொகை",
        "english_equivalent": "Entitlement / Rightful Grant",
        "notes": "Direct bank transfer grant, e.g., Kalaignar Magalir Urimai Thogai (KMUT) ₹1,000/month for women heads.",
    },
    {
        "tamil_term": "பராமரிப்பு உதவித்தொகை",
        "english_equivalent": "Maintenance Allowance",
        "notes": "Monthly grant for severely disabled, mentally challenged, or muscular dystrophy patients.",
    },
    {
        "tamil_term": "மாற்றுத்திறனாளி அடையாள அட்டை (UDID)",
        "english_equivalent": "Unique Disability ID (UDID)",
        "notes": "Standard national identity card indicating disability percentage required for all welfare benefits.",
    },
    {
        "tamil_term": "இணைப்புச் சக்கரம் பொருத்தப்பட்ட வாகனம்",
        "english_equivalent": "Retrofitted Motorized Vehicle",
        "notes": "Motor scooter adapted with two rear support wheels for orthopaedically challenged individuals.",
    },
    {
        "tamil_term": "இலவச தையல் இயந்திரம்",
        "english_equivalent": "Free Sewing Machine",
        "notes": "Livelihood support provided under Sathiyavani Muthu Ammaiyar scheme for trained women and persons with disabilities.",
    },
]

from app.seed_data_departments.education import EDUCATION_SCHEMES
from app.seed_data_departments.agriculture import AGRICULTURE_SCHEMES
from app.seed_data_departments.labour import LABOUR_SCHEMES
from app.seed_data_departments.glossary import ADDITIONAL_GLOSSARY_DATA

SCHEMES_DATA.extend(EDUCATION_SCHEMES)
SCHEMES_DATA.extend(AGRICULTURE_SCHEMES)
SCHEMES_DATA.extend(LABOUR_SCHEMES)

GLOSSARY_DATA.extend(ADDITIONAL_GLOSSARY_DATA)


def seed_database(db: Session):
    """Seed schemes, eligibility rules, and glossary terms if not already populated.
    Updates existing schemes with guidance fields if they were seeded in earlier phases.
    """
    for scheme_dict in SCHEMES_DATA:
        existing = db.query(Scheme).filter(Scheme.scheme_code == scheme_dict["scheme_code"]).first()
        rules_data = scheme_dict.get("rules", [])
        scheme_fields = {k: v for k, v in scheme_dict.items() if k != "rules"}

        if not existing:
            scheme = Scheme(**scheme_fields)
            db.add(scheme)
            db.flush()

            for rule_dict in rules_data:
                rule = EligibilityRule(
                    scheme_id=scheme.id,
                    field_name=rule_dict["field_name"],
                    operator=rule_dict["operator"],
                    value=rule_dict["value"],
                    applies_to=rule_dict["applies_to"],
                )
                db.add(rule)
        else:
            # Update guidance fields on existing record
            existing.required_documents = scheme_fields.get("required_documents", [])
            existing.application_office = scheme_fields.get("application_office", "வட்டாட்சியர் அலுவலகம்")
            existing.application_mode = scheme_fields.get("application_mode", ApplicationMode.BOTH)
            existing.online_application_url = scheme_fields.get("online_application_url")
            existing.processing_time_estimate = scheme_fields.get("processing_time_estimate", "30 நாட்கள்")
            existing.last_verified_date = scheme_fields.get("last_verified_date", existing.last_verified_date)

    # Seed Glossary
    for term_dict in GLOSSARY_DATA:
        existing_term = db.query(SchemeTermGlossary).filter(
            SchemeTermGlossary.tamil_term == term_dict["tamil_term"]
        ).first()
        if not existing_term:
            glossary_item = SchemeTermGlossary(**term_dict)
            db.add(glossary_item)

    db.commit()


if __name__ == "__main__":
    from app.database import SessionLocal, engine, Base
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        seed_database(session)
        print("Successfully seeded schemes with guidance fields and glossary.")
    finally:
        session.close()
