# [Bronze III] 다음수 - 4880 

[문제 링크](https://www.acmicpc.net/problem/4880) 

### 성능 요약

메모리: 109108 KB, 시간: 144 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 4월 9일 15:35:43

### 문제 설명

<p>According to Wikipedia, <em>an arithmetic progression (AP)</em> is a sequence of numbers such that the diﬀerence of any two successive members of the sequence is a constant. For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common diﬀerence 2. For this problem, we will limit ourselves to arithmetic progression whose common diﬀerence is a non-zero integer.</p>

<p>On the other hand, <em>a geometric progression (GP)</em> is a sequence of numbers where each term after the ﬁrst is found by multiplying the previous one by a ﬁxed non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.</p>

<p>Given three successive members of a sequence, you need to determine the type of the progression and the next successive member.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each case is speciﬁed on a single line with three integers (−10,000 < a1, a2, a3 < 10,000) where a1, a2, and a3 are distinct. The last case is followed by a line with three zeros.</p>

### 출력 

 <p>For each test case, you program must print a single line of the form:</p>

<pre>XX v</pre>

<p>where <strong>XX</strong> is either <strong>AP</strong> or <strong>GP</strong> depending if the given progression is an <u>A</u>rithmetic or <u>G</u>eometric <u>P</u>rogression. v is the next member of the given sequence. All input cases are guaranteed to be either an arithmetic or geometric progressions.</p>

