string1=input('введите челое, положительное число')
i=0
max=0
while i!=len(string1):
    if max<int(string1[i]):
        max=int(string1[i])
    i+=1

print(max)

out=input('Нажмите на клавишу enter для выхода')