Garbage Data
- Need to take out or process and turn into usefull data  before using it
- Ex : Thailand's year need to minus 543 to turn into the common year unit(2566-543=2023)

監督式學習
- 收集歷史資料
- 預測結果

discrete(nominal data)
- hot, mild, cold
- classification problem

continuous(numeric)
- 25.3, 25.6, ....
- regression problem
- curve fitting

Preprocess
- Data cleaning

**.arff** file format
- Start with `%` is instruction/info of data
- Start with @
    - @relation Glass : Relation's name **Glass**
    - @attribute 'RI' numeric : Attribute name **RI** type is numeric
    - @attribute 'Type' {'Y', 'N', 'unknown'} : Attribute name **Type**, type is nominal and have 3 attribute(Y,N,unknown)
    - @data : data will put after this

Attribute
- More attribute $\neq$ More accurate
    - If data have no relation with output, it could influence the output in a wrong way
    - If data collect incorrectly also could affect the result badly
