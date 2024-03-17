'''
problem_name = Valid Parentheses
problem_source = https://leetcode.com/problems/valid-parentheses/description/

Algo 
    -
'''

#Using if else
class Solution:
    def isValid(self, s: str) -> bool:
        syntax = list()
        for brace in s:
            if brace in ["(", "{", "["]:    #When the opening braces comes into play
                syntax.append(brace)
            elif brace == ")":
                if not syntax or syntax.pop() != "(":   #When Close brace doesn't match last opening brace, and if the first element is close brace
                    return False 
            elif brace == "}":
                if not syntax or syntax.pop() != "{":   #When Close brace doesn't match last opening brace, and if the first element is close brace
                    return False     
            else:
                if not syntax or syntax.pop() != "[":   #When Close brace doesn't match last opening brace, and if the first element is close brace
                    return False
            
        return not syntax       #When there is opening braces left but no close brace, i.e all the brace not popped



#Another pythonic approach
class Solution:
    def isValid(self, s: str) -> bool:
        braces = {")":"(", "}":"{", "]":"[" }   #Pairing the braces
        syntax = []
        for brace in s:
            if brace in braces.values():    #When the opening braces comes into play
                syntax.append(brace)
            elif not syntax or syntax.pop() != braces[brace]:   #When Close brace doesn't match last opening brace, and if the first element is close brace
                return False
        return not syntax          #When there is opening braces left but no close brace, i.e all the brace not popped
