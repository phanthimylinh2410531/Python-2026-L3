# Removes the dollar sign ("$") in a string

text = input()

def remove_dollar_sign(s):
    new_string = s.replace("$", "")
    return new_string

result = remove_dollar_sign(text)

print("Initial string:", text)
print("New string:", result)