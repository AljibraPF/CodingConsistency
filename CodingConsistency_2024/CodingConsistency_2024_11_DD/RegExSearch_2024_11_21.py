import re

#RegEx to find emails
text = "test@example.com, test@example.org, test@website.net"

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

email_list = re.findall(email_pattern, text)

print("List of emails found:", email_list)
