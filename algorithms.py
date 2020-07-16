# /*
#   String Encode

#   You are given a string that may contain sequences of consecutive characters.
#   Create a function to shorten a string by including the character,
#   then the number of times it appears.
#   */

test1 = "aaaabbcddd"
# // Output: "a4b2c1d3"

test2 = ""
# // Output: ""

test3 = "a"
# // Output: "a1"

test4 = "bbcc"
# // Output: "b2c2"





def removeDuplicates(string):
    # create new string variable
    newStr = ''
    
    # initialize counter variable 
    counter = 1
    if string == '':
        return string
    elif len(string) == 1:
        newStr += string 
        newStr += str(counter)
        return newStr
    # start for loop
    else:
        for i in range(len(string)-1):
            # if current character is equal to previous then we inrement consecutive counter
            if string[i] == string[i+1]:
                counter += 1
            elif string[i] != string[i+1]:
                newStr += string[i]
                newStr += str(counter)
                counter = 1
            
            if i == len(string)-2: # if we're at the second last index we just append current 
                newStr += string[i]
                newStr += str(counter)
            # print('current char: ', string[i])
            # print('newStr: ', newStr)
    
    return newStr

x = removeDuplicates(test1)
print(removeDuplicates(test1))
print(removeDuplicates(test2))
print(removeDuplicates(test3))
print(removeDuplicates(test4))





# //  **********************

# /*
# String Decode
# */

test1 = "a3b2c1d3"
# // Output: "aaabbcddd"

# //  **********************

# // How would you compress this?

twoDScreen = [
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
  ["r", "o", "y", "g", "c", "b", "p"],
]

