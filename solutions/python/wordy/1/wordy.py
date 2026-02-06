def answer(question):
    # Changing all to lower case to facilitate comparisons
    question = question.lower()

    # Defining operations
    operations = {
        'plus':'+',
        'minus':'-',
        'multiplied':'*',
        'divided':'/',
    }

    # Defining useless words (that either are in all questions, or that doesn't affect final result) and removing int from the question text
    USELESS_WORDS = ['what is', 'by', '?']

    for word in USELESS_WORDS:
        question = question.replace(word, '')

    # Now only numbers and names of operations remain

    # Since no operation's name has been substituted by its symbol, all minus signs here are from negative numbers. Let's put them into parentheses before substituting the operations for their symbols
    
    # After doing that, it's time to replace the operations for their symbol counterparts

    for word in question.split():
        if word.startswith('-'):
            question = question.replace(word, '('+word+') ', 1) # Puts negative numbers inside parentheses
        elif word in operations:
            question = question.replace(word, operations[word]) # Substitutes operation names for their symbol
        elif not word.isnumeric(): # Checks if the word is a text of any sort. If so, it's supposed to be an unknown operation
            raise ValueError('unknown operation')
            
    # All valid operations have numbers in odd positions, and operations in even positions. In order to check for that, the following for checks if all numbers are in odd positions.

    for index, word in enumerate(question.split()):
        if (index+1) % 2 != 0 and word.strip("()").replace('-','').isnumeric() == False:
            raise ValueError('syntax error')

    # If there are no question text left, or the number of elements in the  question is even, it is supposed to be a syntax error
    if question == '' or len(question.split())%2 == 0:
        raise ValueError('syntax error')

    # Now we are left only with the operation to be calculated. Since operations are to be done in the order they appear in the text, as proposed, eval can't be directly employed. To do so, the operations are done one by one, from left to right, considering one operation to be 2 numbers and an operator.


    while len(question.split()) >= 3:
        question = str(eval(' '.join(question.split()[:3]))) + ' '.join(question.split()[3:])
    result = eval(question)
    return result
