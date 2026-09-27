def compute_payments(payments):
  ans = {}
  
  for payment in payments:
    merchant_id = payment["merchant_id"] 
    amount = payment["amount"] 
    currency = payment["currency"] 
    status = payment["status"]

    key = (merchant_id, currency)
    
    if status == "succeeded" and key in ans:
      ans[key] += amount
    elif status == "succeeded" and key not in ans: 
      ans[key] = amount

  return ans