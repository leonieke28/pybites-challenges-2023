import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    formatted_poem = []
    empty_line = False
    for line in [line.strip() for line in poem.splitlines(True)]:
        if line == "":
            empty_line = True
            continue
        if not empty_line:
            formatted_poem.append(textwrap.indent(line, " " * INDENTS))
        else:
            formatted_poem.append(line)
        empty_line = False
    print("\n".join(formatted_poem))
