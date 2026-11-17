### Assignment oo_inheritance ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################



# Implement the whole functionality for this assignment in this file!
# Modify and add to the provided code!

class Account:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = float(0)  # einfach self.__balance = 0.0 würde auch gehen

    def __str__(self):
        return f"{self.owner}, Guthaben: {self.__balance}"

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError("Keine negativen Werte erlaubt")
        
            self.__balance += amount
            return True #die ganzen True und False brauchen wir für transfer()

        except ValueError as error:
            print(f"Fehler: {error}")
            return False


    def withdraw(self, amount):        
        try:           
            if amount < 0:
                raise ValueError("Keine negativen Werte erlaubt")
        
            self.__balance -= amount

            return True

        except ValueError as error:
            print(f"Fehler: {error}")
            return False



    #lesender Zugriff auf Balance - property ist der Getter dafür (private variable __)
    @property
    def balance(self):
        return self.__balance
    
    #ohne staticmethod bräuchte man self und müsste für die ausgabe zuerst ein objekt erstellen
    @staticmethod
    def transfer(amount, fromAccount, toAccount):
        if fromAccount.withdraw(amount):        #gibt True/False zurück UND führt die Abbuchung bei True gleich aus!
            toAccount.deposit(amount)
        
    
        
    
class StudentAccount(Account):   
    def withdraw(self, amount):
        try:
            if self.balance - amount <0: #self.balance: ist die !Property! aus der hauptklasse (auf __balance kann hier nicht zugegriffen werden weil private
                raise ValueError("Nicht genügend Geld am Konto")
            
            return super().withdraw(amount) #ruft withdraw auf UND! gibt True oder False zurück

        except ValueError as error:
            print(f"Fehler: {error}")
            return False
        
           
'''
a = Account("Hans")
print(a)
a.deposit(2000)
print(a)
a.withdraw(4000)
print(a)
print(a.balance)

b = StudentAccount("Fraunz")
print(b)
b.deposit(2000)
print(b)
b.withdraw(-1)
b.withdraw(6000)
print(b)
print(b.balance)

Account.transfer(1000, a, b)
print(a.balance)
print(b.balance)

Account.transfer(1000, a, b)
print(a.balance)
print(b.balance)

Account.transfer(-1000, a, b)
print(a.balance)
print(b.balance)

Account.transfer(10000, b, a)
print(a.balance)
print(b.balance)
'''
    

##################### Demo ############
'''
a1 = Account("A")
a2 = Account("B")
a1.deposit(100)
a2.withdraw(100)
print(a1)
print(a2)
Account.transfer(600, a1, a2)
print(a1)
print(a2)

print(a1.owner)
print(a1.balance)

#a1.balance = 999   ##this should not be allowed!

s1 = StudentAccount("S")
s1.deposit(100)

try:
  Account.transfer(500000, s1, a1)
except:
  print("Fehler") ##TODO where should the error message come from?
print(s1)
print(a1)

'''