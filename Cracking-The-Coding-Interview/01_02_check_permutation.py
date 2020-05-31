# check if one string is permutation of other

def check_permutation(str1, str2):
    trig_ls = [0]*128
    if len(str1)!= len(str2):
        return False
    for i in range(len(str1)):
        trig_ls[ord(str1[i])]+=1
        trig_ls[ord(str2[i])]-=1
    for i in range(len(trig_ls)):
        if trig_ls[i]!=0:
            return False
    return True
def main():
    print(check_permutation('iamgood', 'oomaigd'))


if __name__ == "__main__":
    main()