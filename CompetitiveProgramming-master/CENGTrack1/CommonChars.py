from collections import Counter

def CommonChars(words):
    common = []
    
    words = sorted(words)
   
    print(words)
    for letter in words[-1]:
        in_all = True
        
        for word in words[:-1]:
            if letter not in word:
                in_all = False
                break
            
        if in_all:
            common.append(letter)
            
    return common
print(CommonChars(["cook","lock","cool"]))
