# 0x02-minimum_operations

In a text file, there is a single character H. Your text editor can execute only two operations in this: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n`. H characters in the file.
- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return 0

### **Example:**
1. `n = 9`
2. `H`=>`Copy All`=>`Paste`=>`HH`=>`Paste`=>`HHH`=>`Copy All`=>`Paste`=>`HHHHHH`=>`Paste`=>`HHHHHHHHH`
3. Number of operations: `6`

## Concept
Imagine you have a text file that contains only one letter, the letter H. You can perform two actions in this file: Copy All and Paste.

If we're given a number `n`, the challenge is to calculate the minimum number of actions needed to result in exactly `n` H characters in the file. For example, if `n = 3`, we need to find the shortest sequence of actions that will produce three H's in the file.

To solve this challenge, we need to think about how we can use the `Copy All` and `Paste` operations to create n H's. One approach is to start with a single H in the file, and then repeatedly copy and paste it until we have n H's.

For example, if `n = 3`, we can start with the initial H in the file, and then use the `Copy All` and `Paste operations` to create two more H's. This would require two operations: one to copy the H, and one to paste it twice.

But how do we know that this is the shortest sequence of actions? Is there a more efficient way to get to three H's?

One way to approach this problem is to think about the factors of n. If `n` is a prime number, we can't divide it into smaller factors, so we have to create `n` H's one at a time. But if n has factors, we can use those factors to create `n` H's more efficiently.

For example, if `n = 12`, we can divide it into factors of 2, 2, and 3. This means we can create two H's and then copy and paste them twice to get four H's, and then copy and paste those four H's three times to get 12 H's. This requires five operations in total: two to create the initial two H's, two to copy and paste the four H's, and one to copy and paste the 12 H's.

In general, to find the shortest sequence of actions, we need to factorize n and use those factors to create the H's more efficiently. This will require some algorithmic thinking and may involve recursion or dynamic programming.

However, to truly understand how to solve this problem, we'll need to write some code and test it with various inputs. So let's start coding!