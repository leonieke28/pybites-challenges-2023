def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    return [
        round(sum(x) / len(x), 2)
        for x in (sequence[: i + 1] for i in range(len(sequence)))
    ]


running_mean([1, 2, 3])  # [1, 1.5, 2]
