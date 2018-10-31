
s = '    elle  est    \t     pleine  \n         de vide        '
l = s.split()  #!= s.split(" ")
i = [i for i in l if i]
sPropre = " ".join(i)
print(s)
print(sPropre)
