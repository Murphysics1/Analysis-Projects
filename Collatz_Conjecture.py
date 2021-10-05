# -*- coding: utf-8 -*-

i = 0

def main():
    num = int(input('Starting Number: '))
    conj(num)    

def conj(num):
    
    global i
    
    if num == 1:
        print(f'{num}') 
        print(f'Reached 1 in {i} steps')
        
    else:
        if num%2 == 0:
            print(f'{num}')
            x = int(num/2)
            i+=1
            conj(x)
        
        else:
            print(f'{num}')
            x = int(3*num + 1)
            i+=1
            conj(x)

if __name__ == '__main__':
    main()