# [Bronze I] 이진수 덧셈 - 2729 

[문제 링크](https://www.acmicpc.net/problem/2729) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 4월 9일 15:11:02

### 문제 설명

<p>Adding binary numbers is a very simple task, and very similar to the longhand addition of decimal numbers. As with decimal numbers, you start by adding the bits (digits) one column at a time, from right to left. Unlike decimal addition, there is little to memorize in the way of rules for the addition of binary bits: </p>

<p>0 + 0 = 0 <br>
1 + 0 = 1 <br>
0 + 1 = 1 <br>
1 + 1 = 10 <br>
1 + 1 + 1 = 11</p>

<p>Just as with decimal addition, when the sum in one column is a two-bit (two-digit) number, the least significant figure is written as part of the total sum and the most significant figure is "carried" to the next left column. Consider the following examples: </p>

<p><img alt="" src="" style="height:120px; width:620px"></p>

<p>The addition problem on the left did not require any bits to be carried, since the sum of bits in each column was either 1 or 0, not 10 or 11. In the other two problems, there definitely were bits to be carried, but the process of addition is still quite simple. </p>

### 입력 

 <p>The first line of input contains an integer N, (1 <= N <= 1000), which is the number of binary addition problems that follow. Each problem appears on a single line containing two binary values separated by a single space character. The maximum length of each binary value is 80 bits (binary digits). Note: The maximum length result could be 81 bits (binary digits). </p>

### 출력 

 <p>For each binary addition problem, print the problem number, a space, and the binary result of the addition. Extra leading zeroes must be omitted. </p>

