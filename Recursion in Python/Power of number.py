def power(base,expo):
    assert expo>=0 and int(expo)==expo ,'Exponent cannot be negative'
    if expo==0:
        return 1
    elif expo==1:
        return base
    else:
        return base*power(base,expo-1)

print(power(2,4))
