s = 'Pyth1abch2hon'

first = s.find('h')
last = s.rfind('h')

if first != -1 and last != -1 and first != last:
    prefix = s[:first + 1]
    middle = s[first + 1:last]
    suffix = s[last:]
    new_s = prefix + middle[::-1] + suffix
else:
       new_s = s

print(new_s)
