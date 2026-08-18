# Email validator and Bulk Cleaner

import re

emails = ["stanley@gmail.com",
        "john123@yahoo.in",
        "abc_def@test.org",
        "stanley@gmailXcom",
        "iamlee@gmail.com",
        "kevin123@gmail.com",
        "matt45@yahoo.in",
        "abc@",
        "@gmail.com",
        "hello"]

# the pattern to extract valid mails
pattern = r"\w+@\w+\.\w+"

valid_emails = []
invalid_emails = []

for email in emails:
    if re.fullmatch(pattern, email):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

# GENERATE A SUMMARY

print("================== EMAIL REPORT ====================")
print()
# iterate through valid ones
print("Valid Emails")
for i, mail in enumerate(valid_emails, start=1):
    print(f"{i}. {mail}")

# iterate through invalid ones
print()
print("-"*30)
print(f"Invalid Emails")
for i, mail in enumerate(invalid_emails, start=1):
    print(f"{i}. {mail}")

print()
print("-"*30)

# print total emails
print(f"Total: {len(invalid_emails) + len(valid_emails)}")
print(f"Valid: {len(valid_emails)}")
print(f"Invalid: {len(invalid_emails)}")

print()
print("-"*30)

# count most common email provider
print(f"The Most Frequent email Provider: ")
the_hash = {}
pattern = r"\w+\.\w+"
for mail in valid_emails:    # match the domain pattern
        part = re.search(pattern, mail)
        part = part.group()

        the_hash[part] = the_hash.get(part, 0) + 1

most_common = max(the_hash, key=the_hash.get)
print(f"{most_common} ({the_hash[most_common]})")


        










