'''
A function that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized.
Example:

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''

import re

def to_camel_case(s):
    pattern = re.findall(r'[a-zA-Z]+', s)
    if not s:
        return ""
    if pattern[0][0].islower():
        return pattern[0]+"".join(map(lambda x: x.capitalize(), pattern[1:]))
    return pattern[0].capitalize()+"".join(map(lambda x: x.capitalize(), pattern[1:]))
