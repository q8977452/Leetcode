def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False
        #return str(x) == str(x)[::-1]