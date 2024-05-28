# [Silver V] 포켓몬 GO - 13717 

[문제 링크](https://www.acmicpc.net/problem/13717) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2024년 4월 23일 15:22:00

### 문제 설명

<p>Mirko quickly got tired of Jetpack Joyride and started playing Pokémon GO! on his phone. One of the curiosities of this game is the so-called evolution of Pokémon.</p>

<p>In order to evolve Pokémon of species P<sub>i</sub>, Mirko must provide K<sub>i</sub> candy intended for a Pokémon of that species. After the evolution of that Pokémon, he gets 2 candies back.<br>
Pokémon can evolve only​ with the help of candy intended for their species.</p>

<p>Mirko has N species of Pokémon and M<sub>i</sub> candy for Pokémon of species P<sub>i</sub> and wants to know how many total Pokémon he can evolve.</p>

<p>He also wants to know which Pokémon can evolve the most number of times. If there are multiple such Pokémon, output the one with the smallest Pokédex number. In other words, the one that appears earliest in the input data. </p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 70), the number of Pokémon species.<br>
The following 2N lines contains N sets of data, wherein it holds:</p>

<ul>
	<li>line 2i contains string P<sub>i</sub>, 20 characters long at most, the name of the ith Pokémon species;</li>
	<li>line 2i+1 contains integers K<sub>i </sub>​(12 ≤ K<sub>i</sub> ≤ 400) and M<sub>i </sub>(1 ≤ M<sub>i</sub> ≤ 10<sup>4</sup>), the number of candy necessary for the evolution of one Pokémon of the ith species and the total number of candy Mirko has for Pokémon of the ith species </li>
</ul>

### 출력 

 <p>The first line of output must contain the total number of Pokémon that Mirko can evolve.<br>
The second line of output must contain the name of the Pokémon that can evolve the most number of times. </p>

