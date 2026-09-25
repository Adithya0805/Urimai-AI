from enum import Enum


class CompositionType(str, Enum):
    SINGLE = "single"
    COUPLE = "couple"
    NUCLEAR = "nuclear"
    JOINT = "joint"


class RationCardType(str, Enum):
    NONE = "none"
    GREEN = "green"       # TN Rice card (PHH / NPHH-Rice)
    WHITE = "white"       # TN Sugar card / No Commodity (NPHH-Sugar / NPHH-NC)
    KHAKI = "khaki"       # Police personnel
    PHH_AAY = "phh_aay"   # Antyodaya Anna Yojana
    ORANGE = "orange"     # Standard other states
    YELLOW = "yellow"     # Standard other states
    OTHER = "other"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    TRANSGENDER = "transgender"
    OTHER = "other"


class EducationLevel(str, Enum):
    NONE = "none"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HIGHER_SECONDARY = "higher_secondary"
    GRADUATE = "graduate"
    POSTGRADUATE = "postgraduate"
    DROPOUT = "dropout"


class Occupation(str, Enum):
    FARMER = "farmer"
    DAILY_WAGE = "daily_wage"
    SELF_EMPLOYED = "self_employed"
    GOVT_EMPLOYEE = "govt_employee"
    PRIVATE_EMPLOYEE = "private_employee"
    UNEMPLOYED = "unemployed"
    STUDENT = "student"
    HOMEMAKER = "homemaker"
    RETIRED = "retired"
    OTHER = "other"


class MaritalStatus(str, Enum):
    SINGLE = "single"
    MARRIED = "married"
    WIDOWED = "widowed"
    DIVORCED = "divorced"


class CasteCategory(str, Enum):
    SC = "SC"
    ST = "ST"
    BC = "BC"
    MBC = "MBC"
    DNC = "DNC"
    GENERAL = "General"


class RuleOperator(str, Enum):
    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    GREATER_OR_EQUAL = "greater_or_equal"
    LESS_OR_EQUAL = "less_or_equal"
    IN_LIST = "in_list"


class RuleAppliesTo(str, Enum):
    PERSON = "person"
    FAMILY = "family"


class ApplicationMode(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    BOTH = "both"


class ApplicationTrackingStatus(str, Enum):
    NOT_STARTED = "not_started"
    DOCUMENTS_PENDING = "documents_pending"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    RENEWAL_DUE = "renewal_due"



