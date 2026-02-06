def steps(number):
    complete_set = []
    step = number
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while step != 1:
            if step % 2 == 0:
                step = step/2
            else:
                step = step * 3 + 1
            complete_set.append(step)

        return len(complete_set)
        
