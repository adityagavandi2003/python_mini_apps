button_text = []

numbers = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"]
]
operators = ["/", "*", "-", "+"]

# Add number and operator buttons for rows 1-3
for row, nums in enumerate(numbers, start=1):
    for col, num in enumerate(nums):
        button_text.append((num, row, col))
    button_text.append((operators[row-1], row, 3))

# last_row = ["C", "0", "=", "+"]
# for col, text in enumerate(last_row):
#     button_text.append((text, 4, col))
    
# Last row: C, 0, =, +
button_text.append(("C", 4, 0))
button_text.append(("0", 4, 1))
button_text.append(("=", 4, 2))
button_text.append(("+", 4, 3))
