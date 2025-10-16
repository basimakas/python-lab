def countchar(inputString):
    Count={}
    for char in inputString:
        if char in Count:
            Count[char]+=1
        else:
            Count[char]=1
    return Count
str2=input("enter a string:")
result=countchar(str2)
print(result)
