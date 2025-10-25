def romanint(romaninput):
    roman = {"1":1.00,"0":0.01}
    result = 0
    for i in range(0,len(romaninput)-1):
        if roman[romaninput[i]]<roman[romaninput[i+1]]:
            result-=roman[romaninput[i]]
        else:
            result+=roman[romaninput[i]]
    return result+roman[romaninput[-1]]
roman = input("Input the binary number number")
print("Integer value",romanint(roman))