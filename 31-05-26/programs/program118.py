def get_budgets(lst):
    total_budgets=sum(person['budget'] for person in lst) 
    return total_budgets
budgets1=[
    {'name': 'Alice', 'budget': 1000},
    {'name': 'Bob', 'budget': 1500},
    {'name': 'Charlie', 'budget': 2000}
]
print(get_budgets(budgets1))
budgets2=[
    {'name': 'David', 'budget': 500},   
    {'name': 'Eve', 'budget': 1200},    
    {'name': 'Frank', 'budget': 800}
]
print(get_budgets(budgets2))
