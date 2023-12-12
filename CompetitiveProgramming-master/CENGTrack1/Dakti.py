n = int(input())
for _ in range(n):
    words = input().split()
    word_dict = {}
    for word in words:
        number = ""
        for w in word:
            if w.isdigit():
                number += w
            
        # print("number:",number)
        word_dict[int(number)] = word.replace(number, "")
    sorted_words = [word_dict[i] for i in sorted(word_dict)]
    # print(sorted_words)
    print(" ".join(sorted_words))