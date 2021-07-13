names = ['Allen', 'Tom', 'Mayday', 'JJ', 'jolin', 'Jay', 'Jom']

for name in names:
	print('Hi', name)

names.append('123')
print(names) 
#新增內容

print(len(names))
#取長度

print('Asher' in names)
# 檢查有無 回傳布林值