import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))

n = int(input().strip())
emails = [input().strip() for _ in range(n)]

valid_emails = sorted(filter(is_valid_email, emails))
print(valid_emails)
