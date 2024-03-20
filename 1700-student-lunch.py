'''
problem_name = Number of Students Unable to Eat Lunch
problem_source = https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

Algo 
    -Compare number of zeroes of sandwich and students
    -if they are equal return 0
    -else if students number of 0 is less by n
        -iterate over sandwich till the (number of 0-preferred student + 1) of 0-shaped sandwich = i        (Because if the number 0-shaped is more than the number of 0-preferred student, that means when everyone takes their preferred 0-shaped sandwich, there will still be 0-shaped sandwich left, and there will be none to take that one and make the road clear for other sandwiches)
        -return len(sandwich[i:])
    -else if student number of 1 is less by m
        -iterate over sandwich till the (number of 1-preffered student + 1) of 1-shaped sandwich = i
        -return len(sandwich[i:])
'''

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        stdnt_0 = students.count(0)
        stdnt_1 = len(students) - stdnt_0
        sndwch_0 = sandwiches.count(0)
        #sndwch_1 = len(sandwiches) - sndwch_0

        if stdnt_0 == sndwch_0:
            return 0
        elif stdnt_0 < sndwch_0:
            for i in range(stdnt_1 + stdnt_0):       #Iterating over the total number of sandwiches (which is equal to the number of students)
                if sandwiches[i] == 0:
                    stdnt_0 -= 1
                    if stdnt_0 == -1:               #-iterate over sandwich till the (number of 0-preferred student + 1) of 0-shaped sandwich = i
                        break
        else:
            for i in range(stdnt_0 + stdnt_1):
                if sandwiches[i] == 1:
                    stdnt_1 -= 1
                    if stdnt_1 == -1:
                        break
        return len(sandwiches[i:])