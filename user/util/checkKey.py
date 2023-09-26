import re

def check(key):
    # Regular expressions to match phone numbers and email addresses
    phone_pattern = r'\b\d{10}\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    # Find phone numbers and email addresses in the text
    phone_matches = re.findall(phone_pattern, key)
    email_matches = re.findall(email_pattern, )
    
    # Replace phone numbers and email addresses with blurred placeholders
    for phone_match in phone_matches:
        text = text.replace(phone_match, '**********')
        form = 'phoneNumber'
    
    for email_match in email_matches:
        text = text.replace(email_match, '*****@*****.***')
        form = 'email'
    
    return form