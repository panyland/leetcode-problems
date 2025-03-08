# Merge list of intervals by overlapping intervals

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals: return [] 
    sorted_intervals = sorted(intervals)
    result = [sorted_intervals[0]]
    
    
    for j in range(1, len(sorted_intervals)):
        i = 1
        if sorted_intervals[j][0] <= result[i-1][1]:
            upper_limit = max(result[i-1][1], sorted_intervals[j][1])
            new_interval = [result[i-1][0], upper_limit]
            result[i-1] = new_interval
            i -= 1
        else: 
            new_interval = [sorted_intervals[j][0], sorted_intervals[j][1]]
            if new_interval not in result: result.append(new_interval)
            i += 1  
            
    return result

        
print(merge_intervals([[1,3],[2,6],[8,10],[2,6],[15,18]]))  # [[1,6], [8,10], [15,18]]
print(merge_intervals([[1,4],[4,5]]))  # [[1,5]]
print(merge_intervals([[1,3],[5,7]]))  # [[1,3], [5,7]]
print(merge_intervals([[1,10],[2,6],[8,10],[15,18]]))  # [[1,10], [15,18]]
print(merge_intervals([[1,10],[1,10], [1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10]]))
