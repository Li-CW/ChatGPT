ans1 = "? \n\n sdfasdf !\n"
tail = ans1[-1]; 
ans1 = ans1[:-1]
ans1 = ans1.strip()
ans1 = ans1.strip('?')
ans1 = ans1.strip(';')
ans1 = ans1.strip('!')
ans1 = ans1.strip('.')
ans1 = ans1.strip('。')
ans1 = ans1.strip(',')
ans1 = ans1.strip('？')
ans1 = ans1.strip('，')
ans1 = ans1.strip('；')
ans1 = ans1.strip('！')
ans1 = ans1.strip()
ans1 = ans1 + tail

print(ans1)
