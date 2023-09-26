# HW 3
# Problem No. 4

# First Non-Repeating Character
# -----------------------------
# Write a function that returns the first non-repeating character in a string with O(n) 
# efficiency. It should return none or null if there are no non-repeating characters.

# Example
# -----------------
# string =  "aaaaabbbbbbc"
# expected: "c"

# string = "aabab"
# expected: "b"

# string = "aaaaaa"
# expected: None

def find_first_non_repeating(string):

    # empty string check
    if len(string) == 0:
        print("the string is empty: no non-repeating characters")
        return None

    for i, char in enumerate(string):

        # add first char to temp
        if i == 0:
            temp = char

        # char repeats
        elif char == temp[0]:
            temp = temp + char

        # char changes
        else:
            # temp is repeating, so assign new char to temp
            if(len(temp) > 1):
                temp = char
            
            # first non-repeating is temp
            elif(len(temp) == 1):
                break

    # reach end of string and no non-repeating char found
    if len(temp) > 1:
        return None
    
    return temp

string_list = [
    "aaaaabbbbbbc",
    "aabab",
    "aaaaaa",
    "zyxwvu",
    "aabac",
    "ababa",
    "bbqatx",
    "bbggbgge",
    "zztop",
    "zzaayybb",
]

for index, string in enumerate(string_list):
    print("--------------------------------------------------------------")
    result = find_first_non_repeating(string)
    print(f'{index + 1}. {str(string):15} first non repeating = {result}')
    print("--------------------------------------------------------------")
