#!/usr/bin/env python
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
----

Start at i = 0. Move j forward by 1. Calculate the current gas left. If our remaining
gas drops below 0, then increment i and add back in the gas from the previous starting
station. We stop once j = i + N.

This runs in O(N).
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i = j = 0
        gas_left = 0

        if not gas or not cost:
            return 0

        while (j - i) < n:
            gas_left += gas[j % n]
            gas_left -= cost[j % n]
            j += 1
            while gas_left < 0 and i < j:
                gas_left -= gas[i % n]
                gas_left += cost[i % n]
                i += 1
            if i >= n:
                return -1
        return i % n


def main():

    s = Solution()
    print s.canCompleteCircuit([1, 2], [2, 1])
    print s.canCompleteCircuit([2, 4], [3, 4])
    print s.canCompleteCircuit([4], [5])
    print s.canCompleteCircuit([0, 0, 2, 2, 2],
                               [2, 1, 1, 1, 1])

if __name__ == '__main__':
    main()
