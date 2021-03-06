#!/usr/bin/env python


class Vertex():
    def __init__(self, data):
        self.data = data
        self.visited = False

    def __str__(self):
        return '{0}'.format(self.data)

    def __repr__(self):
        return self.__str__()


class Edge():
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph():
    def __init__(self, V, E):
        self.V = V
        self.E = E

    def __str__(self):
        return 'V: {0}\nE: {1}\n'.format(V, E)

    def __repr__(self):
        return self.__str__()

    def unvisit(self):
        'Mark all vertices in graph as not visited'
        for u in self.V:
            u.visited = False


class AdjacencyMatrixGraph(Graph):
    def __init__(self, V, E):
        Graph.__init__(self, V, E)
        self.M = {}
        for u in V:
            for v in V:
                if (u, v) in E:
                    self.M[(u, v)] = 1
                else:
                    self.M[(u, v)] = 0

    def __str__(self):
        s = ''
        for u in self.V:
            for v in self.V:
                s += ' {0} '.format(self.M[(u, v)])
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def neighbors(self, u):
        L = []
        for v in self.V:
            if self.M[(u, v)] or self.M[(v, u)]:
                L.append(v)
        return L


class AdjacencyListGraph(Graph):
    def __init__(self, V, E):
        Graph.__init__(self, V, E)
        self.L = {}
        for u in V:
            self.L[u] = []
        for u in V:
            for v in V:
                if (u, v) in E:
                    self.L[u].append(v)
                    self.L[v].append(u)

    def __str__(self):
        s = ''
        for u in self.L:
            s += '{0}: {1}\n'.format(u, self.L[u])
        return s

    def neighbors(self, u):
        return self.L[u]


def neighbors(u, N):
    """Return list of neighbors of u in NxN lattice
    """
    indices = [u - 1, u + 1,  # left/right
               u - N, u + N]  # up/down
    L = []
    for v in indices:
        if isneighbor(u, v, N):
            L.append(v)
    return L


def isneighbor(u, v, N):
    """Is v a valid neighbor of u in an NxN lattice

    u and v are integers in a 1-based NxN grid lattice,
    represented by a 1-dimensional array
    """
    n = v % N if v % N else N
    m = (v - n) / N + 1

    j = u % N if u % N else N
    i = (u - j) / N + 1

    if v < 1 or v > N * N:
        return False

    k = abs(v - u)

    if k == 1:  # left/right
        return i == m
    elif k == N:  # up/down
        return i >= 1 and i <= N

    return False


def visit(u):
    u.visited = True


def unvisit(u):
    u.visited = False


def search(G, s, t, L, P):
    visit(s)
    for v in G.neighbors(s):
        L.append((s, v))
        if v == t:
            P.append(tuple(L))
        else:
            # v > s: no backtracking
            if not v.visited and v.data > s.data:
                search(G, v, t, L, P)
        L.pop()
    unvisit(s)


def non_back_tracking_paths(N):
    """Return number of non backtracking paths for NxN lattice
    """
    V = [Vertex(i) for i in range(1, N * N + 1)]
    E = []
    for u in V:
        for v in V:
            if isneighbor(u.data, v.data, N):
                E.append((u, v))
    G = AdjacencyMatrixGraph(V, E)
    L, P = [], []
    search(G, V[0], V[-1], L, P)
#    for p in P: print p
    return len(P)
