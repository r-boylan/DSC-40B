def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # TODO: Implement the swap_sum function
    A_copy = A.copy()
    B_copy = B.copy()

    for i in range(len(A_copy)):
        for j in range(len(B_copy)):
            A_copy[i], B_copy[j] = B_copy[j], A_copy[i]

            if abs(sum(A_copy) - sum(B_copy)) == 10:
                A_copy[i], B_copy[j] = B_copy[j], A_copy[i]
                return A_copy, B_copy
            
            A_copy[i], B_copy[j] = B_copy[j], A_copy[i]
    return None
