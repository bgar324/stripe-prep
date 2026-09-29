def validate_businesses(csv_text):
  ans = {
    "valid" : [],
    "invalid" : []
  }

  onboarding_records = csv_text.splitlines()[1:]

  for onboarding_record in onboarding_records:
    business_id,name,country,business_type,tax_id,website = onboarding_record.split(',')


    is_us = country == "US"
    is_gb = country == "GB"
    is_company = business_type == "company"
    is_individual = business_type == "individual"

    if is_us:
      if is_individual:
        if len(tax_id) == 9 and tax_id.isdigit():
          ans["valid"].append(business_id)
        else:
          ans["invalid"].append(business_id)
      elif is_company:
        if (
          tax_id[:2].isdigit()
          and tax_id[2] == "-"
          and tax_id[3:].isdigit()
          and len(tax_id) == 10
        ):
          ans["valid"].append(business_id)
        else:
          ans["invalid"].append(business_id)
    elif is_gb:
      if is_company:
        if len(tax_id) == 8 and tax_id.isdigit():
          ans["valid"].append(business_id)
        else:
          ans["invalid"].append(business_id)
      else:
        ans["invalid"].append(business_id)
    else:
      ans["invalid"].append(business_id)
      
  return ans