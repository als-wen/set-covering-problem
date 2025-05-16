import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results_4th.csv")

plt.figure(figsize=(8, 5))
plt.bar(df["Instance"], df["Total cost"], color="skyblue")
plt.title("Total Cost per Instance")
plt.xlabel("Instance")
plt.ylabel("Total Cost")
plt.tight_layout()
plt.savefig("results/graphics/instance_cost.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(df["Instance"], df["Time"], color="salmon")
plt.title("Execution Time per Instance")
plt.xlabel("Instance")
plt.ylabel("Time (s)")
plt.tight_layout()
plt.savefig("results/graphics/instance_time.png", dpi=300)
plt.close()

print("Was saved successfully")
