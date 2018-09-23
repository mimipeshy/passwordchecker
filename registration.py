import re

value = []
password = [x for x in input("Enter comma-separated passwords: ").split(',')]


def check_password(passwords):
    for password in passwords:
        if len(password) < 6 or len(password) > 12:
            continue
        else:
            pass
        if not re.search("((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12})", password):
            continue
        else:
            pass
        value.append(password)

    return ",".join(value)


print(check_password(password))