def ara(name, area, waterarea):

    y = (waterarea * 100)/area
    x = 100 - y
    return(f"Встране {name} - {x} % суши, {y} % водной поверхности")
print(ara("Russia",30,15))

# print(a)
