# Задание 2. Создайте класс User с свойствами Login и Password. Создайте список объектов
# User из 5 элементов. Выведите из этого списка пользователя с определенными логином и
# паролем;

class User:
    def __init__(self, Login, Password):
        self.Login = Login
        self.Password = Password

Maria = User('bbn', '12345')
Greg = User('greg2018', '12012018greg')
Josh = User('josh2000', '12345')
Vera = User('veramarkovna', 'veravera')
Admin = User('admin', 'admin')

Users = [Maria, Greg, Josh, Vera, Admin]
requested_password = '12345'
requested_login = 'greg2018'

for i in range(len(Users)):
    if Users[i].Password == requested_password:
        print(f'Пользователь [ {Users[i].Login} ; {Users[i].Password}  ] имеет логин, равный запрашиваемому.')

for i in range(len(Users)):
    if Users[i].Login == requested_login:
        print(f'Пользователь [ {Users[i].Login} ; {Users[i].Password}  ] имеет логин, равный запрашиваемому.')
