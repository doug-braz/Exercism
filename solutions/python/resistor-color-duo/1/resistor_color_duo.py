def value(colors):
    COLOR_VALUES = ['black','brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    code = ""
    counter = 0
    
    for color in colors:
        code += str(COLOR_VALUES.index(color))
    return int(code[:2])
