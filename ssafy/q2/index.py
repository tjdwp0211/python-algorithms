import sys

sys.stdin = open("q2/input.txt")

from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    start = 0
    delay_infos = defaultdict(int)
    for _ in range(N):
        c, d = map(int, input().split())
        delay_infos[c] = d

    for i in range(D // 2):
        start += 1
        D -= 1
        if start in delay_infos.keys():
            poped = delay_infos.pop(start)
            for j in range(poped):
                D -= 1
                if start == D:
                    break
        if D in delay_infos.keys():
            poped = delay_infos.pop(D)
            for j in range(poped):
                start += 1
                if start == D:
                    break
        if start == D:
            break
    print(f"#{test_case} {start}")
