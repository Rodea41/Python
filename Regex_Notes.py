
"""Regex"""

import re

p = re.compile('Whatever_pattern_you_want_to_look_for)

##################
"""Raw Strings"""
##################
[r"abc\n\w"] ==> Using the 'r' before the pattern converts to 'raw' format and all special character are nullified



##################
"""Setting up a filter"""
##################
['any character'] ==> returns a set of characters within the brackets []
    Example:
       [abc] # Returns any match of characters a,b, or c.
       [a-c] # Returns the same as [abc] above

[^'any character'] ==> Returns any set of characters EXCEPT the character(s) in the bracket
    Example:
        [^5] # Returns any characters except the number 5
             # If the ^ character is found anywhere else in the bracket
             # it will be treated as a regular ^ . for ex. [5^]

[ \ ]   ==> Backslash is used to escape special characters
    Example:
        ['\['] ==> Searches for the [ character

*  ==> Specifies the literal character can match zero or more times
    Example:
        ca*t # Will look for 'ct' , 'cat', 'caat', 'caaaaaaat', etc.

+  ==> Specifies that the literal character at least 1 or more times.
    Example:
        ca+t #Will look for everything in the above list except 'ct' because no 'a' is present

? ==> Specifies character can match either once or zero times. Used when something is 'optional'
    [home-?brew] #This matches 'homebrew' and 'home-brew' becaus the '-' is optional

{m,n} ==> m specifies the minimum repetition, n specifies the max repition,
    Example:
        a/{1,3}b #Will match with 'a/b', 'a//b', 'a///b' because slash can appear one time and a max of 3 times

##################
"""Special Characters"""
##################
\w ==> Matches any alphanumeric character. Equavalent to saying [a-zA-z0-9_]

\W ==> Matches any non-alphanumeric character; this is equivalent to [^a-zA-Z0-9_]

\d ==> Matches any decimal digit

\D ==> Matches any non-digit character, equavalent to saying [^0-9]

\s ==> Matches any whitespace character

\S ==> Matches any non-whitespace character


##################
"""Regex Methods """
##################
match()     ==> Determine if the RE matches at the beginning of the string.

search()    ==> Scan through a string, looking for any location where this RE matches.

findall()   ==> Find all substrings where the RE matches, and returns them as a list.

finditer()  ==> Find all substrings where the RE matches, and returns them as an iterator.
                                      
group()     ==> Return the string matched by the RE

start()     ==> Return the starting position of the match

end()       ==>Return the ending position of the match

span()      ==> Return a tuple containing the (start, end) positions of the match

DOTALL or S ==> Make . match any character, including newlines. #Example: re.DOTALL or re.S mean the same thing

IGNORECASE or I ==> Do case-insensitive matches. #Example: re.IGNORECASE or re.I mean the same thing
    Example: re.I('Spam') will match with 'Spam', 'spam', 'spAM', and 'SpAm'

MULTILINE or M 

Usually ^ matches only at the beginning of the string, and $ matches only at the end of the string and immediately before the newline (if any)
at the end of the string. When this flag is specified, ^ matches at the beginning of the string and at the beginning of each line within the string, immediately following each newline. Similarly,
the $ metacharacter matches either at the end of the string and at the end of each line (immediately preceding each newline).

 





##################
"""Examples"""
##################

#It is common style to store the match object in a variable then check it it
#returned None. example below:
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')


#Using findall():
p = re.compile(r'\d+') # Convert to raw string then look for any numeric char.
p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
>> ['12', '11', '10']


#Using finditer()
p = re.compile(r'\d+') # Convert to raw string then look for any numeric char.
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
for match in iterator:
     print(match.span())

>>(0, 2) 
>>(22, 24) 
>>(29, 31) 













