def generate_affiliation_link(url):
    start = "http://www.amazon.com/dp/"
    aff_number = url.split("/")[5]
    end = "/?tag=pyb0f-20"
    return f"{start}{aff_number}{end}"
