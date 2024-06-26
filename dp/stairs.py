"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
# %%

def stairs(n):
    "For some reason the solution is the fibonacci suite."
    out = [1, 2]
    for idx in range(n):
        c = out[idx] + out[idx+1]
        out.append(c)
    return out[-3]

stairs(6)




