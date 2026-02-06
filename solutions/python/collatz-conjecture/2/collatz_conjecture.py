def steps(number:int):
    
    step = number
    complete_set = [step]
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while step != 1:
            step = step / 2 if step % 2 == 0 else step * 3 + 1
            complete_set.append(step)

        return len(complete_set)-1
        
