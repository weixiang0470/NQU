Co-NP
- 無解的非確定圖靈機(會一直跑直到當掉)

e
- $$e=\lim_{n \to \infty} (1 + \frac{1}{n})^n$$
- $\frac{de^x}{dx} = e^x$
- $e^{ix} = cos(x) + i*sin(x)$

史特靈逼近
1. $ln(n!) = ln(1) + ln(2) + ... + ln(n)$
    - $e^{ln(x)} = e^{log_{e}(x)} = x$
    - $n! = e^{ln(n!)}$
2. $ln(n!) = n*ln(n) - n + 1$

微分逼近(數值微分)
- 當微分次數多時，會有誤差蔓延的問題$$\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$$
    - 若使用符號微分則沒這個問題

泰勒級數
- 已知$f(a)$ 求$f(x)$ ($f(a)$靠近$f(x)$)
    - 畫圖
    - $\sqrt(2.1)$
- 不是展開到越高階越好

虛擬機技術
- mov ex,ax => 32bits binary code
    - 用c寫switch case
- 機器指令轉換成其他平台的機器指令
    - x86 的器械碼 -> RISC-V 的器械碼
- VMware
    - 在 x86 平台跑另一種 x86 OS,ex: Windows(x86) 跑 Linux(x86)

Docker
- 容器
- 虛擬檔案系統，網路機制
- 沒有虛擬指令

傅立葉轉換
- 1D 
    - 可以做聲音壓縮
- 2D
    - 圖片壓縮（jpeg）

代數
- 複數
    - 畫圖
    - Conjunction : 1+i -> 1-i