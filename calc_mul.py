#!/usr/bin/python3
                
def calc(A,B):
        ax=str(A)
        bx=str(B)
        if ax.isdigit() and bx.isdigit():
                a=float(ax)
                b=float(bx)
                if 0<a and a<b and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
