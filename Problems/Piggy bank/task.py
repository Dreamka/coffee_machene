class PiggyBank:
    def __init__(self, dollar, cent):
        self.dollars = dollar
        self.cents = cent

    def add_money(self, dollars, cents):
        cents_in_dollars = dollars * 100
        all_add_cents = cents_in_dollars + cents

        add_dollars = all_add_cents // 100
        add_cents = all_add_cents - (add_dollars * 100)

        if add_cents + self.cents == 100:
            add_dollars += 1
            add_cents = 0
            self.cents = 0

        self.dollars += add_dollars
        self.cents += add_cents
