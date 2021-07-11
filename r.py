import random
r = random.randint(1,5)

while True:
	num = input("輸入數字1~5：")
	num = int(num)

	if num == r:
		print("答對了")
		break

	else:
		print(r);
		print("答錯了")
