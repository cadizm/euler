#!/usr/bin/env python

#
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.
#
# 1---2---3      1---2---+      1---2---+
# |   |   |      |   |   |      |   |   |
# +---+---4      +---3---4      +---3---+
# |   |   |      |   |   |      |   |   |
# +---+---5      +---+---5      +---4---5
#
# 1---+---+      1---+---+      1---+---+
# |   |   |      |   |   |      |   |   |
# 2---3---4      2---3---+      2---+---+
# |   |   |      |   |   |      |   |   |
# +---+---5      +---4---5      3---4---5
#
# How many routes are there through a 20x20 grid?
#

#
# Implementation notes: nxn grid can be interpreted as NxN lattice graph (for N = n + 1).
# E.g. for N = 3 and 5:
#
# 1---2---3      1---2---3---4---5
# |   |   |      |   |   |   |   |
# 4---5---6      6---7---8---9--10
# |   |   |      |   |   |   |   |
# 7---8---9     11--12--13--14--15
#                |   |   |   |   |
#               16--17--18--19--20
#                |   |   |   |   |
#               21--22--23--24--25
#
#               i = 4, j = 3 --> 18 = (i - 1) * N + j
#
# Number of vertices = N * N
# Number of edges = 2 * N * (N - 1)
#
# In order to construct an adjacency matrix, represent NxN grid as 1-dimensional array
# and compute valid neighbors (i.e., the edges E between vertices V in graph G = (V, E))
#


from euler.math import central_binomial_coefficient
from euler.graph import non_back_tracking_paths


def run():
    # non_back_tracking_paths(N) == central_binomial_coefficient(N - 1)
    # print non_back_tracking_paths(3)
    # print non_back_tracking_paths(4)
    # print central_binomial_coefficient(2)
    # print central_binomial_coefficient(3)

    print central_binomial_coefficient(20)
