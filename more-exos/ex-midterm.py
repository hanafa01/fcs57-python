class FinanceManager:
    def __init__(self):
        self.salary = 3000
        self.month = "October"
        self.expenses = {
            'Savings': 20,
            'Rent': 40,
            'Electricity': 10
        }

    def input_store_salary_month(self):
        try:
            self.salary = float(input("Enter your salary: "))
            self.month = input("Enter your months' salary: ")

            print(f"Salary is {self.salary} for {self.month}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")
    
    def add_expense(self):
        category = input("Enter expense category name (eg savings, rent, electricity): ")

        percentage = float(input(f"Enter the percentage for {category}: "))

        if percentage <= 0 or percentage > 100:
            print("Percentage must be between 0 and 100.")
            return
        
        if sum(self.expenses.values()) + percentage > 100:
            print("Total expense percentages cannot exceed 100%.")
            return

        self.expenses[category] = percentage

    def calculate_allocations(self):
        allocated_amount = {}

        for x in self.expenses:
            a = self.expenses[x] / 100 * self.salary
            allocated_amount[x] = a
            print(f"Amount allocated to {x}: ${a}")

        totalExpense = sum(allocated_amount.values())
        remainder = self.salary - totalExpense
        yearly_rent = allocated_amount['Rent'] * 12
        yearly_electricity = allocated_amount['Electricity'] * 12
        # for category, allocatedamount in allocated_amount.items():
        
        print(f"\nTotal expenses: ${totalExpense:.2f}")
        print(f"Remainder of salary: ${remainder:.2f}")
        print(f"Yearly Rent: ${yearly_rent:.2f}")
        print(f"Yearly Electricity: ${yearly_electricity:.2f}")
        print(f"Total salary squared for fun: ${self.salary ** 2:.2f}")

manager = FinanceManager()
# manager.input_salary_and_month()
# manager.add_expense_category()
manager.calculate_allocations()