is_done = False
largest_number_yet = None
smallest_number_yet = None

while is_done == False:
    try:
        
    
        
    
        number_at_hand = input("Enter number:")
        if number_at_hand == 'done':
            print('Maximum is ', largest_number_yet)
            print('Minimum is ', smallest_number_yet)
            break 
        num_float = float(number_at_hand)
        if largest_number_yet == None  and smallest_number_yet == None:
            largest_number_yet = num_float
            smallest_number_yet = num_float
            continue           
        if largest_number_yet < num_float:
            largest_number_yet = num_float
        if smallest_number_yet > num_float:
            smallest_number_yet = num_float
        
            
       
    except ValueError:
        print('Invalid input')
     
  