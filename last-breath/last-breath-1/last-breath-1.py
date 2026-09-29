def calculate_shipping(order, shipping_rates):
  def calculate_tier_cost(tier, quantity):
    tier_size = (
      quantity
      if tier["max"] is None
      else min(quantity, tier["max"] - tier["min"] + 1)
    )

    if tier["pricing_type"] == "incremental":
      cost = tier_size * tier["price"]
    else:
      cost = tier["price"]

    return cost, tier_size

  country = order["country"]
  items = order["items"]
  shipping_costs = shipping_rates[country]

  total_cost = 0

  for item in items:
    product = item["product"]
    remaining_quantity = item["quantity"]
    tiers = shipping_costs[product]

    for tier in tiers:
      if remaining_quantity == 0:
        break

      tier_cost, units_used = calculate_tier_cost(
        tier,
        remaining_quantity
      )

      total_cost += tier_cost
      remaining_quantity -= units_used

  return total_cost