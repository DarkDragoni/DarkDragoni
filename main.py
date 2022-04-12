# task 1 slice

def isPalindrome(w):
    return w == w[::-1]
 
w = "palindrom"
ans = isPalindrome(w)
 
if ans:
    print("Yes")
else:
    print("No")