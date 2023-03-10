"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    ### TODO
   
def longest_run(mylist, key):
    i = 0
    sum = 0
    summax = 0
    while i < len(mylist):
        if key == mylist[i]:
            sum = sum + 1
            if sum > summax:
                summax = sum
                i = i + 1
            else:
                i = i + 1
        else:
            sum = 0
            i = i + 1
    return summax
            
            

    
        
    ### TODO
    


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recurisve(mylist, key):
    answer = longest_run_recursive_result(mylist, key)
    return answer.longest_size
    
def longest_run_recursive_result(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1, True)
        else:
            return Result(0,0,0, False)
    else:
        right = mylist[len(mylist)//2:]
        left = mylist[:len(mylist)//2]
        r = longest_run_recursive_result(right,key)
        l = longest_run_recursive_result(left,key)
        
        
        if r.is_entire_range and l.is_entire_range:
            summax = r.longest_size + l.longest_size
            return Result(summax, summax, summax, True)
        elif r.is_entire_range:
            if r.longest_size >= (l.right_size + r.longest_size):
                summax = r.longest_size
            else:
                summax = l.right_size + r.longest_size
            return Result(l.left_size, r.right_size + l.right_size, summax, False)
        elif l.is_entire_range:
            if l.longest_size >= (l.longest_size + r.left_size):
                summax = l.longest_size
            else:
                summax = l.longest_size + r.left_size
            return Result(l.left_size + r.left_size, r.right_size, summax, False)
        else:
            if r.longest_size > (l.right_size + r.left_size):
                summax = r.longest_size
            elif l.longest_size > (l.right_size + r.left_size):
                summax = l.longest_size
            else:
                summax = l.right_size + r.left_size
            return Result(l.left_size, r.right_size, summax, False)
            
            
       
    ### TODO
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


