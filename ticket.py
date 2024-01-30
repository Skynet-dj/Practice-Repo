#This program find lottery winners

import random
import time
import blessed
term = blessed.Terminal()

def show(num, digits):
    
    print(term.move_up(3)+term.clear_eos(), end = "")

    print("\r", end = "")
    print("-"*(digits*4+1))

    num = num*(10**(digits-len(str(num))))

    n = 0

    for _ in range(digits):
    
        no = int(num/(10**(digits-n-1)))
        num = num - (no*(10**(digits-n-1)))
        n += 1
    
        print(f"| {no} ", end = "")
        
    print("|")
    print("-"*(digits*4+1))
        

def winners(digits):   
    num = 0  
    dig_ = digits

    while digits > 1:   
        time.sleep(0.1)
        flag = False


        x = random.randint(0,9)

        if random.randint(39,50) ==  49: 
            num = num*10 + x
            digits -= 1
            flag = True          
        else:
            if not flag:
                num = int(num/10)*10 + x
            else:
                num = num*10 + x
                flag = False
                
        show(num, dig_)         

def main():
    
    digits = int(input("\nEnter the number of digits: "))
    no_of_winners = int(input("Enter the number of winners: "))
    print("\n\n\n")
    for _ in range(no_of_winners):
        winners(digits)
    

if __name__ == '__main__' :
    main()           
   
   
