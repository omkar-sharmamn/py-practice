
def check_palindrome(word):
    return (word == word[::-1])

if __name__ == '__main__':
    print check_palindrome("gadag")
