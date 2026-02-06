def convert(number):
       
    return ''.join( sound for index, sound in {3: 'Pling', 5: 'Plang', 7: 'Plong'}.items() if number % index == 0 ) or str(number)

    #if number % 3 == 0:
    #    raindrop += 'Pling'
    #if number % 5 == 0:
    #    raindrop += 'Plang'
    #if number % 7 == 0:
    #    raindrop += 'Plong'
    #    
    #return raindrop if raindrop else str(number)

