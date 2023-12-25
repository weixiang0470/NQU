離散化
- 溫度，年齡，。。。
- 離散化數字屬性
    - 等份裝箱（Equal-width bining）: 1月，2月，用某區間來裝箱，每個箱子有可能數量差很多
    - 等頻裝箱(Equal-frequency bining) : 每個箱子的數量是一樣的
    - K均衡區間離散法(proportional k‐intervaldiscretization) : 箱子的數量 = $\sqrt{實例的數量}$
- Weka  
    - Fliters -> unsupervised -> attribute -> Discretize
        - bins : 箱子數量
        - makeBinary : 離散為二元屬性
        - useEqualFrequency : 使用等頻裝箱

- trainig set
```
@relation 'testing text'

@attribute Text string
@attribute type {yes,no}

@data
'Oil platforms extract crude oil',?
'Canola oil is supposed to be healthy',?
'Iraq has significant oil reserves',?
'There are different types of cooking oil',?
```
- test set
```
@relation 'testing text'

@attribute Text string
@attribute type {yes,no}

@data
'Oil platforms extract crude oil',?
'Canola oil is supposed to be healthy',?
'Iraq has significant oil reserves',?
'There are different types of cooking oil',?
```

ROC Area & PRC Area
- 包越多越好（越逼近1越好）

Citation || Cite
- 如何引用論文
