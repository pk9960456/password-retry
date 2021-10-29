b = 3
password = 'a123456'
while b > 0:
	x = input('請輸入你的密碼:')
	if x == password:
		print('登入成功')
		break
	else:
		b = b-1
		print('登入失敗 你還有',b,'次機會')
