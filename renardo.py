from copy import deepcopy
from numpy import abs
from time import time

def main():
    nums = []
    print()
    print()
    print("==========")
    for i in range(6):
        nums.append(int(input('Nombre %d?  '%(i+1))))
        print("==========")
    obj = int(input('Nombre cible ?'))
    print("==========")
    print()
    print()
    print('=== Tirage === ')
    print(str(obj) + '    '+ '|'.join([str(e) for e in nums]) )
    print()
    print('Résultat : ')
    t = time()
    print(solve(nums, obj))
    print('Effectué en %.2f s'%(time()-t))
    print()
    return

def is_best(s1, o1, curr, obj):
    if curr[0] is None:
        return True
    s2,o2 = curr
    if abs(o2-obj)>abs(o1-obj):
        return True
    elif abs(o2-obj)==abs(o1-obj) and len(s1)<len(s2):
        return True
    return False



def solve(nums, obj, curr_best = (None,0), seq = None):
    #First Iteration
    if seq is None:
        seq = []

    # If found or no more numbers available
    if (obj in nums) or (len(nums)==1):
        if is_best(seq,nums[-1], curr_best, obj):
            return (deepcopy(seq),nums[-1])
        else:
            return curr_best


    else:
        for i in range(len(nums)):
            for j in range(len(nums)):

                # Go through every pair of numbers and try the 4 ops recursively
                if i!=j:

                    ni, nj = nums[i], nums[j]

                    new_nums = deepcopy(nums)
                    new_nums.remove(ni)
                    new_nums.remove(nj)

                    if i<j:
                        # Try +
                        new = ni+nj
                        seq.append('%d + %d = %d'%(ni,nj, new))
                        new_nums.append(new)
                        curr_best = solve(new_nums, obj, curr_best, seq)
                        new_nums.pop()
                        seq.pop()


                        # Try *
                        new = ni*nj
                        seq.append('%d * %d = %d'%(ni,nj, new))
                        new_nums.append(new)
                        curr_best = solve(new_nums, obj, curr_best, seq)
                        new_nums.pop()
                        seq.pop()

                    # Try -
                    if ni-nj>0:
                        new = ni-nj
                        seq.append('%d - %d = %d'%(ni,nj, new))
                        new_nums.append(new)
                        curr_best = solve(new_nums, obj, curr_best, seq)
                        new_nums.pop()
                        seq.pop()

                    # Try /
                    if nums[j]!=0 and ni/nj == ni//nj:
                        new = ni//nj
                        new_nums.append(new)
                        seq.append('%d / %d = %d'%(ni,nj, new))
                        curr_best = solve(new_nums, obj, curr_best, seq)
                        new_nums.pop()
                        seq.pop()




    return curr_best

if __name__ =="__main__":
    main()