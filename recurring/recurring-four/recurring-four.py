import string

def validate_businesses(csv_text, blocked_names):
  def normalize(name):
    illegal = {"inc", "incorporated", "llc", "ltd", "limited", "corp", "corporation"}
    name = name.lower()
    name = name.translate(str.maketrans("", "", string.punctuation))
    words = name.split()

    if words and words[-1] in illegal:
      words.pop()

    return set(words)

  def preprocess_blocked_names(blocked_names):
    ans = []
    
    for blocked_name in blocked_names:
      ans.append(normalize(blocked_name))

    return ans
  
  ans = {
    "valid" : [],
    "invalid" : []
  }

  texts = csv_text.splitlines()[1:]

  blocked_names = preprocess_blocked_names(blocked_names)

  for text in texts:
    '''
    business_id,name,country,business_type,tax_id,website
    b1,Acme Inc,US,company,12-3456789,https://acme.com
    '''

    record = text.split(',')

    business_id = record[0]
    name = record[1]
    country = record[2]
    business_type = record[3]
    tax_id = record[4]

    valid = (
      len(tax_id) == 10
      and tax_id[2] == "-"
      and tax_id[:2].isdigit()
      and tax_id[3:].isdigit()
    )

    valid_company = (
      business_type == "company" 
      and valid
    )

    valid_individual = (
      business_type == "individual" 
      and len(tax_id) == 9
      and tax_id.isdigit()
    )

    normalized_name = normalize(name)

    is_blocked = False
  
    for blocked_name in blocked_names:
      if blocked_name.issubset(normalized_name):
        is_blocked = True
        break
            
    if is_blocked:
      ans["invalid"].append(business_id)
    elif country == "US":
      if valid_company or valid_individual:
        ans["valid"].append(business_id)
      else:
        ans["invalid"].append(business_id)
    elif country == "GB":
      if len(tax_id) == 8 and tax_id.isdigit():
        ans["valid"].append(business_id)
      else:
        ans["invalid"].append(business_id)

  return ans