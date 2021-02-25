TOTAL = 0
YEAR = 0


for line in open("http.log"):

    items = line.split()
    if len(items) < 9:
        continue
    year = items[3].split(':')[0][-4:]
    if year == '1995':
        YEAR += 1
        TOTAL += 1
    
   
print(YEAR)
print(TOTAL)

