def check(st):
	count = 0
	li = list(st)
	li2 = list(st[::-1])
	
	for i in range(int(len(st)/2)):
		if li[i] == li2[i]:
			count+=1
	return count
	

print(check('abdabcccagba'))


