#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This looks like O(n) to me. Only one level deep and it seems constant with whatever number you put in for n. If n is large, the file will take a little longer to run, but not too much longer.

b) This looks like O(n^2), because there is a nested loop. When there's a nested loop, it has to run everything to the squared.

c) Recursion. O(n) time complexity. It'll simply add 2 and loop until bunnies equals 0.

## Exercise II

I don't know if I exactly understand this problem...

If floor is negative, print('cant drop from a negative floor')
Why not just check if we're on a floor that's higher than the floor that will break the eggs.
If we are higher than the floor that breaks the eggs, then go down a floor.
Loop until you reach the safe floor.
If we're lower than the floor that breaks the eggs, no problem, drop the eggs.

Runtime would be O(n). Only need to go one loop deep and it the runtime would depend on the number of stories that the building has.
