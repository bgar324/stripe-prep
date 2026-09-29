def select_fields(records, fields):
  ans = []

  for record in records:
    temp = {}
    for field in fields:
      paths = field.split('.')
      curr = record
      for path in paths:
        if not isinstance(curr, dict) or path not in curr:
          curr = None
          break
        curr = curr.get(path)
      temp[field] = curr
    ans.append(temp)
        

  return ans