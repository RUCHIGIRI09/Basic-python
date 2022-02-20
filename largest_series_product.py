def largest_product(series, size):
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif not series.isdigit() and len(series) > 0:
        raise ValueError("digits input must only contain digits")
        
    def multiply(int_list):
        p = 1
        for num in int_list:
            p *= num
        return p
    
    list = [int(char) for char in series]
    return max([multiply(list[i:i+size]) for i in range(len(series) - size + 1)])