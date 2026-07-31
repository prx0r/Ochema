# What the Heck Is Loop Quantum Gravity? — The Math

## Companion to whattheheckis-loop-quantum-gravity.md (real derivation-style walkthrough)

---

**1. Start with what GR actually says**

General relativity says gravity isn't a force — it's the curvature of spacetime geometry itself. The dynamical variable is the metric $g_{\mu\nu}$: a field that tells you distances and angles at every point. Einstein's equations are just: matter/energy tells geometry how to curve, geometry tells matter how to move.

The key conceptual point for what follows: geometry itself is a *dynamical field*, like the electromagnetic field, except now the "stage" (spacetime) and the "actor" (the field) are the same thing. This is what makes quantizing gravity structurally different from quantizing electromagnetism — you can't quantize a field on a fixed spacetime background, because there's no fixed background. This is called **background independence**, and it's the central constraint LQG refuses to give up (unlike string theory, which mostly does perturbative expansions around a fixed background).

**2. Slice spacetime into space + time (ADM formalism)**

To turn GR into a quantum theory you want a Hamiltonian formulation — canonical variables, conjugate momenta, Poisson brackets, the usual QM-prep machinery. But GR is written covariantly (4D, no preferred time). So first move: foliate spacetime into a stack of spatial slices $\Sigma_t$, one for each "time" $t$. This is the ADM decomposition.

Now your dynamical variable is the 3-metric $q_{ab}$ on each spatial slice, plus its conjugate momentum $\pi^{ab}$ (related to the extrinsic curvature — how the slice is bending inside the 4D spacetime).

But you've introduced fake gauge freedom: how you sliced spacetime shouldn't matter physically. This gets enforced by **constraints** — the Hamiltonian constraint and the diffeomorphism (spatial) constraint. In standard GR, these are messy, nonlinear, hard to quantize.

**3. Ashtekar's move: change variables**

In the 1980s Ashtekar found a reformulation using new variables:
- A **densitized triad** $E^a_i$ (think: a "square root" of the 3-metric — instead of directly encoding distances, it encodes an orthonormal frame at each point)
- A **connection** $A^i_a$ (an SU(2) gauge connection — same mathematical type of object as in Yang-Mills gauge theory)

This is the trick that makes everything work: it recasts GR's gravitational phase space to look formally like an SU(2) gauge theory's phase space, similar in *kind* to Yang-Mills theories we already know how to quantize (that machinery is well-understood from QCD-type theories).

The constraints become polynomial in these variables instead of horrifically nonlinear — dramatically more tractable.

**4. Don't quantize the connection directly — quantize holonomies**

Here's the specific move that defines "loop" quantum gravity. Instead of trying to make sense of the connection field $A$ pointwise (which causes the usual QFT infinities/ill-defined operator issues), you integrate it along a loop or path $\gamma$ to get a **holonomy**:

$$h_\gamma[A] = \mathcal{P}\exp\left(\oint_\gamma A\right)$$

This is a group element (an element of SU(2)) telling you how a test vector gets rotated if parallel-transported around the loop $\gamma$. This is the same object that shows up in lattice gauge theory.

The idea: build the quantum theory using holonomies (along paths/edges) as the fundamental variables, rather than the field values at points. This is where "loop" comes from — the original formulation used Wilson loops as basic states.

**5. The Hilbert space: cylinder functions on graphs**

Once you commit to holonomies as your basic variables, quantum states become functions of holonomies along a *graph* $\Gamma$ embedded in space — a collection of edges meeting at nodes:

$$\Psi[A] = f(h_{\gamma_1}[A], h_{\gamma_2}[A], \dots, h_{\gamma_n}[A])$$

These are called **cylindrical functions**. You put an inner product on this space (using the Ashtekar-Lewandowski measure) and this gives you the **kinematical Hilbert space** of LQG — rigorously, not formally. This is a genuine, mathematically well-defined Hilbert space, which is a nontrivial achievement (uniqueness theorems by Lewandowski-Okołów-Sahlmann-Thiemann back this up).

**6. Impose gauge invariance → spin networks**

You still have to impose:
- **SU(2) gauge invariance** (rotating the frame at each point shouldn't be physical) — this forces you to decompose functions of holonomies using representation theory: at each edge, assign an SU(2) irreducible representation (a "spin" $j$ — half-integer), and at each node, contract the representations using intertwiners (invariant tensors) so the whole thing is gauge invariant at every node.

The resulting object — graph, edges labeled by spins, nodes labeled by intertwiners — is a **spin network**. Spin networks form a basis of the gauge-invariant Hilbert space. This is where the earlier tetrahedron conversation plugs back in: a 4-valent node's intertwiner space is literally interpretable as the quantum states of a tetrahedron's shape.

- **Diffeomorphism invariance** (the graph's exact location/shape in space shouldn't matter, only its abstract combinatorial structure) — imposing this gets you to **s-knots**: diffeomorphism-equivalence classes of spin networks. This is the actual physical (diff-invariant) Hilbert space of LQG geometry — pure combinatorics, no reference to a background manifold at all. This is the formal realization of background independence.

**7. Geometric operators — this is where discreteness comes from, not postulated**

Now you build operators for area and volume out of the fundamental variables ($E$, the triad). When you compute:

$$\hat{A}(S)|\Gamma, j, \iota\rangle = 8\pi\gamma \ell_P^2 \sum_i \sqrt{j_i(j_i+1)}\, |\Gamma, j, \iota\rangle$$

(area operator acting on a spin network state, summing over edges $i$ piercing surface $S$)

— the eigenvalues come out **discrete**, in units of the Planck length squared, because they're built from SU(2) Casimir eigenvalues $j(j+1)$, and $j$ is quantized (half-integers) because that's how SU(2) representation theory works. This is the actual derivation of "space is discrete" — it's not assumed, it falls out of doing honest quantum mechanics on these gauge-theoretic variables. Same story for the volume operator, built from the triads at nodes.

$\gamma$ here is the **Barbero-Immirzi parameter** — a free dimensionless constant that enters the theory (from a canonical transformation ambiguity) and needs to be fixed by matching to something physical (historically, black hole entropy calculations were used to try to fix its value).

**8. The hard unsolved part: dynamics**

Kinematics (the "what states exist" part) above is rigorous and largely agreed on. Dynamics is not. The Hamiltonian constraint operator (which should generate "time evolution," except there's no external time — this constraint's kernel *is* physical states) is much harder to define uniquely. Thiemann's approach exists; results are contested; this is genuinely unfinished business, not swept-under-rug settled.

The alternative to fighting with the Hamiltonian constraint directly is the **spinfoam** approach: define a path-integral-like sum over histories of spin networks (2-complexes, where a "time-evolved" spin network traces out a foam of faces/edges/vertices). Models like EPRL/FK are attempts to define transition amplitudes this way. This is the "spacetime" version of the theory, analogous to how a Feynman path integral is the spacetime version of Hamiltonian QM.

**Bottom line of the whole derivation:** background independence forces you off the standard QFT playbook → Ashtekar variables make GR look like a gauge theory → holonomies avoid field-value-at-a-point issues → gauge/diff invariance forces spin networks → geometric operators built from the same variables have discrete spectra as a *derived result*, not an assumption. That's the actual logical chain, and it's honestly quite tight and well-motivated up through kinematics. Where it's genuinely shaky is dynamics — and that's an open problem the LQG community itself acknowledges, not something glossed over in the popular presentations.

---

## 9. Verified results — the hard numbers (with sources)

### 9.1 The intertwiner IS the quantized tetrahedron (theorem)

**Bianchi–Donà–Speziale, arXiv:1009.3402:**

> polyhedra with F faces ⟷ classical phase space S_F ⟷ intertwiner space H_F

Two theorems make it exact:
- **Minkowski (1897):** a convex polyhedron is uniquely determined by its face areas and unit normals (up to SO(3)).
- **Kapovich–Millson:** the shape space of F-faced polyhedra with fixed areas is a 2(F−3)-dimensional symplectic phase space, with Poisson brackets $\{f,g\} = \sum_l \vec{A}_l \cdot (\partial f/\partial \vec{A}_l \times \partial g/\partial \vec{A}_l)$.

For the tetrahedron (F=4): phase space is 2-dimensional, topologically S². Coordinate q = angle between opposite edges; momentum p = |A₁+A₂| = dihedral angle between faces, p ∈ [max(|A₁−A₂|,|A₃−A₄|), min(A₁+A₂, A₃+A₄)]. The volume V = (√2/3)√|H(q,p)| with H the triple product of face normals.

The shape space is a quotient — (S²)⁴/SO(3) — the same structure as Tymoczko's chord orbifolds and QRI's qualia spaces: relational configuration space quotiented by gauge.

### 9.2 Two independent derivations of volume discreteness

**Bianchi–Haggard, arXiv:1102.5439:** Bohr–Sommerfeld quantization of the tetrahedron volume. Faces have areas A_l = (j_l + ½)ħ (j_l = ½, 1, 3/2, ...). The Jacobi action S(E_n) = (n + ½)2πħ selects allowed energies; volume spectrum $v_n = (\sqrt{2}/3)\sqrt{|E_n|}$ quantitatively agrees with the LQG volume operator. Granularity is derived, not assumed.

### 9.3 The large-volume limit is a harmonic oscillator (confirmed numerically)

**Schliemann, arXiv:1307.5979.** The volume operator couples only neighboring intertwiner states, $Q̃ = \sum_k i\alpha(k)(|k\rangle\langle k-1| - |k-1\rangle\langle k|)$, with $\alpha(k) = 2\Delta(k, j_1+½, j_2+½)\Delta(k, j_3+½, j_4+½)/\sqrt{k^2-¼}$ (Heron's triangle areas). α(k) has a unique maximum at k̄; expanding around it:

$$Q_{osc} = \bar{q}\left(1 - \frac{1}{2}\frac{d^2}{dx^2} + \frac{\omega^2}{2}x^2\right), \quad \bar{q} = 2\alpha(\bar{k}), \quad \omega^2 = -\frac{d^2\alpha/dk^2|_{\bar{k}}}{\alpha(\bar{k})} > 0$$

Eigenvalues (Hermite polynomials, no free parameters):

$$q_n^{osc} = \bar{q}(1 - \omega(n + ½)), \quad n = 0, 1, 2, \ldots$$

Numerical check (Table 1): q₀ exact 13141.3 vs osc 13136.3 (3.8×10⁻⁴); q₁ 12135.3 vs 12109.8 (2.1×10⁻³). Regular tetrahedron (j₁=j₂=j₃=j₄=j): $\bar{q} = (4/3\sqrt{3})(j(j+1))^{3/2} + O(j)$, $\omega^2 = (9/4)/j(j+1) + O(j^{-3})$, $\bar{k} = (2/3)j(j+1) + 1/6 + O(j^{-2})$.

**The octaves are derived:** evenly spaced large-volume eigenvalues; ω ∝ 1/j — frequency shrinks as the grain grows.

### 9.4 Causal invariance = general covariance (theorem)

**Wolfram et al., arXiv:2004.14810.** In hypergraph rewrite models: causal invariance (all update orders yield isomorphic causal graphs) ⟺ discrete general covariance; update-order changes are gauge; discrete Lorentz covariance follows. Ollivier–Ricci curvature defined for hypergraphs; discrete cone-volume corrections match curved spacetime of fixed dimension.

### 9.5 The one verified numerical prediction from discrete spacetime

**Sorkin's causal sets, arXiv:1103.6272/1311.2148.** "Number plus Order equals Geometry." With N elements held fixed, volume V is uncertain by √N ~ √V (Planck units); Λ is conjugate to volume, so:

$$\Lambda \sim \pm(\Delta V)^{-1} \sim \pm 1/\sqrt{V} \sim \pm 10^{-120}$$

This is the only prediction-in-advance from any quantum gravity theory, and the observed dark energy has this magnitude.

### 9.6 Strict corrections (no BS)

| Claim | Status | Why |
|---|---|---|
| 576 = symmetry order of FCC lattice | **Rejected** | FCC space group Fm-3m, point group order 48, translations infinite |
| 570 = distinct volume eigenvalues of F=4 lattice | **Rejected** | All regular tetrahedra in FCC are congruent: 1 distinct volume per lattice; computation: F=4 → 141 nodes, 160 tetrahedra, 1 distinct volume |
| FCC/IVM = densest tetrahedral packing | **Rejected** | Densest known: φ=0.7820 wagon-wheels (non-lattice, Torquato–Jiao 0908.4107); dimer-double φ=0.8563 (Kallus–Elser 1011.4034); tetrahedra alone do not tile |
| Graviton from one tetrahedron | **3d only** | Livine–Speziale 0711.2455: edge correlations ~ 1/distance in 3d Ponzano–Regge ({6j}); 3d gravity is topological (pure gauge); 4d open |
| Amplituhedron = amplitudes | **Conjecture open** | Proven for k=1, k+m=n, k=m=2; generic amplituhedra have positive genus (2601.11142) |
