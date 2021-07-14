data = [1,3,5,7,9]
with open('num.txt','w')as f:
	for num in data:
		f.write(str(num) + '\n')

# 加法只能字串+字串 或是 整數+整數
# 所以必須把整數轉換成字串 