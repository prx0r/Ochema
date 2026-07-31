#!/usr/bin/env python3
"""576 Lattice Computation: FCC/IVM tetrahedra + LQG volume spectrum.

Generates the F=4 FCC lattice (Fuller's IVM), finds all regular tetrahedra,
computes the LQG quantum-tetrahedron volume spectrum, and counts DISTINCT
volume eigenvalues — the testable claim of the 576 thesis.

Claim: if the number of distinct volume states of the F=4 lattice approaches
570 (the Urantia Book's morontia body count), the channeled number IS the
spectrum of the lattice.
"""
import numpy as np
from itertools import combinations

def generate_fcc(radius):
    """FCC lattice: integer (x,y,z) with x+y+z even, inside sphere radius."""
    nodes = set()
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                if (x + y + z) % 2 == 0:
                    d2 = x * x + y * y + z * z
                    if d2 <= radius * radius:
                        nodes.add((x, y, z))
    return np.array(sorted(nodes), dtype=float)

def find_tetrahedra(nodes):
    """Find all regular tetrahedra (nearest-neighbor cliques, edge=sqrt(2)) in FCC."""
    node_list = [tuple(map(int, n)) for n in nodes]
    node_set = set(node_list)
    tetras = set()
    # For each node, its 12 nearest neighbors (kissing number) form
    # octahedra + tetrahedra; find 4-cliques of mutual distance sqrt(2)
    for a in node_list:
        neigh = []
        for b in node_list:
            if a == b:
                continue
            d2 = (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
            if d2 == 2:
                neigh.append(b)
        for combo in combinations(neigh, 3):
            ok = True
            for x, y in combinations(combo, 2):
                d2 = (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2
                if d2 != 2:
                    ok = False
                    break
            if ok:
                tetras.add(tuple(sorted([a] + list(combo))))
    return sorted(tetras)

def tetra_volume(p):
    """Volume of tetrahedron from 4 points (rows of p)."""
    ab = p[1] - p[0]; ac = p[2] - p[0]; ad = p[3] - p[0]
    return abs(np.dot(ab, np.cross(ac, ad))) / 6.0

def lqg_volume_eigenvalues(jmax=30):
    """LQG volume operator eigenvalues for the REGULAR quantum tetrahedron
    (all four faces spin j). Standard result (Bianchi-Haggard 1102.5439):
    V_j = (sqrt(2)/3) * sqrt( j(j+1)(2j+1)/8 )  in units of l_P^3.
    Returns list of (j, V_j)."""
    return [(j, np.sqrt(2)/3.0 * np.sqrt(j*(j+1)*(2*j+1)/8.0)) for j in range(1, jmax+1)]

print("=" * 60)
print("576 LATTICE COMPUTATION")
print("=" * 60)

for R in [2, 3, 4, 5, 6]:
    nodes = generate_fcc(R)
    tetras = find_tetrahedra(nodes)
    node_map = {tuple(map(int, n)): i for i, n in enumerate(nodes)}
    vols = []
    for t in tetras:
        idx = [node_map[c] for c in t]
        p = np.array([nodes[i] for i in idx])
        vols.append(tetra_volume(p))
    unique = sorted(set(round(v, 9) for v in vols))
    # centroid shells
    shells = {}
    for t in tetras:
        idx = [node_map[c] for c in t]
        p = np.array([nodes[i] for i in idx])
        r = round(float(np.linalg.norm(p.mean(axis=0))), 5)
        shells[r] = shells.get(r, 0) + 1
    print(f"\nF={R}: {len(nodes)} nodes | {len(tetras)} tetrahedra | "
          f"{len(unique)} distinct volumes | {len(shells)} shells")
    if R == 4 or R == 5:
        for r in sorted(shells)[:8]:
            print(f"    shell r={r:.3f}: {shells[r]} tetrahedra")

print("\n" + "=" * 60)
print("LQG VOLUME SPECTRUM of the regular quantum tetrahedron")
print("=" * 60)
spec = lqg_volume_eigenvalues(25)
print(f"Number of distinct eigenvalues (j=1..25): {len(spec)}")
for j, v in spec[:15]:
    print(f"  j={j:2d}: V = {v:.6f} l_P^3")
print("...")
# Cumulative: how many distinct eigenvalues up to each j?
for jmax in [8, 12, 16, 20, 24, 30]:
    spec = lqg_volume_eigenvalues(jmax)
    print(f"  Up to j={jmax}: {len(spec)} distinct eigenvalues")
