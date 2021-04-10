time=input('Введите время в секундах')
time=int(time)
timeH=time//3600
timeM=(time-timeH*3600)//60
timeS=time%60
print(f' {timeH} : {timeM} : {timeS}')

out=input('Нажмите на клавишу enter для выхода')