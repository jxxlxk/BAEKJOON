# [Ruby V] 친구 - 10075 

[문제 링크](https://www.acmicpc.net/problem/10075) 

### 성능 요약

메모리: 3980 KB, 시간: 36 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘

### 제출 일자

2023년 4월 11일 16:09:41

### 문제 설명

<p>We build a social network from n people numbered 0, ... , n-1. Some pairs of people in the network will be friends. If person x becomes a friend of person y, then person y also becomes a friend of person x.</p>

<p>The people are added to the network in n stages, which are also numbered from 0 to n-1. Person i is added in stage i. In stage 0, person 0 is added as the only person of the network. In each of the next n-1 stages, a person is added to the network by a host, who may be any person already in the network. At stage i (0 < i < n), the host for that stage can add the incoming person i into the network by one of the following three protocols:</p>

<ul>
	<li><em>IAmYourFriend</em> makes person i a friend of the host only.</li>
	<li><em>MyFriendsAreYourFriends</em> makes person i a friend of each person, who is a friend of the host at this moment. Note that this protocol does not make person i a friend of the host.</li>
	<li><em>WeAreYourFriends</em> makes person i a friend of the host, and also a friend of each person, who is a friend of the host at this moment.</li>
</ul>

<p>After we build the network we would like to pick a sample for a survey, that is, choose a group of people from the network. Since friends usually have similar interests, the sample should not include any pair of people who are friends with each other. Each person has a survey confidence, expressed as a positive integer, and we would like to find a sample with the maximum total confidence.</p>

<table class="table table-bordered" style="width:411px">
	<thead>
		<tr>
			<th>stage</th>
			<th>host</th>
			<th>protocol</th>
			<th>friend relation added</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>0</td>
			<td>IAmYourFriend</td>
			<td>(1, 0)</td>
		</tr>
		<tr>
			<td>2</td>
			<td>0</td>
			<td>MyFriendsAreYourFriends</td>
			<td>(2, 1)</td>
		</tr>
		<tr>
			<td>3</td>
			<td>1</td>
			<td>WeAreYourFriends</td>
			<td>(3, 1), (3, 0), (3, 2)</td>
		</tr>
		<tr>
			<td>4</td>
			<td>2</td>
			<td>MyFriendsAreYourFriends</td>
			<td>(4, 1), (4, 3)</td>
		</tr>
		<tr>
			<td>5</td>
			<td>0</td>
			<td>IAmYourFriend</td>
			<td>(5, 0)</td>
		</tr>
	</tbody>
</table>

<p>Initially the network contains only person 0. The host of stage 1 (person 0) invites the new person 1 through the IAmYourFriend protocol, hence they become friends. The host of stage 2 (person 0 again) invites person 2 by MyFriendsAreYourFriends, which makes person 1 (the only friend of the host) the only friend of person 2. The host of stage 3 (person 1) adds person 3 through WeAreYourFriends, which makes person 3 a friend of person 1 (the host) and people 0 and 2 (the friends of the host). Stages 4 and 5 are also shown in the table above. The final network is shown in the following figure, in which the numbers inside the circles show the labels of people, and the numbers next to the circles show the survey confidence. The sample consisting of people 3 and 5 has totalsurvey confidence equal to 20 + 15 = 35, which is the maximum possible total confidence.</p>

<p><img alt="" src="" style="height:193px; width:320px"></p>

<p>Given the description of each stage and the confidence value of each person, find a sample with the maximum total confidence.</p>

<ul>
	<li>findSample(n, confidence, host, protocol)
	<ul>
		<li>n: the number of people.</li>
		<li>confidence: array of length n; confidence[i] gives the confidence value of person i.</li>
		<li>host: array of length n; host[i] gives the host of stage i.</li>
		<li>protocol: array of length n; protocol[i] gives the protocol code used in stage i (0 < i < n): 0 for IAmYourFriend, 1 for MyFriendsAreYourFriends, and 2 for WeAreYourFriends.</li>
		<li>Since there is no host in stage 0, host[0] and protocol[0] are undefined and should not be accessed by your program.</li>
		<li>The function should return the maximum possible total confidence of a sample.</li>
	</ul>
	</li>
</ul>

### 입력 

 <ul>
	<li>line 1: n</li>
	<li>line 2: confidence[0], ..., confidence[n-1]</li>
	<li>line 3: host[1], protocol[1], host[2], protocol[2], ..., host[n-1], protocol[n-1]</li>
</ul>

### 출력 

 <p>Print return value of function findSample.</p>

