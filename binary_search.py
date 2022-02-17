def find(search_list, value):
   
    left_limit = 0
    right_limit = len(search_list)-1
    
    while left_limit <= right_limit:
        
        middle_position = (left_limit + right_limit) // 2
        
        if search_list[middle_position] < value:
            left_limit = middle_position+1
        
        elif search_list[middle_position] > value:
            right_limit = middle_position-1
        else:
            return middle_position
    
    raise ValueError("value not in array")
