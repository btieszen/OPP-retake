
category_budget ={'Food':500,'Entertainment':200,'Bills':2000}
def month_budget(category_budget):      
    monthly=category_budget
    month=input("What is your total monthly budget: ")
    #monthly.set_budget(month)
    print("Your monthly budget is ",(month))
    for budgets in category_budget.values():
        sum_total =sum(category_budget[item] for item in category_budget)
    print(" The total expense amount is",sum_total )
    total= int(month)-int(sum_total)
    if total <= 0:
        print("You are",total,", you spent to much money this month!!!")
    else:
       print("You have ",total, "left over")