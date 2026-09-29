def process_events(servers, events):
  ans = []
  server_capacities = {}
  server_counts = {}
  user_to_server = {}
  preferred_server = {}

  for server in servers:
    server_id = server["server_id"]
    server_counts[server_id] = 0
    server_capacities[server_id] = server["capacity"]

  for event in events:
    action, user_id = event.split(" ")

    if action == "CONNECT":
      if user_id in user_to_server:
        continue

      has_preferred_server = (
        user_id in preferred_server and
        preferred_server[user_id] in server_counts
      )

      # Try sticky server first
      if has_preferred_server:
        preferred = preferred_server[user_id]

        if server_counts[preferred] < server_capacities[preferred]:
          server_id = preferred
        else:
          server_id = None
      else:
        server_id = None

      # Preferred server didn't work, so find least-loaded
      if server_id is None:
        available_servers = [
          server_id
          for server_id in server_counts
          if server_counts[server_id] < server_capacities[server_id]
        ]

        if available_servers:
          server_id = min(
            available_servers,
            key=lambda server_id: (server_counts[server_id], server_id)
          )

      # No server has capacity
      if server_id is None:
        ans.append(None)
        continue

      user_to_server[user_id] = server_id
      server_counts[server_id] += 1
      ans.append(server_id)

    elif action == "DISCONNECT":
      if user_id not in user_to_server:
        continue

      server_id = user_to_server[user_id]
      del user_to_server[user_id]

      server_counts[server_id] -= 1
      preferred_server[user_id] = server_id

  return ans 