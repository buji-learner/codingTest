""" 깊이 우선 탐색
def dfs(now):
    visited[now] = 1
    print(now, end = "")

    for next in v[now]:
        if visited[next] == 0:
            dfs(next)
"""

# 이걸로 어제 문제 풀어보기!!!
