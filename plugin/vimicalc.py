from decimal import Decimal
import re

import vim

PROCESSED = r' ?=> (\d+\.)?\d+$'
WHITESPACE = r'\s*'

# FIXME: Set up highlighting for the sums and for the parts of the lines that
#        will be processed.
# FIXME: Line references like Soulver
# FIXME: Support units!
# FIXME: Function to print out full calculation used (maybe debug only)
# FIXME: Unit tests!


def main():
    buffer = vim.current.buffer

    for i, line in enumerate(buffer[:-1]):
        process_line(i, line, buffer)

    total = calculate(buffer)

    apply(total, buffer)


def process_line(i, line, buffer):
    match = re.search(PROCESSED, line)
    if match:
        line = line[:match.start()]

    if not re.fullmatch(WHITESPACE, line):
        result = calculate_line(line)
        if result is None:
            buffer[i] = line
        else:
            # FIXME: position sum at the right-hand edge of the window
            buffer[i] = f'{line} => {calculate_line(line)}'
    else:
        buffer[i] = line


def calculate_line(line):
    # FIXME: This is super basic and RIFE with edge cases
    values = (x
              for x
              in re.finditer(r'[0-9. ()*/+-]+', line)
              if x and not re.fullmatch(WHITESPACE, x[0]))

    last_one = None
    for v in values:
        last_one = v

    if last_one is None:
        return last_one

    try:
        result = eval(last_one[0])
    except:
        result = None

    return result


def calculate(buffer):
    return sum(
        (Decimal(line.split()[-1])
         for line
         in buffer
         if re.search(PROCESSED, line)))


def apply(total, buffer):
    line = f'TOTAL: {total}'
    if re.match(r'^TOTAL: \d+$', buffer[-1]):
        buffer[-1] = line
    else:
        buffer.append(line)

    # Ensure we have a blank line before total
    if not re.fullmatch(WHITESPACE, buffer[-2]):
        buffer[-1] = ""
        buffer.append(line)


if __name__ == '__main__':
    main()
