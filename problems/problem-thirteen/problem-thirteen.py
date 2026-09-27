def expired_holds(holds, current_time):
  ans = []
  for hold in holds:
    hold_id = hold["id"]
    created = hold["created"]
    ttl = hold["ttl"]
    captured_at = hold.get("captured_at", None)
    expiration_time = created + ttl

    is_expired = current_time >= expiration_time

    if captured_at != None and captured_at < expiration_time:
      continue
    elif is_expired:
      ans.append(hold_id)

  return ans