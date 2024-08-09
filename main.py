#. Encapsulation in Personal Budget Management
#Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.
    #Task 1: Define Budget Category Class Create a class `BudgetCategory` 
        # with private attributes for category name and allocated budget. -
        # Initialize these attributes in the constructor.
    #Task 2: Implement Getters and Setters -
        # Write getter and setter methods for both the category name and the allocated budget.
        # - Ensure that the setter methods include validation (e.g., budget should be a positive number).
    #Task 3: Add Budget Functionality Implement a method to add expenses to a category
        # and adjust the budget accordingly. -
        # Validate the expense amount before making deductions from the budget.
    #Task 4: Display Budget Details Create a method to display the details of a budget category,
        # including the name, allocated budget, and remaining budget after expense




import budget
import category_display
import update_expense
import expense
category_budget =[{'Food':500,'Entertainment':200,'Bills':2000}]
class BudgetCategory:
 
    def __init__(self,budget = 0):
        self._budget=budget
        
    def get_budget(self):
        return self._budget
    def set_budget(self,x):
        self._budget = x 
    


def monthly_budget(category_budget):
    budget.month_budget(category_budget)
       
def add_expense(category_budget):
    expense.new_expense(category_budget)
    
def display_category_summary(category_budget):
    category_display.display_category_summary(category_budget)
       
       
def main():
    category_budget ={'Food':500,'Entertainment':200,'Bills':2000}
    while True:
        print("\nWelcome to your monthly budget")
        print("1: Enter Monthly Budget amount and see how much money is left")
        print("2: See all expenses and their total amount")
        print("3: Add new expense and their budget")
        print("4: Change the budget on an existing expense")
        print("5: Exit")
        category_name=input("Please make a selection:  ")
        if category_name =="5":
            print("Goodbye")
            break
        try:
            if category_name =="1":
                monthly_budget(category_budget)
                    
            elif category_name =="2":
                display_category_summary(category_budget)
                  
            elif category_name =="3":
                add_expense(category_budget)
                
            elif category_name =="4":
                update_expense.update(category_budget)
                        
        except Exception as e:
            print(f"Please enter a number between 1-5: {e}")
                    
main()
    
    





