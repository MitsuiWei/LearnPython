import random
r = random.randint(1,100)
count = 0;
while count < 3:
	count = count + 1

	num = input("輸入數字1~100：")
	num = int(num)

	if num == r:
		print("答對了!!!!!!!")
		print("這是你猜的第", count ,"次")
		break

	elif num > r:
		print("再小一點")
		

	elif num < r:
		print("再大一點")
		
	
	print("這是你猜的第", count ,"次")
