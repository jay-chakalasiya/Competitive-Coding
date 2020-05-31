# There are three types on operation that can be performed on a string
# 1) insert a character
# 2) remove a character
# 3) replace a character
# check if a string is only one edit or zero edit away



def one_insert_replace_away(s1, s2, mode='i'):  # s1 is smaller
    insert_replace_index=-1
    for i in range(len(s1)):
        if s1[i]==s2[i] and insert_replace_index==-1:
            continue
        else:
            insert_replace_index=i
            break
    if insert_replace_index!=-1:
        if mode=='i':
            return True if s1[insert_replace_index:]==s2[insert_replace_index+1:] else False
        else:
            return True if s1[insert_replace_index+1:]==s2[insert_replace_index+1:] else False
    return True


def one_way(s1, s2):
    if len(s1)==len(s2):
        return one_insert_replace_away(s1, s2, mode='r')
    elif len(s1)>len(s2):
        return one_insert_replace_away(s2, s1, mode='i')
    return one_insert_replace_away(s1, s2, mode='i')
def main():
    print(one_way('acd', 'abcd'))
    print(one_way('pale', 'ple'))
    print(one_way('pale', 'bale'))
    print(one_way('pale', 'ble'))
    print(one_way('a', 'b'))
    print(one_way('bc', 'bc'))

if __name__ == "__main__":
    main()