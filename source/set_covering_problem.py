import pulp
import time

def read(file_path):
    with open(file_path, 'r') as file:
        tokens = file.read().split()

    m = int(tokens[0])
    n = int(tokens[1])
    index = 2

    costs = list(map(int, tokens[index:index + n]))
    index += n
    cov = [[] for _ in range(m)]
    
    for i in range(m):
        amount = int(tokens[index])
        index += 1
        cols = [int(tokens[index + j]) - 1 for j in range(amount)]
        cov[i] = cols
        index += amount

    return m, n, costs, cov


def validation(m, n, costs, cov):
    assert len(costs) == n, "Length of costs don't match n"
    assert len(cov) == m, "Length of coverage don't match m"
    for c in costs:
        assert c > 0, "Costs need to be positive"
    for i in range(m):
        assert len(cov[i]) > 0, f"Row {i} doesn't have coverage"
        for col in cov[i]:
            assert 0 <= col < n, f"Index out of range in coverage of row {i}"


def solving(m, n, costs, cov):
    prob = pulp.LpProblem("Set_Covering_Problem", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x_{j}", cat="Binary") for j in range(n)]

    # Objective function
    prob += pulp.lpSum([costs[j] * x[j] for j in range(n)])

    # Constraints
    for i in range(m):
        prob += pulp.lpSum([x[j] for j in cov[i]]) >= 1

    start = time.time()
    prob.solve()
    amount_time = time.time() - start

    subset = [j for j in range(n) if pulp.value(x[j]) == 1]
    total_cost = pulp.value(prob.objective)

    return subset, total_cost, amount_time

if __name__ == "__main__":
    path = "data/pia-second-part/scp41.txt"  
    m, n, costs, cov = read(path)
    validation(m, n, costs, cov)
    sol, cost, amount_time = solving(m, n, costs, cov)

    print(f"Subset: {sol}")
    print(f"Cost: {cost}")
    print(f"Time: {amount_time:.4f} seconds")
