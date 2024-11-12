def main():
    n = int(input())
    a = 0
    b = 1
    c = 0
    cont = 0
    
    while cont < n:
        if cont == n - 1:
            print(f'{c}', end='')
        else:
            print(f'{c}', end=', ')
        
        a = b
        b = c
        c = a + b
        cont += 1
        
if __name__ == "__main__":
    main()
