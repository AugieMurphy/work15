def authorize( passw ):
    lowerCase = [x for x in passw if x.islower()]
    upperCase = [x for x in passw if x.isupper()]
    num = [x for x in passw if x.isdigit()]
    if( len(lowerCase) >= 1 and len(upperCase) >= 1 and len(num) >=1 ):
        return True
    else:
        return False

def strength( passw ):
    lowerCase = [x for x in passw if x.islower()]
    upperCase = [x for x in passw if x.isupper()]
    num = [x for x in passw if x.isdigit()]
    alphaNumericGuide = [".", "?", "!", "&", "#" , ";", ":", "-", "_", "*" ]
    alphaNumeric = [x for x in passw for y in alphaNumericGuide if x==y]
    strength=0
    if( len(alphaNumeric) >= 1 ):
        if( len(alphaNumeric) >= 2):
            strength+=2
        else:
            strength+=1
    if( len(lowerCase) >= 1 ):
        if( len(lowerCase) >= 2):
            strength+=2
        else:
            strength+=1
    if( len(upperCase) >= 1 ):
        if( len(upperCase) >= 2):
            strength+=2
        else:
            strength+=1
    if( len(num) >= 1 ):
        if( len(alphaNumeric) >= 2):
            strength+=2
        else:
            strength+=1
    if( len(passw) > 6 ):
        if( len(passw) > 8 ):
            strength+=2
        else:
            strength+=1

    return strength

passw = "lalala123?YA!"
print( "passw: " + "lalala123?YA!" )
print( "authorize(passw):  ")
print( authorize(passw))
print( "strength(passw)" )
print( strength(passw) )

