import arrow

# data = arrow.now().format('DD/MM/YYYY')
# print(data)
#output: 14/07/2022
# data = arrow.now().format('HH:mm')
# print(data)
#output: 16:27

date_1 = arrow.get('1998-01-21 18:40:48', 'YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 13:18:20', 'YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)
