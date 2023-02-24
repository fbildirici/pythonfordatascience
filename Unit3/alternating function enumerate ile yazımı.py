##########################
# alternating fonksiyonun enumerate ile yazılmas
##########################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        print(new_string)


alternating_with_enumerate(" python for data science in computational social sciences")
