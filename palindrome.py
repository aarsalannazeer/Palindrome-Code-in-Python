def checkk(w):
    return w == w[::-1]
w = input("Enter the string: ")
w= w.lower()
answer = checkk(w)

if answer:
    print("Yes, it is Palindrome")
else:
    print("No, try anaother word")
