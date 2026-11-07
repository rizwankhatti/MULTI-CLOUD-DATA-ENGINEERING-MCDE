# Task 11 - Student Gradebook
import csv

open("students.csv", "w").write("student_id,name\n101,Ali\n102,Sara\n")
open("scores.csv", "w").write("student_id,subject,marks\n101,Math,90\n101,Eng,80\n101,Sci,85\n102,Math,95\n102,Math,50\n999,Math,60\n")

names = {}
marks = {}
for row in csv.DictReader(open("students.csv")):
    names[row["student_id"]] = row["name"]
    marks[row["student_id"]] = {}

for row in csv.DictReader(open("scores.csv")):
    sid, subject, m = row["student_id"], row["subject"], float(row["marks"])
    if sid not in names:
        print("Rejected unknown ID:", sid)
    elif m < 0 or m > 100:
        print("Rejected bad marks:", sid, m)
    elif subject in marks[sid]:
        print("Rejected duplicate:", sid, subject)
    else:
        marks[sid][subject] = m

report = []
for sid in names:
    if marks[sid]:
        avg = sum(marks[sid].values()) / len(marks[sid])
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 55 else "D" if avg >= 40 else "F"
        report.append([sid, names[sid], avg, grade])

report.sort(key=lambda r: (-r[2], r[0]))           # best average first, then ID

out = csv.writer(open("report.csv", "w", newline=""))
out.writerow(["rank", "student_id", "name", "average", "grade"])
for rank, r in enumerate(report, 1):
    out.writerow([rank] + r)
    print(rank, r)
