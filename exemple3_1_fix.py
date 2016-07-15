balance=float(input('Enter outstanding balance on the credit card in $:\n'))
interest=float(input('Enter annual interest rate in %:\n'))/100
minpayt=0
balancet=0
while balance-balancet<=balance:
    minpayt+=10
    balancet=balance
    for x in range (1,13):
        ipay=round((interest/12*balancet),2)
        ppayd=round((minpayt-ipay),2)
        balancet=round((balancet-ppayd),2)
        if balancet<=0:
            break
print ('RESULTS\nMonthly payment to pay off debt in 1 year:',minpayt,
'\nNumber of months needed:',x,'\nBalance:',balancet)
