##Anchors
# ^      — start of line
# $      — end of line
# \b     — word boundary
# \B     — not a word boundary
##Character Types
# .      — any character
# \s     — whitespace
# \S     — non-whitespace
# \d     — digit (0-9)
# \D     — non-digit
# \w     — word char (A-Z a-z 0-9 _)
# \W     — non-word char

##Quantifiers
# *      — 0 or more
# *?     — 0 or more (non-greedy)

# +      — 1 or more   - greedy to match largest possible string ...
# +?     — 1 or more (non-greedy)

# ?      — 0 or 1

# {n}    — exactly n
# {n,}   — n or more
# {n,m}  — between n and m

##Character Sets
# [aeiou]      — any char in set
# [^XYZ]       — any char NOT in set
# [a-z0-9]     — range of characters

##Groups & Alternation
# (abc)        — capture group
# (?:abc)     — non-capturing group
# |            — OR   (cat|dog)

##Captures (Extraction)
# (      — extraction start
# )      — extraction end
'''
🧠 Quick summary
Pattern	Meaning
$	End of line / string
^	Start of line / string
/m	Makes ^ and $ work per line
\$	Literal dollar sign

Examples
Digits
^\d+$

Email (simple)
^[\w.-]+@[\w.-]+\.\w+$

URL (simple)
https?://\S+

Number (int or decimal)
^-?\d+(\.\d+)?$
'''

import re
x = 'My phone number is 123-456-7890 and my email is sachinklocham@gmail.com my age is 30'
y = re.findall(r'\d{3}-\d{3}-\d{4}', x)#'123-456-7890']
print(y)
y1 = re.findall('[0-9]+', x)#['123', '456', '7890', '30'] digits from string
print(y1)

x2 = 'From : using the : character'
y2 = re.findall('^F.+', x2) #greedy  #['From : using the : character'] - longest match
y3 = re.findall('^F.+:', x2) #greedy  #['From : using the :']
y4 = re.findall('^F.+?:', x2) #non-greedy  #['From :'] shortest match
# first char match F last character match :
print(y2)
print(y3)
print(y4)

#extract 'uct.ac.za' from this string using re.findall?
str1 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y5 = re.findall('@(\S+)', str1) #['uct.ac.za']
#y5 = re.findall('@\S+', str1) #['@uct.ac.za']
#y5 = re.findall('F.+:', str1) #['From stephen.marquard@uct.ac.za Sat Jan  5 09:14:']
#y5 = re.findall('..@\S+..', str1) #['rd@uct.ac.za S']
y5 = re.findall('\S+?@\S+', str1) #['uct.ac.za']
print(y5)

str2 = 'hello $achin'
y6 = re.findall('$', str2) #['']
print(y6)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)#['From: Using the :']
print(y)