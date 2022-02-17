def is_armstrong_number(number):
    
    copy_of_numbers = number
    for sub_number in str(number):
        
        copy_of_numbers -= int(sub_number) ** len(str(number))
    return copy_of_numbers == 0