def unique_events(events):
  seen = {}
  ans = []
  for event in events:
    event_id = event["event_id"]
    event_type = event["type"]
    event_created = event["created"]

    if event_id not in seen or event_created > seen[event_id]["created"] + 86400:
      seen[event_id] = event
      ans.append(event)
    else:
      continue

  return ans