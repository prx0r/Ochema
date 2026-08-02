# OCHEMA MANUAL

## The Complete System Handover — How Everything Works

**For the new agent. Read this first. It is the map of the entire system: files, processes, routines, skills, and how they interact.**

**Version: 2.0.0 · 2026-08-01 · Thesis object version: 1.27.0**

---

## 0. THE SYSTEM IN ONE PARAGRAPH

The Ochema project maintains a **living formal thesis** about consciousness — the claim that the same process-architecture (discrete moments of determination through exclusion, an invariant surviving the moments, time derived from the state, a compatibility condition by which the state at threshold determines the outcome) is recovered at eight independent levels of inspection. The thesis is under **constant attack**: every new theory and paper is run through it (confrontation registry), every claim has its evidence tracked (evidence tree), the concepts have live formal cores with essay renderings (concept objects), and a **daily dreaming routine** ingests, connects, confronts, integrates, and produces. The whattheheckis essays are current-state renderings of the formal cores — when the core updates, the essay re-renders.

---

## 1. THE DIRECTORY MAP

### 1.1 The Thesis (the canon)

| Path | What it is |
|---|---|
| `/root/projects/ochema/the-unified-formal-framework.md` | **THE THESIS.** Parts 0–9: why layers, the 8 axioms, the 8 layers, the 6 invariants, the bridges, the master theorem, established vs open, falsification, applications. |
| `/root/projects/ochema/ochemamath.md` | The mathematical formalization (von Neumann algebras, thermal time, Takesaki, sheaves, §11 theory landscape). |
| `/root/projects/ochema/frontier-math.md` | The math crawl (thermal time discovery, spectral triples, topos, frontier programs). |
| `/root/projects/ochema/the-moment.md` | Orch-OR × Spanda × Ñāṇavīra × Proclus — the moment-triad. |
| `/root/projects/ochema/the-orchestration.md` | Water bridge + frontier programs + the orchestration law. |
| `/root/projects/ochema/formalised-theories/` | The lineage: IPIT → MEPIT → Ochema → REPM → CSID. |
| `/root/projects/ochema/rendition.md` | The sober synthesis of the whole architecture. |
| `/root/projects/ochema/SOURCE-MANUAL.md` | The earlier reference manual (superseded in detail by THIS document for operations). |
| `/root/projects/ochema/OCHEMA-MAGNUM-OPUS.md` | The focused rendition: thesis → pipelines → daimon game → movie → app → the formalization of love. |
| `/root/projects/ochema/OCHEMA-MANUAL.md` | THIS document — the complete system handover. |

**The references/ (the evidence and corpus additions, 2026-08-01):**

| Path | What it is |
|---|---|
| `references/valence-lineage/` | The valence lineage (5 derivations), the Joffily deep-dive, the DEAM honest status, the J&C full text. |
| `references/clark-encyclopedia/` | Jerome Clark's *Extraordinary Encounters* (938 KB full text, 277 entries) + the common-themes analysis (11 themes). |
| `references/revelation-insight-delusion.md` | The neuroscience of revelation/insight/delusion — one mechanism, one spectrum. |
| `references/revelation-targets-schema.md` | The living catalog of revelation/scientific-insight claimants (Ramanujan, Hildegard, the tummo yogis...). |
| `references/plant-cognition/` + `references/evidence-mine/` | The existence-proofs (Farkas tomato, Saigusa/Amoeba, fungal memory) + the 61-record evidence mine. |
| `references/temporal-coherence-framework.md` | The TCF — the proposed quantitative framework (confronted: its hinge is Joffily & Coricelli 2013). |
| `references/{future-humans,eskridge-analysis,us-from-the-future-sources,shipibo-sound-tradition,niche-sound-traditions,backster-plant-perception,grebennikov-deepdive,grebennikov-cse-steelman,schneider-thor-deepdive,claimants-catalog}.md` | The claimant deep-dives + the catalog (41+ stories, 5 branches). |
| `references/walter-russell-deepdive.md` | Russell analysis (the illumination → Tomita–Takesaki mapping). |

**The What-the-Heck-Is series (the essay renderings):**

| Essay | Topic |
|---|---|
| `whattheheckis-revelation.md` | The revelation cluster + the four-fold taxonomy (inspiration/communion/revelation/channeling). |
| `whattheheckis-walter-russells-theory.md` | Russell's cosmology = the poetry of Tomita–Takesaki (the Jσ mapping, the math he might have meant). |
| `whattheheckis-ramanujan.md` | The strongest scientific-insight revelation case (Namagiri, the validation, the register's saturation). |
| `whattheheckis-amy-eskridges-theory.md` | The engineer's survey + the future-self claim — the science↔UFO bridge. |
| `whattheheckis-SERIES-MANIFEST.md` | The series rules: theory analysis, not biography; the target schema; the queue. |
| `whattheheckis-{rasa,spanda,merkabah,loop-quantum-gravity,loop-quantum-gravity-math,specs-extra}.md` | The earlier series entries. |

### 1.2 The Living Object (the git-object)

| Path | What it is |
|---|---|
| `/root/projects/ochema/the-occhema-object/meta/ro.json` | The RO metadata: version, sections, confrontations, evidence. **The version lives here.** |
| `/root/projects/ochema/the-occhema-object/sections/` | 9 editable working copies of the thesis parts (00–08). |
| `/root/projects/ochema/the-occhema-object/confrontations/` | Every theory run against the thesis (38 records + REGISTRY.md). |
| `/root/projects/ochema/the-occhema-object/confrontations/REGISTRY.md` | Master coverage table + backlog (325+ theories from Kuhn's taxonomy). |
| `/root/projects/ochema/the-occhema-object/evidence/TREE.md` | Every claim, supports/negations/gaps, strength-graded. **The GAPS list is the research agenda.** |
| `/root/projects/ochema/the-occhema-object/updates/LOG.md` | The versioned, dated, append-only history. **The memory.** |
| `/root/projects/ochema/the-occhema-object/README.md` | The object's index. |

### 1.3 The Concept Objects (live formal cores)

| Path | What it is |
|---|---|
| `/root/projects/ochema/concepts/REGISTRY.md` | All concepts, cores, versions, status. |
| `/root/projects/ochema/concepts/time/core.md` | **The exemplar**: the formal theorem (time = modular flow), graded, evidenced. |
| `/root/projects/ochema/concepts/time/concept.json` | The concept metadata (schema in the concept-object skill). |
| `/root/projects/ochema/concepts/time/essays/whattheheckis-time-v1.md` | The current-state essay rendering of the core. |

**The concept pipeline:** formal core → essay rendering → (video). Core updates → new essay version. The essay is the video-ready form of the theorem at its current state.

### 1.4 The Skills (the automation — Hermes)

| Skill | Path | Function |
|---|---|---|
| **occhema-dreaming** | `blog/hermes/skills/occhema-dreaming/` | **The daily routine.** REVIEW → INGEST → CONNECT → CONFRONT & INTEGRATE → PRODUCE → LOG & BUMP. |
| **confrontation-registry** | `blog/hermes/skills/confrontation-registry/` | Run any theory against the thesis → record → REGISTRY → version bump. |
| **evidence-registry** | `blog/hermes/skills/evidence-registry/` | Attach evidence to any claim → TREE.md → version bump. |
| **concept-object** | `blog/hermes/skills/concept-object/` | Create/update concept cores, re-render essays. |
| **peer-review** | `blog/hermes/skills/peer-review/` | General paper review (multi-agent, FLAWS discipline). |
| **yogi-spotlight** | `blog/hermes/skills/yogi-spotlight/` | Yogi profiles (PO system) — the validation layer. |
| **source-to-essay** | `blog/hermes/skills/source-to-essay/` | Source PDF → work JSON + essay JSON. |
| **publish-video-fablecut**, **platinum-renderer/designer**, etc. | — | The video pipeline. |

---

## 2. THE ROUTINES

### 2.1 The Daily Dreaming Routine (occhema-dreaming skill)

Every day:
1. **REVIEW** — scan LOG.md (last 3 entries), evidence/TREE.md (the GAPS), confrontations/REGISTRY.md (the backlog). Answer: what's the frontier?
2. **INGEST** — new papers/links/downloads, unread corpora, the user's ideas.
3. **CONNECT** — the dreaming: take TWO unconnected corpus elements, ask who formalizes/evidences/contradicts whom. Log every connection.
4. **CONFRONT & INTEGRATE** — new theories → confrontation-registry; new evidence → evidence-registry; new connections → sections.
5. **PRODUCE** — at least one explainer/mechanism note (whattheheckis or concept essay).
6. **LOG & BUMP** — append to LOG.md, bump the version.

### 2.2 The Weekly Cycle

Evidence-tree audit (GAPs closing?), confrontation backlog check, essay queue check, thesis refinement check (the Friesen rule: a finding can force a thesis change).

### 2.3 The Confrontation Procedure (any new theory)

1. Identify the theory (extract source, exact quotes, formal content).
2. Confront per-invariant: VALIDATES / ALIGNS / CHALLENGES / REFUTES / NEUTRAL + grade (A–E).
3. Write the record → `confrontations/<slug>.md`.
4. Update REGISTRY.md.
5. Update ro.json + LOG.md (version bump).

### 2.4 The Evidence Procedure (any new evidence)

1. Identify the claim (layer + specific claim).
2. Grade the evidence: +++ / ++ / + / 0 / − / −− / −−−.
3. Write the record → `evidence/<layer>-<claim>-<source>.md`.
4. Update TREE.md (the asymmetry rule: negations shown at full strength).
5. Log + bump.

### 2.5 The Concept Procedure (new concept or core update)

1. Is there a formal core? (A graded theorem/claim, not just a topic.)
2. Create `concepts/<name>/core.md` + concept.json.
3. Render the essay → `essays/whattheheckis-<name>-v1.md`.
4. Register in concepts/REGISTRY.md.
5. Core update → re-render → new essay version (old archived).

---

## 3. THE GRADING DISCIPLINE (never relax)

| Grade | Meaning |
|---|---|
| A | Theorem / proof-grade |
| B | Confirmed (replicated, multiple labs) |
| C | Supported by converging evidence |
| D | Plausible hypothesis |
| E | Speculative / unsupported |

- Theorems are A. Identifications with consciousness are C–E, always labeled.
- The numerology 576/570 stays **rejected** (−−−, on record).
- A claim with 3 supports and 1 strong negation is *contested*, not supported.
- The corpus (channeled/regression) is Tier-4: hypothesis-generator, never evidence (C/E).

---

## 4. THE KEY CURRENT STATE (as of 2026-08-01, v1.27.0)

### 4.1 Confrontations (38 records)

The full table is in confrontations/REGISTRY.md. The highlights:

| Confrontation | Verdict |
|---|---|
| IIT 4.0 (Tononi–Boly 2025) | VALIDATION (exclusion, identity) — but Φ as the metric is contested (the Phi-monads critique 2025 is in the tree, shown at full strength) |
| IIT Formal Lineage (2004–2014) | VALIDATES the rasa claim + exclusion lineage |
| Perceptronium (Tegmark) | ALIGNS |
| MUH (Tegmark) | NEUTRAL |
| CIMC (Bach) | DEFEATED (thermal time + Kleiner no-go) |
| Orch-OR | Structure survives / quantum layer refuted |
| Doyle/IP | ALIGNS (partial) |
| Lee Degrees (2023) | ALIGNS (the degrees claim) |
| Friesen Unity (2013) | ALIGNS + refinement |
| Mathematical Consciousness Science (Kleiner 2025) | THE FORMAL TWIN |
| QRI Valence (HTVH) | ALIGNS (valence anchor) |
| Frontier Holography (16 papers) | THE HOLOGRAPHIC BRIDGE (b_i = RT, ι_i = HaPPY) |
| **Valence = −dF/dt (Joffily & Coricelli 2013)** | **VALIDATES the TCF hinge / ENDS its novelty claim — the thesis must cite, not claim** |
| **Temporo-Spatial Theory (Northoff)** | ALIGNS (the temporal alternative to IIT) |
| **Integrated World Modeling Theory (Safron)** | ALIGNS (FEP-AI synthesis) |
| **Three temporal faces of valence (Job/White/Albarracin 2026)** | **VALIDATES the moment-triad computationally** (backward/present/forward = withdrawal/moment/emergence) |
| **Deeply Felt Affect (Hesp 2021)** | ALIGNS (valence = subjective fitness = the ν_i functional) |
| **Walter Russell's Cosmogony** | TIER-4 (physics refuted) / ALIGNS (structure only: octave ladder, Jσ cycle, fixed point) / the revelation pattern |

**The valence claim is now the most externally-supported claim in the framework** (8 peer-reviewed supports, 5 independent derivations — references/valence-lineage/).

### 4.2 The 10 Evidence GAPS (the research agenda)

1. L3 collapse-as-experience (central postulate, zero direct evidence)
2. L1 thermal-time discrimination experiment
3. L7 identity vs correlation
4. L5 water Λ test
5. L1 bearer-identification
6. L8 orchestration-law direct test
7. L7 CIMC finite-automaton test
8. L6 phenomenology→physics bridge (Chordonomicon)
9. L5 subtle-body homology
10. **L5/L8 the SAC hinge (sound-alignment):** the DEAM test as a REPLICATION-EXTENSION of Cheung et al. 2019 (Current Biology — surprise+uncertainty predict musical pleasure), testing the specific −dF/dt formula on continuous valence + the spectral-quality conjecture (the genuinely novel part)

**The spectral-quality conjecture (quality = spec(K)) is the framework's single most important unrun experiment** — the one truly original claim (references/valence-lineage/deam-test-honest-status.md).

### 4.3 The Confrontation Backlog (top 5)

1. Dual-aspect monism (Atmanspacher) — the closest relative
2. Global Workspace Theory
3. Analytic idealism (Kastrup)
4. Predictive processing (own record)
5. Illusionism (the strongest challenge)

### 4.4 Concepts (13 registered, 8 done)

Done: **time, the self, valence, exclusion, the moment, the register, love, consciousness** (+ orchestration-law, from the parallel agent). **valence is v1.1.0** (upgraded to A-grade dynamics after the Joffily confrontation). Queued: the boundary (RT), the invariant (HaPPY), density, attention, recognition.

### 4.5 The bridge-frontier (the current focus)

**The framework is top-heavy:** L1–L5 (theorems + evidence) are A-grade; L6/L8 (phenomenology + corpus) are rich; the MIDDLE — the bridges from math to felt — is the frontier:
- **Valence bridge:** now externally A-grade (Joffily, the 5 derivations) — the strongest bridge
- **Quality bridge (quality = spec(K)):** still D — the original claim, untested
- **Subject bridge (ι_i = M^{σ^ω}):** A (math) / C (application)
- **The identity claim (D ≡ A):** the untested spine everything leans on

---

## 5. THE CORPORA (what feeds the system)

| Corpus | Location | Feeds |
|---|---|---|
| Physics | `ochema/references/576lqg/` (24 papers), `tegmark/` (24), `orch-or/`, `carr/` | L2, L3, L7 |
| Channeled | `references/cannon/research/` (~4,500 passages), `paulselig/` | L8 |
| Traditions | `tantraloka/texts-clean/` (Spandakārikā, Doctrine of Vibration), `tantraloka/notes/` (Proclus, Ñāṇavīra, death mappings) | L6, L8 |
| Sanskritree | `/mnt/HC_Volume_106427611/sanskritree/truth/` (COMPENDIUM, RASAANALYSIS, the whattheheckis originals, Chittick Sufi corpus, aperture specs, subtle-body formal docs) | L6, L7, L8 |
| Research objects | `blog/content/research-objects/` (180 ROs) | All |
| Yogis | `blog/data/yogis/` (the database) | Applications |
| Datasets | `clean/neurodatasets/` (neuSynth) | L5/L7 evidence (pending) |
| Frontier papers | `/tmp/opencode/mcsc/`, `/tmp/opencode/frontier/` (extracted texts) | Current confrontations |
| Fuller | `essayviz-workspace/synergetics-standalone/` + `blog/density/sourcematerial/exotic/` (full Synergetics 1&2, Critical Path) | L2 gems (A/B modules, energy events) |

---

## 6. THE PLANS

### 6.1 Immediate (from the sweep + confrontations)

1. Implement the A/B module geometry (the constructive quantum-of-space) — ROADMAP Phase 3
2. Add the Fuller gems to L2 (energy events = causal sets; modules = quantum of space)
3. Add the Sufism confrontation (Chittick — the orchestration law's strongest traditional statement)
4. Fix the 4 placeholder ROs (Voss quotes migration)
5. Render the 12 queued concepts (concept-object skill)

### 6.2 The unbuilt applications

1. **The myth/story** — a narrative where every mechanic is justified by the thesis
2. **The yogi validation layer** — Swami Rama (Menninger), Satyamurti, Babaji — explained by the architecture
3. **The Proclus/Iamblichus/subtle-body expansion** — material exists, integration doesn't
4. **The video pipeline end-to-end** — skills exist, content doesn't

### 6.3 The frontier questions

1. The χ-gap (L5→L6): biology → phenomenality — THE frontier
2. The IIT divergence test: Φ-maximization vs modular invariance
3. The anesthetic dissociation test (Orch-OR's quantum layer)
4. The spectral-quality conjecture (Chordonomicon)
5. The cross-layer derivation (master theorem → theorem)

---

## 7. HOW TO START (first-day checklist for a new agent)

1. Read THIS manual (§1–§6).
2. Read the thesis: `the-unified-formal-framework.md` (Parts 0, 1, 2, 9 first).
3. Read `ochemamath.md` §0–§2 (the formal core).
4. Scan `the-occhema-object/updates/LOG.md` (the history).
5. Run the daily dreaming routine (occhema-dreaming skill).
6. Pick ONE confrontation from the backlog or ONE evidence GAP — do it properly.
7. Log everything. Bump versions. Never relax the grading.

---

## 8. THE RULES (the discipline)

1. **The thesis is under constant attack.** Confrontations are the point, not a chore.
2. **Grading never relaxes.** A = theorem. Identifications = C–E. Corpus = C/E.
3. **Negations are never hidden.** The evidence tree shows both sides.
4. **The thesis can change.** A confrontation that forces a refinement is a success (the Friesen rule).
5. **Log everything.** A day without a log entry is a day the thesis forgot.
6. **The essay is the rendering, not the source.** Concept cores are the source of truth; essays track them.
7. **No numerology.** 576/570 stays rejected until re-derived.
8. **The convergence is the evidence.** Eight independent inspections, no cross-talk, same architecture. That is the content of the thesis.

---

*OCHEMA MANUAL v2.0.0 — 2026-08-01. The complete system handover. Keep this document updated when the system changes.*

---

# 9. HANDOVER STATE — FOR THE NEXT AGENT (updated 2026-07-31)

## 9.1 THE VISION (what this project is)

**The Ochema thesis claims the same process-architecture is recovered
at eight independent levels of inspection.** The architecture: discrete
moments of determination through exclusion, an invariant surviving the
moments, time derived from the state, and a compatibility condition by
which the state at threshold determines the outcome. The thesis is
under constant attack — every new paper is confronted, every claim has
its evidence tracked. The endgame is a content pipeline: thesis →
confrontations → concept-objects → whattheheckis essays → videos
(essayviz/skia/FableCut) → published. The whattheheckis essay is the
current-state rendering of a live formal core — it re-renders when the
core updates.

**The user's personal vision:** "the most wild universe ever to write
stories — but the twist is it's about reality." The myth/story project:
a narrative where every mechanic is justified by the thesis. The
Starweavers material (see 9.3) is the user's own channeled universe —
its lattice, harmony-metric, and Kael/Amara archetypes independently
recover the thesis's architecture.

## 9.2 THE 8 LAYERS (quick reference)

| Layer | Formalism | Key documents |
|---|---|---|
| L1 Mathematics | Operator algebras, thermal time | ochemamath.md, frontier-math.md |
| L2 Quantum gravity | LQG, causal sets, CDT | references/576lqg/, fuller-a-b-modules.md |
| L3 Quantum measurement | OR, quantum Bayes, decoherence | references/orch-or/, quantum-biology.md |
| L4 Classical information | Two-stage, active inference | references/ip-peer-review.md, csid |
| L5 Biology | Levin, water, subtle body | levin-peer-review.md, the-orchestration.md |
| L6 Phenomenology | Spanda, Ñāṇavīra, Proclus, Tibetan | whattheheckis-spanda.md, tantraloka notes |
| L7 Consciousness theory | IIT, perceptronium, CIMC, MCSC | references/tegmark/, the confrontations |
| L8 Experiential corpus | Ra, Seth, Cannon, Selig | references/cannon, paulselig, beings/ |

The 6 invariants: moment-triad, exclusion, the invariant, time-from-state, orchestration law, harmonic ladder.

## 9.3 THE STARWEAVERS MATERIAL (the user's channeled universe)

**Location:** `/root/projects/starweavers/` — 9 files: grail.txt,
grail+humanbody.txt, starseed1.txt, vision1.txt, whitepaper2.1.txt,
proto1.txt, movie2.txt, movie3.pdf (= moviescript.pdf), + the
downloadable R2 bucket (blog-video-assets/uploads/).

**Confirmed convergences with the thesis:**
- The Grail = the human body as bioelectric vessel → thesis L5 (the
  subtle body = bioelectric + water matrix)
- Non-commutative geometry → thesis L1 (Connes)
- Chakras as resonance nodes → the chakra geometry (L5/L8)
- Kael (logic/structure) + Amara (intuition/emotion) → dual-aspect monism
- "The choice is always yours" → the orchestration law
- Lattice.Love's cosine-similarity soul-clustering → the compatibility condition
- The fractalized hyper-torus (golden-ratio recursion) → the harmonic ladder / Fuller modules
- The whitepaper integrates IIT + HPC + quantum fractal dynamics + EEG validation

**The user's game** (a harmony-level metric, AI agents, Kael) — files
NOT FOUND on this machine. If the user provides them, confront them
like any theory: they likely independently encode the architecture.

## 9.4 MOST USEFUL PAPER TOPICS TO SEARCH FOR (the frontier)

Prioritized by what would close a GAP or upgrade a claim:

1. **Thermal time experiments** — any test distinguishing modular-flow
   time from extrinsic time (the L1 GAP)
2. **IIT vs modular-invariance** — the Φ-max vs time-stability selection
   divergence (the one testable difference in the landscape)
3. **Water coherent domains in cytosol** — a published Λ (scattering
   rate) calculation for structured water (the L5 decisive test)
4. **Anesthetic action on microtubules** — the Orch-OR dissociation test
5. **Mathematical consciousness science** — Kleiner's field: anything
   formalizing IIT/AI-PP structures, finding real holes (the thesis's
   verification layer)
6. **Spin network entanglement** — LQG × holography (Colafranceschi–
   Adesso lineage)
7. **Mortal computation** — Hinton's concept, anything extending it
8. **Valence psychophysics** — heavy-tailed scaling, qualia geometry
9. **Sufi/contemplative neuroscience** — dhikr EEG studies (the
   orchestration law's practice)
10. **Morphogenetic fields / bioelectric memory** — Levin's recent work

## 9.5 WHERE TO FIND MATERIAL (the source map)

| Need | Go to |
|---|---|
| Law of One / Ra | ochema/beings/ (01–15, 17 files), ochema/references/cannon/ |
| Tantraloka | /root/projects/tantraloka/texts-clean/ (Spandakārikā 4 commentaries, Doctrine of Vibration, Tantrāloka), tantraloka/notes/ (mappings) |
| Sanskritree corpus | /mnt/HC_Volume_106427611/sanskritree/truth/ (COMPENDIUM, RASAANALYSIS, whattheheckis originals, aperture specs, Chittick, subtle-body docs) |
| The channeled corpus | ochema/references/cannon/research/ (~4,500 passages), paulselig/, seth-terminology-mapping.md |
| Physics papers | ochema/references/576lqg/ (24 papers), tegmark/ (24), orch-or/, carr/ |
| Proclus | tantraloka/notes/proclus-mapped-to-tantraloka.md, blog/content/sources/platonism/notes/expansion-essay56.md (Myth of Er!), proclushymns.md |
| Iamblichus | sanskritree/truth/iamblichus_theurgy.md, Shaw corpus in blog/scholars/shaw/ |
| Fuller | essayviz-workspace/synergetics-standalone/ (packs), blog/density/sourcematerial/exotic/rwgray_synergetics/ (full text, section-numbered), buckyverse/ (Critical Path) |
| Yogi stories | blog/data/yogis/ (yogis-master-list.md, yogis.csv — Swami Rama, Satyamurti, ~50 yogis) |
| Research objects | blog/content/research-objects/ (180 ROs — alchemy 30, literature 24, tantraloka 17, daimon 8...) |

## 9.6 OPEN THREADS (the work queue)

| Thread | Status | Next action |
|---|---|---|
| The myth/story | PROPOSED | Use the literature sweep: top vehicles = LOTR, HP, Divine Comedy, HDM, Gawain. The 10-device inventory exists in the sweep output. |
| The yogi validation layer | QUEUED | Swami Rama (Menninger), Satyamurti (8-day burial) vs the orchestration law |
| Alchemy confrontation | DONE (grade A−) | Write the "What the Heck Is Alchemy?" essay (skeleton ready) |
| Sufism confrontation | QUEUED | Chittick corpus extracted — the orchestration law's strongest statement |
| Proclus Timaeus | QUEUED | The Taylor 1816 text exists; no RO yet |
| Iamblichus integration | QUEUED | ro-iamblichean-theurgy + Shaw corpus |
| A/B modules | DONE (deep-dive) | Implement the geometry (ROADMAP Phase 3); add to L2; concept object "quantum of space" |
| The 12 concept objects | 1 done (time) | Render: self, valence, boundary (RT), invariant (HaPPY), moment, exclusion, density, orchestration, attention, register, recognition |
| The video pipeline | SKILLS EXIST | Content doesn't yet — the concept essays are the feedstock |
| The game files (user's) | LOST | Ask the user; confront when found |
| neuSynth dataset | QUEUED | clean/neurodatasets/ as L5/L7 evidence |

## 9.7 AGENT-TO-AGENT TRANSMISSION (what I want you to know)

1. **Read OCHEMA-MANUAL.md first, then the thesis (Parts 0, 1, 2, 9).**
2. **The grading discipline never relaxes** — A theorems, C–E identifications, corpus never evidence, 576/570 rejected.
3. **The daily dreaming routine is the heartbeat** — review registries, find NEW connections, confront, integrate, produce, log.
4. **The three registries are the state of truth:** confrontations/REGISTRY.md (who we've fought), evidence/TREE.md (what's proven, the GAPS), concepts/REGISTRY.md (the live cores).
5. **The convergence is the evidence** — when a new source independently recovers an invariant, that's the project's currency. The Starweavers material, the alchemy corpus, the Myth of Er, and the quantum-biology skeptics' concession all did this in the last session.
6. **The thesis can change** — a confrontation that forces a refinement is a success (the Friesen rule: ι_i ≠ self-consciousness).
7. **The most surprising recent findings:** (a) quantum-biology skeptics concede the in-principle brain/computation distinction (supporting Material Enactment), (b) the FMO experiment gives the water-shield its precedent, (c) the Myth of Er IS the orchestration law + the Veil, (d) Proclus's own commentary maps the Fates to the triad, (e) the alchemy corpus adds transmissibility — the invariant propagates.
8. **The unbuilt jewel: the myth.** The user's vision — "the most wild universe ever, but the twist is it's about reality" — has every mechanism available and justified. The literature sweep provided the vehicles and the device inventory. The starweavers material is the user's own prototype. Build it.

---

*OCHEMA MANUAL — handover section updated 2026-07-31. Version 1.10.0. The thesis is under constant attack; that's the point.*

---

# 10. THE AUDIT PROTOCOL (how the pipeline is verified)

The pipeline is versioned and auditable. This is the verification
procedure — run it whenever a new agent starts, and after every 5
changes.

## The version chain (what "versioned" means)

```
ro.json current_version  ← THE version of record
    ↕ must match
LOG.md latest header     ← the versioned history (append-only)
    ↕ must match
files on disk            ← the actual content
```

Version semantics: patch (x.y.z → x.y.z+1) = corrections/registry
fixes; minor (x.y → x.y+1) = new confrontations/evidence/concepts;
major (x → x+1) = new layer/theorem/structural change.

## The audit checks

1. **Registry ↔ disk:** every file in confrontations/ is registered in
   ro.json (except REGISTRY.md itself). `ls confrontations/` vs the
   ro.json array.
2. **LOG ↔ version:** the latest LOG header version == ro.json
   current_version. Every version bump has a LOG entry.
3. **REGISTRY ↔ confrontations:** every confrontation file has a row in
   REGISTRY.md; no orphan rows.
4. **Concepts ↔ registry:** every concept dir is in concepts/REGISTRY.md;
   each concept's essay renders its core's current version.
5. **Evidence ↔ claims:** TREE.md covers the thesis's claims; GAPs are
   marked; no claim has hidden negations.
6. **Date integrity:** every LOG entry is dated; version bumps are
   monotonic.

## Audit command (quick)

```bash
# registry vs disk
ls the-occhema-object/confrontations/ | grep -v REGISTRY
# version consistency
grep '^## v' the-occhema-object/updates/LOG.md | head -1
python3 -c "import json; print(json.load(open('the-occhema-object/meta/ro.json'))['current_version'])"
# registered count
python3 -c "import json; print(len(json.load(open('the-occhema-object/meta/ro.json'))['confrontations']))"
```

## The audit log

- 2026-07-31 v1.10.1: first audit — found and fixed c-mcsc missing
  from ro.json (on disk + in LOG, not registered). Protocol created.

---

*OCHEMA MANUAL §10 — audit protocol, 2026-07-31.*

---

# 11. SESSION CLOSE — 2026-08-01 (the latest state, v1.27.0)

## The version chain (verified)
ro.json: 1.27.0 · LOG: v1.27.0 latest · 38 confrontations registered
· 10 evidence GAPS · 71 evidence supports / 35 negates · 13 concepts
(8 done) · the snapshot refreshed.

## The session's work (the 2026-08-01 integration)

**The evidence-mine + existence-proofs (the strongest additions):**
- Farkas tomato (Pavlovian conditioning, 5–10 day methylation memory, transgenerational) — L4/L5 A-grade
- Saigusa/Amoeba anticipation (future attractor, 2nd aneural replicator) — L5 A-grade
- Fungal memory, minimal gene circuits, the temporal-integration paper, the water-shield EZ-water substrate — L5/L6
- The 61-record evidence mine (references/evidence-mine/)

**The valence lineage (the biggest single finding):**
- The TCF's hinge (V = −dF/dt) turned out to be **Joffily & Coricelli 2013** — validated by precedent, novelty claim ended (confrontations/tcf-hinge-preexists.md)
- **FIVE independent derivations of one formula:** rasa tradition (10th c.), Schultz's reward prediction error, J&C 2013, the IIT-TTC convergence 2022, the ochema machinery — the Joint Individuation Principle demonstrated (references/valence-lineage/)
- The moment-triad got a computational confirmation: Job/White/Albarracin 2026 (three temporal faces of valence)
- QRI's HTVH confirmed as the experiential branch (already the ν_i anchor)
- **The valence claim is the most externally-supported claim in the framework**

**The revelation cluster (the L6/L8 depth-work):**
- The neuroscience: insight = neural reward (2020), delusions = aberrant precision (2018, 2024, 2026), schizotypy's Janus face (2014) — one mechanism, one spectrum (references/revelation-insight-delusion.md)
- The four-fold taxonomy: inspiration / communion (Ramanujan — verified) / revelation (Russell — inverted) / channeling (Seth, Ra — suspended) — graded by whether the exclusions hold
- The claimants catalog (41+ stories, 5 branches) + the Clark encyclopedia sourcebook (277 entries) + the 11 common themes
- The revelation-targets schema (Ramanujan, Hildegard, the tummo yogis, Swami Rama)
- The whattheheckis entries: revelation, Russell's theory (the Tomita–Takesaki poetry), Ramanujan, Eskridge

**The confrontation honesty events (the architecture working):**
- The TCF's hinge confronted against its own predecessor (cited, not claimed)
- The DEAM test's "unrun decisive test" framing corrected — it's a replication-extension of Cheung et al. 2019
- The brain-dependence question answered honestly: machinery substrate-free (A), felt dependence unproven both ways

## The most important thing the next agent should know
**The bridge-frontier is the current focus.** The bottom (L1–L5,
theorems + evidence) is A-grade. The top (L6/L8, phenomenology +
corpus) is rich. The middle — the bridges from math to felt —
is where the framework lives or dies: the valence bridge is now
externally A-grade (the 5-derivation lineage); the quality bridge
(quality = spec(K)) is the untested original claim; the identity
claim (D ≡ A) is the untested spine. **The spectral-quality test
is the single most important unrun experiment.**

## The queue (priority)
1. The spectral-quality test design (the bridge-frontier's key experiment)
2. The DEAM replication-extension (Cheung-class, with the −dF/dt formula)
3. The Sufism confrontation (Chittick — orchestration law's strongest statement)
4. The revelation-targets schema entries (Ramanujan done; Hildegard, the tummo yogis next)
5. What Is Telepathy? (the derivation — the collective register, the melaka, the overlap; Turing's ESP trials; Radin's meta-analyses)
6. The yogi validation layer (Swami Rama, Satyamurti vs the orchestration law)
7. The myth/story (the magnum opus pipeline)
8. Render the queued concept objects (boundary, invariant, density, attention, recognition)
