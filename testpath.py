from pathlib import Path



#p = Path("D:/htmlsource").glob("*")
p = Path("D:/htmlsource")


i = [{"name": x, "address": x} for x in p.iterdir()]

print (i)

x = []
for e in p.iterdir():
     x.append ({"name": e, "address": e})
     print (e)

print (x)
# print (p.iterdir())