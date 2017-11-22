alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "aaaaabbbbbabbbaabbababbaaababaab"
s = "I canT DAnCE i CANt TALK Hey"
new_string=""

s = s.replace(' ', '')
while len(s) % 5 != 0:
    s = s[:-1]
print(s)


for i in s:
    if ord(i) > 90:
        new_string += "b"
    else:
        new_string += "a"

print(new_string)