amount = int(input("enter amount: "))

Yearly_rate = int(input("enter rate: "))

Duration = int(input("enter yearly duration: "))

Monthly_Duration = Duration *12

Monthly_rate = Yearly_rate /100/12

Rate =  (1 + Monthly_rate)**120

cal = Monthly_rate * Rate

Division = (1 + Monthly_rate)**120 

Divide = Division - 1

Calculation = cal / Divide

Monthly_repayment = amount * Calculation

print(Monthly_repayment)