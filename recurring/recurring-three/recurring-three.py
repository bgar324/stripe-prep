def reconcile(invoices, payments):
  ans = {
    "accepted": [],
    "excess": [],
    "unknown_invoice": [],
    "remaining_balances": {
        ...
    }
  }
  # invoice_id -> [due_date, amount]
  
  invoice_dict = {}
  for invoice in invoices:
    # "invoiceA,2026-01-10,1000"
    invoice_id, due_date, amount = invoice.split(',')
    amount = int(amount)
    # since invoice_id's are unique
    invoice_dict[invoice_id] = [due_date, amount]

  # iterate over payments checking existence then writing string
  for payment in payments:
    # "payment1,1000,Paying off: invoiceA"
    # to deal with Paying off: invoiceA use lstrip()
    payment_id, amount, raw_memo = payment.split(',')
    amount = int(amount)
    # raw_memo = Paying off: invoiceA
    memo = raw_memo.split(':')[1].lstrip()

    if memo in invoice_dict:
      expected = invoice_dict[memo][1]
      if amount <= expected:
        ans["accepted"].append(payment_id)
        invoice_dict[memo][1] -= amount
      # at this point, expected is strictly greater than amount and shouldn't be considered
      else:
        ans["excess"].append(payment_id)
    else:
      ans["unknown_invoice"].append(payment_id)

  for key, value in invoice_dict.items():
    invoice_id = key
    amount = value[1]
    ans["remaining_balances"][invoice_id] = amount

  return ans

  '''
  time: O(length of invoices + length of payments) => O(L + P)
  space: O(L)
  '''