loan_amt=15000
year=3
anual_interest_rate=3

def monthly_payment(amt,time,rate):
   monthly_payment = (amt*(1 + rate/100)**time)
   return monthly_payment
  

total_amount =monthly_payment(loan_amt,year,anual_interest_rate)
print("total amount including interest is : ",round(total_amount))
print("interest amount : ",round(total_amount-loan_amt))
print("monthly payable : ",round(total_amount/(year*12)))
