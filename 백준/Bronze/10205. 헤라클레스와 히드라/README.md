# [Bronze III] 헤라클레스와 히드라 - 10205 

[문제 링크](https://www.acmicpc.net/problem/10205) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2023년 4월 4일 16:04:04

### 문제 설명

<p>Heracles<sup>1</sup> was a famous tragic hero in Greek mythology. He was a half-god illegitimate child of Zeus and Hera, hated by his mother who did whatever she could to make his life hell, and preferably get him killed. He possessed superhuman strength and high intelligence, but was also given to madness, killing his children, many of his teachers, bosses, lovers, and others. He is famous for 12 labors he had to perform for his archenemy Eurystheus, as a punishment for killing his own children.</p>

<p>The second of these labors involved killing the Lernaean Hydra, a giant multi-headed super-venomous<sup>2</sup> serpent bred specifically by Heracles’s mother for the purpose of killing Heracles (and a few innocent people). The big problem with killing the hydra was that as soon as one chopped off a head, two new ones sprouted up in its place, and the hydra was alive as long as it had at least one head. Heracles’s nephew Iolaus eventually realized that the heads did not regrow when the stump was cauterized (scorched with a firebrand).</p>

<p>In this problem, you will be given a sequence of actions that Heracles and Iolaus took, which is either just chopping off a head, or chopping+cauterizing. You are to determine how many heads will be left at the end.</p>

<p><sup>1</sup>known to Romans as “Hercules”</p>

<p><sup>2</sup>In fact, Heracles used the venom to dip his arrows and kill a few other monsters with it later.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of a data set is an integer 1 ≤ h ≤ 50, the initial number of heads of the hydra. The second line is a string of at most 100 characters, each either a lowercase ‘c’ (for chopping off a head without cauterizing), or ‘b’ (for chopping with cauterizing).</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number.</p>

<p>Then, on a line by itself, print the number of heads the hydra has at the end of the sequence. The inputs will never be such that Heracles chops off more heads than the hydra has.</p>

<p>Each data set should be followed by a blank line.</p>

