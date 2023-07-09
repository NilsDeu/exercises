""" leetcode: 13. Roman to Integer"""

def romanToInt(s: str) -> int:
    """Given a roman numeral, converts it to an integer."""
    arabic = 0
    lookahead = True
    for index, value in enumerate(s):
        if index+1 > len(s)-1:
            lookahead = False
        match(value):
            case "I":
                if lookahead and s[index+1] in ("V",  "X"):
                    arabic -= 1
                else:
                    arabic += 1
            case "V":
                arabic += 5
            case "X":
                if lookahead and s[index+1] in ("L",  "C"):
                    arabic -= 10
                else:
                    arabic += 10
            case "L":
                arabic += 50
            case "C":
                if lookahead and s[index+1] in ("D",  "M"):
                    arabic -= 100
                else:
                    arabic += 100
            case "D":
                arabic += 500
            case "M":
                arabic += 1000
    return arabic


arabic = romanToInt("III")
print(arabic)  
arabic = romanToInt("LVIII")
print(arabic)  
arabic = romanToInt("MCMXCIV")
print(arabic)            
    
