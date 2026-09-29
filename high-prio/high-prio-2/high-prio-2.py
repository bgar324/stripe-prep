def find_flagged_merchants(events, thresholds, min_charges):
  flagged_merchants = set()
  freq = {}
  ans = []
  occurences = {}
  charge_to_merchant = {}

  for event in events:
    split = event.split(',')
    type = split[0]
    is_fraudulent = split[4]
    is_fraudulent = is_fraudulent == "true"

    if type == "CHARGE":
      type, event_id, merchant_id, amount, is_fraudulent = event.split(',')
      occurences[merchant_id] = occurences.get(merchant_id, 0) + 1
      if is_fraudulent:
        charge_to_merchant[event_id] = merchant_id
        freq[merchant_id] = freq.get(merchant_id, 0) + 1
      if occurences[merchant_id] >= min_charges:
        ratio = freq.get(merchant_id, 0) / occurences[merchant_id]
        if ratio >= thresholds[merchant_id] and merchant_id not in flagged_merchants:
          flagged_merchants.add(merchant_id)
          ans.append(merchant_id)
        else:
          continue
    elif type == "DISPUTE":
      charge_id = split[1]
      if charge_id not in charge_to_merchant:
        continue
      else:
        merchant_id = charge_to_merchant[charge_id]
        freq[merchant_id] -= 1
        del charge_to_merchant[charge_id]

  return ans

'''
for part two, keep a check of occurences and if occurences then geq min_charges then eval the ratio and equality
'''
'''
for part three, requires big shift
we need to map charge_id to the merchant_id
then have merchant_id count
'''