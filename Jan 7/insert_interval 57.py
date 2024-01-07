"""
Mark's question
https://leetcode.com/problems/insert-interval/description/

Notes:
    0:45:02
    Way clunkier than I'd like. There was a python solution that was under 20 lines... This is pathetic :(
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # ALL that we do here is insert newInterval into the correct position
        
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        ind = 0
        added = 0
        for i in intervals:
            print(i)
            if i[0] > newInterval[0]:
                # This is where the replacing happens!!
                ind = intervals.index(i)
                added = 1
                if ind < 0:
                    ind = 0
                test = []
                test.append(newInterval)
                intervals = intervals[:ind] + test + intervals[ind:]
                break 
            else:
                continue
        if added != 1:
            intervals.append(newInterval)
        # Replacement has happened.
        intervals = self.check_overlap(intervals, ind)

        return intervals
    
    def check_overlap(self, ints, ind):
        """
        
        """

        replaced = 0        
        for i in range(len(ints)):
            j = i+1
            length = len(ints)
            while j < length:
                print("compare " + str(ints[i]) + " and " + str(ints[i+1]))
                if ints[i][1] >= ints[i+1][0]:
                    print("    " + str(ints[i]) + " and " + str(ints[i+1]))
                    
                    if ints[i][1] > ints[i+1][1]:
                        pass
                    else:
                        ints[i][1] = ints[i+1][1]
                    ints.remove(ints[i+1]) 
                    replaced = 1

                j += 1
            
            if replaced:
                return ints

            ##################################
            # if ints[i][1] >= ints[i+1][0]: #
            #     ints[i][1] = ints[i+1][1]  #
            #     ints.remove(ints[i+1])     #
            ##################################

        return ints
