# Assume that we have a method isSubstring which checks if one is substring of other
# Write a function which says if a string is rotation of another


def isSubstring(s1, s2): # s1 is substring of s2
    if s1 in s2:
        return True
    else: 
        return False

def string_rotation(string1, string2):
    if string1 in string2*2:
        return True
    else:
        return False


def main():
    print(string_rotation('waterbottle', 'erbottlewat'))

if __name__ == "__main__":
    main()