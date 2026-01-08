import os
import csv
from collections import defaultdict

# Baca dataset
processes = []
allocation = {}
request = {}

with open("d:/gitos/os-202501-250202946/praktikum/week11-deadlock-detection/code/dataset_deadlock.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Proses"]
        processes.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]

# Bangun Wait-For Graph
wait_for = defaultdict(list)

for p1 in processes:
    for p2 in processes:
        if p1 != p2 and request[p1] == allocation[p2]:
            wait_for[p1].append(p2)

# Deteksi siklus (DFS)
visited = set()
stack = set()
deadlock_processes = set()

def dfs(p):
    visited.add(p)
    stack.add(p)
    for neighbor in wait_for[p]:
        if neighbor not in visited:
            dfs(neighbor)
        elif neighbor in stack:
            deadlock_processes.update(stack)
    stack.remove(p)

for p in processes:
    if p not in visited:
        dfs(p)

# Output hasil
print("\n=== HASIL DETEKSI DEADLOCK ===")
if deadlock_processes:
    print("Deadlock terdeteksi")
    print("Proses yang terlibat deadlock:")
    for p in deadlock_processes:
        print("-", p)
else:
    print("Tidak terjadi deadlock")

print("\nWait-For Graph:")
for p in wait_for:
    print(f"{p} menunggu {wait_for[p]}")
