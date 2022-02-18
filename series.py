def slices(series, length):
    sere = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length <= 0:
        raise ValueError("slice length cannot be negative")
    elif len(series) == 0:
        raise ValueError("series cannot be empty")
    elif length == '':
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        lst_ins = list(series)
        sere_temp = ''
        while len(lst_ins) >= length:
            
            for i in range(length):
                sere_temp = sere_temp + lst_ins[i]
            lst_ins.pop(0)
            sere.append(sere_temp)
            sere_temp = ''
        
    return sere
        
            
