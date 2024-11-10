def convert_(temperatura):
    return (temperatura * (9 / 5)) + 32

def main():
    temperatura = float(input())
    print(f'{convert_(temperatura):.2f}')
    
if __name__ == '__main__':
    main()
    
