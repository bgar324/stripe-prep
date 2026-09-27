def perform_request(send_request, max_attempts):
  attempts = 0
  waits = []
  while True:
    response = send_request()
    status_number = response["status"]
    attempts += 1
    # return 2xx

    first_number = status_number // 100

    if first_number == 2:
      return (waits, response)
    # retry 429 or 5xx with a check first
    elif status_number == 429 or first_number == 5:
        if attempts < max_attempts:
            if status_number == 429 and "retry_after" in response:
                waits.append(response["retry_after"])
            continue
        else:
            return (waits, response)
    # if its a 4xx, do not retry and return final response
    else:
      return (waits, response)