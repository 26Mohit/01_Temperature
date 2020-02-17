# quick component to convert degrees C To F.
# Function takes in value, does conversion and puts answer into a list


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main routine
temperatures = [0, 40, 100]
converter = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F". format(item, answer)
    converter.append(ans_statement)

print(converter)