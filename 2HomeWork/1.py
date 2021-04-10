data_type = []
int_char = 5#целое число
data_type.append(int_char)
float_char = 1.5#число с плавающей точкой
data_type.append(float_char)
complex_char = complex(5, 8)#комплексное число
data_type.append(complex_char)
str_symbol = 'asd' #строка
data_type.append(str_symbol)
list_char = [2, '4', 2.6, 'dfg']# список
data_type.append(list_char)
list_cort = (2, '4', 2.6, 'dfg')# кортеж
data_type.append(list_cort)
set_char = set('adffjsahfksd')# множество
data_type.append(set_char)
dict_char = {'asd':5,'dsa':6,'abra':'kodabra'}#словарь
data_type.append(dict_char)
bool_char = True#логический тип
data_type.append(bool_char)
bytes_char = 'abraкодабра'.encode('utf-8')#байты
data_type.append(bytes_char)
bytes_array = bytearray(bytes_char)#массив байтов
data_type.append(bytes_array)
non_char = None #тип нон
data_type.append(non_char)

for i in data_type:
    print(type(i),' - ',i)
