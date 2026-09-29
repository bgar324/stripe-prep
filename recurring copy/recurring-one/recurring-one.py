def calculate_shipping(order, shipping_rates):
  total_cost = 0
  destination = order["country"]
  items = order["items"]
  product_rates = shipping_rates[destination]

  for item in items:
    product = item["product"]
    remaining_quantity = item["quantity"]
    tiers = product_rates[product]

    for tier in tiers:
      price_per_unit = tier["price"]
      pricing_type = tier["pricing_type"]

      if remaining_quantity == 0:
        break

      if tier["max"] is None:
        if pricing_type == "incremental":
          total_cost += remaining_quantity * price_per_unit
        else:
          total_cost +=  price_per_unit
        break

      tier_capacity = tier["max"] - tier["min"] + 1
      units_in_tier = min(remaining_quantity, tier_capacity)

      if pricing_type == "incremental":
        total_cost += units_in_tier * price_per_unit
      else:
        total_cost += price_per_unit

      remaining_quantity -= units_in_tier

  return total_cost