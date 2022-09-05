def isPalindrome(string, i):
    if (i > len(string) / 2):
        return True
    ans = False
    if ((string[i] is string[len(string) - i - 1]) and isPalindrome(string, i + 1)):
        ans = True
    return ans


string = str(input("Input word : "))
if (isPalindrome(string, 0)):
    print("Yes")
else:
    print("No")