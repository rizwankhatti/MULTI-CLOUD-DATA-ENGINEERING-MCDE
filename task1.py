# Task 01 - Transaction Analyzer
data = [
    {"id": 1, "customer": "Ali", "category": "Food", "amount": 500, "status": "success"},
    {"id": 2, "customer": "Ali", "category": "Travel", "amount": 200, "status": "failed"},
    {"id": 3, "customer": "Sara", "category": "Food", "amount": 700, "status": "success"},
]

ids = []
total = {}
cats = {}
for t in data:
    if t["id"] in ids:                       # duplicate id -> error
        raise ValueError("Duplicate ID")
    ids.append(t["id"])

    name = t["customer"]
    if name not in total:                    # every customer starts at 0
        total[name] = 0
        cats[name] = {}
    if t["status"] == "success":             # failed ones are ignored
        total[name] += t["amount"]
        c = t["category"]
        cats[name][c] = cats[name].get(c, 0) + t["amount"]

report = []
for name in total:
    top = max(cats[name], key=cats[name].get) if cats[name] else None
    report.append([name, total[name], top])

report.sort(key=lambda r: (-r[1], r[0]))     # high spending first, then A-Z
for rank, r in enumerate(report, 1):
    print(rank, r)
