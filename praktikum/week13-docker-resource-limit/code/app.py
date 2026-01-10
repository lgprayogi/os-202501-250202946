import time

data = []

print("Program started", flush=True)

try:
    while True:
        # allocate memory slowly
        data.append("A" * 10_000_000)  # ~10 MB
        print(f"Allocated memory chunks: {len(data)}", flush=True)
        time.sleep(0.5)
except MemoryError:
    print("Memory limit exceeded!")
