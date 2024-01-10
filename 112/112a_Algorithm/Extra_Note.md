# **Chap 1 : Computational Thinking(CT)**
- A thinking way to solve problem throughth computer logic, an ability to turn computation into abstraction
- Proposed by **Jeannette M.Wing** in 2006 

## Computational Thinking for Educators by Google
1. Decomposition
    - A problem can be decompose into smaller subproblem
    - Solve all the subproblem == solve the problem
2. Pattern Recognition
    - Get the **feature/rule** from a large data set to **identify/classify** the data set
    - When the subproblem/other problem having the same feature then we solve it with the same solution
3. Pattern Generalization and Abstraction
    - To **filter/ignore** unnecessary feature/rule 
    - Focus on the more important feature/rule to concretize the problem
    - ex: Mind map (Tony Buzan in 1970)
4. Algorithm
    - A well design plan to solve the problem
    - A program to solve the problem in a finite step

## Requirement of Algorithm
1. Input
    - 0 or multiple input data, all input data need a clear defination
2. Output
    - At least 1 ouput
3. Definiteness
    - Every step need to have clear defination
4. Effectiveness
    - Every step need to be clear and effective, user can get the result by itself
5. Finiteness
    - The program end in finite step
    
# **Chap 2 : Data Structure**
## Data
- Combination of Word, Number, Symbol, Garph, ...
- Data Processing : Data -> Information
## Program
- Data Structure determine can the program do it's task effectively and rapidly
- Algorithm determine can the program solve the problem correctly and clearly
- Data Structure + Algorithm == program execute efficiently 
## Data type
- Primitive Data Type
    - Also call Scalar Data Type
    - Integer, Float, Bool, Double, Character, ...
- Structured Data Type
    - Also call Virtual Data Type
    - String, Array, Pointer, List, File, ...
- Abstract Data Type
    - ADT : Set of Value + Operation + Attribute
    - EX, Stack : Integer/Float/String + Push/Pop + Last_in_First_out
## Common Data Structure
- Array
    - Static, Contiguous Allocation, use index to get element
    - Fixed memory size, may cause to waste of memory, initial an array with size
    - Benefits : easy design, time fix when read and modify an element in an array 
    - Bads : When insert and delete data in an array will need to move large data(all element in an array)
```
Array[5]={"a","b","c","d","e"};
print(Array[0]) # a
print(Array[3]) # d
```
- Matrix
    - Can represent by 2D-Array
    - A[3][3]    

$$ A =
\left[
\begin{matrix} 
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} 
\end{matrix}
\right]_{3*3}
$$

- Sparse Matrix
    - If a matrix have many "0" element called a sparse matrix, ex:

$$ B =
\left[
\begin{matrix} 
25 & 0 & 0 & 32 & 0 & -25 \\
0 & 33 & 77 & 0 & 0 & 0 \\
0 & 0 & 0 & 55 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
101 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 38 & 0 & 0 & 0 
\end{matrix}
\right]_{6*6}
$$
- can use 3-tuple data structure to represent the B matrix 
    - A[0,1] : store the **row** of B matrix
    - A[0,2] : store the **column** of B matrix
    - A[0,3] : store the **sum** of the none "0" element
    - All none "0" element represent by **(i,j,item-value)**
```
   | 1 | 2 |  3  |
   |-------------|
 0 | 6 | 6 |  8  | 
 1 | 1 | 1 |  25 | 
 2 | 1 | 4 |  32 |
 3 | 1 | 6 | -25 |
 4 | 2 | 2 |  33 |
 5 | 2 | 3 |  77 |
 6 | 3 | 4 |  55 |
 7 | 5 | 1 | 101 |
 8 | 6 | 3 |  38 |
```
- Operation in Matrix
    - Addition 
        - All matrix need to have the same size
        - $c_{ij} = a_{ij} + b_{ij}$
    - Multiply
        - Need satisfy $ A_{m*n} * B_{n*p} == C_{m*p}$
        - $c_{11} = a_{11}*b_{11}+a_{12}*b_{21}+...+a_{1n}*b_{n1}$
        - ...
        - $c_{1p} = a_{11}*b_{1p}+a_{12}*b_{2p}+...+a_{1n}*b_{np}$
        - ...
        - $c_{m1} = a_{m1}*b_{11}+a_{m2}*b_{21}+...+a_{mn}*b_{n1}$
        - ...
        - $c_{mp} = a_{m1}*b_{1p}+a_{m2}*b_{2p}+...+a_{mn}*b_{np}$
    - Transpose Matrix
        - Change the row with column of the origin matrix
        - If $A^t$ is the transpose matrix of $A$, then $A^t[i,j]=A[j,i]$

$$ 
A =
\left[
\begin{matrix} 
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
\right]_{3*3}
$$
$$ 
A^t =
\left[
\begin{matrix} 
1 & 4 & 7 \\
2 & 5 & 8 \\
3 & 6 & 9
\end{matrix}
\right]_{3*3}
$$

- Linked List
    - Dynamic data structure, data store in memory randomly
        - Ask a memory space from OS when inserting data
        - After deleted data, return memory space(free) to OS
    - Benefits : Insert and delete data is convenient
    - Bads : Traversal and search elements need to do it sequentially
    
