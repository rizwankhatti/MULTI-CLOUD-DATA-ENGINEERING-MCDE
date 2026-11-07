# Task 13 - Booking Scheduler
from datetime import datetime

bookings = []        # each: [id, room, start, end]

def add_booking(booking_id, room, start, end):
    if end <= start:
        raise ValueError("End must be after start")
    for b in bookings:
        if b[0] == booking_id:
            raise ValueError("Duplicate ID")

    conflicts = []
    for b in bookings:
        if b[1] == room and start < b[3] and end > b[2]:    # overlap
            conflicts.append(b[0])
    if conflicts:
        return "Rejected, conflicts with " + str(conflicts)
    bookings.append([booking_id, room, start, end])
    return "Accepted"

def t(hhmm):
    return datetime.strptime("2026-11-07 " + hhmm, "%Y-%m-%d %H:%M")

print(add_booking(1, "A", t("09:00"), t("10:00")))    # Accepted
print(add_booking(2, "A", t("10:00"), t("11:00")))    # Accepted (touching is OK)
print(add_booking(3, "A", t("09:30"), t("10:30")))    # Rejected
