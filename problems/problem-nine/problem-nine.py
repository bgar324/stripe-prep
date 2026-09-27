def repeated_fingerprints(payments, threshold):
  freq = {} # counting frequency of each fingerprint
  # maps fingerprint -> frequency

  payment_to_fingerprint = {}
  payment_ids = []
  # maps fingerprint -> payment
  for payment in payments:
    payment_id = payment["payment_id"]
    fingerprint = payment["fingerprint"]

    if fingerprint in freq:
      freq[fingerprint] += 1
      payment_to_fingerprint[fingerprint].append(payment_id)
    else:
      freq[fingerprint] = 1
      payment_to_fingerprint[fingerprint] = [payment_id]
    

  for key, value in freq.items():
    if value >= threshold:
      payment_id_arr = payment_to_fingerprint[key]
      for payment in payment_id_arr:
        payment_ids.append(payment)

  return payment_ids