# check if a string is permutation of a palindrome

# Input "Tact Coa"
# Output True (Example: "taco cat", "atco cta")
def rearrage_ords(c):
    return ord(c)-32 if ord(c)>=ord('a') and ord(c)<=ord('z') else ord(c)

def pelindrome_permutation(string):
    trigs = [False]*128
    for chararcter in string:
        trigs[rearrage_ords(chararcter)] = not trigs[rearrage_ords(chararcter)]
    return False if trigs[ord('A'):ord('Z')+1].count(True)>1 else True


def main():
    print(pelindrome_permutation("So patient a nurse to nurse a patient so"))

if __name__ == "__main__":
    main()