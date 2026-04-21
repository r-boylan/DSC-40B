def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # TODO: Implement the swap_sum function
    for i in range(len(A)):
        for j in range(len(B)):
            A[i], B[j] = B[j], A[i]

            if sum(A) - sum(B) == 10:
                return A, B

            A[i], B[j] = B[j], A[i]
    return None
