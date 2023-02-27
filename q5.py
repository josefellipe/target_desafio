string = "omordnilap mu é oãn ossI"

def invert_string(string):
    reverse_string = ""
    for i in range(len(string)):
        reverse_string += string[len(string)-1-i]
    return reverse_string


print(invert_string(string))