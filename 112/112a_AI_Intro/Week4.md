# **Classifier**

OneR
- Classify with only one attribute
- Rule: 
    - 計算每個類值出現的頻率
    - 找到最頻繁出現的類值
    - 使這個規則由此屬性值中最多的類值組成
    - 對資料集的每一個屬性重複以上的動作，然後選擇錯誤率最低的屬性

Overfitting
- Data of a certain category having too much, others insufficient (某一類的資料過多，另一類不足)
- A classifier fit training set too well (太過於符合訓練資料的分類器)
    - Computer only know learned data, if not learned will easily give wrong result (電腦只會學習過的資料，沒學過的很容易誤判)
    - Will get **high accuracy** if use **training set**, but **others** will be **low accuracy**. EX: Use trainnig set get 100% accuracy, but Cross-validation get only 75% accuracy

Naive Bayes
- Base on Probability
- Assumptions:
    - all attritube are important
    - all attribute are independent
- If some attribute of value have 0, will add 1 to every attribute value(zero-frequency problem)

Decision Tree
- Ideal tree is ony have 2 branch with 1 yes 1 no
- Goal : Minimum tree
- Entropy($p_1,p_2,...,p_n$) = $-p_1logp_1-p_2logp_2-...-p_nlogp_n$
    - log base 2

Pruning
- J48
    - minNumObj
    - confidenceFactor : the smaller the more pruning
    - subtreeRaising : True will consider the subtree raising operation when prunning
- why : unpruned decision tree may due to overfitting to training set, sometime prunning the decision tree will have better result

Nearest-neighbor(instance-based)
- Lazy learning
- Find the nearest "class" in training set (尋找訓練資料集中與新實例**最相似**的實例)
- 相似性函數
    - Euclidean distance
    - Manhattan distance or city block distance
    - Nomeric attribute : **different attribute value** -> distance == 1, if **same attribute value** -> distance == 0
    - sigmoid function, normalization distance into **0~1**

Ideal
- Ideal classifier is use relatively less attribute to identify efficiently (相對少的屬性並且足夠去辨識)

TPR(True Positive Rate)
- $True Positives \over ALl Positive$

FPR(False Positive Rate)
- $False Positives \over All Negative$

Percision
- $TP \over (TP+FP)$

Recall
- $TP \over (TP+FN)$

Data set
- kaggle
- uci 