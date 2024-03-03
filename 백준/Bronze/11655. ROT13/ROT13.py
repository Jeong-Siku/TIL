s = input()
transformed = []
for i in s:
    if i.isalpha():
        if i.isupper():
            transformed.append(chr((ord(i)-65+13)%26+65))
        else:
            transformed.append(chr((ord(i)-97+13)%26+97))
    else:
        transformed.append(i)

print("".join(transformed))