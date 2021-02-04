"""
Dictionary Challenge
"""
# Key = word, Value = number of times the word appears

sentence = 'I am so happy to learn Python which make myself ' \
           'happy and interested in Python Python Python Python'

sentence_dict = {}
for each_word in sentence.split(' '):
    sentence_dict[each_word] = sentence_dict.get(each_word, 0) + 1

print(sentence_dict)


