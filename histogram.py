def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    # TODO: Implement the histogram function
    binned = {}
    for bin in bins:
        bucket = [point for point in points if point < bin[1]]
        binned[bin] = len(bucket)
        points = points[len(bucket):]
    return list[binned.values()]
