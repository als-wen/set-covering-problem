from set_covering_problem import solving, validation 

# Example data
m = 3
n = 4
costs = [1, 2, 3, 4]
cov = [
    [0, 1],    # Row 0 covered by subsets 0 and 1
    [1, 2],    # Row 1 covered by subsets 1 and 2
    [2, 3]     # Row 2 covered by subsets 2 and 3
]

validation(m, n, costs, cov)

sol, cost, amount_time = solving(m, n, costs, cov)

print("Subsets:", sol)
print("Costo total:", cost)
print("Tiempo de ejecución:", round(amount_time, 4), "s")
