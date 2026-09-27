def error_counts(lines):
  ans = {}
  
  for line in lines:
    timestamp, service, level, message = line.split('|', 3)
    if level == "ERROR":
      if service in ans:
        ans[service] += 1
      else:
        ans[service] = 1

  return ans