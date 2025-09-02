"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""
import datetime
attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    attendance[student_id] = {
        "name": name,
        "present_days": [],
        "absent_days": []
    }

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for iden in student_ids:
        if iden in attendance:
            if today not in attendance[iden]["present_days"]:
                attendance[iden]["present_days"].append(today)
            if today in attendance[iden]["absent_days"]:
                attendance[iden]["absent_days"].remove(today)

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for iden in student_ids:
        if iden in attendance:
            if today not in attendance[iden]["absent_days"]:
                attendance[iden]["absent_days"].append(today)
            if today in attendance[iden]["present_days"]:
                attendance[iden]["present_days"].remove(today)

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    only_present = kwargs.get("only_present", False)
    only_absent = kwargs.get("only_absent", False)

    report = {}

    for iden, details in attendance.items():
        if only_present and not details["present_days"]:
            continue
        if only_absent and not details["absent_days"]:
            continue
        report[iden] = details

    return report

register_student(1, "Alice")
register_student(2, "Bob")
register_student(3, "Charlie")

mark_present([1, 3])
mark_absent([2])

print("Full Report:", get_report())
print()
print("Only Present:", get_report(only_present=True))
print()
print("Only Absent:", get_report(only_absent=True))

