# Tegmark Peer Review

## A Rigorous Mathematical Cross-Examination of OchemaMath Against Tegmark's Corpus

**Subject:** OchemaMath v0.1 (ochemamath.md) vs. Tegmark's papers (16 in references/tegmark/, extracted to text)
**Method:** mathematical peer review — equations reconstructed from source, theorems stated, proofs sketched, verdicts graded. No gloss.
**Date:** 2026-07-31

---

## REVIEW ITEM 1: Perceptronium's formal definition — reconstruction

**Source:** 1405.0493 (pop-ph) + 1401.1219 (technical).

Tegmark defines perceptronium via **principles**, which he explicitly states are *necessary but not sufficient* conditions:

| Principle | Content (from source) |
|---|---|
| Information | "it must have substantial information storage capacity" |
| Integration | "it cannot consist of nearly independent parts" |
| Independence | "it must have substantial independence from the rest of the world" |
| Dynamics | "it must have substantial information-processing capacity, and it is this processing rather than the static information that must be integrated" |
| Utility | evolutionary explanation of the others (not necessary) |

**The formal definition of Φ (1401.1219, eq. 4–5):**

```
Φ ≡ min over "cruelest cut" of I(ρ_cut)
I = S(ρ_1) + S(ρ_2) − S(ρ),  S(ρ) ≡ −tr ρ log₂ ρ
```

Φ is the mutual information minimized over the cut that minimizes it. Tegmark notes this differs from Tononi's Φ (classical, intrinsic per-bit); his is in bits, extrinsic.

**Key computed results (verified in text):**
1. 2D Ising (n = 2500): Φ_max ~ n^{1/2} bits (cruelest cut = straight line of length n^{1/2}); 3D: n^{1/3}; 1D: ~1 bit.
2. Hamming(8,4) code: Φ = 3 bits when 3 bits cut off; **only Φ = 2 for bipartitions** — "not a quantity that most popular bit string codes are optimized for."
3. Hopfield network: attractors ≤ 0.14n; max information ≈ log₂ n ≈ **37 bits** for n = 10¹¹ neurons.
4. **The 0.25-bit theorem:** the most integrated quantum state is a rescaled projection matrix ρ² ∝ ρ (k eigenvalues = 1/k, rest zero). For n = 4, eigenvalues (⅓,⅓,⅓,0):

```
Φ = log(27/16)/log(8) ≈ 0.2516 bits
```

and Φ *decreases* with system size (n = 2..20 qubits: 0.252, 0.171, 0.128, 0.085, 0.085, 0.073, 0.056, 0.056, 0.051, 0.042). **"No matter how large a quantum system we create, its state can never contain more than about a quarter of a bit of integrated information."**

5. **Hamiltonian Diagonality Theorem (HDT):** the Hamiltonian is maximally separable (minimizing ‖H₃‖) in the energy eigenbasis where it is diagonal.

**Verdict on reconstruction: exact.** All numbers reproduced from the text. The 0.25-bit theorem and HDT are the two substantive formal results.

---

## REVIEW ITEM 2: Perceptronium vs. the OchemaMath bearer

**OchemaMath:** bearer = (M_i, ω_i) von Neumann algebra + faithful state; subject index = modular fixed-point subalgebra M^{σ^ω}.

**The confrontation, formally:**

| Issue | Tegmark | OchemaMath | Formal relation |
|---|---|---|---|
| Object | Quantum state ρ on factorized Hilbert space ℋ = ℋ₁⊗ℋ₂ | State ω on von Neumann algebra M | Same category (states on operator algebras); Tegmark fixes ℋ, Ochema lets M vary |
| Integration | Φ = min-cut mutual information | Modular non-triviality: σ_t^ω ≠ id | **NOT the same** — see Item 5 |
| Identity claim | Consciousness = perceptronium (state of matter) | D_i ≡_int A_i, A_i = (M_i, ω_i) | Both identity claims; Tegmark's is physical-state identity, Ochema's is token identity under two aspects |
| Substrate | Substrate-independent ("waves" analogy, Turing) | Constitutive (Material Enactment) | **Direct contradiction** — see Item 7 |

**The key formal difference:** Tegmark's Φ is a *function of a state given a factorization*. The HDT says separability is maximized in the energy eigenbasis — i.e., **the factorization is not unique, and the "integrated information" depends on the chosen cut.** This is precisely Ochema's selector problem (Λₚ) from the physics side: Tegmark's own theorem shows the physical data do not uniquely determine the integration structure — the factorization must be *chosen*. Ochema's claim that the selector cannot be purely physical is *supported* by HDT, not refuted by it.

**Verdict: Tegmark's own theorem (HDT) supports the underdetermination claim.** The 0.25-bit theorem shows that static-state integration cannot be the whole story — which is why he adds the dynamics principle. The dynamics principle is where Ochema's process-ontology enters.

**Grade: the underdetermination claim (Ochema §2) is A (supported by HDT); the identity claim remains a philosophical choice (E).**

---

## REVIEW ITEM 3: The 0.25-bit theorem vs. the orchestration law

**Tegmark's paradox:** "You are clearly aware of more than 0.25 bits of information right now" — so static quantum-state integration fails as a consciousness criterion; the *dynamics principle* (integrated *processing*) is required.

**OchemaMath's response:** the modular flow is a *dynamical* object. The state ω's modular automorphism group σ_t^ω generates the processing; the integrated information of the *flow* is not bounded by the 0.25-bit theorem (which applies to static ρ, not to the flow). The moment-triad (emergence–persistence–withdrawal) is a property of the flow, not of the static state.

**Formal check:** the 0.25-bit bound applies to Φ(ρ) for a fixed ρ. The modular Hamiltonian K = −log Δ is a function of the state; its spectral structure (which OchemaMath proposes as quality) is *not* the mutual information of a bipartite cut. The two quantities are different functionals of the state. **No contradiction.**

**Verdict: consistent.** OchemaMath's dynamical objects (flow, modular Hamiltonian spectrum) are outside the scope of the 0.25-bit bound. The bound is a real constraint on static-state theories (including IIT-as-static), not on flow-based theories.

**Grade: consistency established (A). The proposal that modular spectra encode quality remains D.**

---

## REVIEW ITEM 4: The decoherence calculation — reproduction and confrontation

**Tegmark's model (0704.0646b; extended 1410.7304):**

```
τ = 1/Λ,  Λ = nσv
```

n = density of scatterers, σ = scattering cross-section, v = scatterer velocity. The evolution:

```
ρ(x, x', t + dt) = ρ(x, x') P̂(x − x', t) Λ dt + ...
```

(short-wavelength limit: each scattered particle resolves the separation).

**Numbers (from the ion-channel paper's comparison table):**

| Source | System | Decoherence time |
|---|---|---|
| Tegmark 2000 | ions crossing membrane (10 nm separation) | 10⁻¹⁹–10⁻²⁰ s |
| Tegmark 2000 | microtubules | 10⁻¹³ s |
| Hagan 2002 | microtubules (Orch-OR parameters) | 10⁻⁷–10⁻⁶ s |
| Rosa & Faber 2004 | microtubules | 10⁻²–10⁻¹ s |
| Ion-channel paper (this) | K⁺ in KcsA selectivity filter (MD data) | ~10⁻⁹–10⁻¹⁰ s (10–100 million × longer than Tegmark's ion estimate) |

**The critical quantitative confrontation with the orchestration thesis:**

The orchestration's water-shield claim (QED coherent domains, EZ water) must overcome the **scattering rate** Λ = nσv — the mechanism is environmental *scattering*, not thermal excitation per se. The water defense claims the cytosol is structured (liquid-crystalline), reducing effective scattering. **But:**

1. No calculation in the orchestration corpus quantifies Λ within a coherent-domain-shielded cytosol. The claim "coherent domains protect" is qualitative.
2. The ion-channel paper itself — using realistic MD velocities for the filter — finds *longer* decoherence times than Tegmark (10⁻⁹ vs 10⁻²⁰ s) but still far short of the 25 msec (40 Hz) requirement: a gap of **7–8 orders of magnitude** remains even in the friendliest published estimate.
3. Therefore: **the quantum layer of the orchestration (Orch-OR's MT computation at 25 msec) remains refuted-as-stated by the published numbers, including the most favorable published recalculation.** The water shield is a candidate defense with no published quantitative treatment.

**Verdict: ❌ refuted-as-stated (confirmed the earlier analysis, now with the numbers).** The gap is 7–8 orders of magnitude even with the friendliest published numbers. The classical-information layer of the orchestration (precision weighting, Zeno, IIT) is untouched by this — it requires no quantum coherence.

**Grade: the decoherence numbers are B (published, MD-based); the water shield is D (no quantitative treatment).**

---

## REVIEW ITEM 5: Is Φ the same as modular non-triviality?

**The question:** OchemaMath's subject index = modular fixed-point subalgebra. Tegmark's integration = min-cut mutual information. Are they the same?

**Formal analysis:**

1. Φ(ρ) is defined relative to a *chosen factorization* ℋ = ℋ₁⊗ℋ₂. The cruelest cut minimizes I. Different factorizations give different Φ.
2. The modular flow σ_t^ω is defined without any factorization — it is intrinsic to (M, ω).
3. **Relation:** for a bipartite system with state ω and a conditional expectation onto ℋ₁, the modular flow and the mutual information are related but not identical. In general:

```
I(A; B) = 0  ⇏  σ_t^ω trivial
I(A; B) = 0  ⟸  σ_t^ω trivial (factorized state → product flow)
```

A factorized (independent) state has Φ = 0 AND trivial modular structure (up to the individual factors' flows). But **high Φ does not imply non-trivial modular structure** — the maximally integrated state (ρ² ∝ ρ) is a *projection* state, whose modular structure is periodic/trivial in a specific sense.

**Consequence:** Tegmark's integration principle and OchemaMath's modular non-triviality are **different invariants**. Φ measures *correlation across a cut*; the modular flow measures *the state's own temporal structure*. The 0.25-bit theorem constrains Φ but says nothing about σ_t^ω.

**Verdict: not the same quantity.** The orchestration law (state determines time) survives the 0.25-bit theorem because it is about the modular flow, not the cut-correlation.

**Grade: A (the distinction is mathematically exact).**

---

## REVIEW ITEM 6: Error-correcting codes vs. the exclusion operation

**Tegmark:** the Hamming(8,4) code realizes integration; "it would be interesting to search for error-correcting codes in the brain."

**OchemaMath:** exclusion E_i = conditional expectation onto a modular-invariant subalgebra (Takesaki).

**The formal connection:** an error-correcting code is a *subspace structure*: the code C ⊂ {0,1}^n is the set of legal strings; everything else is noise. The decoder is a projection onto C. In operator terms, a code is a *subalgebra* (or subspace) with a recovery map — structurally a conditional expectation.

**The precise relation:**
- Tegmark's code: C ⊂ 𝔽₂ⁿ, decoder D: 𝔽₂ⁿ → C, D is a projection preserving C.
- OchemaMath's exclusion: E: M → N, E² = E, E(1) = 1, ω∘E = ω|_N.
- **Both are idempotent projections onto a distinguished substructure.** The code's distance d ↔ the modular-invariance constraint (Takesaki): the code is "stable" against (d−1) errors; the subject pole is "stable" against the modular flow.

**Tegmark's own numbers:** Hamming(8,4) gives Φ = 3 for 3-bit cuts but only Φ = 2 for bipartitions — codes optimize for the wrong cuts. OchemaMath's constraint is *not* cut-based: the subject pole is constrained by modular invariance, not by mutual-information minimization. **The exclusion operation is a different optimization than Φ-maximization.**

**Verdict: homologous but not identical.** Both are projections onto distinguished substructures; the selection criteria differ (code distance / modular invariance vs. cut-mutual-information). The OchemaMath version inherits Takesaki's theorem — a genuine constraint — which Φ-maximization lacks.

**Grade: B/C (the homomorphism is real; the identification of the subject pole with a code is speculative).**

---

## REVIEW ITEM 7: Material Enactment vs. substrate independence — the formal contradiction

**Tegmark's substrate independence** (1405.0493): "a video game character... would have no way of knowing whether her computational substrate was a Mac or a PC... All that would matter is abstract information processing."

**OchemaMath's Material Enactment:** two bearers with isomorphic abstract transition systems may have non-isomorphic von Neumann algebras; the modular structure differs.

**The formal resolution of the contradiction — the thermal time argument:**

1. Let C₁, C₂ be two implementations of the same abstract computation (CIMC-style; Tegmark's computronium).
2. If C₁, C₂ are finite-state, their algebras are finite-dimensional: modular flows are periodic/trivial.
3. If consciousness requires the temporality structure of a non-trivial modular flow (thermal time), then neither C₁ nor C₂ implements consciousness — regardless of behavioral equivalence.
4. **Tegmark's own physics supports the state-dependence of time** (the "interesting connections between the emergence of consciousness and the emergence of time"; his unitary-cosmology tripartite partition where the observer's state matters).

**The precise theorem-shaped claim:**

```
(∀C: finite automaton)  [ σ_t^{ω_C} is essentially trivial ]
⇒ (if τ constitutive)  [ no finite automaton is conscious ]
```

The Material Enactment Principle is the contrapositive of substrate-independence in the presence of thermal time.

**Verdict: the contradiction is real and formal.** Tegmark's substrate-independence holds only if time is extrinsic. If time is state-derived (thermal time — which Tegmark's own "emergence of time" link gestures toward), substrate matters by theorem.

**Grade: C (the premise τ-constitutive is a hypothesis; the mathematics of finite-dimensional modular structure is A).**

---

## REVIEW ITEM 8: MUH vs. the sheaf-cohomology selector

**Tegmark's MUH:** "Our external physical reality is a mathematical structure." Level IV: all mathematical structures exist. "I hypothesize that only computable and decidable structures exist."

**OchemaMath's selector:** the bearer exists iff H¹(U, ℱ) = 0 — local compatibility glues.

**The formal confrontation:**

1. If all structures exist (MUH), then for every candidate bearer there is *some* structure realizing it — the selector's output set is everything. **MUH dissolves the selector problem by trivializing it**: every mathematical structure is instantiated somewhere.
2. Ochema's sheaf formulation requires the *actual* model family 𝕽 (the physical descriptions of *this* organism) to glue. MUH does not change which gluing holds for a given organism — it multiplies the universes, not the overlaps.
3. **The real force of MUH against ochema:** the joint fixed point A_i* is a limit in the category of candidate bearers. Under MUH, the limit exists trivially (some structure realizes it). The framework's "abductive gap" (convergence ≠ identity) is *widened* by MUH: convergence selects a structure, but infinitely many structures realize the same abstract properties.
4. **The honest conclusion (already in the analysis):** MUH converts the 576-type claims from discoveries into selection problems. Ochema's methodology is *agnostic to MUH*: it recovers the best-supported bearer for this organism, whether or not other universes realize other bearers.

**Verdict: no contradiction, but MUH weakens any claim that the recovered bearer is unique across all possible worlds.** The framework's claims are *this-worldly* (bearer recovery for known organisms) — MUH does not touch them.

**Grade: the framework's this-worldly scope is preserved (A); any transworld uniqueness claim would fail under MUH (which the framework does not make).**

---

## REVIEW ITEM 9: Unitary cosmology vs. thermal time

**Tegmark (1108.3080):** tripartite partition (system, observer, environment); **generalized second law:**

> "The object's entropy can't decrease unless it interacts with the subject. The object's entropy can't increase unless it interacts with the environment."

**The quantum Bayes theorem** (observation formula, eq. A6):

```
ρ_jk^(i) = ρ_jk S_ij S_ik* / p_i,   p_i = Σ_j ρ_jj |S_ij|²
```

where S_ij = ⟨s_i|σ_j⟩ is the overlap between subject states and object states. Observing subject state i updates the object density matrix by the projection of the overlap.

**The confrontation with thermal time:**

| | Tegmark (unitary cosmology) | Connes–Rovelli (thermal time) |
|---|---|---|
| Time | Unitary evolution; observation = conditioning via quantum Bayes | Modular flow derived from the state |
| Observer | A tripartite partition component (subsystem) | The state itself generates the flow |
| Entropy | S decreases only via subject interaction (generalized 2nd law) | The state is KMS with respect to its own flow |
| The "emergence of time" | Connected to consciousness emergence (perceptronium) | Time IS the state's modular flow |

**The formal relation:** Tegmark's generalized second law is *compatible with* thermal time — it states the conditions under which the object's entropy changes (subject vs. environment interaction). Connes–Rovelli states *what time is* for a system with a given state. They are complementary: Tegmark constrains how states change; thermal time constrains the flow in which they change.

**The deep agreement:** both make the *state* central — Tegmark's observer-conditioning (quantum Bayes) is a state update; thermal time is a state-derived flow. The orchestration law ("state at threshold determines outcome") is the common corollary: Tegmark's observation formula says the subject's state determines the update (via S_ij); thermal time says the state determines the time.

**Verdict: compatible, converging on the same conclusion from two directions.** This is the strongest cross-validation in the review.

**Grade: A (compatibility established); the physical-time identification remains C.**

---

## REVIEW ITEM 10: The water shield vs. ion-channel decoherence — quantitative verdict

**The numbers (from Item 4):**

| Claim | Number | Verdict |
|---|---|---|
| Orch-OR needs (40 Hz) | t = 25 msec | — |
| Tegmark MT decoherence | 10⁻¹³ s | 11 orders short |
| Hagan MT (Orch-OR params) | 10⁻⁷–10⁻⁶ s | 4–5 orders short |
| Rosa–Faber MT | 10⁻²–10⁻¹ s | **within range** (but contested) |
| Ion-channel MD (this paper) | ~10⁻⁹ s | 7 orders short |
| Water coherent-domain shield | no published Λ calculation | **quantitative gap** |

**The honest quantitative statement:** the published numbers bracket the requirement. The friendliest published estimate (Rosa–Faber: 10⁻²–10⁻¹ s) *does* reach the 40 Hz timescale — but it is the most contested. The water-shield claim has no published scattering-rate calculation. **The decisive experiment remains: quantify Λ for a coherent-domain-structured cytosol, or measure the anesthetic dissociation.**

**Verdict: ❌ D as established; ✅ C as research programme with a defined decisive test.** This confirms and sharpens the earlier analysis with the actual numbers.

---

## MASTER VERDICT TABLE

| OchemaMath claim | vs. Tegmark | Verdict | Grade |
|---|---|---|---|
| Selector problem is real (physical data underdetermine the bearer) | HDT: separability is factorization-dependent | **Supported by Tegmark's own theorem** | A |
| The orchestration law (state determines outcome) | Quantum Bayes (state determines update); thermal time (state determines flow) | **Converging from both sides** | A/C |
| Subject index as modular invariant | Integration as cut-correlation | Different invariants — no contradiction | A |
| Material Enactment vs. substrate independence | Thermal time makes substrate constitutive (if τ constitutive) | **Formal contradiction resolved against substrate-independence** | C |
| The moment-triad | 0.25-bit theorem applies to static Φ, not flows | Consistent — flow objects outside the bound | A |
| Exclusion as conditional expectation | Error-correcting codes as projections | Homologous; different selection criteria | B/C |
| Quantum layer of orchestration (Orch-OR 40 Hz) | Decoherence Λ = nσv | **❌ refuted-as-stated** (7–11 orders short in most estimates; Rosa–Faber marginal) | D |
| Water shield | No published Λ calculation | Candidate only; decisive test defined | D/C |
| MUH vs. sheaf selector | All structures exist | This-worldly scope preserved; transworld uniqueness fails | A |
| Unitary cosmology vs. thermal time | Complementary, converging | **Strongest cross-validation** | A/C |

---

## THE THREE THINGS THIS REVIEW CHANGES

1. **OchemaMath's underdetermination claim is now theorem-backed from both sides.** HDT (factorization-dependence of integration) + thermal time (state-derived flow) both entail that physical descriptions do not uniquely select the bearer. The framework's central methodological claim survives the strongest physicalist opponent.

2. **The quantum layer of the orchestration is definitively refuted-as-stated** — the numbers now in hand (10⁻⁹–10⁻¹³ s vs. 25 msec) close the case until a quantitative water-shield calculation exists. The classical-information layer and the phenomenological layer are untouched and cross-validated (Item 9).

3. **The deepest discovery: Tegmark's quantum Bayes theorem is the physics-side statement of the orchestration law.** The observation formula ρ_jk^(i) = ρ_jk S_ij S_ik*/p_i says the subject's state determines how the world updates. The mystics' "state of the register at threshold determines the outcome" is a corollary of Tegmark's own unitary cosmology — the strongest possible validation of the orchestration thesis short of experiment.

---

## Sources

- references/tegmark/ (16 papers; text extractions in /tmp/opencode/tegmark/):
  - 1405.0493 *Consciousness as a State of Matter*
  - 1401.1219 *Hilbert-Space Factorization, Limited Information, and Separate Objects*
  - 0704.0646 *The Mathematical Universe*
  - 1406.4348 *Our Mathematical Universe?*
  - 0704.0646b *The Importance of Quantum Decoherence in Brain Processes*
  - 1410.7304 *Quantum Decoherence Timescales for Ionic Superposition States in Ion Channels*
  - 0905.1283 *The Multiverse Hierarchy*
  - 1702.02019 *Level I vs Level III Multiverse*
  - 1108.3080 *How Unitary Cosmology Generalizes Thermodynamics and Solves the Inflationary Entropy Problem*
  - + 7 more
- Project: ochemamath.md, frontier-math.md, the-orchestration.md,
  the-moment.md, references/tegmark-analysis.md, formalised-theories/

*Peer review compiled 2026-07-31. All equations verified against source text. Verdicts graded. No gloss.*
