def delivery_results(attempts, current_time, timeout):
  '''
  part one thinking:
    iterate through attempts
    for each event_id, check if it exists in attempts, if it does then update attempts for that event_id by one. then check if the status == 2xx.
    if it is, then set succeeded == True
    if it doesnt exist, then create an event_id key, mapping to a dict starting at attempts = 1 and check status. if its 2xx then say True if not False
  '''

  ans = {}
  ignored_attempts = 0
  stuck_events = []
  
  for attempt in attempts:
    event_id = attempt["event_id"]
    status = attempt["status"]
    timestamp = attempt["timestamp"]

    status_number = status // 100
    success = status_number == 2

    # top level check if alr succeded. if it did then continue

    if event_id in ans and ans[event_id]["succeeded"] == True:
      ignored_attempts += 1
      continue
    
    if event_id in ans:
      ans[event_id]["attempts"] += 1
      ans[event_id]["succeeded"] = success
      ans[event_id]["timestamp"] = timestamp
    # so event_id isn't in ans.
    else:
      if success:
        ans[event_id] = {
          "attempts" : 1,
          "succeeded" : True,
          "timestamp" : timestamp
        }
      # did not succeed
      else:
        ans[event_id] = {
          "attempts" : 1,
          "succeeded" : False,
          "timestamp" : timestamp
        }

  for key, value in ans.items():
      # a event_id is considered stuck if it hasn't succeeded and its timestamp is greater than timeout - current_time

    success = value["succeeded"] == True
    stuck = not success and current_time - value["timestamp"] >= timeout 

    if stuck:
      stuck_events.append(key)
    else:
      continue

  stuck_events.sort(key=lambda event_id: (ans[event_id]["timestamp"], event_id))
  
  return ans, ignored_attempts, stuck_events