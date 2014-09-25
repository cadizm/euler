#!/usr/bin/env python


def print_grid(N):
    for i in range(1, N * N + 1):
        print '{0:4d}'.format(i),
        if i % N == 0:
            print


class Grid():
    def __init__(self, N, G):
        self.N = N
        self.buf = [i for i in G]

    def neighbors(self, start):
        'Neighbors w/ distance <= 3'
        L = []
        # left range
        if self.inRange(start, start - 3):
            L.append(self.buf[start-3-1:start])
        # right range
        if self.inRange(start, start + 3):
            L.append(self.buf[start-1:start+3])
        # up range
        if self.inRange(start, start - 3 * self.N):
            L.append([self.buf[start-1],
                     self.buf[(start-1)-(1*self.N)],
                     self.buf[(start-1)-(2*self.N)],
                     self.buf[(start-1)-(3*self.N)]])
        # down range
        if self.inRange(start, start + 3 * self.N):
            L.append([self.buf[start-1],
                     self.buf[(start-1)+(1*self.N)],
                     self.buf[(start-1)+(2*self.N)],
                     self.buf[(start-1)+(3*self.N)]])
        # diagonal up & left range
        if self.inRange(start, start - 3 * self.N - 3):
            L.append([self.buf[start-1],
                     self.buf[(start-1)-(1*self.N)-1],
                     self.buf[(start-1)-(2*self.N)-2],
                     self.buf[(start-1)-(3*self.N)-3]])
        # diagonal up & right range
        if self.inRange(start, start - 3 * self.N + 3):
            L.append([self.buf[start-1],
                     self.buf[(start-1)-(1*self.N)+1],
                     self.buf[(start-1)-(2*self.N)+2],
                     self.buf[(start-1)-(3*self.N)+3]])
        # diagonal down & left range
        if self.inRange(start, start + 3 * self.N - 3):
            L.append([self.buf[start-1],
                     self.buf[(start-1)+(1*self.N)-1],
                     self.buf[(start-1)+(2*self.N)-2],
                     self.buf[(start-1)+(3*self.N)-3]])
        # diagonal down & right range
        if self.inRange(start, start + 3 * self.N + 3):
            L.append([self.buf[start-1],
                     self.buf[(start-1)+(1*self.N)+1],
                     self.buf[(start-1)+(2*self.N)+2],
                     self.buf[(start-1)+(3*self.N)+3]])
        return L

    def inRange(self, start, end):
        'Is end in range from start'
        n = self.N
        if start % self.N != 0:
            n = start % self.N
        m = (start - n) / self.N + 1

        j = self.N
        if end % self.N != 0:
            j = end % self.N
        i = (end - j) / self.N + 1

        if end < 1 or end > self.N * self.N:
            return False

        s, t = abs(end - start), abs(m - i)
        if s == 3:  # left/right
            return m == i
        elif s == 3 * self.N:  # up/down
            return m >= 1 and m <= self.N
        elif t == 3 and end in [start - 3 * self.N - 3, start - 3 * self.N + 3,  # diag up left/right
                                start + 3 * self.N - 3, start + 3 * self.N + 3]:  # diag down left/right
            return end >= 1 and end <= self.N * self.N
        return False
