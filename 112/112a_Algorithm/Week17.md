文字處理
- 字串比對
- 正規表達式
    - `[0-9]*` : 0個以上的數字
    - `[0-9]+` : 1個以上的數字
    - `[0-9]?` : 0-1個的數字
    - `\.` : 比對 **.**
    - `[0-9]+(\.[0-9]*)?` : 可比對**3.14**或**3**
    - `\d` : [0-9]
    - `\w` : [a-zA-Z0-9_]


myfind.py
```
def myfind(t,s):
    for i in range(len(s)):
        found = True
        for len1 in range(len(t)):
            if s[i+len1] != t[len1]:
                found = False
                break
        if found:
            return i
```

KMP
- 母字串會一直往前進
- 子字串會查看失敗函數，然後看失敗了要從哪裡開始繼續比對
- KMP $O(n)$ 一般字串比對 $O(n^2)$

trie
- 多元樹
- subtree 為 tree 的下一個可能字元 ,ex: `tea`與`teo` 為 `te` 的subtree
```
         --(tea)
       /
(te)--
       \
         --(teo)
```

Patricia trie
- 將trie中的tree省略subtree的開頭(與tree一樣的部分)
    - `a`與`o` 為 `te` 的 subtree
```
         --(a)
       /
(te)--*
       \
         --(o)
```

EX
1. romane
2. romanus
3. ruber
4. rubens
- trie
```
(r)
    -(roma)
        -(romane)
        -(romanus)
    -(rube)
        -(ruber)
        -(rubens)
```

倒排索引
- 決定搜尋到的**文件**
- 假設以下文本
```
T0=0. "it is what it is"
T1=1. "what is it"
T2=2. "it is a banana"
``` 
- 建立反向檔案索引
```
"a" : {2}
"banana" : {2}
"it" : {0,1,2}
"is" : {0,1,2}
"what" : {0,1}
```
- 若我們的搜尋條件為 "what","it","is",那就將搜尋條件的反向索引做AND $(\bigcap)$
```
{0,1} AND {0,1,2} AND {0,1,2} = {0,1}
```

Google
- PR
    - 決定網頁的重要性
        - 一個**重要的網頁**投票給你比起一堆**沒用的網頁**還來的有用
    - 畫圖

圖論
- 有向圖
    - 有方向性
    - 相鄰矩陣，畫圖
        - 密度很高較有效，用一個bit就可以存
    - 連結串列，畫圖
        - 密度較低時使用
- 無向圖
    - 無方向性
- 代理法
    - networkx : python 套件可用於圖論部份

Caesar
- key = 3
    - `attack` -encrypt-> `dwwdfn`

vegenere
- key = 3 , {1,2,3}
    - `attack` 
        - encryption : `a` move 1 , `t` move 2 , `t` move 3 , `a` move 1 , `c` move 2 , `k` move 3
        - `bvwben`

xor
- msg = "hello" , key=3
```
h->ASCII = 0110 1000
key=3    = 0000 0011
encryption : 
    0110 1000 (original)
xor 0000 0011 (key)
-------------- 
    0110 1011 (encrypted)
--------------
xor 0000 0011 (key)
--------------
    0110 1000 (original)
--------------
```
- repeat steps above for all char