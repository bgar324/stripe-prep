def reconcile(stripe_records, bank_records):
  '''
  pointers
  '''

  stripe_records_length = len(stripe_records)
  bank_records_length = len(bank_records)
  
  # if stripe_records_length == 0 and bank_records_length != 0:
  #   return {
  #     "matched" : [],
  #     "amount_mismatch" : [],
  #     "missing_from_stripe" : []
  #   }


  '''
  in the main loop compare each curr
  '''

  ans = {
    "matched": [],
    "amount_mismatch": [],
    "missing_from_stripe": [],
    "missing_from_bank": [],
  }

  stripe_map ={}
  bank_map = {}

  for record in stripe_records:
    id = record["id"]
    amount = record["amount"]
    if id in stripe_map:
      stripe_map[id] += amount
    else:
      stripe_map[id] = amount


  for record in bank_records:
    id = record["id"]
    amount = record["amount"]
    if id in bank_map:
      bank_map[id] += amount
    else:
      bank_map[id] = amount

  for payment_id, amount in stripe_map.items():
    if payment_id in bank_map and bank_map[payment_id] == amount:
      ans["matched"].append(payment_id)
    elif payment_id in bank_map and bank_map[payment_id] != amount:
      ans["amount_mismatch"].append(payment_id)
    else:
      ans["missing_from_bank"].append(payment_id)

  for payment_id, amount in bank_map.items():
    if payment_id not in stripe_map:
      ans["missing_from_stripe"].append(payment_id)

  for payment_id, arr in ans.items():
    arr.sort()

  return ans