# Task 10 - Inventory Reconciliation
import csv

open("inventory.csv", "w").write("sku,name,quantity\nP01,Pen,10\n")
open("movements.csv", "w").write("sku,type,units\nP01,OUT,4\nP01,OUT,9\nP01,IN,2\nP99,IN,5\n")

stock, names = {}, {}
for row in csv.DictReader(open("inventory.csv")):
    stock[row["sku"]] = int(row["quantity"])
    names[row["sku"]] = row["name"]

rejected = []
for row in csv.DictReader(open("movements.csv")):          # in order
    sku, kind, units = row["sku"], row["type"], int(row["units"])
    if sku not in stock:
        rejected.append([sku, kind, units, "unknown SKU"])
    elif units <= 0:
        rejected.append([sku, kind, units, "units must be positive"])
    elif kind not in ("IN", "OUT"):
        rejected.append([sku, kind, units, "invalid type"])
    elif kind == "OUT" and units > stock[sku]:
        rejected.append([sku, kind, units, "not enough stock"])
    elif kind == "IN":
        stock[sku] += units
    else:
        stock[sku] -= units

out = csv.writer(open("updated_inventory.csv", "w", newline=""))
out.writerow(["sku", "name", "quantity"])
for sku in stock:
    out.writerow([sku, names[sku], stock[sku]])

out = csv.writer(open("rejected_movements.csv", "w", newline=""))
out.writerow(["sku", "type", "units", "reason"])
out.writerows(rejected)
print(stock, rejected)
