const rawBase = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";
const API_BASE = rawBase.trim().replace(/\/+$/, "");

export interface Family {
  id: string;
  composition_type: string;
  district: string;
  taluk: string;
  address: string;
  ration_card_type: string;
  total_household_income: number;
  user_id?: string;
  created_by?: string;
  created_at: string;
  updated_at: string;
  persons?: Person[];
}

export interface Person {
  id: string;
  family_id: string;
  name: string;
  age: number;
  gender: string;
  education_level: string;
  occupation: string;
  occupation_detail?: string;
  marital_status: string;
  caste_category: string;
  disability_status: boolean;
  disability_type?: string;
  special_flags: string[];
  land_holding_acres?: number;
  crop_type?: string;
  created_at?: string;
}

export interface EligibleScheme {
  id: string;
  scheme_code: string;
  name_english: string;
  name_tamil: string;
  name_transliteration: string;
  department: string;
  category: string;
  description_english: string;
  description_tamil: string;
  benefit_amount: string;
  source_url: string;
  last_verified_date: string;
  required_documents?: string[];
  application_office?: string;
  application_mode?: string;
  online_application_url?: string;
  processing_time_estimate?: string;
}

export interface FailedRule {
  field_name: string;
  operator: string;
  expected_value: string;
  actual_value?: string;
  applies_to: string;
  reason: string;
}

export interface PartiallyEligibleScheme {
  scheme: EligibleScheme;
  failed_rules: FailedRule[];
}

export interface PersonEligibilityResponse {
  person_id: string;
  person_name: string;
  eligible_schemes_count: number;
  partially_eligible_schemes_count: number;
  eligible_schemes: EligibleScheme[];
  partially_eligible_schemes: PartiallyEligibleScheme[];
}

export interface EligibleSchemeGuidance {
  scheme_id: string;
  scheme_code: string;
  name_tamil: string;
  name_english: string;
  department?: string;
  benefit_amount: string;
  benefit_summary_tamil: string;
  required_documents: string[];
  where_to_apply_tamil: string;
  application_mode: string;
  online_application_url?: string;
  steps_tamil: string[];
  processing_time_estimate: string;
  source_url: string;
  is_stale: boolean;
  disclaimer_tamil?: string;
  using_structured_data_only?: boolean;
}

export interface MissingConditionGuidance {
  field_name: string;
  missing_condition_tamil: string;
  how_to_resolve_tamil: string;
}

export interface PartiallyEligibleSchemeGuidance {
  scheme_id: string;
  scheme_code: string;
  name_tamil: string;
  name_english: string;
  benefit_amount: string;
  why_not_eligible_tamil: string;
  missing_conditions: MissingConditionGuidance[];
  action_advice_tamil: string;
  source_url: string;
}

export interface PersonGuidanceResponse {
  person_id: string;
  person_name: string;
  eligible_schemes_count: number;
  partially_eligible_schemes_count: number;
  eligible_schemes_guidance: EligibleSchemeGuidance[];
  partially_eligible_schemes_guidance: PartiallyEligibleSchemeGuidance[];
}

export interface IntakeTurnResponse {
  session_id: string;
  reply: string;
  current_step: string;
  is_completed: boolean;
  saved_family_id?: string;
  saved_person_ids?: string[];
  family_data?: Record<string, any>;
  persons_data?: Record<string, any>[];
}

export interface ApplicationStatusRecord {
  id: string;
  person_id: string;
  scheme_id: string;
  status: string;
  last_updated: string;
  next_action_note?: string;
  pending_documents: string[];
  renewal_due_date?: string;
  person_name?: string;
  scheme_code?: string;
  scheme_name_tamil?: string;
  scheme_name_english?: string;
}

export interface AuthUserResponse {
  id: string;
  phone: string;
  role: string;
  is_volunteer: boolean;
  family_ids: string[];
}

function translateToTamilError(status: number, rawDetail?: string, messageTa?: string): string {
  if (messageTa) {
    return messageTa;
  }
  if (rawDetail && rawDetail.includes("Authentication required")) {
    return "அங்கீகாரம் தேவை. தயவுசெய்து தொலைபேசி எண் மூலம் உள்நுழையவும்.";
  }
  if (status === 401) {
    return "அங்கீகாரம் தேவை. தயவுசெய்து தொலைபேசி எண் மூலம் உள்நுழையவும்.";
  }
  if (status === 403) {
    return "இந்த விவரங்களை அணுக தங்களுக்கு அனுமதி இல்லை.";
  }
  if (status === 404) {
    return rawDetail || "கோரப்பட்ட விவரங்கள் சர்வரில் கிடைக்கவில்லை.";
  }
  if (status === 429) {
    return "அதிகமான கோரிக்கைகள். சிறிது நேரம் காத்திருந்து மீண்டும் முயற்சிக்கவும்.";
  }
  if (status >= 500) {
    return "சேவை தற்காலிகமாக கிடைக்கவில்லை. சில நொடிகள் கழித்து மீண்டும் முயற்சிக்கவும்.";
  }
  return rawDetail || "தொழில்நுட்ப பிழை ஏற்பட்டது. மீண்டும் முயற்சிக்கவும்.";
}

export async function fetchFromApi<T>(
  path: string,
  options?: RequestInit,
  retries: number = 3
): Promise<T> {
  const url = `${API_BASE}${path}`;

  // Attach token if available
  let token: string | null = null;
  if (typeof window !== "undefined") {
    token = localStorage.getItem("urimai_token");
  }

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(options?.headers as Record<string, string>),
  };

  let lastError: Error | null = null;

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        ...options,
        headers,
      });

      if (!res.ok) {
        let errorDetail = `API Error: ${res.status}`;
        let messageTa: string | undefined = undefined;
        try {
          const errorJson = await res.json();
          if (errorJson.message_ta) {
            messageTa = errorJson.message_ta;
          }
          if (errorJson.message) {
            errorDetail = errorJson.message;
          } else if (errorJson.detail) {
            errorDetail =
              typeof errorJson.detail === "string"
                ? errorJson.detail
                : JSON.stringify(errorJson.detail);
          }
        } catch {
          // fallback
        }

        // On 4xx client errors (e.g. 400, 401, 403, 404, 422), do not retry
        if (res.status >= 400 && res.status < 500 && res.status !== 408) {
          throw new Error(translateToTamilError(res.status, errorDetail, messageTa));
        }

        // If server error (502, 503, 504), let it retry
        if (attempt < retries && (res.status === 502 || res.status === 503 || res.status === 504 || res.status === 500)) {
          const delay = Math.pow(2, attempt) * 1000;
          await new Promise((resolve) => setTimeout(resolve, delay));
          continue;
        }

        throw new Error(translateToTamilError(res.status, errorDetail, messageTa));
      }

      return await res.json();
    } catch (err: any) {
      lastError = err;
      // If network failure (e.g. Render server waking up / cold start) and retries remaining, wait with backoff
      if (attempt < retries) {
        const delay = Math.pow(2, attempt) * 1200; // 1.2s, 2.4s, 4.8s
        await new Promise((resolve) => setTimeout(resolve, delay));
      }
    }
  }

  throw (
    lastError ||
    new Error(
      "இணைப்பு பிழை: சர்வர் தயாராகிறது அல்லது இணைய இணைப்பு துண்டிக்கப்பட்டுள்ளது. தயவுசெய்து சில நொடிகள் கழித்து மீண்டும் முயற்சிக்கவும்."
    )
  );
}

// Complete typed API Client
export const api = {
  // Auth
  sendOtp: (phone: string) =>
    fetchFromApi<{ status: string; message: string }>("/auth/phone/send-otp", {
      method: "POST",
      body: JSON.stringify({ phone }),
    }),
  verifyOtp: (phone: string, otp: string) =>
    fetchFromApi<{
      status: string;
      access_token: string;
      user: { id: string; phone: string; role: string };
    }>("/auth/phone/verify-otp", {
      method: "POST",
      body: JSON.stringify({ phone, otp }),
    }),
  getMe: () => fetchFromApi<AuthUserResponse>("/auth/me"),
  logout: () => {
    if (typeof window !== "undefined") {
      localStorage.removeItem("urimai_token");
    }
    return fetchFromApi<{ status: string }>("/auth/logout", { method: "POST" });
  },

  // Families & Persons
  createFamily: (data: Partial<Family>) =>
    fetchFromApi<Family>("/families", { method: "POST", body: JSON.stringify(data) }),
  getFamily: (id: string) => fetchFromApi<Family>(`/families/${id}`),
  listFamilies: () => fetchFromApi<Family[]>("/families"),
  addPerson: (familyId: string, data: Partial<Person>) =>
    fetchFromApi<Person>(`/families/${familyId}/persons`, {
      method: "POST",
      body: JSON.stringify(data),
    }),
  getPerson: (id: string) => fetchFromApi<Person>(`/persons/${id}`),

  // Schemes
  getSchemes: (department?: string, category?: string) => {
    const params = new URLSearchParams();
    if (department) params.set("department", department);
    if (category) params.set("category", category);
    const query = params.toString() ? `?${params.toString()}` : "";
    return fetchFromApi<EligibleScheme[]>(`/schemes${query}`);
  },
  getScheme: (codeOrId: string) => fetchFromApi<EligibleScheme>(`/schemes/${codeOrId}`),

  // Eligibility & Guidance
  getPersonEligibility: (personId: string) =>
    fetchFromApi<PersonEligibilityResponse>(`/persons/${personId}/eligibility`),
  getPersonGuidance: (personId: string) =>
    fetchFromApi<PersonGuidanceResponse>(`/persons/${personId}/guidance`),
  getFamilyGuidance: (familyId: string) =>
    fetchFromApi<any>(`/families/${familyId}/guidance`),

  // Conversational Intake
  sendIntakeMessage: (sessionId: string, message: string) =>
    fetchFromApi<IntakeTurnResponse>("/intake/message", {
      method: "POST",
      body: JSON.stringify({ session_id: sessionId, message }),
    }),
  resumeIntake: () => fetchFromApi<IntakeTurnResponse>("/intake/resume"),

  // Application Tracking
  createApplicationTracking: (data: {
    person_id: string;
    scheme_id: string;
    status: string;
    pending_documents?: string[];
    next_action_note?: string;
  }) =>
    fetchFromApi<ApplicationStatusRecord>("/applications", {
      method: "POST",
      body: JSON.stringify(data),
    }),
  getPersonApplications: (personId: string) =>
    fetchFromApi<ApplicationStatusRecord[]>(`/persons/${personId}/applications`),
  updateApplicationStatus: (appId: string, data: Partial<ApplicationStatusRecord>) =>
    fetchFromApi<ApplicationStatusRecord>(`/applications/${appId}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),

  // Health Check
  getHealth: () => fetchFromApi<{ status: string; service: string }>("/health"),

  // Admin Dashboard Endpoints
  adminLogin: (email: string, password: string) =>
    fetchFromApi<{
      status: string;
      access_token: string;
      user: { id: string; email: string; name: string; role: string };
    }>("/auth/admin/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    }),
  getAdminStats: () => fetchFromApi<DashboardStats>("/admin/dashboard/stats"),
  getAdminReviewQueue: (status?: string) => {
    const query = status ? `?status=${status}` : "";
    return fetchFromApi<SchemeReviewItem[]>(`/admin/freshness/review-queue${query}`);
  },
  resolveAdminReview: (reviewId: string, reviewerNotes: string, updateVerifiedDate: boolean = true) =>
    fetchFromApi<SchemeReviewItem>(`/admin/freshness/verify/${reviewId}`, {
      method: "POST",
      body: JSON.stringify({ reviewer_notes: reviewerNotes, update_verified_date: updateVerifiedDate }),
    }),
  getAdminStuckApplications: (daysThreshold: number = 7) =>
    fetchFromApi<StuckApplication[]>(`/admin/applications/stuck?days_threshold=${daysThreshold}`),
  getAdminErrorLogs: (limit: number = 50) =>
    fetchFromApi<ErrorLogItem[]>(`/admin/logs/errors?limit=${limit}`),
  getAdminAuditLogs: (limit: number = 50) =>
    fetchFromApi<AdminAuditLog[]>(`/admin/audit-logs?limit=${limit}`),
  updateAdminRule: (
    schemeId: string,
    ruleId: string,
    data: {
      field_name?: string;
      operator?: string;
      value?: string;
      applies_to?: string;
      admin_notes: string;
    }
  ) =>
    fetchFromApi<any>(`/admin/schemes/${schemeId}/rules/${ruleId}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),
  triggerAdminFreshnessCheck: (thresholdDays: number = 180) =>
    fetchFromApi<{ total_schemes_checked: number; stale_schemes_flagged: number; review_queue_count: number }>(
      `/admin/freshness/run-check?threshold_days=${thresholdDays}`,
      { method: "POST" }
    ),
  triggerAdminFollowups: (pendingDaysThreshold: number = 7) =>
    fetchFromApi<{ total_applications_checked: number; documents_pending_reminders_generated: number; notifications_created: number }>(
      `/admin/applications/trigger-followups?pending_days_threshold=${pendingDaysThreshold}`,
      { method: "POST" }
    ),
};

export interface DashboardStats {
  total_families: number;
  total_persons: number;
  total_applications: number;
  active_schemes_count: number;
  stale_schemes_count: number;
  stuck_applications_count: number;
  schemes_zero_matches: Array<{
    scheme_id: string;
    scheme_code: string;
    name_tamil: string;
    name_english: string;
    department: string;
    rules_count: number;
  }>;
  total_extractions_logged: number;
  recent_errors_count: number;
}

export interface SchemeReviewItem {
  id: string;
  scheme_id: string;
  scheme_code: string;
  scheme_name_tamil: string;
  scheme_name_english: string;
  department: string;
  source_url: string;
  last_verified_date?: string;
  flagged_reason: string;
  status: string;
  reviewer_notes?: string;
  created_at: string;
  reviewed_at?: string;
}

export interface StuckApplication {
  id: string;
  person_id: string;
  person_name: string;
  family_id: string;
  district: string;
  scheme_id: string;
  scheme_code: string;
  scheme_name_tamil: string;
  scheme_name_english: string;
  department: string;
  status: string;
  days_stuck: number;
  last_updated: string;
  pending_documents: string[];
  next_action_note?: string;
}

export interface ErrorLogItem {
  id: string;
  log_type: string;
  session_id?: string;
  raw_input?: string;
  target_field?: string;
  error_message?: string;
  created_at: string;
}

export interface AdminAuditLog {
  id: string;
  admin_user_id: string;
  admin_email: string;
  action: string;
  entity_type: string;
  entity_id: string;
  before_value?: Record<string, any>;
  after_value?: Record<string, any>;
  ip_address?: string;
  created_at: string;
}

