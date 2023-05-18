with open('grades.txt') as r:
    ls = []
    for line in r:
        line = line.strip()
        ls.append(int(line))
  
print(ls)