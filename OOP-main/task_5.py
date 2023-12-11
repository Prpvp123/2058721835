class CPerson:
    def __init__(self, name, surname, patronymic, birthday, floor):
        self.name = name
        self.birthday = birthday
        self.surname = surname
        self.patronymic = patronymic
        self.floor = floor

    def register(self):
        self.name, self.surname, self.patronymic = map(str,
                                                       input('ФИО: ').split())
        self.birthday = input('Когда вы роделись?: ')
        self.floor = input('Ваш пол: ')

    def hello(self):
        print(
            f'Ваш профиль:\nФИО: {self.name} {self.surname} {self.patronymic}\nРоделись: {self.birthday}\nПол: {self.floor}')


bob = CPerson('', '', '', '', '', )
bob.register()
bob.hello()
