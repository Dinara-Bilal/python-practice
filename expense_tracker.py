expense= []

def add_expense(item,amoount):
   expenses.append({"item": item, "amount": amount})
  print{f"Added: {item}-Rs.{amount}")

def total_expense():
  total = sum(exp["amount'] for exp in expenses)
              return total

              def show_expenses():
              print("\n--- Expense Report---")
              for exp in expenses:
              print(f"{exp['item']}: Rs.{exp['amount']}")
              print(f"Total: Rs.{total_expense()}")

              add_expense("Books", 1500)
              add_expense("Internet",2000)
              add_expense("Food",1000)

              show_expenses()
