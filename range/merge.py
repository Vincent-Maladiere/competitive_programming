"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
"""
# %%
def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    out = []
    prev_int = intervals[0]

    for idx in range(1, len(intervals)):
        
        current_int = intervals[idx]
        
        if prev_int[1] >= current_int[0]:
            prev_int[1] = max(prev_int[1], current_int[1])
        else:
            out.append(prev_int)
            prev_int = current_int
        
    out.append(prev_int)

    return out


# %%
