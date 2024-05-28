# [Bronze II] 비교 연산자 - 5656 

[문제 링크](https://www.acmicpc.net/problem/5656) 

### 성능 요약

메모리: 113388 KB, 시간: 848 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 15일 22:47:33

### 문제 설명

<p>The relational operators in C programming language are shown in the table below. Of course the last two are also known as equality operators. </p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th style="width:10%">Operator</th>
			<th style="width:20%">Meaning</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>></td>
			<td>Greater Than</td>
		</tr>
		<tr>
			<td>>=</td>
			<td>Greater Than or Equal to</td>
		</tr>
		<tr>
			<td><</td>
			<td>Less than</td>
		</tr>
		<tr>
			<td><=</td>
			<td>Less than or Equal</td>
		</tr>
		<tr>
			<td>==</td>
			<td>Equal</td>
		</tr>
		<tr>
			<td>!=</td>
			<td>Not Equal</td>
		</tr>
	</tbody>
</table>

<p>These operators compare the value of the two operands it is working on (The value on its left and the value on its right) and returns true or false (one or zero). For example value of 2 > 3 is interpreted as “false” (As 2 is actually less than 3), value of 3 != 4 is interpreted as true and value of 3 >= 3 is also interpreted as true. You have to find out this interpretation using a program.</p>

### 입력 

 <p>The input file contains around 12000 line of input. Each line contains two integers a and b separated by an operator “>”, “>=”, “<”, “<=”, “==” or “!=”. Input is terminated by a line which contains an “E” instead of the operators. Note that there is also a space between any operator and operand. You can assume (-10000 ≤ a, b ≤ 10000).</p>

### 출력 

 <p>For each line of input produce one line of output. This line contains the serial of output followed by a string “true” or “false” (without the quotes) which denotes how the expression is interpreted in C language. Look at the output for sample input for details.</p>

