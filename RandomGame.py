import random
r = random.randint(1,100)

while True:
	num = input("輸入數字1~100：")
	num = int(num)

	if num == r:
		print("答對了!!!!!!!")
		break

	elif num > r:
		print("再小一點")

	elif num < r:
		print("再大一點")
