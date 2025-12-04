import time
import random


L = "audit.log"
T = 30.0
C = 5

# Start the audit
with open(L, "w") as f:
    f.write(f"--- START ---\n")

print(f"\nMonitoring (T > {T}°C)...")

for _ in range(C):
    temp = round(random.uniform(28.0, 35.0), 1)

    # Logic: Alert or Normal
    if temp > T:
        action = "ALERT: Initiate Cooling!"
    else:
        action = "Normal."

    # Log & Print
    entry = f"[{time.strftime('%H:%M:%S')}] {temp}°C | {action}"
    with open(L, "a") as f:
        f.write(entry + "\n")
    print(entry)

    time.sleep(0.3)

print("--- END ---")
