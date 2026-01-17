#word matching
def match_words(words):
    #character count
    ctr=0
    #blank list
    lst=[]
    #check each and every word in the list
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("List of words with the first and last character the same",lst)
    return ctr
count=match_words(['abc','xyz','aba','1221','aa','hello','wow'])
print("Number of words with the first and last character the same:",count)
