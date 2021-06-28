def pallindrome(s):
    s=s.lower()
    l=len(s)
    if(l<2):
        return True
    elif s[0]==s[l-1]:
        return pallindrome(s[1:l-1])
    else:
        return False

s='Malayalam'
ans=pallindrome(s)
if ans:
    print('Yes')
else:
    print('No')
    
