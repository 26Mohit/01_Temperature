# quick component to convert degrees F To C.
# Function takes in value, does conversion and puts answer into a list


def to_c(from_f):
    centigrade = (from_f-32)*5/9
    return centigrade


# Main routine
temperatures = [0, 32, 100]
converter = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C". format(item, answer)
    converter.append(ans_statement)

print(converter)