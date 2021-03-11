from decimal import Decimal
import re

PROCESSED = r' ?=> -?(\d+\.)?\d+$'
WHITESPACE = r'\s*'
TOTAL_LINE = r'^TOTAL: -?(\d+\.)?\d+$'

# FIXME: Set up highlighting for the sums and for the parts of the lines that
#        will be processed.
# FIXME: Line references like Soulver
# FIXME: Support units! (In particular, money!)
# FIXME: Function to print out full calculation used (maybe debug only)
# FIXME: Support thousands separators
# FIXME: Prevent lines being added below TOTAL
# FIXME: Remove extra blank lines before TOTAL


def main(vim):
    buffer = vim.current.buffer

    subtotals = calculate(buffer)

    total = 0
    for i, subtotal in enumerate(subtotals):
        if subtotal is not None:
            total += subtotal
        apply_subtotal(i, subtotal, buffer)

    apply(total, buffer)


def apply_subtotal(i, subtotal, buffer):
    """Update a line of the buffer to append/amend the result."""
    buffer[i] = processed_line(buffer[i], subtotal)


def original_line(line):
    """Trim off any existing result."""
    match = re.search(PROCESSED, line)
    return line[:match.start()] if match else line


def processed_line(line, subtotal):
    """Add the result to the end of a line."""
    line = original_line(line)
    if subtotal is not None:
        line += f' => {subtotal}'
    return line


def calculate_line(line):
    """Calculate the 'result' of a line."""
    values = find_maths(line)

    last_one = None
    for v in values:
        last_one = v

    if last_one is None:
        return last_one

    try:
        result = eval(last_one)
    except:
        result = None

    return result


def find_maths(line: str):
    """Find all the things that might be maths in a line."""
    # FIXME: This is super basic and undoubtedly RIFE with edge cases
    return (x[0].strip()
            for x
            in re.finditer(r'[0-9. ()*/+-]+', line)
            if x and not re.fullmatch(WHITESPACE, x[0]))


def calculate(buffer):
    """Calculate the result for each line of the buffer."""
    b = [original_line(line) for line in buffer]
    if re.match(TOTAL_LINE, b[-1]):
        b.pop()
        if re.fullmatch(WHITESPACE, b[-1]):
            b.pop()

    return (calculate_line(line) for line in b)


def apply(total, buffer):
    """Ensure the last line of a buffer contains the total.

    N.B. returns None: it mutates the buffer passed in.
    """
    line = f'TOTAL: {total}'
    if re.match(TOTAL_LINE, buffer[-1]):
        buffer[-1] = line
    else:
        buffer.append(line)

    # Ensure we have a blank line before total
    if not re.fullmatch(WHITESPACE, buffer[-2]):
        buffer[-1] = ""
        buffer.append(line)


if __name__ == '__main__':
    # We can't import vim globally, because then the pure Python test cases
    # won't work. Import it here instead, and pass it in.
    import vim

    main(vim)
