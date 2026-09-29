def calculate_fees(csv_text, merchant_overrides):
  def calculate_card_fee(amount, percent, fixed):
    return round((amount * percent) + fixed)

  def calculate_bank_fee(amount, percent, max_fee):
    return min(max_fee, round(amount * percent))
  records = csv_text.splitlines()[1:]

  ans = {}

  for record in records:
    id,merchant_id,amount,currency,country,provider,type,status = record.split(',')
    # tx1,m1,1000,usd,US,card,payment,succeeded

    amount = int(amount)
    
    is_card = provider == "card"
    is_bank = provider == "bank"
    is_us = country == "US"
    valid = status == "succeeded" and type == "payment"
    has_override = merchant_id in merchant_overrides and provider in merchant_overrides[merchant_id]

    if valid:
      fee = 0
      if has_override:
        if is_card:
          percent = merchant_overrides[merchant_id]["card"]["percent"]
          fixed = merchant_overrides[merchant_id]["card"]["fixed"]
          fee = calculate_card_fee(amount, percent, fixed)
        elif is_bank:
          percent = merchant_overrides[merchant_id]["bank"]["percent"]
          max_fee = merchant_overrides[merchant_id]["bank"]["max_fee"]
          fee = calculate_bank_fee(amount, percent, max_fee)
      else:
        if is_card:
          if is_us:
            fee = calculate_card_fee(amount, 0.029, 30)
          else:
            fee = calculate_card_fee(amount, 0.039, 30)
        elif is_bank:
          fee = calculate_bank_fee(amount, 0.008, 500)
      ans[merchant_id] = ans.get(merchant_id, 0) + fee

  return ans