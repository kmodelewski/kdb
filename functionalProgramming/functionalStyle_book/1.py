from collections.abc import Sequence
def sum_numbers(seq: Sequence[int]) ->int:
    if len(seq)==0:
        return 0
    return seq[0] + sum_numbers(seq[1:])

print(sum_numbers([10,1]))