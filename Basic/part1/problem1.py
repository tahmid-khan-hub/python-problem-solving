''' Given a string, return a string where for every char in the original, there are two chars.
'The' → 'TThhee'
'AAbb' → 'AAAAbbbb'
'Hi-There' → 'HHii--TThheerree' '''

s = input()
l = len(s)
for i in range (0, l):
  print(s[i] + s[i], end='')
