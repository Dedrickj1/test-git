def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    for i in range (len(sorted_list)-1):
        if sorted_list[i+1] - sorted_list[i] != 1:
            return False
        return True