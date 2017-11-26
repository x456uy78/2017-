def pyramid(n):
    for i in range(0,n,1):
        print(" "*(n-i)+"*"*(1+2*i))
        
        
def multiplication_table(m, n):
    for i in range(1,10):
        for j in range(m,n+1):
            print("%d x %d = %d\t" % (j,i,i*j),end='')
        print('')
    print('\n')