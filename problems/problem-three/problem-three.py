def build_balance_history(transactions):
  '''
  so basically credit means add on and debit means subtract?
  '''
  ans = []
  rejected_transactions = []
  balance = 0
  for i, val in enumerate(transactions):
    type = val["type"]
    amount = val["amount"]

    if type == "debit" and balance - amount < 0:
      rejected_transactions.append(i)
    elif type == "credit":
      balance += amount
    else:
      balance -= amount

    ans.append(balance)

  return (ans, rejected_transactions)