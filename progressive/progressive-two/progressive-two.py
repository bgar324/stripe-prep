def endpoint_stats(lines, min_requests):
  ans = {}

  # request_id -> [endpoint, error_count, latency_ms]
  request_metrics = {}

  for line in lines:
    timestamp, request_id, endpoint, status, latency_ms = line.split('|')

    status = int(status)
    latency_ms = int(latency_ms)

    is_error = 500 <= status <= 599
    curr_error = 1 if is_error else 0

    # Remove previous contribution
    if request_id in request_metrics:
      prev_endpoint, prev_error, prev_latency = request_metrics[request_id]

      prev_request_count, prev_error_count, prev_total_latency = ans[prev_endpoint]

      ans[prev_endpoint] = [
        prev_request_count - 1,
        prev_error_count - prev_error,
        prev_total_latency - prev_latency
      ]

      if ans[prev_endpoint] == [0, 0, 0]:
        del ans[prev_endpoint]

    # Add current contribution
    if endpoint not in ans:
      ans[endpoint] = [0, 0, 0]

    request_count, error_count, total_latency = ans[endpoint]

    ans[endpoint] = [
      request_count + 1,
      error_count + curr_error,
      total_latency + latency_ms
    ]

    request_metrics[request_id] = [
      endpoint,
      curr_error,
      latency_ms
    ]

  best_endpoint = None
  best_average = -1

  for endpoint, metrics in ans.items():
    req_count, err_count, total_latency = metrics

    if req_count >= min_requests:
      average_latency = total_latency / req_count

      if (
        average_latency > best_average
        or (
          average_latency == best_average
          and (best_endpoint is None or endpoint < best_endpoint)
        )
      ):
        best_average = average_latency
        best_endpoint = endpoint

  return {
    "stats": ans,
    "highest_average_latency_endpoint": best_endpoint
  }