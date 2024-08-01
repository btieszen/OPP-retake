# updates the buget on a specific expense


def update(category_budget):
 
    print(category_budget)
    expense = input("What is the expense you would like to update: ")
    
    if expense in category_budget:
        new_budget=input("What would you like the new budget to be: ")
        budget_new=int(new_budget)
        total_new= {expense:budget_new}
        category_budget.update(total_new)  
        print(category_budget)
    else:
        print((expense)," is not an expense")