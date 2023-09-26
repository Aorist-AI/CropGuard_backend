import re

def check(text):
    # Regular expressions to match phone numbers and email addresses
    phone_pattern = r'\b\d{10}\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    # Find phone numbers and email addresses in the text
    phone_matches = re.findall(phone_pattern, text)
    email_matches = re.findall(email_pattern, text)
    
    # Replace phone numbers and email addresses with blurred placeholders
    for phone_match in phone_matches:
        text = text.replace(phone_match, '**********')
    
    for email_match in email_matches:
        text = text.replace(email_match, '*****@*****.***')
    
    return text

# # Example usage
# input_text = "Please contact me at 1234567890 or email me at john@example.com"
# blurred_text = check(input_text)
# print(blurred_text)
