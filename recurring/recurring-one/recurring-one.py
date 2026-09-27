def calculate_shipping(order, shipping_rates):
  ans = 0
  
  country = order["country"]
  items = order["items"]

  rates = shipping_rates[country]

  for item in items:
    product = item["product"]
    quantity = item["quantity"]

    tiers = rates[product]
    
    for tier in tiers:
      pricing_type = tier["pricing_type"]
      if quantity == 0:
        break
      
      tier_price = tier["price"]
      

      # if tier["max"] == None and pricing_type == "fixed":
      #   ans += tier_price
      # else:
      #   ans += quantity * tier_price

      if tier["max"] is None:
          tier_capacity = quantity
      else:
          tier_capacity = tier["max"] - tier["min"] + 1
      
      units_in_tier = min(quantity, tier_capacity)

      if pricing_type == "fixed" and quantity > 0:
        ans += tier_price
      elif pricing_type == "incremental":
        ans += units_in_tier * tier_price
      quantity -= units_in_tier

  return ans