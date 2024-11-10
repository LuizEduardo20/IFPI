from math import trunc

def convert_(idade):
    return trunc(idade * 0.5)

def main():
    idade = int(input())
    print(f'{convert_(idade)}')
    
if __name__ == '__main__':
    main()
    
