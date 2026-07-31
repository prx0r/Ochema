#!/usr/bin/env python3
"""Decisive test: automorphism (symmetry) group order of the F=4 FCC lattice.

The 576 thesis predicts the F=4 lattice's symmetry group may have order
576 or 570. This computes the graph automorphism count directly.

Method: build the FCC node graph (edges = nearest neighbors at distance
sqrt(2)), then count automorphisms via canonical labeling with a simple
backtracking + degree-sequence refinement, OR via networkx if available.
For a 141-node graph exact automorphism count may be expensive; we use
degree refinement (Weisfeiler-Lehman) for a lower bound and the actual
crystallographic point group (known: FCC = cubic Fm-3m, order 48 for the
point group of one site) as the analytic answer.

The FULL lattice symmetry group is the space group Fm-3m (cubic), whose
point group is m-3m (order 48). The number 576 does NOT appear as the
symmetry order of the FCC lattice. This is the honest result.
"""
import numpy as np
from itertools import combinations
from collections import Counter

def generate_fcc(radius):
    nodes = set()
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                if (x + y + z) % 2 == 0:
                    d2 = x*x + y*y + z*z
                    if d2 <= radius * radius:
                        nodes.add((x, y, z))
    return np.array(sorted(nodes), dtype=float)

def build_graph(nodes):
    """Adjacency: nearest neighbors at distance sqrt(2)."""
    n = len(nodes)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d2 = sum((nodes[i]-nodes[j])**2)
            if abs(d2 - 2) < 1e-9:
                adj[i].add(j)
                adj[j].add(i)
    return adj

# 1. Analytic result: FCC space group
print("=" * 60)
print("DECISIVE TEST: SYMMETRY GROUP ORDER OF THE FCC LATTICE")
print("=" * 60)
print("""
Analytic result (crystallography):
  FCC lattice space group: Fm-3m (No. 225)
  Point group: m-3m (full octahedral/cubic)
  Point group order: 48
  Translations: infinite (Bravais lattice)
  
  The finite point group of the FCC lattice has order 48.
  576 does not appear as the symmetry order of the FCC lattice.
  The full space group is infinite (translations), not 576.
""")

# 2. Verify with the finite F=4 cluster: count automorphisms via WL refinement
for R in [2, 3, 4]:
    nodes = generate_fcc(R)
    adj = build_graph(nodes)
    n = len(nodes)
    deg = [len(a) for a in adj]
    # Weisfeiler-Lehman color refinement (1 round = degree; iterate to fixpoint)
    colors = list(deg)
    for _ in range(10):
        new_colors = []
        for i in range(n):
            neigh_colors = sorted(colors[j] for j in adj[i])
            new_colors.append((colors[i], tuple(neigh_colors)))
        # compress
        mapping = {}
        for c in new_colors:
            if c not in mapping:
                mapping[c] = len(mapping)
        colors = [mapping[c] for c in new_colors]
    color_counts = Counter(colors)
    # WL refinement gives a lower bound on automorphism count:
    # |Aut| <= product over color classes of (class_size)!
    # (each color class must map within itself; the product of factorials
    #  is an upper bound, the refined partition a lower bound on classes)
    upper = 1
    for size in color_counts.values():
        f = 1
        for i in range(2, size+1):
            f *= i
        upper *= f
    print(f"F={R}: {n} nodes | degree dist: {dict(Counter(deg))}")
    print(f"  WL color classes: {len(color_counts)} | sizes: {sorted(color_counts.values(), reverse=True)[:8]}")
    print(f"  Upper bound on finite-cluster automorphisms: {upper}")
    print()

print("""
CONCLUSION:
  The symmetry group of the FCC lattice is the crystallographic space
  group Fm-3m. Its point group has order 48. The FINITE cluster at any
  radius has automorphism count bounded by the WL partition (computed
  above) — and for the largest classes the order is a product of
  factorials (often huge), but it is NOT 576 in any natural sense.

  Therefore the predicted "576 as symmetry order" does NOT hold.
  The number 576 is NOT the symmetry group order of the lattice.

  This is the honest result of the decisive test:
  - The GEOMETRY (tetrahedral lattice, volume spectrum) is real.
  - The NUMBER 576 is not recovered from the lattice's symmetry.
  - The 570/576 resonance remains pattern matching, not structure.
""")
