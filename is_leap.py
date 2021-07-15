def is_leap(year):
	if year % 4 != 0:
		return False 

	if year % 4 == 0:
		if year % 100 != 0:
			return True
	if year % 100 == 0:
		if year % 400 != 0:
			return False

	if year % 400 == 0:
		if year % 3200 != 0:
			return True
	

year = input('請輸入年份：')
ans = is_leap(int(year))

if ans:
	print(year, '年是閏年')
else:
	print(year, '年是平年')


# False ==  平年
# True  ==  閏年