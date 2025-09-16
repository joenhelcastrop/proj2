def convert_to_peso(dollars):
    return dollars * 57.17

def convert_to_yen(dollars):
    return dollars * 146.67

d1 = float(input("Enter currency in ($): "))
p1 = convert_to_peso(d1)
y1 = convert_to_yen(d1)

d2 = float(input("Enter currency in ($): "))
p2 = convert_to_peso(d2)
y2 = convert_to_yen(d2)

d3 = float(input("Enter currency in ($): "))
p3 = convert_to_peso(d3)
y3 = convert_to_yen(d3)

print("\nDollar($)\tPhil Peso(P)\tJpn Yen(Y)")
print(round(d1), "\t\t", round(p1), "\t\t", round(y1))
print(round(d2), "\t\t", round(p2), "\t\t", round(y2))
print(round(d3), "\t\t", round(p3), "\t\t", round(y3))

