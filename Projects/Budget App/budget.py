class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def myName(self):
        return self.name

    def get_ledger(self):
        return self.ledger

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def deposit(self, depo, desc=''):
        self.ledger.append({"amount": depo, "description": desc})
        self.balance += depo

    def withdraw(self, withd, desc=''):
        if self.check_funds(withd):
            self.balance -= withd
            self.ledger.append({"amount": -1 * withd, "description": desc})
            return True
        else:
            return False

    def transfer(self, amount, destination):
        if self.balance >= amount:
            self.balance -= amount
            self.ledger.append({
                "amount":
                -1 * amount,
                "description":
                'Transfer to ' + destination.myName()
            })
            destination.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def __str__(self):
        nameLength = len(self.name)
        starcount = (30 - nameLength) // 2
        ledgesheet = '*' * starcount + self.name + '*' * starcount + '\n'
        for i in self.ledger:
            numString = f'{i["amount"]:.2f}'
            if len(i["description"]) >= 24:
                ledgesheet += (i["description"][:23])
                ledgesheet += (' ' * (30 - 23 - len(numString)))
                ledgesheet += numString
                ledgesheet += '\n'
            else:
                ledgesheet += (i["description"])
                ledgesheet += (' ' *
                               (30 - len(i["description"]) - len(numString)))
                ledgesheet += numString
                ledgesheet += '\n'
        ledgesheet += 'Total: ' + str(self.balance)
        return ledgesheet


def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    Percentage = 100
    sum = 0
    length = 0
    for i in categories:
        sum += i.get_balance()
        if len(i.myName()) > length:
            length = len(i.myName())
    for i in range(11):
        result += ' ' * (3 - len(str(Percentage)))
        result += str(Percentage) + '|'
        for i in categories:
            if (i.get_balance() * 100 / sum) >= Percentage:
                result += ' o '
            else:
                result += '   '
        result += ' \n'
        Percentage -= 10
    result += " " * 4 + '-' * (3 * len(categories) + 1) + '\n'
    for i in range(length):
        result += ' ' * 4
        for c in categories:
            try:
                result += ' ' + c.myName()[i] + ' '
            except:
                result += ' ' * 3
        result += ' \n'

    return result
