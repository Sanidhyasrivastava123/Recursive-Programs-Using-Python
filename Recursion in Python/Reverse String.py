def reverse(strng):
    if len(strng) <= 1:
        return strng
    else:
        return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])

print(reverse('Sanidhya'))
