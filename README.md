import numpy as np

# Матрица стоимости перевозок
costs = np.array([[500, 1000, 900],
                  [600, 1100, 900],
                  [400, 1000, 900]])

# Объёмы поставщиков
supply = [1000, 1500, 700]

# Потребности потребителей
demand = [1200, 1000, 1000]

# Метод наименьшей стоимости
def least_cost_method(costs, supply, demand):
    plan = np.zeros_like(costs)
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        i, j = np.unravel_index(np.argmin(costs), costs.shape)
        amount = min(supply[i], demand[j])
        plan[i, j] = amount
        supply[i] -= amount
        demand[j] -= amount
        costs[i, j] = np.inf
    return plan

# Целевая функция
def calculate_objective(plan, costs):
    return np.sum(plan * costs)

# Решение
plan = least_cost_method(costs, supply, demand)
objective_value = calculate_objective(plan, costs)

print("Опорный план:\n", plan)
print("Целевая функция F =", objective_value)
