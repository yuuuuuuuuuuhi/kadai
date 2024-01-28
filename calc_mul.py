import re

def calc(A, B):
    ai, bi = str(A), str(B)
    p = re.compile('^-?\d+(\.\d+)?$')

    if p.match(ai) and p.match(bi):
        a, b = float(ai), float(bi)
        if 1 <= a < 1000 and 1 <= b < 1000:  
            return round(a * b)
    return -1

def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()