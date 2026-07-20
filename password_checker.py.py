password=input("enter the password:")
length=len(password)
has_upper=False
for ch in password:
    if ch.isupper():
        has_upper=True
        break
has_lower=False
for ch in password:
    if ch.islower():
        has_lower=True
        break
has_digit=False
for ch in password:
    if ch.isdigit():
        has_digit=True
        break
has_symbol=False
for ch in password:
    if not ch.isalnum():
        has_symbol=True
        break

score=0
if length>=8:
    score+=1
if has_upper:
    score+=1
if has_lower:
    score+=1
if has_digit:
    score+=1
if has_symbol:
    score+=1

if score==5:
    print("Strong password")
elif score>=3:
    print("Medium password")
else:
    print("Weak password")


