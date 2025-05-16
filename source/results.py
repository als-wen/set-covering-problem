import os
import pandas as pd
from set_covering_problem import read, validation, solving

files = ["scp41.txt", "scp51.txt", "scpa1.txt", "scpb1.txt"]
directory = "data/pia-3rd/"
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
df.to_csv("results/results_3rd.csv", index = False)
print("Was saved successfully")
