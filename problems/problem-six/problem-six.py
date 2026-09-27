from collections import deque

def allowed_requests(timestamps, limit, window):
  ans = []
  queue = deque()

  for timestamp in timestamps:
    while queue and queue[0] < timestamp - window + 1:
      queue.popleft()

    if len(queue) < limit:
      queue.append(timestamp)
      ans.append(True)
    else:
      ans.append(False)

  return ans