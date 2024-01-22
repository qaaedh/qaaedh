import random

def generate_three_digit_code():
    code = ""
    for _ in range(3):
        code += str(random.randint(0, 9))
    return code

def generate_four_digit_code():
    code = ""
    for _ in range(4):
        code += str(random.randint(1, 6))
    return code

three_digit_code = generate_three_digit_code()
four_digit_code = generate_four_digit_code()

print("Kolmenumeroinen koodi:", three_digit_code)
print("Nelinumeroinen koodi:", four_digit_code)