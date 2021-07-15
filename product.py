products = []
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

for p in products:
	print(p[0], '的價格', p[1])


with open('product.csv', 'w', encoding='utf8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')