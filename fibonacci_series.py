pre_num = 0
curr_num = 1
for n in range(20):  
    next_num = pre_num + curr_num
    print(next_num)
    pre_num = curr_num
    curr_num = next_num
