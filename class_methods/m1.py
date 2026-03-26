
account_user_details = [
    {
        'customer_name' : 'customer1',
        'customer_id' : 101,
        'address' : 'nagpur,440008',
        'account_no' : 9182767383,
        'account_type' : 'savings',
        'initial_deposit' : 5000
    },
    {
        'customer_name' : 'customer2',
        'customer_id' : 102,
        'address' : 'nagpur,440123',
        'account_no' : 9738292921,
        'account_type' : 'savings',
        'initial_deposit' : 1000
    },
    {
        'customer_name' : 'customer3',
        'customer_id' : 103,
        'address' : 'nagpur,443628',
        'account_no' : 9628304642,
        'account_type' : 'current',
        'initial_deposit' : 10000
    },
    {
        'customer_name' : 'customer4',
        'customer_id' : 104,
        'address' : 'nagpur,440292',
        'account_no' : 9745201647,
        'account_type' : 'savings',
        'initial_deposit' : 3000
    },
    {
        'customer_name' : 'customer5',
        'customer_id' : 105,
        'address' : 'nagpur,440009',
        'account_no' : 9413124123,
        'account_type' : 'current',
        'initial_deposit' : 15000
    }
]

class bank_details:
    customer_name = ''
    customer_id = 0
    address = ''
    account_no = 0
    account_type = ''
    initial_deposit = 0

    def __init__(self,accountuserdetails):
        self.customer_name = accountuserdetails.get('customer_name')
        self.customer_id = accountuserdetails.get('customer_id')
        self.address = accountuserdetails.get('address')
        self.account_no = accountuserdetails.get('account_no')
        self.account_type = accountuserdetails.get('account_type')
        self.initial_deposit = accountuserdetails.get('initial_deposit')

    def deposit(self,amount):
        print(f'account number : {self.account_no} deposited with {amount}')
        self.initial_deposit = self.initial_deposit + amount

    def withdraw(self,amount):
        print(f'account number : {self.account_no} withdrawn with {amount}')
        self.initial_deposit = self.initial_deposit - amount

    def getcustdetails(self):
        print('-'*20)
        print(f'customer details')
        print(f'customer_name = {self.customer_name}')
        print(f'customer_id = {self.customer_id}')
        print(f'address = {self.address}')
        print(f'account_no = {self.account_no}')
        print(f'account_type = {self.account_type}')
        print(f'initial_deposit = {self.initial_deposit}')
        print('-'*20)




c1 = bank_details(account_user_details[0])
c1.getcustdetails()
c1.deposit(3000)
c1.getcustdetails()
c1.withdraw(1000)
c1.getcustdetails()
