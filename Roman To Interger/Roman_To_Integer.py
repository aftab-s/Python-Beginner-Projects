class solution(object):
    s = input()                         #Inputing the Roman Numeral
    def romanToInt(s):
        mapping = {                     #Creating a Dictionary to Store the Roman Values
                'I' : 1,                #And Corresponding Intergers
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
            }

        Integer = 0                     #Initializing the Integer Value
        for i in range(len(s)):
            # Range Should NOT Cross the Length of the Input Sequence of Characters(Roman Numerals)
            # Also the Mapping value of the Corresponding Iteration Must be Less Than The Next One
            if i+1 != len(s) and mapping[s[i]] < mapping[s[i+1]]:       
                Integer -= mapping[s[i]]
            else:
                Integer += mapping[s[i]]
        return Integer                  
        print(romanToInt(s))

obj = solution()
obj.romanToInt()