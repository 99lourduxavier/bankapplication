import random
accno=int(input("enter the account number:"))
gmail=input("enter the gmail:")
r='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 
if r in gmail: 
    print("valid gmail:",gmail)
    break
else:
    print("please,enter valid gmail")
    continue
mobno=int(input("enter the mobno:")) 
if len(mobno)!=10 or mobno[0]!=9:
    print("please,enter valid mobile no")
    continue
else: 
    print("mobno:",mobno)
    break
psd=int(input("enter the password:"))
l=len(psd)
if l!=6:
    print("password must be atleast 6 characters:")
    continue
else:
    print("password valid")
    break
y=input("1.balance/2.withdrawl/3.deposit/4.ministatement") 
print(y) 
ch=int(input("enter your choice:")) 
if ch=="1":
    balance()
if ch=="2": 
    withdrawl()  
if ch=="3":
    deposit()
if ch=="4":
    ministatement()      
def balance():    
    a=random.randint(2000,3000) 
    print("accno:",a)
    balan=9000  
    print("available balance :",balan) 
    balance() 
def withdrawl(): 
    minbal=5000 
    withamt=int(input("enter the withdrawl amount:")) 
    temp=balan+minbal 
    if withamt>temp:
        balan=balan-withamt 
        print("amount withdrawled:") 
        withdrawl()  
def deposit():
    dep=int(input("amount to be deposited:")) 
    deplist=[] 
    deplist.append(dep) 
    print("amount has been added:")
    deposit() 
def ministatement(): 
    print("gmail:",gmail) 
    print("accno:",a) 
    print("balance:",balan)
