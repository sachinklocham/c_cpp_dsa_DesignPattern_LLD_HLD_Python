// return numbers we can sort, return indexes - do not sort at all
/*
1) Brute-Force (No Extra Space, Simple)
Time → O(n²)
Space → O(1)
Guaranteed correct
Works on unsorted arrays

2) Sort + Two-Pointer (Technically O(1) Extra)
This is the best optimized without hash map.
Time → O(n log n) (because of sorting)
Space → O(1) if in-place sort is allowed
Much faster than brute force
But original indices get lost

3) Sort + Two-Pointer While Preserving Indices
If interviewer insists on:
no extra space for main algorithm
but indices must be returned
Minimal extra memory trick:

4) Hash Map Solution (For Comparison Only)
This is the true optimal in practice:
Time → O(n)
Space → O(n)

*/
#include <iostream>

int main() {

    return 0;
} 