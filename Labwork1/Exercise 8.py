# Extracts the even items in a given integer list

input_string = input()
list_string = input_string.split()
list_number = []

for x in list_string:
    list_number.append(int(x))

def extract_even(list):
    even_items = []
    for item in list:
        if item % 2 == 0:
            even_items.append(item)
    return even_items

result = extract_even(list_number)

print("Integer list:", list_number)
print("Even items:", result)