# THE TEMPORAL COHERENCE FRAMEWORK (TCF)

## A working mathematical framework for the felt — designed from OchemaMath + Rasa + the evidence

**Prepared:** 2026-08-01 · **Design brief:** "a mathematical
framework that would actually work, then with evidence." This is
the synthesis: everything in the thesis's machinery reduces to
computable quantities from existing data types, with falsifiable
predictions and the evidence already on record.

**⚠️ CONFRONTED 2026-08-01: the master equation is NOT original —
it is Joffily & Coricelli (2013), "Emotional valence and the
free-energy principle" (PLoS Comput Biol, PMC3681730).** See
the-occhema-object/confrontations/tcf-hinge-preexists.md. The
formula is VALIDATED by precedent (peer-reviewed, 13 years old);
the thesis must cite, not claim. **The genuinely novel core: the
spectral-quality conjecture (quality = spec(h_ω)), the aneural
extension, the sound-alignment application, and the DEAM test.**

**⭐ THE LINEAGE (the confirmation, not the setback):** the formula
has FIVE independent derivations — the rasa tradition (10th c.),
reward prediction error (Schultz 1997–2022), Joffily & Coricelli
(2013), the IIT-TTC convergence (2022), and the Ochema machinery.
Five starting points, zero cross-talk, one formula — the Joint
Individuation Principle demonstrated. See
references/valence-lineage.md (full text of J&C saved at
references/valence-lineage/joffily-coricelli-2013.xml).

**Status: a DESIGN — the framework is proposed, its quantities are
computable, its predictions are falsifiable, and its first three
tests use data that already exists. The core is a rediscovery +
extension of a published theory; the extensions are original.**

---

## 0. THE DESIGN PRINCIPLE

Every framework fails when its core quantity is unmeasurable
(IIT's Φ is contested; panpsychism has none). The TCF's core
principle:

> **Everything felt reduces to relative entropy (surprise) and its
> time-derivative (valence), and everything structural reduces to
> the modular Hamiltonian's spectrum (quality). Both are
> computable from data that already exists.**

The key mathematical discovery (the design's hinge):

> **Predictive surprise S_pw = the relative entropy S(ω‖ω_pred)
> between the current state and the predicted state.**

The FEP machinery (surprise = −log p) and the modular machinery
(relative entropy = ω(log ω − log φ)) are THE SAME QUANTITY. The
thesis's two biggest pillars — thermal time and predictive
processing — turn out to measure the same thing. That identity is
the framework's load-bearing wall.

---

## 1. THE FIVE AXIOMS

**Axiom 1 (The bearer is a state).** The bearer is (M, ω) — a von
Neumann algebra with a faithful state. The state IS the register.

**Axiom 2 (Experience is the state's own flow).** Experience at a
moment = the behavior of ω under its own modular flow σ_t^ω. Time
is from the state (Connes–Rovelli); the moment-triad is the flow's
local structure.

**Axiom 3 (The felt = entropy + its derivative + the spectrum).**
A moment's felt content has three computable components:
1. **Intensity** = the relative entropy S(ω‖ω_pred) — how far the
   current state is from the prediction (surprise)
2. **Valence** = its time-derivative: V(t) = −d/dt(smooth(S(ω‖ω_pred)))
   — whether the state is converging to coherence (resolution =
   pleasure) or diverging (threat = pain)
3. **Quality** = the local modular Hamiltonian's spectrum h_ω =
   −log ω — the "geometry of the return" (the rasa)

**Axiom 4 (The future attractor constrains the prediction).**
ω_pred is not a passive extrapolation of the past — it is pulled by
the target state ω* (the morphogenetic target, the anticipated
pulse, the planarian's head). The orchestration law: τ(ω) = f(ω, ω*).

**Axiom 5 (The moment-triad is the flow's local structure).**
- **Emergence:** S(ω‖ω_pred) rising — the state departing from
  prediction (novelty, superposition building)
- **Persistence:** S flat near the attractor — the KMS-stable
  state, the Zeno-pin held
- **Withdrawal:** S minimized — the state collapses onto the
  prediction; the transition ω → ω′; the moment ends

---

## 2. THE MASTER EQUATION

```
V(t) = −d/dt [ smooth( S( ω(t) ‖ ω_pred(t) ) ) ]
ω_pred(t) = F( history, ω* )
```

**Read in words:** the felt valence at a moment is the rate at which
the state's distance from its prediction (pulled by its future
attractor) is decreasing. Resolution = the return to coherence,
felt as pleasure. Rasa = the *geometry* of that return. Camatkāra =
the return that also relaxes the boundary.

**Why this works as a framework (and the others don't):**

| Framework | Core quantity | Computable? | The failure mode |
|---|---|---|---|
| IIT | Φ (cause-effect integration) | Contested (phi-monads) | Measures current correlation, not history |
| Panpsychism | Ubiquity axiom | Never | No experiments |
| FEP | Free energy | Yes | No felt content — no valence, no quality |
| **TCF** | **S(ω‖ω_pred) + −dS/dt + spec(h_ω)** | **Yes — from any predictive model + state data** | **Everything is measurable** |

---

## 3. THE GEOMETRY — WHERE RASA AND THE LATTICE ENTER LEGITIMATELY

The 576 numerology is dead (rejected on record). But the GEOMETRY
survived — and enters the framework at exactly one legitimate place:

**3.1 The harmonic ladder = the modular spectrum's structure.**

The LQG large-volume spectrum is harmonic (Schliemann:
q_n = q̄(1−ω(n+½))). The rasa theory's claim: the blisses = the
ladder's upper notes. The TCF's version:

> **When a state is coherent (near its attractor), the local
> modular Hamiltonian's spectrum shows harmonic structure — peaks
> at octave spacings. The "density octave" of the traditions = the
> modular spectrum's level structure. This is the SAME harmonic
> spectrum appearing at L2 (LQG volume), L1 (modular Hamiltonian),
> L6 (felt quality), and L8 (the blisses) — the cross-layer
> invariant, now measurable.**

**Testable:** near-resolution moments (in music, in meditation, in
the plant's recovery) should show harmonic peaks in the local
surprise time-series spectrum. The spectral-quality test, given
its first operational form.

**3.2 The FCC lattice = the attractor-space geometry.**

The tetrahedron/FCC geometry survives as the METRIC STRUCTURE of
attractor space: the resolution paths (the rasa's "returns") are
paths through a lattice of attractor states. The specific rasa =
the path's geometry:
- **śānta** = the direct return to the symmetric center (shortest
  path, slow)
- **raudra** = the violent bypass (high-energy path, fast)
- **adbhuta** = the novel path (never-before-traversed — the "rasa
  zone")

**Testable:** cluster the resolution paths in surprise-state-space
(from any time-series with annotated felt states); the clusters
should correspond to the rasa taxonomy — a computational
classification of the nine rasas, from data.

**3.3 The tetrahedron = the minimal moment.**

The K₄ (4 vertices, 6 edges) — the minimal structure with a center
— is the geometry of the minimal moment: the state, its prediction,
its attractor, and the boundary. Not numerology: the minimal number
of objects required for the master equation to be defined is four
(state, prediction, attractor, boundary). The tetrahedron is the
moment's minimal diagram.

---

## 4. THE EVIDENCE — WHAT ALREADY SUPPORTS IT

### 4.1 The anticipation evidence (Axiom 4 — the attractor pull)

**Saigusa 2008 (PRL):** slime mold slows at the time the next pulse
*would have occurred* — the state's prediction is pulled by the
anticipated event, not the past. **Amoeba 2026 (Sci Rep):**
replicated in a second organism.

**The TCF reading:** ω_pred(t) fits the data better WITH ω* (the
anticipated pulse) than without. **The anticipation experiments ARE
the attractor-pull test, already run.**

### 4.2 The habituation evidence (Axiom 3 — surprise weighting)

**Farkas 2025 (tomato):** habituation = the plant downweights the
predictable stimulus. **Boisseau 2016 (slime mold):** stimulus-
specific habituation with spontaneous recovery.

**The TCF reading:** habituation = the precision-weighting of ω_pred
— the predictable is downweighted because its surprise contribution
is zero. **The prediction-error scaling test (irregular vs regular
stimuli) is the direct test — designed, unfunded, cheap.**

### 4.3 The conditioning evidence (Axiom 3 + 4 — the learned attractor)

**Farkas 2025 (tomato conditioning):** ultrasound becomes a
predictor of drought — the plant learned the association. **Latzel
2018 (strawberry):** anticipates nutrient positions by light cue,
epigenetic substrate.

**The TCF reading:** conditioning = the state learning its
attractor-predictor map: ω_pred gains structure from experience.
**The register (ω) IS the learned map.**

### 4.4 The aging evidence (Axiom 4 — attractor failure)

**Levin 2025 (Adv Sci):** aging emerges after developmental goals
complete — the attractor ω* loses its pull.

**The TCF reading:** aging = ω* decaying = the future no longer
constraining the present. **The framework predicts: aging should
correlate with the decline of anticipatory behavior — measurable.**

### 4.5 The temporal-integration evidence (Axiom 5 — the moment)

**Temporal integration across biological scales (2026):** minimum
temporal windows as a biologically invariant constraint.

**The TCF reading:** the "temporal window" IS the moment's
integration time — the smoothing scale in the master equation.
The specious present (human ~100ms–3s) and the plant's slow moment
(days) are the SAME structure at different smoothing scales.

### 4.6 The DEAM dataset (Axiom 3 — the valence test, data exists)

**DEAM: 6.9k tracks with second-by-second valence annotations.**
The cheapest test in the framework:
- Compute S(t) from an audio predictive model (PMEF-H or any
  standard audio surprise model)
- Compute V(t) = −d/dt(smooth(S(t)))
- Correlate with the annotated valence
- **Prediction: V(t) correlates with annotated valence BETTER than
  S(t) does** — the derivative, not the level, is the felt
  quantity. This is the rasa formula's first large-scale test,
  and the data exists NOW.

---

## 5. THE PREDICTIONS (falsifiable, prioritized)

| # | Prediction | Test | Data status | If wrong |
|---|---|---|---|---|
| P1 | Valence ∝ −dS/dt, not S | DEAM correlation | **Exists now** | The rasa formula dies |
| P2 | Response ∝ prediction error | Irregular vs regular stimuli on plants/slime molds | Cheap to run | The orchestration law dies |
| P3 | Anticipation fits better WITH ω* | Re-analyze Saigusa/Amoeba with/without attractor term | **Data exists** | The future-attractor claim dies |
| P4 | Coherent states show harmonic spectral peaks | Near-resolution time-series spectra (music, meditation) | New data | The octave identity dies |
| P5 | Resolution paths cluster by rasa | Surprise-state-space clustering | New data | Rasa-as-geometry dies |
| P6 | Aging correlates with anticipation decline | Longitudinal anticipatory measures | New data | The attractor-failure account dies |

**The framework's advantage: P1 and P3 use data that ALREADY
EXISTS.** The first two tests are free.

---

## 6. THE ONE-SENTENCE STATEMENT

**The felt quality of a moment is the rate at which the state
converges to its prediction (pulled by its future attractor),
shaped by the spectrum of its own time — V(t) = −d/dt(S(ω‖ω_pred)),
with ω_pred = F(history, ω*) — and every term is computable from
data we already have.**

---

## 7. THE HONEST BOUNDARY

- **The hinge identity (S_pw = relative entropy) is the framework's
  load-bearing wall and its main risk.** If the two quantities
  diverge in practice (if predictive surprise and modular relative
  entropy are NOT the same), the framework splits. **The DEAM test
  is also the hinge test.**
- **The felt claim remains.** The framework predicts V(t)
  correlates with *annotated* valence — but annotation is behavior,
  not phenomenality. The hard problem is still not closed; the TCF
  claims the *structure* of the felt is computable, not that
  computing it IS the feeling.
- **The harmonic-spectrum claim (P4) is the most speculative** —
  the octave identity is D until measured.
- **Grades:** the mathematics of relative entropy and modular flow
  are A. The hinge identity is B/C (structural). The rasa-geometry
  claims are D (testable). The felt-identity remains E/C.

---

## 8. THE ROADMAP

1. **This week (free):** P1 — run DEAM through the formula. The
   rasa formula's first large-scale test. Also P3 — re-analyze the
   Saigusa/Amoeba data with the attractor term.
2. **This month (cheap):** P2 — the habituation test (greenhouse +
   speaker + tomato batch, or slime mold + quinine).
3. **Next:** P4 (the spectral test — music/meditation data),
   P5 (rasa clustering), P6 (aging + anticipation).

**The TCF is designed to be killed by P1.** If valence doesn't
track the derivative of surprise, the whole framework falls — and
that's the point. A framework that can die is a framework that can
be tested; one that can be tested is one that can work.

---

*THE TEMPORAL COHERENCE FRAMEWORK — 2026-08-01. Everything felt
reduces to relative entropy and its derivative; everything
structural reduces to the modular spectrum; the future attractor
pulls the prediction; the moment is the flow's local structure;
and the first two tests use data that already exists. The hinge is
identified; the predictions are falsifiable; the caveat never
relaxes.*
