def divide(ourdividend, ourDivisor):
    sign = (-1 if((ourdividend < 0)^(ourDivisor < 0)) else 1)

    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)

    quotientnumber = 0
    tempnumber = 0

    for i in range(31, -1, -1):
        if( tempnumber + (ourDivisor << i) <= ourdividend):
            tempnumber += ourDivisor << i
            quotientnumber |= 1 << i
        print('number ', tempnumber, quotientnumber)

    if sign ==  -1:
        quotientnumber =- quotientnumber
    return quotientnumber

a = int(input('enter a for a/b : '))
b = int(input('enter b for a/b : '))
print('result of ', a,'/',b,'is',divide(a,b))