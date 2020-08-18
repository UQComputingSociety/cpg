# UQCS Competitive Programming Group

The aim of this group is to get practice with programming questions such as those found on LeetCode, and to apply to this skills to programming competitions such as Google CodeJam, Advent of Code, Google Kickstart and (potentially) team-based competitions such as the International Collegiate Programming Contest (or ICPC). We aim to meet on a **weekly basis** to discuss and work together on challenging and interesting programming problems, and get some valuable experience for technical interviews along the way!

The plan is to work through **three** problems every week: one easy, one medium and one hard difficulty. We will start with simple algorithms based on simple data structures anyone with CSSE1001-level programming experience should be familiar with (such as lists and dictionaries). As time goes on, we will progress to more advanced programming techniques, and some of the sessions will briefly introduce these techniques.

## Textbook

The "text" is [_Competitive Programming 3_](http://www.sso.sy/sites/default/files/competitive%20programming%203_1.pdf). We won't (for now, this may change in the future) be using problems out of this book, but we will be following the contents as a rough guide of what to cover. For more problems, refer to CP3, there are hundreds in each section! However, note that this book has code snippets written in C/C++/Java. The reference for each section is given in the "CP3 reference" column of the schedule at the bottom of this README.

## Week 3: Graphs, Breadth-First Search and Depth-First Search

We will work through the following problems, each based around graphs. You are highly encouraged to try out more problems to get familiar with these graphs and traversals!

**Easy: [Flood Fill](https://leetcode.com/problems/flood-fill/)**

> An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
> 
> Given a coordinate `(sr, sc)` representing the starting pixel (row and column) of the flood fill, and a pixel value `newColor`, "flood fill" the image.
> 
> To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the `newColor`.
> 
> At the end, return the modified image.

**Medium: [Number of Islands](https://leetcode.com/problems/number-of-islands/)**

> Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Medium: [Course Schedule](https://leetcode.com/problems/course-schedule/)**

> There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.
> 
> Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`
> 
> Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**Hard: [Bus Routes](https://leetcode.com/problems/bus-routes/)**

> We have a list of bus routes. Each `routes[i]` is a bus route that the `i`-th bus repeats forever. For example if `routes[0] = [1, 5, 7]`, this means that the first bus (`0`-th indexed) travels in the sequence `1->5->7->1->5->7->1->...` forever.
> 
> We start at bus stop `S` (initially not on a bus), and we want to go to bus stop `T`. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return `-1` if it is not possible.

## Week 2: Data Structures

We will work through the following problems, each based around some data structure. You are highly encouraged to try out more problems to get familiar with these data structures (and others)!

**Easy (Trees): [Invert a Binary Tree](https://leetcode.com/problems/invert-binary-tree/)**

> Invert a binary tree.

**Medium (Stacks): [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)**

> Implement a basic calculator to evaluate a simple expression string. The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero.

**Medium (2D Arrays): [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)**

> Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
> 
> 1. Each row must contain the digits 1-9 without repetition.
> 2. Each column must contain the digits 1-9 without repetition.
> 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

**Hard (2D Arrays, for discussion): [Sudoku Solver](https://leetcode.com/problems/sudoku-solver)**

> Write a program to solve a Sudoku puzzle by filling the empty cells.

## Week 1: Beginnings

We will work through the following problems:

**Easy: [Two Sum](https://leetcode.com/problems/two-sum/)**

> Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Medium: [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)**

> Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

**Hard: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)**

> There are two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively. Find the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`. You may assume `nums1` and `nums2` cannot be both empty.

## Tentative Schedule

| #       | Week starting | Topic                                      | CP3 reference |
|---------|---------------|--------------------------------------------|---------------|
| Week 1  |         3 Aug | Beginnings                                 | N/A           |
| Week 2  |        10 Aug | Data Structures                            | 2.1-2.4       |
| Week 3  |        17 Aug | Graphs, DFS, BFS                           |               |
| Week 4  |        24 Aug | Dynamic Programming                        |               |
| Week 5  |        31 Aug | ...                                        |               |
| Week 6  |         7 Sep | ...                                        |               |
| Week 7  |        14 Sep | ...                                        |               |
| Week 8  |        21 Sep | ...                                        |               |
| Break   |        28 Sep |                                            |               |
| Week 9  |         5 Oct | ...                                        |               |
| Week 10 |        12 Oct | ...                                        |               |
| Week 11 |        19 Oct | ...                                        |               |
| Week 12 |        26 Oct | ...                                        |               |
