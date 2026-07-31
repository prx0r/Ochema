# OCHEMA AV — The Audio-Visual Arm

## The aesthetics arm's production line + the experiment program

**Prepared:** 2026-07-31 · **Base:** references/aesthetics-to-ochema.md
(rasa × ochema), references/fatherfucker-notes.md (the recovered
corpus), the hxrmxs repo (PMEF-H, the Hybrid Predictive Emotion
Frame), musictheory-1 (the DEAM EEG seed), Part 9.3, ochemamath §7.

---

## 1. THE AV THESIS (what this arm claims)

The felt quality of experience IS the geometry of the state's
trajectory (Part 9.3). The AV arm renders that claim and TESTS it:
music is the invariant's native medium; the composition pipeline is
the bearer; the artworks are state-space navigators. The production
line: essay → emotional coordinates → rasa mode → visual + audio
from one source (COMPOSITION-THESIS), with the invariant-composition
mechanisms (structural-homology, recognition-transaction,
climax-assimilation, constraint-tournament) as the rules of
composition.

## 2. THE EXPERIMENT PROGRAM (the testable core)

### The hypothesis (the user's intuition, formalized)

**Harmony is what we expect vs what happens.** Musical pleasure =
the predictive payoff of surprise resolution, precision-weighted.
Formally (from PMEF-H, the hxrmxs repo — the existing spec):

- **Anticipation** Ant(t) = normalized Shannon entropy of the prior
  belief (suspense)
- **Surprise** S(t) = D_KL(Q(t) ‖ P(t)) (prediction error)
- **Precision-weighted surprise** S_pw(t) = ω(t)·S(t), ω = 1/(H+ε)
  (the orchestration law's weighting — attention as precision
  weighting, L4)
- **Predictive valence** V_p(t) = −tanh(k_p · d/dt smooth(S_pw))
  (pleasure = the NEGATIVE RATE OF CHANGE of surprise — resolution
  payoff)
- **Tension** T(t) = α·S_pw + (1−α)·T(t−1) (leaky integrator)

**The thesis connection:** V_p is the felt quality of the state's
trajectory — the derivative of surprise, not surprise itself. This
is the spectral-quality conjecture's affective face: the harmonic
ladder's resolution structure IS the valence trajectory. And
harmony-as-expected-vs-actual is the orchestration law in the
aesthetic domain: the state (the predictive model) at threshold (the
chord onset) determines the outcome (the felt resolution).

### The experiment: EEG × harmony × FEP surprise

**The design (extending musictheory-1's seed: harmonic surprise →
frontal phase reset; DEAM corpus):**

- **Stimuli**: chord progressions from the Chordonomicon 6D-engine
  corpus (666k songs), selected to span the 6D vectors — the rasa→6D
  signature table gives the a-priori valence labels (śānta = low
  geom distance/high consonance...).
- **Independent variables**: (1) model-derived surprise S_pw(t)
  from the PMEF-H TPM (System 2 = a transformer trained on the
  corpus; System 1 = real-time KL), (2) the 6D geometric distance
  from symmetry, (3) harmony category (consonant/dissonant/resolved/
  unresolved).
- **Dependent variables**: EEG — frontal phase reset (the
  musictheory-1 prediction), N100/P300 surprise response, frontal
  midline theta (anticipation), gamma (the 40 Hz arm), alpha
  coherence; plus self-reported pleasure (continuous valence
  ratings) and the HTVH heavy-tailed scaling (log ratings, not
  0–10).
- **The predictions (falsifiable):**
  1. **Pleasure tracks −d/dt(S_pw), not S_pw** — the resolution
     payoff, not the surprise itself. (This discriminates the
     predictive-valence claim from a naive surprise-aversion
     claim.)
  2. **Frontal phase reset scales with S_pw, precision-weighted**
     (the musictheory-1 seed).
  3. **The 6D geometric distance predicts the EEG surprise response
     better than chroma/audio features alone** — the geometry IS
     the structure (Part 9.3's operational claim).
  4. **The valence ratings are heavy-tailed** (HTVH) and their
     tails correspond to the extreme 6D regions (the ladder's
     extremes).
  5. **Coherence restoration rate ↔ valence** (musictheory-1):
     the speed of the state's return to its attractor after a
     surprise predicts felt pleasure — the orchestration law's
     Zeno-pin, measurable.

**The kill conditions (honest):** if pleasure tracks S_pw directly
(rather than its derivative), or if the 6D geometry adds nothing
over standard audio features, or if the heavy-tailed structure is an
artifact of the rating scale — the aesthetic arm's core claim is
refuted-as-stated. The experiment is designed to be able to lose.

**The protocol**: 24–40 participants; EEG (32+ channels); continuous
valence via a slider (log-scale); stimuli = 60 progressions × 3
conditions (predicted/unpredicted-with-resolution/unpredicted-
without); pre-registered analyses; the PMEF-H TPM published with the
data. The DEAM corpus provides the offline validation set (6.9k
tracks with continuous valence/arousal annotations — the surprise
time-series can be computed and correlated with the annotations
before any EEG is run).

### The lineage (why this is the right next experiment)

The thesis's valence bridge has: the theorem side (coherence
functional), the tradition side (rasa, validated), the peer-reviewed
anchor (HTVH — heavy tails), and now the built side (the 6D engine +
PMEF-H). **What's missing is the controlled measurement** — the EEG
experiment closes the loop: the geometry (6D) → the physiology
(phase reset, coherence restoration) → the feeling (valence), with
the predictive model as the bridge. This is the thesis's most
designable experiment — it can be pre-registered, run on existing
corpora, and it has genuine kill conditions.

## 3. THE PRODUCTION LINE (what the AV arm builds)

```
ESSAY (the concept core's whattheheckis)
  → Emotional arc extraction (5D: valence/arousal/control/
    transcendence/tension — the COMPOSITION-THESIS coordinates)
  → Rasa mode (nearest 6D signature)
  → VISUAL: the platinum renderer + the shader packs (the 93
    fragments; the invariant-composition mechanisms)
  → AUDIO: the 7-mapper AV framework (ColorMapper/GeometryMapper/
    TimbreMapper — 12 notes→12 hues via the circle of fifths,
    octave = brightness, chords→polygons)
  → NARRATIVE: the voiceover directs attention (precision
    weighting, applied)
  → The recognition-transaction: climax ≠ endpoint; the six seconds
    of space; the camatkāra aperture (the Albers dissolve — all
    boundaries vanish at the pearl)
```

The production line IS the aesthetics arm: every output is a
state-space navigator for the viewer's register, built from the
essay's core. The video pipeline (essayviz/skia/FableCut) gains the
rasa-mapping stage: the whattheheckis essays are already the Bibles;
now they carry emotional coordinates.

## 4. THE DISCIPLINE (the arm's rules)

- The identity (quality = geometry) is D — the experiment program
  exists to promote or refute it; kill conditions are designed in.
- The PMEF-H is the hxrmxs repo's spec (Tier-3-ish: mathematical
  spec, not peer-reviewed) — used as the model, not as evidence.
- The rasa corpus is Tier-4 (validated quotes, not evidence).
- The shader films are the myth side: Tier-4 content, rendered.
- The tractatus corpus is prior formal metaphysics — the AM0 σ-flip
  is the thesis's σ-flip, previously formalized; the Buddhism/Śaiva
  divergence stands unresolved (both recorded).
- No pseudo-scientific emotion meters: the REVIEW.md failure
  conditions are the arm's own quality gate.

---

*OCHEMA AV v1.0.0 — 2026-07-31. The aesthetics arm: renders the
claim, tests the claim, and the experiment is designed to be able to
lose.*
