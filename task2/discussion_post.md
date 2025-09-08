[Source code URL](https://github.com/SerenaYZhang/CS6120_tasks/tree/main/task2)

**Benchmark** [Pull Request](https://github.com/sampsyo/bril/pull/429)
I created a new benchmark for sorting an array of 5 integers in ascending order using the insertion sort algorithm. This benchmark is heavily inspired by the existing benchmark bubblesort by Jiajie Li, adopting the functions ``pack`` and ``print_array`` for easier array manipulation. The size of the array that can be sorted is currently fixed at 5 integers, but this length could be easily edited to be smaller or larger. 

I tested my sorting algorithm by editing ``# ARGS: 5 22 81 7 35 60`` with different parameters and making sure that the end result was the correct sorted order. 

The hardest part of this task was writing code in bril. Although the syntax is well documented and there are many other benchmarks to reference, the language style feels like a different way of thinking compared to the programming languages I'm most familiar with. 

**Analyze Bril Programs**
I wrote a simple program that prints out what arithmetic operation is being called ("adding", "subtracting", "multiplying", or "dividing"). To validate my program, I wrote my own test cases with different arithmetic operation scenarios and used turnt to check that the output matched with the expectation. 

One thing I found annoying was that if there are issues in the program, turnt would only show that the program failed to run on the test cases with error message ``# exit code: 1`` with no additional information. This means that debugging often required me to run the program on the test cases without using turnt, which feels like an extra step that could be streamlined. 

**CFG**
I implemented the CFG algorithm derived in class using Python. One design choice I made was to use numerical indices to identify blocks, and I used a dictionary to map a label to the numerical index of its block. 

I again tested my CFG implementation using turnt, creating test cases from the 3 example bril code we saw in class. To check that the blocks are correctly formed, I printed out all of the blocks and the instructions for each block to make sure that the number of blocks is accurate and each one holds the correct order of instructions. To check that I find the correct CFG, I print out each block's successors. Since we went over the 3 examples in class and marked out the blocks and CFG for each, I manually inspected the print statements for each test case and made sure they matched our results. 

I believe I deserve a Michelin star for familiarizing myself with bril tools and applying what we learned in class in implementing CFG and adding my own design choices to it. 