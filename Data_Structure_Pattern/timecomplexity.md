=> simple operation constant time 
a= a+10;

=> 10^8 simple operation are allowed in a program generally on leetcode. time depends on language.

input size n = 10 max then program can be of different complexity ...
    if max complexity = O(n) means 10 simple operation
    if max complexity = O(logN) means lig base 2 (10)  equals almost 3 - operations
                    = O(n*logN)
    if max complexity = O(n^2) means 100 operations
                    = O(n^3) => 1000 operations
                    = O(2^n) =>> 1024 operation
                    = O(n!) => 10*9*8*7 ... 2*1  operations
                    = O(n^n) => 10^10 operation

if n = 1000
then on leetcode O(n) allowed
O(n^2) = 10^6 allowed
O(n^3) = 10^9 not allowed TLE , as 10^8 max operations allowed.





