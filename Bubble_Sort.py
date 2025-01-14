def bubble_sort(input_list):
    for idx in range(0,len(input_list)):
        min_idx = idx
        for j in range( 1, len(input_list)-idx):
            if input_list[j-1] > input_list[j]:
                input_list[j-1], input_list[j] = input_list[j], input_list[j-1];

# add any list of number here 
l = [5,2,4,6,1,3];

bubble_sort(l);
print(l);
