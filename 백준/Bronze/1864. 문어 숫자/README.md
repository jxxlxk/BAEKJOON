# [Bronze II] 문어 숫자 - 1864 

[문제 링크](https://www.acmicpc.net/problem/1864) 

### 성능 요약

메모리: 109240 KB, 시간: 116 ms

### 분류

사칙연산, 구현, 수학, 문자열

### 제출 일자

2024년 4월 8일 20:31:55

### 문제 설명

<p>Certain rows of ripple patterns in ocean-floor sand, limited to areas of the sea with very weak currents and low numbers of bottom-crawling creatures, have long puzzled oceanographers. In a recent discovery certain to revolutionise the field of animal linguistics, marine biologists have realised that these patterns are made by octopuses and represent a numbering system. Though as yet they can only speculate as to what the octopuses might be counting, they have succeeded in decoding the numbering system.</p>

<p>The digits used by the octopuses and the ripple patterns that represent them are quite unusual by land-based standards. Researchers have agreed to use the following typewriter symbols to represent corresponding similarly-shaped ripple patterns, and have determined their numeric values, as follows:</p>

<p>- represents 0<br>
\ represents 1<br>
( represents 2<br>
@ represents 3<br>
? represents 4<br>
> represents 5 <br>
& represents 6<br>
% represents 7<br>
/ represents −1</p>

<p>Marine exo-neurologists are particularly excited by the negative digit, and hope that this new insight into cephalopod neurology will lead to significant advances in their science, which is in its infancy.</p>

<p>As you might expect, the octopus system is base 8 in which each place value is 8 times the value to its right, as in the following examples:</p>

<p>(@& is 2 × 8<sup>2</sup> + 3 × 8 + 6 = 158<br>
?/-- is 4 × 8<sup>3</sup> + −1 × 8<sup>2</sup> + 0 × 8 + 0 = 1984<br>
/(\ is −1 × 8<sup>2</sup> + 2 × 8 + 1 = −47</p>

<p>Your task is to take octopus numbers and represent them as standard base 10 numbers.</p>

### 입력 

 <p>Input consists of octopus numbers, one per line. Each number consists of a sequence of between one and eight octopus digits. A single ‘#’ on a line by itself indicates the end of input. This line should not be processed.</p>

### 출력 

 <p>Output consists of the corresponding decimal numbers, one per line.</p>

