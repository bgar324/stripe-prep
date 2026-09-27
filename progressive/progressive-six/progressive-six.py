def flag_velocity(payments, max_payments, window):
    ans = []
    app = {}

    for payment in payments:
        fingerprint = payment["fingerprint"]
        timestamp = payment["timestamp"]

        if fingerprint not in app:
            app[fingerprint] = []

        arr = app[fingerprint]

        while arr and arr[0] < timestamp - window + 1:
            arr.pop(0)

        if len(arr) >= max_payments:
            ans.append(True)
        else:
            ans.append(False)
            arr.append(timestamp)

    return ans