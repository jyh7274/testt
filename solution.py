# def solution(s):
#     # Solution 1
#     str_length = len(s)
#     maximum = 0
#     for index in range(1, int(round(str_length/2))+1):
#         fragment = s[:index]
#         if str_length % len(fragment) == 0:
#             number_of_fragment = str_length/len(fragment)
#             if fragment * int(number_of_fragment) == s and number_of_fragment > maximum:
#                 maximum = number_of_fragment
#     return int(maximum)
"""
Problem 2-1:
    Commander Lambda's space station is HUGE. And huge space stations take a LOT of power.
    Huge space stations with doomsday devices take even more power. 
    To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface.
    But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels.
    You and your team of henchmen have been assigned to repair the solar panels, 
    but you'd rather not take down all of the panels at once if you can help it, 
    since they do help power the space station and all!

    You need to figure out which sets of panels in any given array 
    you can take offline to repair while still maintaining the maximum amount of power output per array, 
    and to do THAT, you'll first need to figure out what the maximum output of each array actually is. 
    Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array,
    and returns the maximum product of some non-empty subset of those numbers. 
    So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5],
    then the maximum product would be found by taking the subset:
        xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".

    Each array of solar panels contains at least 1 and no more than 50 panels,
    and each panel will have a power output level whose absolute value is no greater than 1000
    (some panels are malfunctioning so badly that they're draining energy,
    but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels 
    to produce the positive output of the multiple of their power values). The final products may be very large, 
    so give the solution as a string representation of the number.
"""
# def solution(xs):
#     # Solution 2-1
#     if max(xs) != 0:
#         total_mul = 1
#     else:
#         return str(0)
#     count_negative = 0
#     negative_nums = []
#     for element in xs:
#         if element == 0:
#             continue
#         else:
#             total_mul = total_mul * element
#             if element < 0:
#                 count_negative += 1
#                 negative_nums.append(element)
#     if count_negative % 2 == 0:
#         pass
#     else:
#         if len(negative_nums) == 1 and len(xs) == 1:
#             return str(total_mul)
#         total_mul = total_mul / max(negative_nums)
#     return str(total_mul)

"""
Problem 2-1:
    Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers). 

"""
def solution(x, y):
    # Solution 2-2
    # calculate coordinates of each ends of the triangle
    # calculate the ID
    # indexing

     max_y = y + x - 1
     max_x = x + y - 1
     start_id = get_id(1, max_y, 1)
     end_id = get_id(1, max_x, 2)
     return str(list(range(start_id, end_id + 1))[x - 1])

def get_id(first, index, start_dif):
    # Sub-function for solution 2-2
    next_value = first
    dif = start_dif
    if index == 0:
        return first
    for repeat_index in range(index-1):
        next_value = next_value + dif
        dif = dif + 1
    return next_value

