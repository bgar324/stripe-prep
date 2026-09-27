def process_requests(requests):
  '''
  iterate over requests, mapping the key to the payload
  '''
  idempotency_payloads = {}
  ans = []
  for request in requests:
    idempotency_key = request["idempotency_key"]
    payload = request["payload"]
    
    seen = idempotency_key in idempotency_payloads
    
    if not seen:
      idempotency_payloads[idempotency_key] = payload
      ans.append("processed")
      
    elif seen and idempotency_payloads[idempotency_key] != payload:
      ans.append("conflict")
      
    else:
      ans.append("duplicate")

  return ans