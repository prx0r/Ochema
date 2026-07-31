# The Ochema Object

## The Canonical Living Research Object for the Ochema Thesis

**ro_id: `ro:occhema-thesis`** — schema v2 · current version **1.1.0**

---

## What This Is

This is the **canonical, versioned, living research object** for the
project's formal theory. It is the git-object of the thesis: the thing
that persists and grows while working notes change.

- **The core document** is `the-unified-formal-framework.md` (the
  thesis at eight levels of inspection, with applications).
- **The mathematical core** is `ochemamath.md` (the formalization).
- **Everything else in the repo** — the papers, the peer reviews, the
  tradition mappings, the corpus extractions — is *input* to this
  object.

---

## The Directory Structure

```
the-occhema-object/
├── meta/
│   └── ro.json                 ← the RO metadata (schema v2)
├── sections/                   ← one file per thesis section
│   ├── 00-introduction.md      ← why layers
│   ├── 01-foundation.md        ← minimal axioms
│   ├── 02-layers.md            ← the eight layers
│   ├── 03-invariants.md        ← cross-layer invariants
│   ├── 04-bridges.md           ← inter-layer bridges
│   ├── 05-master-theorem.md    ← the convergence theorem
│   ├── 06-established-open.md  ← established vs open
│   ├── 07-falsification.md     ← falsification conditions
│   └── 08-applications.md      ← architecture through the traditions
├── confrontations/             ← every theory run against the thesis
│   ├── tegmark-peer-review.md
│   ├── ip-peer-review.md
│   ├── cimc-confrontation.md
│   ├── iit4-validation.md
│   └── orch-or-confrontation.md
└── updates/                    ← the versioned update log
    └── LOG.md                  ← every change, dated, versioned
```

---

## The Update Protocol (how this stays alive)

This is a living object. Any new work — a new paper, a new
confrontation, a new section, a correction — is added following this
protocol:

### 1. New sections
- Add the file to `sections/` following the numbering.
- Register it in `meta/ro.json` under `sections`.
- Log the change in `updates/LOG.md`.

### 2. New confrontations
Any new theory or paper is **run through the thesis** before being
absorbed:

1. Read the source (extract to text, verify quotes).
2. Reconstruct its formal claims (equations, exact statements).
3. Run it against the thesis: what does it **support**? What does it
   **challenge**? Where does it **fail**?
4. Write the confrontation in `confrontations/` (following the peer
   review format: equations, verdicts, grades).
5. Update the Master Verdict Table in the core document.
6. Log in `updates/LOG.md` with the version bump.

### 3. Version bumps
- **Patch (1.1.0 → 1.1.1):** corrections, clarifications, small
  additions to existing sections.
- **Minor (1.1 → 1.2):** new confrontations, new applications, new
  papers absorbed.
- **Major (1.x → 2.0):** a new layer, a new theorem, a structural
  change to the thesis itself.

### 4. The grading discipline (never relax)
- Theorems are theorems (A).
- Confirmed results are B.
- Identifications with consciousness are C–E, always labeled.
- The numerology (576/570) stays rejected unless re-derived.
- Every confrontation ends with a verdict table and grades.

---

## The Source Map (what feeds the object)

| Input | Where it lives | What it contributes |
|---|---|---|
| The theory lineage | `formalised-theories/` | IPIT → MEPIT → Ochema → REPM → CSID |
| The formalization | `ochemamath.md` | Operator algebras, thermal time, sheaves, topos |
| The physics corpus | `references/576lqg/` | LQG, causal sets, constructor theory, verification |
| The consciousness physics | `references/tegmark/` | Perceptronium, IIT 4.0, quantum Bayes, decoherence |
| The quantum biology | `references/orch-or/` | OR threshold, anesthetic dissociation test |
| The water bridge | `the-orchestration.md` | Coherent domains, EZ water, the shield |
| The moment | `the-moment.md` | Orch-OR × Spanda × Ñāṇavīra × Proclus |
| The traditions | `beings/`, `references/cannon/`, `references/paulselig/` | Densities, beings, the transition, the orchestration law |
| The old peer reviews | `references/tegmark-peer-review.md`, `references/ip-peer-review.md` | The confrontation record |
| The series | `whattheheckis-*.md` | The explainers |

---

## The Master Verdict Table (current)

| Theory | vs The Thesis | Verdict | Grade |
|---|---|---|---|
| IIT 4.0 (Tononi–Boly 2025) | Identity claim + exclusion axiom | **VALIDATION** | B/C |
| Perceptronium (Tegmark 2014) | Identity; dynamics principle | Support (fault line: intrinsic aspect) | B/C |
| MUH (Tegmark) | Geometry IS physics | Neutral (scope) | B/C |
| CIMC (Bach 2026) | Substrate irrelevance | **Defeated by thermal time** | A/C |
| Orch-OR (Hameroff–Penrose) | Moment as collapse | Structure survives; quantum layer refuted | C/D |
| Spanda (Kashmir Śaivism) | Time-from-state; moment-triad | **Deepest convergence** | A/C |
| Ñāṇavīra | Moment-structure; collapse prefigured | Striking convergence | C |
| Proclus | Triad; time-from-procession | Convergence | C |
| Tibetan clear light / bardo | Triad (4th derivation); transition | Convergence | C |
| Doyle/IP | Two-stage; adequate determinism | Partial (info-as-substance fails) | B/E |
| Levin | Generate→select; targets | Empirical ground (χ-gap open) | B |
| Degrees of Consciousness (Lee 2023) | Graded bearer; consciousness meter | **ALIGNS** (adopt the degreed-property analysis) | B/C |
| Unity Thesis (Friesen 2013) | Unity invariant; split-brain defense | **ALIGNS** + refinement: ι_i ≠ self-consciousness | C |
| Channeled corpus | Orchestration law | Hypothesis generators | C/E |
| The numerology 576/570 | — | **Rejected** | — |

**Full coverage: the confrontation registry — `confrontations/REGISTRY.md`
(14 confronted, backlog of 325+ from Kuhn's taxonomy, priority targets
listed). Run any new theory through the confrontation-registry skill.**

---

## The Current Frontier (what the object is hunting)

1. **The χ-gap** (L5→L6): biology → phenomenality. The one open
   bridge. Levin closes mechanism→agency; agency→phenomenality is
   open.
2. **The IIT divergence test**: Φ-maximization vs modular-invariance
   selection — the one testable divergence in the landscape. Run the
   experiment, one dies.
3. **The anesthetic dissociation test**: the decisive experiment for
   Orch-OR's quantum layer.
4. **The spectral-quality conjecture**: quality = modular Hamiltonian
   spectrum — the Chordonomicon test is the operationalization.
5. **The cross-layer derivation**: derive any two layers from a common
   formalism — the master theorem becomes a theorem.

---

*The Ochema Object v1.1.0 — 2026-07-31. Living document. Add, confront,
version, never relax the grading.*
