i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1
  
frutas = ["maçã", "banana", "cereja"]
for x in frutas:
	if x == "banana":
		break
	print(x)
  
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)
  
frutas = ["maçã", "banana", "cereja"]
for x in frutas:
	if x == "banana":
		continue
	print(x)
