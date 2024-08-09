# add new expense and checks to see if over budget


def new_expense(category_budget):

    monthly_budget=input("What is your monthly budget: ")
    monthly=int(monthly_budget)
    new=input("What is the new expense you would like to add: ")
    new_budget= input("How much would you like to budget: ")
    for categories in category_budget.values():
            sum1 =sum(category_budget[item] for item in category_budget)
            new_budgets = int(new_budget)
            total_sum =sum1+new_budgets
    if monthly <= total_sum:
        print("Your new expensene will put you at zero or negative")
        answer= input("Do you want to continue to add(yes/no)")
        if answer =="yes": 
            total_new= {new:new_budgets}
            category_budget.update(total_new)  
            print((new)," has been added to ",(category_budget))
        else:
            print((new),"has not been added")
            print(category_budget)
    else:
        total_new= {new:new_budgets}
        category_budget.update(total_new)  
        print("Your update expenses are ",(category_budget))