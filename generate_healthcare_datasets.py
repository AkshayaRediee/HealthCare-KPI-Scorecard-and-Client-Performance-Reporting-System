import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# -----------------------
# 1. Clients (50 rows)
# -----------------------
client_ids = np.arange(2001, 2001 + 50)
segments = ["employer", "health_plan", "provider", "government"]

clients = pd.DataFrame({
    "client_id": client_ids,
    "client_name": [f"Client {i}" for i in range(1, 51)],
    "contracted_members": np.random.randint(3000, 30000, size=50)
})

clients["active_members"] = (clients["contracted_members"] * np.random.uniform(0.75, 0.95, size=50)).astype(int)
clients["segment"] = np.random.choice(segments, size=50, p=[0.4, 0.3, 0.2, 0.1])

start_dates = pd.to_datetime("2021-01-01")
clients["go_live_date"] = [
    (start_dates + pd.Timedelta(days=int(d))).date()
    for d in np.random.randint(0, 1500, size=50)
]

clients["status"] = np.random.choice(
    ["active", "implementation", "terminated"],
    size=50,
    p=[0.7, 0.2, 0.1]
)

# -----------------------
# 2. Coaches (100 rows)
# -----------------------
coach_ids = np.arange(3001, 3001 + 100)
regions = ["Southeast", "Northeast", "Midwest", "West"]
specialties = ["diabetes", "hypertension", "behavioral_health", "cardiology", "general_wellness"]

coaches = pd.DataFrame({
    "coach_id": coach_ids,
    "coach_name": [f"Coach {i}" for i in range(1, 101)],
    "region": np.random.choice(regions, size=100),
    "specialty": np.random.choice(specialties, size=100),
    "status": np.random.choice(["active", "on_leave", "terminated"], size=100, p=[0.8, 0.1, 0.1])
})

# -----------------------
# 3. Patients (5,000 rows)
# -----------------------
num_patients = 5000
patient_ids = np.arange(10001, 10001 + num_patients)

ages = np.random.choice(range(18, 90), size=num_patients)
genders = np.random.choice(["M", "F", "Other"], size=num_patients, p=[0.48, 0.48, 0.04])

conditions = ["diabetes", "hypertension", "COPD", "CHF", "asthma", "none"]
condition_probs = [0.25, 0.25, 0.1, 0.1, 0.15, 0.15]
chronic_condition = np.random.choice(conditions, size=num_patients, p=condition_probs)

def risk_from_condition(cond):
    if cond in ["CHF", "COPD"]:
        return np.random.choice(["high", "medium"], p=[0.7, 0.3])
    elif cond in ["diabetes", "hypertension"]:
        return np.random.choice(["high", "medium", "low"], p=[0.3, 0.5, 0.2])
    elif cond == "asthma":
        return np.random.choice(["medium", "low"], p=[0.4, 0.6])
    else:
        return np.random.choice(["medium", "low"], p=[0.2, 0.8])

risk_level = [risk_from_condition(c) for c in chronic_condition]

enroll_start = pd.to_datetime("2021-01-01")
enrollment_dates = [
    (enroll_start + pd.Timedelta(days=int(d))).date()
    for d in np.random.randint(0, 1500, size=num_patients)
]

patient_client_ids = np.random.choice(clients["client_id"], size=num_patients)

cities = ["Atlanta", "Buford", "Savannah", "Charlotte", "Miami", "Orlando", "Raleigh", "Nashville", "Tampa", "Augusta"]
states = ["GA", "GA", "GA", "NC", "FL", "FL", "NC", "TN", "FL", "GA"]
city_choices = np.random.choice(len(cities), size=num_patients)
patient_cities = [cities[i] for i in city_choices]
patient_states = [states[i] for i in city_choices]

member_status = np.random.choice(["active", "disenrolled", "pending"], size=num_patients, p=[0.8, 0.15, 0.05])
has_mobile_app = np.random.choice(["yes", "no"], size=num_patients, p=[0.7, 0.3])

patients = pd.DataFrame({
    "patient_id": patient_ids,
    "age": ages,
    "gender": genders,
    "chronic_condition": chronic_condition,
    "risk_level": risk_level,
    "enrollment_date": enrollment_dates,
    "client_id": patient_client_ids,
    "city": patient_cities,
    "state": patient_states,
    "member_status": member_status,
    "has_mobile_app": has_mobile_app
})

# -----------------------
# 4. Coaching Sessions (12,000 rows)
# -----------------------
num_sessions = 12000
session_ids = np.arange(50001, 50001 + num_sessions)

session_dates = [
    (enroll_start + pd.Timedelta(days=int(d))).date()
    for d in np.random.randint(0, 1500, size=num_sessions)
]

session_patient_ids = np.random.choice(patients["patient_id"], size=num_sessions)
session_types = np.random.choice(["phone", "video", "message"], size=num_sessions, p=[0.5, 0.3, 0.2])
coach_ids_for_sessions = np.random.choice(coaches["coach_id"], size=num_sessions)

completed_flags = np.random.choice(["yes", "no"], size=num_sessions, p=[0.8, 0.2])

duration_minutes = [
    0 if completed_flags[i] == "no" else int(np.random.normal(28, 8))
    for i in range(num_sessions)
]
duration_minutes = [max(0, d) for d in duration_minutes]

topics = ["medication_adherence", "diet", "exercise", "mental_health", "follow_up"]
session_topics = np.random.choice(topics, size=num_sessions, p=[0.25, 0.2, 0.25, 0.15, 0.15])

no_show = ["yes" if completed_flags[i] == "no" else "no" for i in range(num_sessions)]

sessions = pd.DataFrame({
    "session_id": session_ids,
    "patient_id": session_patient_ids,
    "session_date": session_dates,
    "completed": completed_flags,
    "coach_id": coach_ids_for_sessions,
    "session_type": session_types,
    "duration_minutes": duration_minutes,
    "topic": session_topics,
    "no_show": no_show
})

# -----------------------
# 5. Support Tickets (5,000 rows)
# -----------------------
num_tickets = 5000
ticket_ids = np.arange(80001, 80001 + num_tickets)

created_dates = [
    (enroll_start + pd.Timedelta(days=int(d))).date()
    for d in np.random.randint(0, 1500, size=num_tickets)
]

ticket_patient_ids = np.random.choice(patients["patient_id"], size=num_tickets)

issue_types = ["medication", "app", "scheduling", "claims", "device", "other"]
issue_type_probs = [0.25, 0.2, 0.2, 0.15, 0.1, 0.1]
ticket_issue_types = np.random.choice(issue_types, size=num_tickets, p=issue_type_probs)

resolved_flags = np.random.choice(["yes", "no"], size=num_tickets, p=[0.85, 0.15])

response_time = np.round(np.random.gamma(shape=2.0, scale=3.0, size=num_tickets), 1)

priority_levels = ["low", "medium", "high", "urgent"]
priority_probs = [0.4, 0.35, 0.2, 0.05]
ticket_priorities = np.random.choice(priority_levels, size=num_tickets, p=priority_probs)

channels = np.random.choice(["phone", "email", "app", "web"], size=num_tickets, p=[0.4, 0.25, 0.25, 0.1])

resolved_dates = []
first_contact = []
for i in range(num_tickets):
    if resolved_flags[i] == "no":
        resolved_dates.append(pd.NaT)
        first_contact.append("no")
    else:
        days_to_resolve = np.random.randint(0, 3)  # 0–2 days
        rd = pd.to_datetime(created_dates[i]) + pd.Timedelta(days=int(days_to_resolve))
        resolved_dates.append(rd.date())
        fcr = "yes" if response_time[i] <= 2 and days_to_resolve == 0 else "no"
        first_contact.append(fcr)

tickets = pd.DataFrame({
    "ticket_id": ticket_ids,
    "patient_id": ticket_patient_ids,
    "created_date": created_dates,
    "response_time_hours": response_time,
    "resolved": resolved_flags,
    "issue_type": ticket_issue_types,
    "priority": ticket_priorities,
    "channel": channels,
    "resolved_date": resolved_dates,
    "first_contact_resolution": first_contact
})

# -----------------------
# Save to CSV
# -----------------------
patients.to_csv("patients.csv", index=False)
sessions.to_csv("coaching_sessions.csv", index=False)
tickets.to_csv("support_tickets.csv", index=False)
coaches.to_csv("coaches.csv", index=False)
clients.to_csv("clients.csv", index=False)

print("Datasets generated: patients.csv, coaching_sessions.csv, support_tickets.csv, coaches.csv, clients.csv")