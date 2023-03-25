class atm(object):
    def __init__(self,cardnum,pinnum):
        self.cardnum=cardnum
        self.pinnum=pinnum
    def cashwithdrawl(self,withdrawl):
        print('cash withdrawl:',withdrawl)
    def balanceenquiry(sel,balance):
        print('remaining balance',balance)
bank=atm(1234567,2324)
print(bank.cashwithdrawl(2000))
print(bank.balanceenquiry(1000 ))  
print(bank.cardnum)
print(bank.pinnum)         
