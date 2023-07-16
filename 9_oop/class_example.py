class Bill:
    def __init__(self):
        self.money = 0


    def add_m(self, count):
        self.money += count


    def buy(self, count, name):
        pass


# наследование
class Saving_Bill(Bill):

    def can_by(self,count):
        return False

    def boy(self, count, name):
        raise Exception('Нельзя снимать с накопительного счета')



if __name__ == '__main__':
    leo_bill = Bill()
    print(leo_bill.money)
    leo_bill.add_m(1000)
    print(leo_bill.money)
    a = 1
    if a:
        print('ef')