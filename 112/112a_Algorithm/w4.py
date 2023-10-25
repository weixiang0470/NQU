def _each(fc,a,i):
    if i < len(a):
        if fc(a[i]):out(a[i])
        _each(fc,a,i+1)
        
out = lambda x:print(x)

if __name__ == "__main__" :
    a=0
    for i in range(1,6):
        if i%2==1:
            print(f'i={i}')

    array = [1,2,3,4,5]
    _each(lambda x:x%2==1,array,0)


