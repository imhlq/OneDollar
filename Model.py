# One dollar Model
import random
import json

class Member:
    money = 0

class Room:

    def __init__(self, num, init_money, ex_money):
        self.member = []
        self.ex_money = ex_money
        for _ in range(num):
            mem = Member()
            mem.money = init_money
            self.member.append(mem)
    
    def exchange(self):
        for p in self.member:
            if p.money >= self.ex_money:
                p.money -= self.ex_money
                np = random.choice(self.member)
                while np == p:
                    np = random.choice(self.member)
                np.money += self.ex_money


    def moneyList(self):
        return [p.money for p in self.member]

    def goRun(self, n, Save_Period = 1):
        self.lines = {}
        for i in range(n):
            if i % Save_Period == 0:
                self.lines[i] = self.moneyList()
            self.exchange()

    
    def save(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.lines, fp)