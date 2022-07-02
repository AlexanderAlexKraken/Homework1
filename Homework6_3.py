class Worker:
# атрибуты класса
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self.wage = wage
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wege, bonus):
        super().__init__(name, surname, position, wege, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surename
    def get_total_income(self):
        self._total_income = {'Заработаная плата': self.wage, 'Бонус': self.bonus}
        return self._total_income
        print(f'суммарный доход {total_income}')

a = Position('Вася', 'Пирожков', 'топ менеджер', 10, 50)
print(a.get_full_name(), a.get_total_income())
print(a.name)
print(a.surename)
print(a.position)
