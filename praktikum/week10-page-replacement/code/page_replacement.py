import os
from collections import deque


def fifo(reference, frame_count):
    frames = []
    queue = deque()
    page_fault = 0
    table = []

    for page in reference:
        # CEK HIT / FAULT (SEBELUM GANTI)
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_fault += 1

            if len(frames) < frame_count:
                frames.append(page)
                queue.append(page)
            else:
                # FIFO: buang yang paling lama masuk
                old = queue.popleft()
                idx = frames.index(old)
                frames[idx] = page
                queue.append(page)

        table.append((page, frames.copy(), status))

    return page_fault, table


def lru(reference, frame_count):
    frames = []
    last_used = {}
    page_fault = 0
    table = []

    for time, page in enumerate(reference):
        # CEK HIT / FAULT (SEBELUM GANTI)
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_fault += 1

            if len(frames) < frame_count:
                frames.append(page)
            else:
                # LRU: cari page paling lama tidak dipakai
                lru_page = min(frames, key=lambda p: last_used[p])
                frames[frames.index(lru_page)] = page

        last_used[page] = time
        table.append((page, frames.copy(), status))

    return page_fault, table


def print_table(title, table, frame_count):
    print(f"\n{title}")
    print("-" * 50)
    header = "Page\t" + "\t".join([f"F{i+1}" for i in range(frame_count)]) + "\tStatus"
    print(header)
    print("-" * 50)

    for page, frames, status in table:
        row = f"{page}\t"
        for i in range(frame_count):
            row += f"{frames[i] if i < len(frames) else '-'}\t"
        row += status
        print(row)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "reference_string.txt")

    with open(file_path, "r") as file:
        reference = list(map(int, file.read().split(",")))

    frame_count = 3

    fifo_fault, fifo_table = fifo(reference, frame_count)
    lru_fault, lru_table = lru(reference, frame_count)

    print_table("FIFO Page Replacement", fifo_table, frame_count)
    print(f"\nTotal Page Fault FIFO: {fifo_fault}")

    print_table("LRU Page Replacement", lru_table, frame_count)
    print(f"\nTotal Page Fault LRU: {lru_fault}")


if __name__ == "__main__":
    main()
