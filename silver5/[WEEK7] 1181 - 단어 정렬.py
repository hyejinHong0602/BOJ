# n = int(input())
# word_list=[]
# sorted_list=[]
# for i in range(n):
#     word = input()
#     word_count=len(word)
#     word_list.append((word, word_count))
#
# word_list.sort(key = lambda word: (word[1], word[0]))
#
# words_list = list(set(word_list))
# for word in word_list:
#     print(word[0])

words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))


words_list = list(set(words_list))


words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])

# 다시 확인