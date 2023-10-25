Boundary Visualizer
- Visualization -> BoundaryVisualizer
- Can plot training tree with the classification decision graph

IBK
- KNN numbers affect the boundary, higher KNN will be more complex(Graph will mixed)

J48
- minNumObj : The higher the more simple tree, but accuracy will be affeced

Linear Regression
- Past
    - Statistic method to find a line that can represent(closed to) all data 
    - $x = w_0 + w_1a_1 + ... + w_ka_k$
- Mean absolute error
    - $|p_1-a_1| + ... + |p_n-a_n| \over n$
- Root mean absolute error
    - $\sqrt{(p_1-a_1)^2 + ... + (p_n-a_n)^2 \over n }$
- Relative absolute error
    - $|p_1-a_1| + ... + |p_n-a_n| \over |a_1-\bar{a}| + ... + |a_n-\bar{a}|$
- Root relative squared error
    - $\sqrt{(p_1-a_1)^2 + ... + (p_n-a_n)^2 \over (a_1-\bar{a})^2 + ... + (a_n-\bar{a})^2}$
- Trend of error become smaller and smaller is called **convergence**

Multi-response linear regression
- Can do classification 
- Each class will have its own regression model
- Example : 
1. Use addClassification(filter) to add an extra class, based on linear regression and output classification set as true
2. Use NumericToNominal(filter) change back to nominal type of output
3. At classify use OneR to predict