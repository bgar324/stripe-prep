def export_transactions(fetch_page):
  transactions = {}
  cursor = None
  ans = []

  conflicts = set()
  seen = set()

  while True:
    page = fetch_page(cursor)

    trans = page["transactions"]
    next_cursor = page["next_cursor"]

    for tran in trans:
      tran_id = tran["id"]
      if tran_id in transactions and transactions[tran_id] != tran:
        conflicts.add(tran_id)
      elif tran_id in transactions and transactions[tran_id] == tran:
        continue
      else:
        transactions[tran_id] = tran
        ans.append(tran)

    if next_cursor == None:
      break

    if next_cursor in seen:
      return {
        "transactions" : ans,
        "conflicts" :  conflicts,
        "cursor_cycle_detected" : True
      }
    else:
      seen.add(next_cursor)
      cursor = next_cursor

  return {
    "transactions" : ans,
    "conflicts" :  conflicts,
    "cursor_cycle_detected" : False
  }

  '''
  part two asks:
    transaction IDs can appear more than once, only include the first one in the answer

    if there is a conflict, append the conflict transaction id to a conflict set, then return that set.
  '''