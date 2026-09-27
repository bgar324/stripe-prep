def build_sessions(timestamps, gap):
  ans = []
  '''
  intuition -- 
  ingest the first timestamp, creating an array, then continue rightward until top + gap < curr.
  at that point append that array u created into ans
  '''
  i = 0
  while i < len(timestamps):
    curr = [timestamps[i]]

    while i + 1 < len(timestamps) and timestamps[i + 1] <= curr[-1] + gap:
      curr.append(timestamps[i + 1])
      i += 1

    ans.append({
      "start_time" : curr[0],
      "end_time" : curr[-1],
      "number_of_events" : len(curr)
    })
    i += 1

  return ans