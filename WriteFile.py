data = [1,3,5,7,9]
with open('num.txt','w')as f:
	for num in data:
		f.write(str(num) + '\n')

# write只能寫入'字串'