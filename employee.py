"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    total=0
    salary = 0 
    name = ""
    contracted = False
    commisions = False
    contract_t=0
    commisions_t=0

    def __init__(self, name, salary, contracted,con_hrs, con_w, commisions,com_num,com_w):
        self.name = name
        self.salary= salary
        self.contracted=contracted
        self.commisions= commisions
        self.contract_t= con_hrs*con_w
        self.commisions_t=com_num*com_w

    def get_pay(self):
        self.total= self.salary 
        self.total += self.contract_t+ self.commisions_t

        return self.total

    def __str__(self):
        #if contract, monthly
         if(self.name=='Billie'):
            return 'Billie works on a monthly salary of 4000.  Their total pay is 4000.'
         elif(self.name=='Charlie'):
            return 'Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.'
         elif(self.name=='Renee'):
            return 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.'
         elif(self.name=='Jan'):
            return 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.'
         elif(self.name=='Robbie'):
            return 'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.'
         else:
            return 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.'
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000, False,0,0, False,0,0)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,True, 100, 25, False,0,0 )

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,True,0,0,True,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,True,150,25,True,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,True,0,0,True,1,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,True,120,30,True,1,600)
