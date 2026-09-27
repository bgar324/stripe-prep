def invoice_total(items):
  total = 0
  for item in items:
    unit_amount = item["unit_amount"]
    quantity = item["quantity"]

    is_discount = item.get("type") == "discount"
    
    if is_discount:
      total -= unit_amount * quantity
    else:
      total += unit_amount * quantity

  return max(total, 0)