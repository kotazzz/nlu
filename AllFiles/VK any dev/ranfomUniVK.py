import random
i = 0
s = ''
while i < random.randrange(50,300):
 s+=f"&#{random.randrange(1,25565)};"
 i+=1
print(s)
input()