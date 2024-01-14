import random
total_filip_number=0
total_head_number=0
total_teal_number=0

number=int(input('How manay flip you went to do ?'))

while total_filip_number<number:
    head_or_teil=random.randrange(0,2)
    
    if head_or_teil==0:
        total_head_number=total_head_number+1
    
    else :
        total_teal_number=total_teal_number+1
    
    total_filip_number=total_filip_number+1
    
print(f'out of coin: {total_filip_number} head {total_head_number} and {total_teal_number}') 
