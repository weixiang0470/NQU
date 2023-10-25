```
C(n,k) = C(n-1,k-1)+C(n-1,k)
            取到
```
- 機率與統計 :  很重要,AI裡面用到很多

Hanoi
- n===0 , done
- 先把第n-1從現在柱搬到暫時柱，通過目標柱
- 把第n從從現在柱搬到目標柱
- 最後把n-1從暫時柱搬到目標柱，通過現在柱

Algorithm practice
- [leetcode](https://leetcode.com)

函數式編程
```
fibonacci = lambda n: \
    0 if n == 0 else  \
    1 if n == 1 else  \
    fibonacci(n-1) + fibonacci(n-2)
```
- In **lambda function** can use `\` to have multiple lines(better visualise)
- Can do recursion in **lambda function**
- 將迴圈，if等用函數的形式來編寫程式 
- EX:
```
一般寫法
a=0
for i in range(1,6):
    if i%2==1:
        print(i)
```
```
函數式編程
out = lambda x:print(x)
def _each(fc,a,i):
    if i < len(a):
        if fc(a[i]):out(a[i])
        _each(fc,a,i+1)
if __name__ == "__main__" :
    array = [1,2,3,4,5]
    _each(lambda x:x%2==1,array,0)
```


Bug
```
If = lambda cond, a, b: a if cond else b
Fibonacci = lambda n: \
  If(n<2, n, Fibonacci(n-1)+Fibonacci(n-2))
print('Fibonacci(8)=', Fibonacci(8))

Error output :
RecursionError: maximum recursion depth exceeded while calling a Python object
```
- 函數的參數會先算（直接算）, 所以這只程式會一直呼叫自己**Fibonacci(n-1)**

Solution : 
```
If = lambda cond, a, b: a if cond else b()
Fibonacci = lambda n: \
  If(n<2, n, lambda:Fibonacci(n-1)+Fibonacci(n-2))
print('Fibonacci(8)=', Fibonacci(8))

Output :
Fibonacci(8)= 21
```
- 將IF的第二個參數（用來遞回的）改成函數形式那麼就可以防止遞回先算的情況

**Curry**
```
If  = lambda cond: lambda a: lambda b: a() if cond else b()
Fibonacci = lambda n: \
  If(n<2)(lambda:n)(lambda:Fibonacci(n-1)+Fibonacci(n-2))
print('Fibonacci(8)=', Fibonacci(8))
```
- 將一個函數三個參數拆分成一個一個參數傳三次進去

