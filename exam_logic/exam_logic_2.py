from collections import defaultdict

def anagram_count(lst):
    word_dict = defaultdict(int)
    for word in lst:
        key = ''.join(sorted(word))
        word_dict[key] += 1

    for key,counter in word_dict.items():
        print(key,":", counter)


if __name__ == '__main__':
    words = ["java", "jjava", "vaj", "aavj", "j", "vjaa", "dan", "and", "ddan"]
    anagram_count(words)
