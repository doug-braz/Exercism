def translate(text):
    final_phrase = ""
    vowels = ('a','e','i','o','u')

    for word in text.split():
        final_phrase += " "
        if text.lower().startswith(('a','e','i','o','u','xr','yt')):
            final_phrase += word + 'ay'
            continue
        if word[-1].lower() == 'y' and len(word)==2:
            final_phrase += word[::-1]+'ay'
            continue
        if word[1:].lower().startswith('qu'):
            final_phrase += word[3:]+word[:3]+'ay'
            continue
        if (word[0].lower().lower() not in vowels and word[1].lower() not in vowels and word[2].lower() == 'y'):
            final_phrase += word[2:]+word[0:2]+'ay'
            continue
        if word.lower().startswith(('sch','thr')):
            final_phrase += word[3:]+word[:3]+'ay'
            continue
        if word.lower().startswith(('ch','st','th','qu')):
            final_phrase += word[2:]+word[:2]+'ay'
            continue
        if word.lower().startswith(vowels) == False:
            final_phrase += word[1:]+word[0]+'ay'
            continue
        
    return final_phrase[1:]
        
        
    
    
    
    
    #vowels = ('a','e','i','o','u') 
    #if text.lower().startswith(('a','e','i','o','u','xr','yt')):
    #    return text + 'ay'
    #if text[-1].lower() == 'y' and len(text)==2:
    #    return text[-1]+text[0]+'ay'
    #if text[1:].lower().startswith('qu'):
    #    return text[3:]+text[:3]+'ay'
    #if (text[0].lower().lower() not in vowels and text[1].lower() not in vowels and text[2].lower() == 'y'):
    #    return text[2:]+text[0:2]+'ay'
    #if text.lower().startswith(('sch','thr')):
    #    return text[3:]+text[:3]+'ay'
    #if text.lower().startswith(('ch','st','th','qu')):
    #    return text[2:]+text[:2]+'ay'
    #if text.lower().startswith(vowels) == False:
    #    return text[1:]+text[0]+'ay'


