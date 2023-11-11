driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	
age = input('請問你的年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過側測驗了')
	else:
		print('奇怪你怎麼會開過車')
else:
	print('是喔~')