# Method to perform basic string compression using counts if repeated characters
# Example: aabcccccaaa = a2b1c5a3
# if compressed string does not become smaller than original then return original string
# assume string has only upper and lower case letters


def string_compression(string):
    if len(string)==0:
        return string
    counter=0
    currrent_char=string[0]
    compressed_string=''
    for i in range(len(string)):
        if currrent_char == string[i]:
            counter+=1
        if currrent_char != string[i]:
            compressed_string+=currrent_char+str(counter)
            currrent_char=string[i]
            counter=1
    compressed_string+=currrent_char+str(counter)
    return compressed_string if len(compressed_string)<len(string) else string


def main():
    print(string_compression('abbbbcd'))
    print(string_compression('aabcccccaaa'))
    print(string_compression('abcdef'))
    print(string_compression('a'))
    


if __name__ == "__main__":
    main()