def merchant_totals(csv_text):
  ans = {
    "totals" : {},
    "conflicts" : []
  }

  raw = {}
  mapping = {}
  
  lines  = csv_text.splitlines()
  
  for line in lines[1:]:
    record_type, payment_id, merchant_id, amount, currency, status = line.split(',')
    if payment_id not in raw:
       raw[payment_id] = line
       if record_type == "payment":
         mapping[payment_id] = merchant_id
    elif raw[payment_id] != line:
      ans["conflicts"].append(payment_id)
  
  for key, value in raw.items():
    record_type, payment_id, merchant_id, amount, currency, status = value.split(',')
    amount = int(amount)
    if status == "succeeded":
      if record_type == "payment":
        if merchant_id in ans["totals"]:
          ans["totals"][merchant_id] += amount
        else:
          ans["totals"][merchant_id] = amount
    
      elif record_type == "refund":
        original_payment_id = merchant_id
        original_merchant = mapping[original_payment_id]
    
        ans["totals"][original_merchant] = max(ans["totals"].get(original_merchant, 0) - amount, 0)
        
  return ans