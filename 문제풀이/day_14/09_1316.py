N = int(input())

cor_word_count = 0
wrong_word_count = 0

for _ in range(N):
    word = input()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            select_word = word[i+1:]
            if select_word.count(word[i]) > 0:
                wrong_word_count += 1

    if wrong_word_count == 0:
        cor_word_count += 1

print(cor_word_count)


