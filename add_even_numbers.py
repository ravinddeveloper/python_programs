

# add up all the  even number bw 100 to 200


def add_even_numbers():
	start_num = 100
	end_num = 200
	current_num = start_num
	total_sum = 0 
	while current_num <= end_num:
		if current_num % 2 == 0:
			total_sum += current_num
			current_num +=1
	print("Sum of even numbers between 100 and 200:", total_sum)	  
     
        
add_even_numbers()
       