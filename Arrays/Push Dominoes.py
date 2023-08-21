import collections


def pushDominoes(dominoes: str) -> str:
    domino = list(dominoes)
    q = collections.deque()

    for i, d in enumerate(domino):
        if d != ".":
            q.append((i, d))

    while q:
        i, d = q.popleft()

        if d == 'L' and i > 0 and domino[i - 1] == '.':
            q.append((i - 1, 'L'))
            domino[i - 1] = 'L'
        elif d == 'R':
            if i + 1 < len(domino) and domino[i + 1] == '.':
                if i + 2 < len(domino) and domino[i + 2] == 'L':
                    q.popleft()
                else:
                    q.append((i + 1, 'R'))
                    domino[i + 1] = 'R'

    return ''.join(domino)

dominoes = ".L.R...LR..L.."
print(pushDominoes(dominoes))