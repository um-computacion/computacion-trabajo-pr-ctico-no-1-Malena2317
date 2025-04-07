
def decimal_to_roman(decimal):
    if not (0 < decimal < 4000):
        print ("El numero se encuentra fuera del rango (1-3999)")
        return "Número fuera del rango"
    
    roman_values = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    roman = ""  #aca se guarda el numero romano que se va formando 
    for  value , symbol in roman_values :   # recorre una lista de pares , value es el numero decimal y symbol su respectivo en romano
        while decimal >= value:  # mientras el decimal sea mayor a numero actual se sigue agregando el simbolo romano
            roman += symbol  #agrega el simbolo romano al reusltado final
            decimal -= value  #reste ese valor del numero original 
    return roman


