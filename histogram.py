def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    # TODO: Implement the histogram function
    result = []
    n = len(points)
    i = 0
    for left, right in bins:
        count = 0
        width = right - left
        while i < n and points[i] < right:
            if points[i] >= left:
                count += 1
            i += 1
        result.append(count / (n * width))
    return result
