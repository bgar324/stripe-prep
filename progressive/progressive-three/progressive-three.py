def customer_states(events):
    customers = {}
    invalid = []
    mapping = {}

    for i, event in enumerate(events):
        customer_id = event["customer_id"]
        event_type = event["type"]

        if customer_id not in customers:
            if event_type == "created":
                customers[customer_id] = {
                    "status": "active",
                    "email": event.get("email")
                }
            else:
                invalid.append(i)

            continue

        customer = customers[customer_id]
        status = customer["status"]

        if status == "deleted" or status == "merged":
            invalid.append(i)
            continue

        if event_type == "created":
            invalid.append(i)
            continue

        if event_type == "reactivated":
            if status != "suspended":
                invalid.append(i)
            else:
                customer["status"] = "active"
            continue

        if event_type == "email_updated":
            customer["email"] = event["email"]
            continue

        if event_type == "suspended":
            customer["status"] = "suspended"
            continue

        if event_type == "deleted":
            customer["status"] = "deleted"
            continue

        if event_type == "merged":
            merge_into = event["into"]

            if merge_into == customer_id:
                invalid.append(i)
                continue

            if merge_into not in customers:
                invalid.append(i)
                continue

            target_status = customers[merge_into]["status"]

            if target_status == "deleted" or target_status == "merged":
                invalid.append(i)
                continue

            mapping[customer_id] = merge_into
            customer["status"] = "merged"
            continue

        invalid.append(i)

    for customer_id in mapping:
        final_customer = mapping[customer_id]

        while final_customer in mapping:
            final_customer = mapping[final_customer]

        mapping[customer_id] = final_customer

    return customers, invalid, mapping