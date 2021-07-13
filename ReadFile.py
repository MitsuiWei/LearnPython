data = []
with open('food.txt', 'r')as f:
	for line in f:
		print(line.strip())
		# .strip可以去除多餘空行
		data.append(line)

print(data)
# 這邊可以證明\n的存在