def find_flagged_merchants(events, thresholds, min_charges):
  ans = []
  freq = {} # occurence of fraudulent charges
  total_charges = {} # total charges
  flagged = set()

  for event in events:
    type, charge_id, merchant_id, amount, is_fraudulent = event.split(',')
    is_fraudulent = is_fraudulent == "true"
    total_charges[merchant_id] = total_charges.get(merchant_id, 0) + 1
    net_charges = total_charges[merchant_id]
    freq[merchant_id] = freq.get(merchant_id, 0)
    merchant_threshold = thresholds[merchant_id]

    if is_fraudulent:
      freq[merchant_id] = freq[merchant_id] + 1

    if net_charges >= min_charges:
      if freq[merchant_id] / total_charges[merchant_id] >= merchant_threshold and merchant_id not in flagged:
        flagged.add(merchant_id)
        ans.append(merchant_id)

  return ans