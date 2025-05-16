import os
import pandas as pd
from set_covering_problem import read, validation, solving

files = ["rail2536", "rail4284", "rail4872"]
directory = "data/pia-4th/"
results = []

for file in files:
    file_path = os.path.join(directory, file)
    m, n, costs, cov = read(file_path)
    validation(m, n, costs, cov)
    
    sol, cost, amount_time = solving(m, n, costs, cov)
    
    results.append({
        "Instance": file,
        "Subsets": len(sol),
        "Total cost": cost,
        "Time": round(amount_time, 4)
    })

df = pd.DataFrame(results)
df.to_csv("results/results_4th.csv", index = False)
print("Was saved successfully")
