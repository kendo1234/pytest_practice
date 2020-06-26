def is_a_palindrome(s):
    return s == s[::-1]


s = "bob"
answer = is_a_palindrome(s)

if answer:
    print("Yes")
else:
    print("No")
