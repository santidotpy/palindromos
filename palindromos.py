def is_palindrome(sth):
    if type(sth) != str:
        sth = str(sth)
    sth = sth.replace(' ', '').lower()
   # sth = sth.lower()
    return sth == sth[::-1]


if __name__ == '__main__':
    pass
    # word = 'H a N N a H'
    # print(word)
    # print(is_palindrome(word))