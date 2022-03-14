from collections import deque

pizza_orders = deque([int(el) for el in input().split(', ')])
employees_capacities = [int(el) for el in input().split(', ')]
total_pizzas = 0

while pizza_orders and employees_capacities:
    current_order = pizza_orders.popleft()
    current_employee = employees_capacities.pop()

    if current_order <= 0:
        employees_capacities.append(current_employee)
        continue

    if current_order > 10:
        employees_capacities.append(current_employee)
        continue

    if current_order <= current_employee:
        total_pizzas += current_order
    else:
        made_pizzas = current_employee
        total_pizzas += made_pizzas
        current_order -= made_pizzas
        pizza_orders.appendleft(current_order)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    employees_capacities = [str(el) for el in employees_capacities]
    print(f'Employees: {", ".join(employees_capacities)}')
else:
    print('Not all orders are completed.')
    pizza_orders = [str(el) for el in pizza_orders]
    print(f'Orders left: {", ".join(pizza_orders)}')
