balance=float(input('Enter outstanding balance on the credit card in $:\n'))
interest=float(input('Enter annual interest rate in %:\n'))/100
minpay=float(input('Enter minimum monthly payment rate in %:\n'))/100
x=1
tpay=0
for x in range (1,13):
    ipay=round((interest/12*balance),2)
    minpayt=round((minpay*balance),2)
    ppayd=round((minpayt-ipay),2)
    balance=round((balance-ppayd),2)
    print('Month:',x,'\nMinimum monthly payment:',minpayt,'\nInterest paid:',ipay,'\nPrincipal paid:',ppayd,'\nRemaining balance:',balance)
    tpay=round((tpay+minpayt),2)
    x+=1
print ('RESULTS\nTotal amount paid:',tpay,'\nRemaining balance:',balance)
