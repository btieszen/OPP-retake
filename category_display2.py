#displays all catagories

def __init__(self,category_name,sum1):
    self.__category_name=category_name
    self.__sum1=sum1


def display_category_summary(category_budget):
    
    print("Your expenses and amount are: ")
    print(category_budget)
    for categories in category_budget.values():
        sum1 =sum(category_budget[item] for item in category_budget)
    print(" The total expense amount is",sum1 )