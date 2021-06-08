import collections
import re
# def mostCommonWord(paragraph, banned):
#     par_list = paragraph.split(' ')
#     par_list1 = paragraph.split('.').split(',').lower()
#     a = collections.Counter(par_list)
#     for i, word in enumerate(par_list):
#         max_ = max(a, a.get)



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
par_list1 = re.split("\s|(?<!\d)[,.](?!\d)", paragraph)
par_list1 = par_list1.lower()
print(par_list1)