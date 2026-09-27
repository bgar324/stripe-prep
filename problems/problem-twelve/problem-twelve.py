def processing_orders(transfers):
  # pre-process dependency count

  freq = {}
  dep = {}
  ans = []
  stack = []
  for transfer in transfers:
    transfer_id = transfer["id"]
    dependency = transfer["depends_on"]
    dep_count = len(dependency)

    freq[transfer_id] = dep_count
    
    for d in dependency:
      if d in dep:
        dep[d].append(transfer_id)
      else:
        dep[d] = [transfer_id]
    
    if dep_count == 0:
      stack.append(transfer_id)

  while len(stack) != 0:
    top = stack.pop()
    ans.append(top)

    for dependent in dep.get(top, []):
      freq[dependent] -= 1

      if freq[dependent] == 0:
        stack.append(dependent)

  if len(ans) < len(transfers):
    return "Error"
  else:
    return ans