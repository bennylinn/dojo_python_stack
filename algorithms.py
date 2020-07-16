# /*
#   String: Rotate String

#   Create a standalone function that accepts a string and an integer, and rotates the characters in the string to the right by that given integer amount.
# */

test1Str = "Hello World"
test1RotateAmnt = 0
# // Output: "Hello World"

test1Str = "Hello World"
test1RotateAmnt = 1
# // Output: "dHello Worl"

test1Str = "Hello World"
test1RotateAmnt = 2
# // Output: "ldHello Wor"

test1Str = "Hello World"
test1RotateAmnt = 4
# // Output: "orldHello W"



def rotate(string, rotateamt):
    holdingString = string
    

    for i in range(rotateamt):
        print('loop: ', i)
        newStr = ""
        # get last character
        lastChar = holdingString[-1]
        print('last char', lastChar)
        # last char placed into newStr
        newStr=lastChar
        print('added last char', newStr)
        # add rest of the string to new variable
        newStr+= holdingString[ 0:len(string)-1 ] # --> gets everything but last char
        print('added rest of char', newStr)
        # add newstr to holding var
        holdingString = newStr

    return holdingString

# print(rotate(test1Str, 0))
# print(rotate(test1Str, 1))
# print(rotate(test1Str, 2))
# print(rotate(test1Str, 3))
print(rotate(test1Str, -1))



# // **************************

# /*
#   String: ionIs Rotat (Is Rotation)

#   Create the function isRotation(str1,str2) that
#   returns whether the second string is a rotation of the first.
# */

test1StrA = "ABCD"
test1StrB = "CDAB"
# // Output: true
# //   - if you start from A in the 2nd string, the letters are in the same order, just rotated

test2StrA = "ABCD"
test2StrB = "CDBA"
# // Output: false
# //   - all same letters in 2nd string, but out of order

def isRotation(str1, str2):
    # len(str1) != len(str2)

    # for loop range(len(str2))
    # check if each rotation of str2 == str1
    # else false
    return 