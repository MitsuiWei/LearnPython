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

	
	


	# test2 = []
	# test2.append(name)
	# test2.append(price)
	# test2.append(test)

	# products.append(test2)
	# 三維清單


print(products)

print(products[0][0]) 
# 珍珠奶茶 , 0 -> 取到 珍珠奶茶

for p in products:
	print(p[0], '的價格', p[1])