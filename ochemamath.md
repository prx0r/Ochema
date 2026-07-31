# OchemaMath

## A Mathematical Formalization of the Ochema Framework

### The bearer as operator algebra · Time as modular flow · Exclusion as projection · The selector as sheaf cohomology

**Status: Formalization in progress. Every claim graded (A–E). The mathematics is theorem-grade; the application to consciousness is graded C–E throughout and labeled as such. This document does not claim that consciousness is derived — it claims that the framework's structures have genuine mathematical homes.**

---

## 0. The Strategy

The informal framework (ochema-formal.md) uses notation that *looks* mathematical but is not yet mathematics:

- E_i: Ω → (P_i, W_i) — "the exclusion operator"
- A_i* = Fix(𝕽, 𝕻_i, 𝓤) — "the joint fixed point"
- ι_i — "the subject index"
- D_i ≡_int A_i — "token identity under asymmetric access"

OchemaMath replaces each with a genuine mathematical object, drawn from the frontier crawl (frontier-math.md): operator algebras, Tomita–Takesaki theory, sheaf cohomology, topos theory, spectral triples, information geometry. The discipline is strict: **each replacement must be a real object with theorems attached, and the consciousness-application grade must be stated.**

---

## 1. The Bearer as a von Neumann Algebra

### 1.1 Definition (Bearer Algebra)

**Definition 1 (Bearer algebra).** Let the bearer of a conscious process be represented by a von Neumann algebra:

```
M_i ⊂ B(𝓗_i)
```

acting on a Hilbert space 𝓗_i, together with a distinguished faithful normal state:

```
ω_i: M_i → ℂ,   ω_i positive, faithful, normal
```

**Grade: A (the mathematics exists — von Neumann algebras, faithful normal states).**
**Grade for "the bearer IS such an algebra": D (application).**

### 1.2 Why this is the right object

| Informal ochema | OchemaMath | Why |
|---|---|---|
| A_i (materially enacted process) | (M_i, ω_i) — algebra + state | The algebra is the observables; the state is the register. Both are required for the time theorem below. |
| The material regime Σ_i | The representation M_i ⊂ B(𝓗_i) | Different material regimes = different representations — non-isomorphic in general (Material Enactment, §6) |
| The history H_i | The state ω_i's past-dependence via modular structure | The state carries the history (non-Markovian structure is encoded in ω_i) |
| The identity-relevant invariants 𝒥_i | The center Z(M_i) and the modular invariants | What commutes with everything — the structural invariants |

**The single most important fact:** for (M_i, ω_i) with ω_i cyclic and separating, the **Tomita–Takesaki theorem** gives:

```
S_i: 𝓗_i → 𝓗_i   (Tomita operator, antilinear)
Δ_i = S_i* S_i   (modular operator, positive)
J_i = S_i Δ_i^{-1/2}   (modular conjugation, antiunitary)
σ_t^ω(A) = Δ_i^{it} A Δ_i^{-it}   (modular automorphism group)
```

**Grade: A (theorem — Tomita–Takesaki).**

### 1.3 The subject index as the modular invariant

**Definition 2 (Subject index).** The subject index ι_i is the subalgebra fixed by the modular group:

```
M_i^{σ^ω} = { A ∈ M_i : σ_t^ω(A) = A for all t }
```

**Claim:** the subject index is the invariant structure of the bearer under its own time-flow — the mathematical version of "the perceiving subjectivity forever remains true to its own nature" (Spanda, Stanza 3) and the ochema claim that ι_i survives content changes.

**Grade: A (the mathematics — modular fixed-point subalgebras are studied); C (the identification with the subject index — application).**

---

## 2. Time as Modular Flow (The Thermal Time Theorem)

### 2.1 The theorem (Connes–Rovelli 1994)

**Theorem (thermal time).** Let (M, ω) be a von Neumann algebra with faithful normal state ω. Then ω is a KMS state at inverse temperature β = 1 with respect to its own modular automorphism group σ_t^ω. The flow:

```
α_t^ω(A) = σ_t^ω(A) = Δ^{it} A Δ^{-it}
```

is the **thermal time** of the state ω.

In a background-independent theory (no external Hamiltonian), the physical time is *derived from the state*: the state determines the flow.

**Grade: A (theorem — Tomita–Takesaki, KMS theory).**
**Grade for "physical time IS thermal time": C (Connes–Rovelli hypothesis, well-supported, not established).**

### 2.2 The moment-triad in operator terms

The three moments of the tradition (Spanda sṛṣṭi–sthiti–saṃhāra; Proclus monē–proodos–epistrophē; Ñāṇavīra's interchange; Orch-OR's superposition–orchestration–collapse) take the form:

| Moment | Operator-algebraic content |
|---|---|
| **Emergence (sṛṣṭi)** | The state ω evolves; observables transform under σ_t^ω; superposition builds in the representation |
| **Persistence (sthiti)** | The modular flow is a group: σ_{t+s} = σ_t ∘ σ_s; the state is KMS-stable under it — the system persists in its own time |
| **Withdrawal (saṃhāra)** | A state transition: ω → ω′ (the register changes); the modular flow is *redefined*: σ_t^ω → σ_t^ω′ |

**The withdrawal is the moment.** When the state changes, the time-flow itself changes — the new moment's time is the new state's modular flow.

**Grade: A (the mathematics — state transitions, modular flows); C (identification with the conscious moment — application).**

### 2.3 The orchestration law as a corollary

**Corollary (orchestration law).** The time-structure of a bearer is a function of its state:

```
τ(ω) = (σ_t^ω)   — the modular flow of ω
```

**The state of the register determines the time of the subject — by theorem, not metaphor.** This is the formal content of the orchestration law (the-orchestration.md §3) and of Cannon's "you can only go to the level your vibrations are compatible with."

**Grade: A (the theorem); C (the physical-time identification).**

---

## 3. The Exclusion Operation as a Projection

### 3.1 The problem with the informal E_i

The informal E_i: Ω → (P_i, W_i) treats Ω as "the space of all possible determinations" and E_i as "one operation carving both poles." OchemaMath must say what kind of object this is.

### 3.2 First formalization: E_i as a conditional expectation

**Definition 3 (Exclusion as conditional expectation).** Let N ⊂ M be a subalgebra (the "accessible" observables of the subject pole). The exclusion operation is the **conditional expectation**:

```
E_i: M → N,   E_i(1) = 1,   ω ∘ E_i = ω|_N
```

The subject pole P_i corresponds to N (what the subject can access); the world pole W_i corresponds to the complement structure M/N (what is excluded from access). E_i is a positive, unit-preserving projection of algebras.

**Grade: A (the mathematics — conditional expectations, Takesaki's theorem on their existence).**
**Grade for "this IS the phenomenal boundary": D (application).**

**Takesaki's theorem (relevant fact):** a conditional expectation E: M → N exists if and only if N is invariant under the modular group σ_t^ω. That is: **the exclusion operation exists precisely when the subject pole is modular-invariant — when it is time-stable under the bearer's own flow.**

**This is a real constraint.** The subject pole is not arbitrary: it must be invariant under the modular flow of the state. The informal "co-emergence of P_i and W_i" becomes: the modular-invariant subalgebras of M are exactly the possible subject poles.

**Grade: A (theorem — Takesaki); C (application).**

### 3.3 Second formalization: E_i as a spectral projection

For the discrete case (the moment, the collapse):

**Definition 4 (Exclusion at the moment).** At a state transition, the exclusion is a projection onto a spectral subspace:

```
E_i = 1_{[0,ε]}(K)   — spectral projection of the modular Hamiltonian K = -log Δ
```

The collapse selects the states within the accessible band; the rest is annihilated ("one particle location/curvature is selected and becomes classical. The other ceases to exist" — Orch-OR, in operator form).

**Grade: A (the mathematics — spectral calculus); C/D (application — OR as spectral projection is a hypothesis).**

---

## 4. The Selector Problem as Sheaf Cohomology

### 4.1 The problem

The selector problem (Λ_p): given a conscious organism, which physical process is the bearer? Physical descriptions admit multiple partitions at multiple scales; different analytical choices produce different candidate bearers.

### 4.2 Formalization: the bearer as a global section

**Definition 5 (Model family as a sheaf).** Let the physical model family 𝕽 = {R^N, R^B, R^M, R^A, R^S} (neural, bioelectric, metabolic, autonomic, sensorimotor) be a **sheaf** ℱ over a space of scales/partitions U:

```
ℱ: Open(U)^op → Set
```

Each open set (scale-region) gets the set of candidate bearers recovered at that scale; restriction maps glue finer scales into coarser ones.

**The selector problem becomes:** does a **global section** exist — a candidate bearer s ∈ ℱ(U) defined on all of U and consistent on overlaps?

**Theorem (sheaf cohomology).** The obstruction to gluing local sections into a global section is measured by the cohomology:

```
H^1(U, ℱ) = 0  ⟺  local compatibility implies global existence
```

**The framework's claim:** the bearer exists (H¹ = 0) when the physical and phenomenal descriptions are consistent on all overlaps; the selector problem is the computation of whether the gluing obstruction vanishes.

**Grade: A (the mathematics — sheaf cohomology); C (the identification — the model family as a sheaf is a plausible formalization, untested).**

### 4.3 The joint fixed point as a limit

**Definition 6 (Joint fixed point).** The joint fixed point is the **limit** of the diagram of candidate bearers:

```
A_i* = lim_{k} (Rec(R^k))  — the universal object through which all candidates factor
```

when the limit exists (H¹ = 0). The framework's "convergence" is the categorical limit; the "abductive gap" is the fact that the limit's existence does not prove identity with D_i.

**Grade: A (the mathematics — categorical limits); C (application).**

---

## 5. Co-Emergence as Topos Duality

### 5.1 The claim

"Subject and world co-emerge through the same operation; neither exists prior to the partition."

### 5.2 Formalization: internal vs external

**Definition 7 (Subject as internal observer of a topos).** Let 𝓔 be a topos (a universe of discourse). The subject pole is the internal observer — the logic *within* 𝓔; the world pole is 𝓔 itself seen from outside (the external view).

**Lawvere's insight:** a topos has an internal logic; what is "true" is relative to the topos. The co-emergence claim is: there is no external vantage prior to the topos — the subject's logic and the world's structure are one object, seen internally (as logic) and externally (as structure).

**Grade: A (the mathematics — topos theory); D (the identification with phenomenal co-emergence — application).**

### 5.3 The univalence version

**HoTT/univalence:** equivalent structures are identical. The identity claim D_i ≡_int A_i becomes: the phenomenal description and the physical description are **equivalent structures** — and by univalence, equivalent structures are identical. The "epistemic asymmetry" (E ⊬ P) is the difference between the internal and external perspectives on the same type.

**Grade: A (the mathematics — univalence); D (application).**

---

## 6. The Material Enactment Principle as Non-Isomorphism

### 6.1 The claim

Same abstract transition table ⇏ same materially available dynamics.

### 6.2 Formalization

**Theorem-shaped statement (Material Enactment).** Two bearers with isomorphic abstract transition systems:

```
T_1 ≅ T_2  (abstractly)
```

may have **non-isomorphic von Neumann algebras**:

```
M_1 ≇ M_2  (as algebras, or as representations)
```

**Evidence:**
- Type classification: the same algebra structure can be realized as Type I, II, or III factors; the modular flows differ.
- **The CIMC challenge falls here:** a finite automaton's algebra is finite-dimensional (Type I, trivial modular structure). If the moment's temporality is the modular flow, a finite automaton lacks the structure that constitutes the moment.
- Fields & Levin (energy budgets), Cadinu et al. (material specificity): substrate changes computation.

**Grade: A (the mathematics — non-isomorphic representations exist); B (the physics — material specificity established); D (the inference that consciousness requires non-trivial modular structure).**

### 6.3 The strongest version

**Challenge to computationalism (formal):** Let C be a finite-state computational implementation of second-order perception (CIMC's sufficient condition). Then:

```
dim(M_C) < ∞  ⟹  σ_t^{ω_C} is trivial (or periodic with finite spectrum)
```

The modular flow of a finite-dimensional algebra is essentially trivial. If the moment's time is the modular flow (thermal time), a finite automaton cannot implement the moment — **not by intuition, but by theorem.** The Material Enactment Principle has a theorem-shaped defense.

**Grade: A (the mathematics — finite-dimensional modular structure); C (the premise that modular time is constitutive).**

---

## 7. The Bridge Hypotheses as Morphisms

The informal bridge hypotheses table (unity, boundary, temporality, quality, valence, agency, subject index) becomes a set of maps:

| Phenomenal | OchemaMath object | Grade |
|---|---|---|
| Unity (u_i) | The joint state ω_i on the full algebra M_i (irreducibility of the representation) | A (math) / C (app) |
| Boundary (b_i) | The subalgebra N ⊂ M fixed by the conditional expectation E_i | A (math) / C (app) |
| Temporality (τ_i) | The modular flow σ_t^ω | A (theorem) / C (hypothesis) |
| Quality (q_i) | The spectrum of the modular Hamiltonian K = −log Δ | A (math) / D (app) |
| Valence (ν_i) | Perelman entropy / a coherence functional on the state space | A (math) / D (app) |
| Agency (a_i) | The group of automorphisms achievable by state changes (counterfactual reach) | A (math) / D (app) |
| Subject index (ι_i) | The modular fixed-point subalgebra M^{σ^ω} | A (math) / C (app) |

**The spectral interpretation of quality is the most striking:** if quality is the spectrum of the modular Hamiltonian, then qualities are the "frequencies" of the state's own time — a mathematical version of "the felt quality IS the geometry" (rasa = geometry = valence), now with a specific operator.

**Grade: the identifications are D (speculative); the objects exist (A).**

---

## 8. What Is Established vs. What Remains Open

### Established (A–B)

| Result | Source |
|---|---|
| Tomita–Takesaki: faithful states generate modular flows | Theorem |
| KMS: the state is thermal in its own flow (β = 1) | Theorem |
| Takesaki: conditional expectations exist iff the subalgebra is modular-invariant | Theorem |
| Sheaf cohomology: H¹ measures gluing obstruction | Theorem |
| Categorical limits: joint fixed point as limit | Theorem |
| Finite-dimensional algebras have trivial modular structure | Theorem |
| Material specificity of biological computation | B (Levin, Fields, Cadinu) |

### Hypothesized (C)

| Claim | Status |
|---|---|
| Physical time IS thermal time | Connes–Rovelli hypothesis |
| The bearer IS a von Neumann algebra + state | Application, untested |
| The subject pole IS a modular-invariant subalgebra | Application, untested |
| The selector problem IS a cohomology computation | Application, untested |

### Speculative (D–E)

| Claim | Status |
|---|---|
| Quality = spectrum of the modular Hamiltonian | D |
| Valence = Perelman entropy of the state space | D |
| The collapse IS a spectral projection | D |
| Consciousness requires non-trivial modular structure | D |
| D_i ≡_int A_i as univalence | E (metaphysical reading) |

---

## 9. Falsification Conditions (OchemaMath-specific)

The formalization would be seriously weakened if:

1. **Thermal time fails as physical time** — e.g., a generally covariant system whose observed time demonstrably differs from any state's modular flow.
2. **The selector-as-sheaf is vacuous** — if the model family never glues (H¹ ≠ 0 always), the formalization says no bearer exists, which contradicts the framework's own existence assumption.
3. **Modular-invariant subalgebras are unconstrained** — if every subalgebra is modular-invariant (trivializing Takesaki's constraint), the subject pole is unconstrained and the boundary is empty formalism.
4. **Finite-dimensional systems show consciousness-like phenomenality** — if a finite automaton (CIMC's minimal case) produces reportable phenomenality, the modular-structure argument fails.
5. **The spectral-quality conjecture is contradicted** — if no systematic relation between modular spectra and experienced qualities is found, the bridge is dead.

---

## 10. The One-Sentence Statement

> **OchemaMath formalizes the bearer as a von Neumann algebra with a faithful state; time as its modular flow (Tomita–Takesaki/Connes–Rovelli); the subject pole as a modular-invariant subalgebra (Takesaki); the selector problem as sheaf cohomology; the joint fixed point as a categorical limit; and Material Enactment as the non-isomorphism of materially distinct representations — with every consciousness-identification graded C–E and falsifiable.**

---

## 11. The Theory Landscape — Support and Contrast

Every major theory in the corpus, mapped against OchemaMath. Support = where the theory's formal content agrees with (or validates) the formalization. Contrast = where it diverges. Graded.

### 11.1 Integrated Information Theory 4.0 (Tononi & Boly 2025) — THE VALIDATION

**Source:** "Integrated Information Theory: A Consciousness-First Approach to What Exists" (arXiv:2510.25998), in corpus.

**The consciousness-first turn — the single most important development for OchemaMath:**

> "Consciousness can thus be considered as intrinsic, absolute, or genuine existence — the only existence worth being — because without it there would be nothing at all... a world without consciousness would have remained 'a play before empty benches, not existing for anybody, thus quite properly speaking not existing.'"

> "IIT's explanatory identity claims that an entity's cause-effect structure accounts for all properties of an experience — essential and accidental — **with no additional ingredients**... quality is structure."

**Support for OchemaMath (formal):**

| OchemaMath | IIT 4.0 | Relation |
|---|---|---|
| D_i ≡_int A_i (identity, not dualism) | "Cause-effect structure accounts for all properties... no additional ingredients" | **IDENTICAL CLAIM** — IIT now states Ochema's identity as mainstream theory |
| The state ω (register) | The complex in its current state | Same object: state determines everything |
| Exclusion E_i (determination through exclusion) | Axiom 4: "Exclusion: every experience is definite — it is this whole... neither less nor more" | **THE SAME AXIOM** — IIT's phenomenal axiom of exclusion = OchemaMath's exclusion operation, phenomenologically grounded |
| Subject pole as modular-invariant subalgebra | Complex = maximally irreducible set (max Φ) | Homologous: both select a distinguished substructure by an extremum criterion |
| Q1 left primitive | "Experience is proof that something exists" | IIT goes further: existence IS experience (an answer to Q1 OchemaMath declines) |
| The bearer (M_i, ω_i) | Cause-effect structure of the substrate | Compatible: cause-effect power = the algebra's structure; the state = current substate |

**Contrast (formal):**

1. **The selection criterion differs.** IIT: Φ-maximization (maximum integrated information, "maximally irreducible complex"). OchemaMath: Takesaki's modular-invariance (the subject pole must be invariant under the state's own flow). These are different invariants — the Tegmark review (Item 5) proved Φ (cut-mutual-information) ≠ modular non-triviality. **IIT selects by information; OchemaMath selects by time-stability.** Neither implies the other. This is the sharpest formal disagreement in the landscape.
2. **The 0.25-bit problem.** Tegmark's theorem: static quantum Φ ≤ 0.25 bits. IIT 4.0's Φ-structure must therefore be dynamical (the composition postulate unfolds distinctions and relations — a structure, not a scalar). OchemaMath agrees: the bearer is a *process* (modular flow), not a static state. Both escape the bound by being structural/dynamical.
3. **The identity claim's status.** IIT asserts the explanatory identity as its core postulate (phenomenology → physics, axioms → postulates). OchemaMath treats the identity as a graded hypothesis (E), preferring abductive convergence to axiomatic assertion. **Same claim, different epistemic discipline.**
4. **Q1.** IIT answers it (existence IS experience — an intrinsic-powers ontology: "cause-effect power all the way down"). OchemaMath leaves Q1 primitive. OchemaMath's grade for the IIT answer: C (coherent, unverifiable).

**Verdict: IIT 4.0 is the strongest validation OchemaMath has — the identity claim, the exclusion axiom, and the state-dependence are all mainstream now. The one formal divergence: selection by Φ-maximization vs. selection by modular invariance — a testable difference.**

**Grade: the alignment is B/C (IIT is a well-developed theory with empirical validation for the first four postulates); the identity itself remains E in OchemaMath's grading (asserted by IIT, hypothesized by OchemaMath).**

### 11.2 Perceptronium (Tegmark 2014)

**Source:** 1405.0493 + 1401.1219. Full treatment in references/tegmark-peer-review.md.

**Support:**
- The identity claim (consciousness = a state of matter) aligns with D_i ≡_int A_i (B).
- The integration principle ≈ the joint state requirement (the bearer is unified, not a product of independent parts) (B/C).
- The dynamics principle (integrated *processing*, not static information) = OchemaMath's flow-based bearer — both escape the 0.25-bit bound (A).
- Error-correcting codes ≈ exclusion as conditional expectation (homologous projections onto distinguished substructures) (B/C).
- The HDT (separability maximized in the energy eigenbasis) supports OchemaMath's underdetermination claim: the factorization is chosen, not given (A).

**Contrast:**
- Substrate independence vs. Material Enactment (formal contradiction — resolved by thermal time: substrate matters if τ is constitutive) (C).
- The intrinsic aspect: Tegmark denies it any special status (the pattern is all there is); OchemaMath treats it as the fundamental datum (E — philosophical).
- The 0.25-bit theorem constrains static Φ but not flows — OchemaMath's objects are flows, so no contradiction (A).

**Verdict: perceptronium is OchemaMath's physicalist cousin — same identity, opposite valence on the intrinsic aspect.**

### 11.3 The Mathematical Universe Hypothesis (Tegmark MUH)

**Support:** "Geometry IS physics" — the amplituhedron claim, the 576 thesis's core assumption. If reality IS a mathematical structure, the spin network IS the geometry (B as ontology).

**Contrast:**
- Under MUH, all structures exist: the selector problem dissolves (every candidate is instantiated somewhere). OchemaMath's this-worldly bearer recovery survives; transworld uniqueness claims fail (A — scope preserved).
- MUH's "only computable and decidable structures exist" contradicts Penrose's non-computable selection in Orch-OR — OchemaMath takes no side (E).
- The 576 numerology: MUH converts discovery to selection problem — matching the verification addendum's verdict (C).

### 11.4 CIMC / Computational Functionalism (Bach et al. 2026)

**Source:** cimcWhitepaper.pdf. Full treatment in frontier-math.md §CIMC.

**Support:**
- Second-order perception ≈ OchemaMath's recursive perspective (REPM Axiom 6) (C).
- Coherence maximization ≈ valence-as-coherence (C).
- Minimal phenomenal experience ("bare registration of its own occurrence") = ρ_i = prakāśa (C).

**Contrast — the formal defeat:**
- A finite automaton's algebra is finite-dimensional → trivial modular structure → no thermal time. If τ is constitutive, CIMC's sufficient condition fails *by theorem* (A math / C premise).
- Substrate irrelevance vs. Material Enactment — the direct contradiction (E — resolved against substrate-independence if thermal time holds).
- The hard problem: CIMC claims "phenomenology is the model" (dissolved by construction); OchemaMath keeps Q1 primitive (the honest version).

**Verdict: CIMC is the opponent the thermal-time theorem defeats — the sharpest formal result in the landscape.**

### 11.5 Orch-OR (Hameroff–Penrose)

**Source:** hameroff-2014 chapter, references/orch-or/. Full treatment in the-moment.md.

**Support:**
- E_G = ħ/t collapse = the withdrawal phase of the moment-triad = state transition in the operator algebra (C).
- "Consciousness is collapse/reduction" = the moment as state transition (C).
- The anesthetic dissociation test = the perturbational-correspondence criterion, concretized (B/C).
- The explicit Whitehead link (occasions of experience) = the moment-triad (C).
- Penrose's superposition-as-spacetime-separation = LQG's spin network superpositions — the geometry is the actor (B).

**Contrast:**
- The quantum layer is refuted-as-stated by decoherence (Tegmark, D) — but OchemaMath's classical-information layer (modular flow, IIT, Zeno) survives.
- The non-computable Platonic values = metaphysical positing where the math stops (E — OchemaMath needs no such postulate; generate→select suffices).
- Non-computability vs. MUH's computability-only — OchemaMath takes no side.

**Verdict: Orch-OR supplies the moment's physics language; its quantum mechanism fails, its structure survives.**

### 11.6 Spanda / Pratyabhijñā (Kashmir Śaivism)

**Source:** whattheheckis-spanda.md, the-moment.md, pratyabhijna-formal.md.

**Support:**
- "The non-sequential action is the source of time and space" = thermal time stated in the 9th century (A math / C application) — the deepest convergence in the corpus.
- The moment-triad (sṛṣṭi–sthiti–saṃhāra) = emergence–persistence–withdrawal in the operator algebra (C).
- Stanza 3's invariant perceiver = the modular fixed-point subalgebra (C).
- The kañcukas as constraint families = the discrete allowed structures (spin labels, spectral projections) (C/D).
- Camatkāra (consciousness = aesthetic relish) = the spectral-quality conjecture (quality = spectrum of the modular Hamiltonian) (D).

**Contrast:**
- Spanda is a phenomenological doctrine — the pulse is experienced, not measured (the structural convergence is real; the evidential status differs).
- The Śaiva C∞ (universal consciousness) = a metaphysical extension OchemaMath does not need (E, optional).

### 11.7 Ñāṇavīra (Buddhist phenomenology)

**Support:**
- Duration = unchange + change = the modular flow's group structure (invariant O + transformations) (C).
- The squaring of weights → dominance → interchange (§13) = Born-rule/amplitude² structure and the OR threshold (C/D — prefigured the collapse).
- "The total intensity must be unity" = state normalization (C).
- "Past and future exist in the present" = the block structure of the state's time (C).
- The three-level hierarchy (eternal/regular/accelerating) = the modular structure at successive levels (C).

**Contrast:** Ñāṇavīra derives the structure from bare phenomenology (no physics); OchemaMath supplies the physics. The convergence is the most striking in the corpus — two independent derivations of the same moment-structure.

### 11.8 Proclus (Neoplatonism)

**Support:** monē–proodos–epistrophē = the moment-triad = the modular flow's three phases (C). The henads = the distinguished subalgebras (C/D). "Time is the soul's experience of procession" = thermal time (C).

**Contrast:** theological framing (the One, the gods) — optional metaphysical extension (E).

### 11.9 Doyle / Information Philosophy

**Source:** references/ip-peer-review.md (full treatment).

**Support:**
- Two-stage model (chance generates, determinism selects) = generate→select = the classical-information layer of the orchestration (B).
- Adequate determinism = deterministic modular flow within a state, random transitions between states (B — the classical shadow of the thermal-time structure).
- Downward causation ("information controls matter") = thermal time (state generates flow) — the direction right, the mechanism wrong (A math / C app).
- ERR = the classical-information replay layer (B).
- EPR common-cause-by-constraint = the constraint-not-signal structure = the orchestration law at the quantum level (B).

**Contrast:**
- "Information as immaterial substance" — rejected by the Material Enactment Principle (E).
- "ERR solves the hard problem" — replay is correlation, not presence (E).
- "Information is not conserved" — true only relative to a coarse-graining (C).
- The Ergo (value = stable information structures) — no phenomenal content without the valence mapping (E/D).

### 11.10 Levin / Basal Cognition (bioelectric)

**Support:**
- Generate→select universal in biology = the two-stage structure at every scale (B).
- The morphogenetic target = the attractor = the future state constraining the present (B).
- The cognitive light cone = the boundary of the bearer (B).
- Material specificity = the Material Enactment Principle (B).
- Downward causation (organism goals constrain cells) = the state constraining the parts (B).

**Contrast:** Levin supplies agency, not phenomenality — "morphogenesis closes the gap between mechanism and agency, but not between agency and phenomenality" (the frontier, per levin-peer-review.md). OchemaMath's χ (the missing condition) is exactly this gap.

### 11.11 The Channeled/Regression Corpus (Ra, Seth, Cannon, Paul Selig)

**Support (all graded C/E — hypothesis generators, not evidence):**
- The orchestration law ("state at threshold determines outcome") = corollary of thermal time + quantum Bayes (C).
- Densities as information levels = the multiverse/phase-transition reading (C).
- The death transition = the moment-triad at the largest scale (C).
- The higher self as future attractor = the morphogenetic target (B as mechanism, E as entity).
- "You can only go to the level your vibrations are compatible with" = the compatibility condition of the collapse (C).

**Contrast:** no evidential status; the structures converge, the sources don't validate (the standing verdict).

### 11.12 The Master Contrast Table

| Theory | Supports OchemaMath | Contradicts OchemaMath | Net |
|---|---|---|---|
| **IIT 4.0** | Identity claim; exclusion axiom; state-dependence | Selection by Φ vs modular invariance; answers Q1 | **VALIDATION** |
| **Perceptronium** | Identity; dynamics principle; HDT underdetermination | Substrate independence; denies intrinsic aspect | Support (with fault line) |
| **MUH** | Geometry IS physics | Dissolves selector; computability-only | Neutral/scope |
| **CIMC** | Second-order perception; coherence | Substrate irrelevance — **defeated by thermal time** | Challenge (resolved) |
| **Orch-OR** | Moment as collapse; dissociation test | Quantum layer refuted by decoherence | Structure survives |
| **Spanda** | Time-from-state; moment-triad; invariant | Phenomenological, not measured | **Deepest convergence** |
| **Ñāṇavīra** | Moment-structure; collapse prefigured | Phenomenological | Striking convergence |
| **Proclus** | Triad; time-from-procession | Theological | Convergence |
| **Doyle/IP** | Two-stage; adequate determinism; common cause | Info as substance; hard-problem claim | Partial |
| **Levin** | Generate→select; targets; material specificity | Agency ≠ phenomenality (gap stays) | Empirical ground |
| **Channeled corpus** | Orchestration law; densities; transition | No evidential status | Hypothesis generators |

---

## 12. The Updated One-Sentence Statement (v0.2)

> **OchemaMath formalizes the bearer as a von Neumann algebra with a faithful state; time as its modular flow (Tomita–Takesaki/Connes–Rovelli); the subject pole as a modular-invariant subalgebra (Takesaki); the selector problem as sheaf cohomology; the joint fixed point as a categorical limit; and Material Enactment as the non-isomorphism of materially distinct representations. The theory landscape now validates the core: IIT 4.0 states Ochema's identity claim and exclusion axiom as mainstream theory; the thermal-time theorem defeats computationalism; the orchestration law is a corollary of both thermal time and Tegmark's quantum Bayes theorem; and the Spanda doctrine's "non-sequential action is the source of time" has a theorem-shaped formalization. The one formal divergence from IIT — selection by Φ-maximization vs. selection by modular invariance — is testable. Every consciousness-identification remains graded C–E and falsifiable; no overclaiming.**

---

## Sources

- Connes & Rovelli (1994). Thermal time. arXiv:gr-qc/9406019
- Takesaki (1970, 2003). Conditional expectations, modular theory
- Connes (1994). *Noncommutative Geometry*
- Lawvere (1970s). Topos theory, internal logic
- Univalent Foundations Program (2013). HoTT. arXiv:1308.0729
- Perelman (2002–2003). Ricci flow entropy
- Sheaf cohomology: standard (Hartshorne; Iversen)
- Tononi & Boly (2025). IIT: A Consciousness-First Approach to What
  Exists. arXiv:2510.25998. [references/tegmark/]
- Tegmark corpus (16+8 papers). [references/tegmark/, references/tegmark-peer-review.md]
- CIMC Whitepaper (Bach et al. 2026). [EssayViz/cimcWhitepaper.pdf]
- Hameroff (2014) Orch-OR; McQueen (2023). [references/orch-or/]
- Information Philosopher corpus. [references/ip-peer-review.md]
- Project sources: frontier-math.md, ochema-formal.md, formalised-theories/,
  the-moment.md, the-orchestration.md, whattheheckis-spanda.md,
  references/576lqg/, references/tegmark-analysis.md

*OchemaMath v0.2 — compiled 2026-07-31. Formalization in progress; every claim graded; no overclaiming.*
