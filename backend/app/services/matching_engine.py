from decimal import Decimal
from typing import List, Tuple, Optional, Any
from app.models.enums import RuleOperator, RuleAppliesTo
from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme, EligibilityRule
from app.schemas.eligibility import (
    FailedRuleDetail,
    EligibleSchemeItem,
    PartiallyEligibleSchemeItem,
    PersonEligibilityResponse,
    FamilyEligibilityResponse,
)


def evaluate_rule(
    rule: EligibilityRule,
    person: Person,
    family: Family,
) -> Tuple[bool, Optional[FailedRuleDetail]]:
    """Evaluates a single EligibilityRule against a Person or Family.
    Returns (True, None) if passed, or (False, FailedRuleDetail) if failed.
    """
    target = person if rule.applies_to == RuleAppliesTo.PERSON else family
    field_name = rule.field_name
    actual_raw = getattr(target, field_name, None)

    # Normalize enum value if applicable
    if hasattr(actual_raw, "value"):
        actual_val = actual_raw.value
    else:
        actual_val = actual_raw

    actual_str = str(actual_val) if actual_val is not None else "None"
    expected_str = rule.value.strip()

    # 1. Boolean field handling (e.g. disability_status)
    if isinstance(actual_val, bool):
        expected_bool = expected_str.lower() in ("true", "1", "yes")
        if rule.operator == RuleOperator.EQUALS:
            passed = (actual_val == expected_bool)
        elif rule.operator == RuleOperator.NOT_EQUALS:
            passed = (actual_val != expected_bool)
        else:
            passed = False

        if passed:
            return True, None
        return False, FailedRuleDetail(
            field_name=field_name,
            operator=rule.operator,
            expected_value=expected_str,
            actual_value=actual_str,
            applies_to=rule.applies_to,
            reason=f"{field_name} is {actual_val}, requires {expected_bool}",
        )

    # 2. List field handling (e.g. special_flags on Person)
    if isinstance(actual_val, list):
        actual_list_lower = [str(x).strip().lower() for x in actual_val]
        expected_tokens = [t.strip().lower() for t in expected_str.split(",")]

        if rule.operator in (RuleOperator.IN_LIST, RuleOperator.EQUALS):
            # Check if any expected token is present in the person's special_flags
            passed = any(tok in actual_list_lower for tok in expected_tokens)
        elif rule.operator == RuleOperator.NOT_EQUALS:
            passed = not any(tok in actual_list_lower for tok in expected_tokens)
        else:
            passed = False

        if passed:
            return True, None
        return False, FailedRuleDetail(
            field_name=field_name,
            operator=rule.operator,
            expected_value=expected_str,
            actual_value=str(actual_val),
            applies_to=rule.applies_to,
            reason=f"{field_name} does not contain required tag '{expected_str}'",
        )

    # 3. Numeric comparisons (e.g. age, total_household_income)
    is_numeric = isinstance(actual_val, (int, float, Decimal))
    if not is_numeric and actual_val is not None:
        try:
            float(str(actual_val))
            float(expected_str)
            is_numeric = True
        except ValueError:
            is_numeric = False

    if is_numeric and actual_val is not None:
        try:
            actual_num = float(actual_val)
            expected_num = float(expected_str)

            if rule.operator == RuleOperator.GREATER_OR_EQUAL:
                passed = actual_num >= expected_num
                op_symbol = ">="
            elif rule.operator == RuleOperator.LESS_OR_EQUAL:
                passed = actual_num <= expected_num
                op_symbol = "<="
            elif rule.operator == RuleOperator.GREATER_THAN:
                passed = actual_num > expected_num
                op_symbol = ">"
            elif rule.operator == RuleOperator.LESS_THAN:
                passed = actual_num < expected_num
                op_symbol = "<"
            elif rule.operator == RuleOperator.EQUALS:
                passed = actual_num == expected_num
                op_symbol = "=="
            elif rule.operator == RuleOperator.NOT_EQUALS:
                passed = actual_num != expected_num
                op_symbol = "!="
            else:
                passed = False
                op_symbol = rule.operator.value

            if passed:
                return True, None

            # Format integer nicely without decimal if whole number
            disp_actual = int(actual_num) if actual_num.is_integer() else actual_num
            disp_expected = int(expected_num) if expected_num.is_integer() else expected_num
            return False, FailedRuleDetail(
                field_name=field_name,
                operator=rule.operator,
                expected_value=expected_str,
                actual_value=str(disp_actual),
                applies_to=rule.applies_to,
                reason=f"{field_name} is {disp_actual}, requires {op_symbol} {disp_expected}",
            )
        except (ValueError, TypeError):
            pass

    # 4. In-list comparison for scalar string / enum (e.g. education_level in [higher_secondary, graduate])
    if rule.operator == RuleOperator.IN_LIST:
        allowed = [x.strip().lower() for x in expected_str.split(",")]
        passed = str(actual_val).strip().lower() in allowed
        if passed:
            return True, None
        return False, FailedRuleDetail(
            field_name=field_name,
            operator=rule.operator,
            expected_value=expected_str,
            actual_value=actual_str,
            applies_to=rule.applies_to,
            reason=f"{field_name} is '{actual_val}', requires one of [{expected_str}]",
        )

    # 5. Generic string / enum equality
    actual_norm = str(actual_val).strip().lower()
    expected_norm = expected_str.lower()

    if rule.operator == RuleOperator.EQUALS:
        passed = (actual_norm == expected_norm)
        reason = f"{field_name} is '{actual_val}', requires '{expected_str}'"
    elif rule.operator == RuleOperator.NOT_EQUALS:
        passed = (actual_norm != expected_norm)
        reason = f"{field_name} is '{actual_val}', must not be '{expected_str}'"
    else:
        passed = False
        reason = f"{field_name} comparison failed for operator {rule.operator.value}"

    if passed:
        return True, None
    return False, FailedRuleDetail(
        field_name=field_name,
        operator=rule.operator,
        expected_value=expected_str,
        actual_value=actual_str,
        applies_to=rule.applies_to,
        reason=reason,
    )


def evaluate_person_eligibility(
    person: Person,
    family: Family,
    schemes: List[Scheme],
) -> PersonEligibilityResponse:
    """Evaluates all active schemes against a given Person and their Family."""
    eligible_schemes: List[EligibleSchemeItem] = []
    partially_eligible_schemes: List[PartiallyEligibleSchemeItem] = []
    ineligible_count = 0

    for scheme in schemes:
        if not scheme.is_active:
            continue

        rules = scheme.rules
        if not rules:
            continue

        matched_count = 0
        failed_rules: List[FailedRuleDetail] = []

        for rule in rules:
            passed, failure_detail = evaluate_rule(rule, person, family)
            if passed:
                matched_count += 1
            else:
                if failure_detail:
                    failed_rules.append(failure_detail)

        total_rules = len(rules)

        if matched_count == total_rules:
            eligible_schemes.append(
                EligibleSchemeItem(
                    scheme_id=scheme.id,
                    scheme_code=scheme.scheme_code,
                    name_english=scheme.name_english,
                    name_tamil=scheme.name_tamil,
                    department=scheme.department,
                    category=scheme.category,
                    benefit_amount=scheme.benefit_amount,
                    source_url=scheme.source_url,
                    matched_rules_count=matched_count,
                    total_rules_count=total_rules,
                )
            )
        elif matched_count > 0:
            partially_eligible_schemes.append(
                PartiallyEligibleSchemeItem(
                    scheme_id=scheme.id,
                    scheme_code=scheme.scheme_code,
                    name_english=scheme.name_english,
                    name_tamil=scheme.name_tamil,
                    department=scheme.department,
                    category=scheme.category,
                    benefit_amount=scheme.benefit_amount,
                    source_url=scheme.source_url,
                    matched_rules_count=matched_count,
                    total_rules_count=total_rules,
                    failed_rules=failed_rules,
                )
            )
        else:
            ineligible_count += 1

    return PersonEligibilityResponse(
        person_id=person.id,
        person_name=person.name,
        family_id=family.id,
        eligible_schemes=eligible_schemes,
        partially_eligible_schemes=partially_eligible_schemes,
        ineligible_schemes_count=ineligible_count,
    )


def evaluate_family_eligibility(
    family: Family,
    schemes: List[Scheme],
) -> FamilyEligibilityResponse:
    """Evaluates all active schemes for each person in the given Family."""
    persons_eligibility: List[PersonEligibilityResponse] = []

    for person in family.persons:
        res = evaluate_person_eligibility(person, family, schemes)
        persons_eligibility.append(res)

    return FamilyEligibilityResponse(
        family_id=family.id,
        district=family.district,
        taluk=family.taluk,
        total_household_income=family.total_household_income,
        total_persons=len(family.persons),
        persons_eligibility=persons_eligibility,
    )
