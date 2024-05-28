# [Bronze II] 팬케이크 사랑 - 2520 

[문제 링크](https://www.acmicpc.net/problem/2520) 

### 성능 요약

메모리: 109108 KB, 시간: 140 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2023년 11월 21일 16:27:40

### 문제 설명

<p>A filled pancake consists of a pancake and its filling. In this problem, you will be given a list of ingredients you have and your task is to prepare as many filled pancakes as possible.</p>

<p>Given 8 cups of milk, 8 egg yolks, 4 tablespoons of sugar, 1 teaspoon of salt, and 9 cups of flour, we can prepare 16 pancakes. For the purpose of this problem, we assume that these quantities scale arbitrarily: for any x ≥ 0, if you have x times as much of every ingredient, you can prepare ⌊16x⌋ pancakes.</p>

<p>Given the necessary ingredients, you can prepare the following fillings:</p>

<ul>
	<li>banana pancake: 1 banana</li>
	<li>strawberry pancake: 30 g of strawberry jam</li>
	<li>chocolate pancake: 25 g of chocolate spread</li>
	<li>walnut pancake: 10 walnuts</li>
</ul>

<p>Banana pieces can be combined. For example, you can use three pieces of 1/3 banana each to create a banana pancake.</p>

### 입력 

 <p>The first line of the input file contains an integer t specifying the number of test cases. Each test case is preceded by a blank line. Each test case consists of two lines.</p>

<p>The first line of a test case contains five integers c<sub>m</sub>, y, s<sub>su</sub>, s<sub>sa</sub>, and f, meaning that you have c<sub>m</sub> cups of milk, y egg yolks, s<sub>su</sub> tablespoons of sugar, s<sub>sa</sub> teaspoons of salt, and f cups of flour.</p>

<p>The second line contains four integers b, g<sub>s</sub>, g<sub>c</sub>, and w, meaning that you have b bananas, g<sub>s</sub> grams of strawberry jam, g<sub>c</sub> grams of chocolate spread, and w walnuts.</p>

<p>All quantities are between 0 and 10<sup>6</sup>, inclusive.</p>

### 출력 

 <p>For each test case, output a single line containing a single integer – the maximum number of filled pancakes you can prepare.</p>

