def reconcile(invoices, payments):
  '''
  preprocess to get into a dict for fast lookup
  '''

  ans = {
    "accepted": [],
    "excess": [],
    "unknown_invoice": [],
    "remaining_balances": {}
  }

  invoice_dict = {}

  for invoice in invoices:
   invoice_id, _, amount = invoice.split(',')
   amount = int(amount)

   invoice_dict[invoice_id] = {
     # "due_date" : due_date,
     "amount" : amount
   }

  for payment in payments:
    payment_id, amount, memo = payment.split(',')
    amount = int(amount)
    invoice_id = memo.split(":")[1].lstrip()

    if invoice_id not in invoice_dict:
      ans["unknown_invoice"].append(payment_id)
    else:
      expected_payment = invoice_dict[invoice_id]["amount"]
      if amount <= expected_payment:
        ans["accepted"].append(payment_id)
        invoice_dict[invoice_id]["amount"] -= amount
      else:
        ans["excess"].append(payment_id)

  for key in invoice_dict:
    ans["remaining_balances"][key] = invoice_dict[key]["amount"]
    
  return ans