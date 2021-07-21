dic0 = {
	'name' : '麥香奶茶',
	'price' : 10 
}

dic1 = {
	'name' : '珍珠奶茶',
	'price' : 60 
}

dic1['黑糖珍奶']       #如果沒有 '=' 單純代表查找
dic1['黑糖珍奶']  = 90 #新增內容至字典
print(dic1) #{'name': '珍珠奶茶', 'price': 60, '黑糖珍奶': 90}


drinks = [dic0, dic1]
print(drinks[0]['name']) #麥香奶茶