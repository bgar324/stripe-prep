def subscription_states(events):
  transition = {
    "created" : "active",
    "paused" : "paused",
    "resumed" : "active",
    "canceled" : "canceled"
  }

  valid = {
    "active" : ["paused", "canceled"],
    "paused" : ["resumed", "canceled"]
  }

  ans = {}
  rejected = []

  for event in events:
    subscription_id = event["subscription_id"]
    event_type = event["type"]
    
    prev = ans.get(subscription_id)
    
    if prev is None and type == "created":
      ans[subscription_id] = transition[type]
    elif event_type in valid.get(prev, []):
      ans[subscription_id] = transition[type]
    else:
      rejected.append(event)
      
  return (ans, rejected)