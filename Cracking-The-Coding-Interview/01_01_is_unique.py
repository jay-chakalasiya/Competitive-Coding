# Check if string contains all the unique characters


def is_unique(string):
    trig_ls = [False]*128
    for character in string:
        if trig_ls[ord(character)]:
            return False
        trig_ls[ord(character)] = True
    return True

def main():   
    print(is_unique('jdfksj'))

if __name__== "__main__":
    main()