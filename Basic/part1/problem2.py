''' Return True if the string "cat" and "dog" appear the same number of times in the given
string.
'catdog' → True
'catcat' → False
'1cat1cadodog' → True'''

s = input()
flag = False
if(s.count("cat") == s.count("dog")):
  flag = True
  print(flag)
else:
  print(flag)