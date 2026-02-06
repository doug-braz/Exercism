def color_code(color):
    color_values = [
        [0, 'black'],
        [1, 'brown'],
        [2, 'red'],
        [3, 'orange'],
        [4, 'yellow'],
        [5, 'green'],
        [6, 'blue'],
        [7, 'violet'],
        [8, 'grey'],
        [9, 'white']
    ]

    for item in color_values:
        if color.lower() == item[1]:
            return item[0]

def colors():
    color_values = [
        [0, 'black'],
        [1, 'brown'],
        [2, 'red'],
        [3, 'orange'],
        [4, 'yellow'],
        [5, 'green'],
        [6, 'blue'],
        [7, 'violet'],
        [8, 'grey'],
        [9, 'white']
    ]

    all_colors = []
    for item in color_values:
        all_colors.append(item[1])
    return all_colors
    
        
