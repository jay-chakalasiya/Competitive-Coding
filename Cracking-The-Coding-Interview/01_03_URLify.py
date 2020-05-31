# A method to replace spaces with %20, 
# assume that string has sufficient spaces at the end to hold extra character
# the true length of string is also given
# 
# Input "Mr John Smith    ", 13
# Output "Mr%20John%20Smith"


def URLify(string, length):
    current_index = len(string)

    for i in range(length-1, -1, -1):
        print(i, string[i], current_index, string)
        if string[i]==' ':
            string[current_index-3:current_index]='%20'
            current_index-=3
        else:
            string[current_index-1]=string[i]
            current_index-=1
    return string



def main():
    print(URLify(list('Mr John Smith    '), 13))
    



if __name__ == "__main__":
    main()