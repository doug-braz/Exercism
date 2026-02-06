def label(colors):
    COLOR_CODE = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    resistance = (COLOR_CODE.index(colors[0])*10 + COLOR_CODE.index(colors[1])) * 10 ** COLOR_CODE.index(colors[2])
    if str(resistance).endswith('000000000'):
        return f'{int(resistance/1000000000)} gigaohms'
    if str(resistance).endswith('000000'):
        return f'{int(resistance/1000000)} megaohms'
    if str(resistance).endswith('000'):
        return f'{int(resistance/1000)} kiloohms'
    return f'{resistance} ohms'
    

