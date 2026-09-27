# import math

def calculate_fees(csv_text, merchant_overrides):
  records = csv_text.splitlines()[1:]

  ans = {}
  US_RATE = 0.029
  NON_US_RATE = 0.039
  BANK_RATE = 0.008

  # tx1,m1,1000,usd,US,card,payment,succeeded
  # tx3,m2,500,usd,CA,bank,payment,failed

  for record in records:
    id_, merchant_id, amount, currency, country, provider, type, status = record.split(',')

    succeeded = status == "succeeded" and type == "payment"
    # check existence of merchant_id and provider in merchant_overrides
    has_override = merchant_id in merchant_overrides and provider in merchant_overrides[merchant_id]
    
    fee = 0
    
    if succeeded:
      if has_override:
        merchant_percent = merchant_overrides[merchant_id][provider]["percent"]
        if provider == "card":
          merchant_fixed = merchant_overrides[merchant_id][provider]["fixed"]
          fee = round((int(amount) * merchant_percent) + merchant_fixed)
        else:
          merchant_max_fee = merchant_overrides[merchant_id][provider]["max_fee"]
          fee = min(round(int(amount) * merchant_percent), merchant_max_fee)
      elif not has_override:
        if provider == "card":
          if country == "US":   
            fee = round((int(amount) * US_RATE) + 30)
          else:
            fee = round((int(amount) * NON_US_RATE) + 30)
        else:
          fee = min(round(int(amount) * BANK_RATE), 500)
        
      if merchant_id in ans:
        ans[merchant_id] += fee
      else:
        ans[merchant_id] = fee
    else:
      continue

  return ans