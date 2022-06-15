from builtins import range
from typing import List, Any


class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description,
        })
        self.balance -= amount

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if not self.withdraw(amount, "Transfer to " + other_category.name):
            return False

        other_category.deposit(amount, "Transfer from " + self.name)
        return True

    def check_funds(self, amount):
        return self.balance >= amount

    def spent(self):
        spent = 0
        for i in self.ledger:
            amount = i["amount"]
            if amount < 0:
                spent += amount

        return -spent

    def __str__(self):
        string = [self.name.center(30, "*")]
        for i in self.ledger:
            desc = i["description"][0:23]
            string.append("{:<23}{:>7.2f}".format(desc, i["amount"]))

        string.append("Total: {}".format(self.balance))
        return "\n".join(string)


def create_spend_chart(categories):

    if len(categories) > 4:
        return "ERR: More than 4 categories"

    spending = [c.spent() for c in categories]
    total = sum(spending)

    percent = []
    for obj in categories:

        quotient = obj.spent() / total
        percent.append(int(round(quotient * 100, -1)))

    row = []
    string = ["Percentage spent by category"]
    for i in range(100, -10, -10):
        for x in range(len(categories)):
            if percent[x] == i:
                row.append(" o ")
                percent[x] -= 10
            else:
                row.append("   ")
        sentence = '{0:3}|{1[0]}{1[1]}{1[2]}'.format(i, row)
        string.append(sentence)
        row.clear()
    padding = " " * 4
    string.append((padding + "-" * 3 * len(categories) + "-"))

    cat_string = []

    for x in categories:
        cat_string.append(len(x.name))

    for i in range(max(cat_string)):
        n = 0
        for x in categories:
            if i < len(x.name):
                row.append(" " + x.name[i] + " ")
            else:
                row.append("   ")
        sentence = '{0}{1[0]}{1[1]}{1[2]}'.format(padding, row)
        string.append(sentence)
        row.clear()

    return "\n".join(string)
