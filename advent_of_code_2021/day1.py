def part1(lines) -> int:
    last = None
    total_deeper = 0
    for line in lines:
        if last and line > last:
            total_deeper += 1
        last = line
    return total_deeper
