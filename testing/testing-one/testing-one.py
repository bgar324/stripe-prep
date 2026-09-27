# Read Part 1 of testing-one.txt first.
# Write your route_tickets function below.


# Below your function, add input variables and a call that prints the result.
# Click Run, then compare the output with the answer you expected.
# Add your own check before moving to the next part.

def route_tickets(tickets, rules):
  ans = []
  # topic -> {ticket_id, team}

  # i want to preprocess rules so there is a mapping from topic to team

  cleaned_up_rules = {}
  for i, rule in enumerate(rules):
    rule_topic = rule["topic"]
    rule_team = rule["team"]
    rule_country = rule["country"]
    rule_priority = rule["priority"]

    key = (rule_topic, rule_country)
    existence = key in cleaned_up_rules

    if existence:
      prev =  cleaned_up_rules[key]["priority"]
      if prev < rule_priority:
        cleaned_up_rules[key]["priority"] = rule_priority
        cleaned_up_rules[key]["team"] = rule_team
        cleaned_up_rules[key]["index"] = i
      else:
        continue
    # doesnt exist
    else:
      cleaned_up_rules[key] = {
        "team" : rule_team,
        "priority" : rule_priority,
        "index" : i
      }
      

  # since we only want the first occurence of topic, we can take advantage of that

    
  for ticket in tickets:
    ticket_id = ticket["ticket_id"]
    topic = ticket["topic"]
    country = ticket["country"]

    key_country = (topic, country)
    key_asterisk = (topic, "*")
    country_exists = key_country in cleaned_up_rules
    asterisk_exists = key_asterisk in cleaned_up_rules

    if not country_exists and not asterisk_exists:
      ans.append({
        "ticket_id" : ticket_id,
        "team" : None
      })
    else:
      if country_exists and not asterisk_exists:
        ans.append({
          "ticket_id" : ticket_id,
          "team" : cleaned_up_rules[key_country]["team"]
        })
      elif not country_exists and asterisk_exists:
        ans.append({
          "ticket_id" : ticket_id,
          "team" : cleaned_up_rules[key_asterisk]["team"]
        })
      # both exist
      else:
        country_priority = cleaned_up_rules[key_country]["priority"]
        asterisk_priority = cleaned_up_rules[key_asterisk]["priority"]
        if country_priority == asterisk_priority:
          country_index = cleaned_up_rules[key_country]["index"]
          asterisk_index = cleaned_up_rules[key_asterisk]["index"]
          if country_index < asterisk_index:
            ans.append({
              "ticket_id" : ticket_id,
              "team" : cleaned_up_rules[key_country]["team"]
            })
          else:
            ans.append({
              "ticket_id" : ticket_id,
              "team" : cleaned_up_rules[key_asterisk]["team"]
            })
        elif country_priority > asterisk_priority:
          ans.append({
            "ticket_id" : ticket_id,
            "team" : cleaned_up_rules[key_country]["team"]
          })
        else:
          ans.append({
            "ticket_id" : ticket_id,
            "team" : cleaned_up_rules[key_asterisk]["team"]
          })

  return ans

# tickets = [
#     {"ticket_id": "t1", "topic": "billing", "country": "US"},
#     {"ticket_id": "t2", "topic": "payouts", "country": "GB"},
#     {"ticket_id": "t3", "topic": "billing", "country": "GB"},
#     {"ticket_id": "t4", "topic": "login", "country": "US"}
# ]

tickets = [
    {"ticket_id": "t1", "topic": "billing", "country": "US"},
    {"ticket_id": "t2", "topic": "billing", "country": "GB"}
]

rules = [
    {"topic": "billing", "team": "billing-general", "country": "*", "priority": 10},
    {"topic": "billing", "team": "billing-us", "country": "US", "priority": 20},
    {"topic": "payouts", "team": "payouts-general", "country": "*", "priority": 5}
]

print(route_tickets(tickets, rules))