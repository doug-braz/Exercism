def value(colors):
    COLOR_VALUES = ['black','brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    return COLOR_VALUES.index(colors[0])*10 + COLOR_VALUES.index(colors[1])
    
    #code = ""
    #counter = 0
    
    #for color in colors:
    #    code += str(COLOR_VALUES.index(color))
    #return int(code[:2])
