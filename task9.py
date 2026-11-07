# Task 09 - Log Inspector
# line format: 2026-11-07 10:30:00 | ERROR | message
bad_lines = 0

def read_errors(path):
    global bad_lines
    number = 0
    for line in open(path):                  # reads one line at a time
        number += 1
        parts = line.strip().split(" | ")
        if len(parts) != 3:
            bad_lines += 1                   # skip and count broken line
        elif parts[1] == "ERROR":
            yield (number, parts[0], parts[2])

def summarize_errors(path):
    counts = {}
    for number, time, message in read_errors(path):
        date = time[:10]
        counts[date] = counts.get(date, 0) + 1
    return counts

open("sample.log", "w").write(
    "2026-11-07 10:30:00 | ERROR | Connection lost\n"
    "2026-11-07 10:31:00 | INFO | All good\n"
    "broken line\n"
    "2026-11-08 09:00:00 | ERROR | Disk full\n")

print(list(read_errors("sample.log")))
bad_lines = 0
print(summarize_errors("sample.log"), "broken lines:", bad_lines)
