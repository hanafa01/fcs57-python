class FinanceManager:
    def __init__(self):
        self.salary = 0.0
        self.month = ""
        self.expenses = {}

    def input_salary_and_month(self):
        try:
            self.salary = float(input("Enter your monthly salary: "))
            self.month = input("Enter the month: ")
            print(f"Salary of ${self.salary} recorded for {self.month}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")

    def add_expense_category(self):
        while True:
            category = input("Enter the expense category (or type 'done' to finish): ").strip()
            if category.lower() == 'done':
                break
            try:
                percentage = float(input(f"Enter the percentage allocated to {category}: "))
                if percentage <= 0 or percentage > 100:
                    print("Percentage must be between 0 and 100.")
                    continue
                if sum(self.expenses.values()) + percentage > 100:
                    print("Total expense percentages cannot exceed 100%.")
                    continue
                self.expenses[category] = percentage
            except ValueError:
                print("Invalid input. Please enter a numeric value for percentage.")

    def calculate_allocations(self):
        allocated_amounts = {category: (self.salary * percentage / 100) for category, percentage in self.expenses.items()}
        sorted_allocations = dict(sorted(allocated_amounts.items(), key=lambda x: x[1], reverse=True))
        
        total_expense = sum(allocated_amounts.values())
        remainder = self.salary - total_expense
        yearly_rent = allocated_amounts.get("Rent", 0) * 12
        yearly_electricity = allocated_amounts.get("Electricity", 0) * 12

        # Display allocations
        print("\nExpense Allocations:")
        for category, amount in sorted_allocations.items():
            print(f"Amount allocated to {category}: ${amount:.2f}")

        print(f"\nTotal expenses: ${total_expense:.2f}")
        print(f"Remainder of salary: ${remainder:.2f}")
        print(f"Yearly Rent: ${yearly_rent:.2f}")
        print(f"Yearly Electricity: ${yearly_electricity:.2f}")
        print(f"Total salary squared for fun: ${self.salary ** 2:.2f}")

        # Fun calculation with random amount (e.g., $50) divided by total allocated for savings
        if 'Savings' in allocated_amounts:
            savings_allocation = allocated_amounts['Savings']
            remaining_after_random = 50 / savings_allocation if savings_allocation > 0 else None
            if remaining_after_random:
                print(f"Remaining after dividing $50 by savings allocation: ${remaining_after_random:.2f}")
            else:
                print("No allocation for savings, skipping additional calculation.")
        else:
            print("Savings category not set, skipping additional calculation.")

# Example usage
manager = FinanceManager()
manager.input_salary_and_month()
manager.add_expense_category()
manager.calculate_allocations()
