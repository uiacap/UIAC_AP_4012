import re

pass_regex = re.compile(r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[\~\#\?\!\@\$\%\^\&\*\-\+\/\[\]\(\)]).{8,}")
email_regex = re.compile(r'\b[A-Za-z0-9]+@[A-Za-z0-9.]+\.[A-Z|a-z]{2,7}\b')

n = int(input())
answer = []
for i in range(n):
    email, password = input().split(' ')

    if not pass_regex.match(password) and not email_regex.match(email):
        answer.append('invalid_email_password')
    elif not pass_regex.match(password):
        answer.append('invalid_password')
    elif not email_regex.match(email):
        answer.append('invalid_email')
    else:
        answer.append('true')

print('\n'.join(answer))
