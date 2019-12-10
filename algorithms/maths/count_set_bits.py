# recursive approach to find the number of set 
# bits in binary representation of positive integer n 
  
def count_set_bits(n): 
     
    if (n == 0): 
        return 0
  
    else: 
        return (n & 1) + count_set_bits(n >> 1) 
          
# Get value from user 
n = 41
  
# Function calling 
print(count_set_bits(n))

