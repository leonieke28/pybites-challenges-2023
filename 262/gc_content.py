def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    a = sequence.lower().count("a")
    g = sequence.lower().count("g")
    c = sequence.lower().count("c")
    t = sequence.lower().count("t")
    total = a + g + c + t
    gc_total = g + c

    return round((gc_total / total) * 100, 2)
