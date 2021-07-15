import os

# 讀取檔案
products = []
if os.path.isfile('product.csv'):
	with open('product.csv', 'r', encoding='utf8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
		name, price = line.strip().split(',')
		products.append([name, price])
	print(products)
else:
	print('找不到檔案！')






# 讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	# test = input('測試')

	p = []
	p.append(name)
	p.append(price)
	# p = [name, price] 等同於9,10,11行	

	products.append(p) 
	# 二維清單

print(products)

# print(products[0][0]) 
# # 珍珠奶茶 , 0 -> 取到 珍珠奶茶

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格', p[1])

# 寫入檔案
with open('product.csv', 'w', encoding='utf8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')