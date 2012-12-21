Problem
========

You are given a tree (a simple connected graph with no cycles).You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest contains even number of vertices

Your task is to calculate the number of removed edges in such a forest.

>>Input:

The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges. 2 <= N <= 100. 
Next M lines contains two integers ui and vi which specifies an edge of the tree. (1-based index)

>>Output:

Print a single integer which is the answer

Sample Dataset
==============

>>Sample Input 

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8

>>Sample Output :

2
