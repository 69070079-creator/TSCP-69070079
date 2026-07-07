"""main"""
total = int(input())
charge = total * 0.10
if charge < 50:
    charge = 50.0
elif charge > 1000:
    charge = 1000.0
a = total + charge
vat = a * 0.07
bill = a + vat
print(f"{bill:.2f}")
