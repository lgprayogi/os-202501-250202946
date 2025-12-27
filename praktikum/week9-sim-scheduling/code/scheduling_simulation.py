import csv
import os

# BACA DATASET CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "dataset.csv")

proses_list = []

with open(CSV_FILE, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # lewati header

    for row in reader:
        proses_list.append({
            "proses": row[0],
            "arrival": int(row[1]),
            "burst": int(row[2])
        })


# FCFS ALGORITHM

def fcfs(processes):
    time = 0
    result = []

    for p in sorted(processes, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        waiting = start - p["arrival"]
        time += p["burst"]
        turnaround = time - p["arrival"]

        result.append({
            **p,
            "waiting": waiting,
            "turnaround": turnaround
        })

    return result

# SJF NON-PREEMPTIVE
def sjf_non_preemptive(processes):
    time = 0
    completed = []
    ready_queue = processes.copy()

    while ready_queue:
        available = [p for p in ready_queue if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x["burst"])
        ready_queue.remove(p)

        waiting = time - p["arrival"]
        time += p["burst"]
        turnaround = time - p["arrival"]

        completed.append({
            **p,
            "waiting": waiting,
            "turnaround": turnaround
        })

    return completed



# TAMPILKAN HASIL

def print_table(title, data):
    print(f"\n{title}")
    print("Proses  Arrival  Burst  Waiting  Turnaround")

    total_wt = 0
    total_tat = 0

    for p in data:
        total_wt += p["waiting"]
        total_tat += p["turnaround"]

        print(f"{p['proses']:6} {p['arrival']:7} {p['burst']:6} "
              f"{p['waiting']:8} {p['turnaround']:11}")

    n = len(data)
    print("Rata-rata Waiting Time   :", total_wt / n)
    print("Rata-rata Turnaround Time:", total_tat / n)



if __name__ == "__main__":
    fcfs_result = fcfs(proses_list)
    sjf_result = sjf_non_preemptive(proses_list)

    print_table("HASIL SIMULASI FCFS", fcfs_result)
    print_table("HASIL SIMULASI SJF NON-PREEMPTIVE", sjf_result)
