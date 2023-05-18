num = int(input())
booms = [0] + [int(input()) for _ in range(1, num + 1)] + [0]
clicks = []

for i in range(1, num + 1):
    prev_i, cur_i, next_i = booms[i - 1], booms[i], booms[i + 1]
    if prev_i <= cur_i >= next_i:
        clicks.append(i)

print("\n".join(map(str, clicks)))
