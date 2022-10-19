n = input()
t = int(n[0])
n.pop(0)

for i in range (t):
 frase = n[i].split()
 frase.reverse()
 b = False
 for j in frase:
  try:
    a = int(j)
    b = True
    break
  except ValueError: 
    b = False
 if b:
  print ("MATEMATICA", end="" if i == t-1 else ";")
 else:
  p = ""
  for k in range (len(frase)):
    s = "" 
    if k == len(frase) -1: 
      s = "" if i == t-1 else ";"
    else: 
      s = " "
    p += frase[k] + s
  print (p, end="")
  "" if i == t-1 else ";"
