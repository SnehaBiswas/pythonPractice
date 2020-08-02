def anagram(str1, str2):
    if len(str1) == len(str2):
        for c in str1:
            if str1.count(c) != str2.count(c):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    assert anagram('robust', 'bustor')

