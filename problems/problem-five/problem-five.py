def fetch_all_customers(fetch_page):
  ans = []
  page = fetch_page(None)
  seen = set()
  cursors_seen = set()
  while True:
    data = page["data"]
    for d in data:
      cus = d["id"]
      if cus in seen:
        continue
      ans.append(cus)
      seen.add(cus)
    if page["next_cursor"] == None or page["next_cursor"] in cursors_seen:
      break
    else:
      cursors_seen.add(page["next_cursor"])
      page = fetch_page(page["next_cursor"])

  return ans