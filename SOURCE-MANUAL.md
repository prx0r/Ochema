# Source Manual

## The Ochema Research System — Complete Reference

**The canonical navigation document for everything built, the plans, and how to validate and use it.**
**Version: 1.0 · 2026-07-31**

---

## HOW TO USE THIS MANUAL

This is the map. Read Part 1 for the structure, Part 2 for the
canonical documents, Part 3 for the living registries, Part 4 for the
skills/automation, Part 5 for the plans, Part 6 for validation, Part 7
for the corpora, and Part 8 for the frontier/next steps.

---

# PART 1: THE SYSTEM AT A GLANCE

```
                    THE THESIS
         the-unified-formal-framework.md (8 layers)
                     + ochemamath.md (formal core)
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   CONFRONTATION      EVIDENCE         APPLICATIONS
   REGISTRY           TREE             (Part 9 of thesis)
   (theories vs       (per-claim       (traditions run
    thesis)            evidence)        through machinery)
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    THE OCHEMA OBJECT
              (canonical living research object)
              meta/ro.json · sections/ · confrontations/
              evidence/ · updates/LOG.md
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     THE LINEAGE      THE SERIES        THE PIPELINE
     formalised-      whattheheckis-    skills →
     theories/        *.md              videos (essayviz/skia)
     (IPIT→CSID)      (explainers)      → publish (FableCut)
```

---

# PART 2: THE CANONICAL DOCUMENTS

## 2.1 The Theory Lineage (formalised-theories/)

The five-stage intellectual history, in order. Each stage is superseded
but preserved — the lineage is the project's provenance.

| File | Stage | Status |
|---|---|---|
| 01-IPIT-inexternalist-process-identity-theory.md | Original identity theory | Superseded |
| 02-MEPIT-materially-enacted-inexternalist.md | Sharpened, evidence-graded | Superseded |
| 03-OCHEMA-formal-framework.md | **Best single framework doc** | CURRENT |
| 04-REPM-reflexive-enactive-process-monism.md | **Frontier ontology** | LEADING EDGE |
| 05-CSID-constraint-selection-information-dynamics.md | Doyle reconstruction | Companion |
| README.md | The lineage explained | — |

## 2.2 The Formal Core

| Doc | What it is | Read when |
|---|---|---|
| **ochemamath.md** | The mathematical formalization: bearer as von Neumann algebra (M, ω), time as modular flow (thermal time), exclusion as conditional expectation (Takesaki), selector as sheaf cohomology, Material Enactment as non-isomorphism. §11 = the full theory landscape (11 theories, support/contrast). | You need the math |
| **frontier-math.md** | The math crawl: thermal time discovery, spectral triples, Ricci flow, topos/HoTT, information geometry, the frontier programs (CDT, shape dynamics, tensor networks, GFT, quantum Darwinism, analog gravity). | You need the frontier math map |

## 2.3 The Capstone

| Doc | What it is |
|---|---|
| **the-unified-formal-framework.md** | THE thesis. Part 0: why layers. Part 1: the 8 minimal axioms. Part 2: the 8 layers (L1 math → L8 experiential corpus). Part 3: the 6 cross-layer invariants. Part 4: inter-layer bridges (the χ-gap = the frontier). Part 5: the master theorem (cross-layer convergence, demonstrated not derived). Part 6: established vs open. Part 7: falsification. Part 9: applications (densities, beings, rasa, recognition, death, Seth — the traditions run through the machinery). |

## 2.4 The Supporting Analyses (ochema/ root)

| Doc | Covers |
|---|---|
| ochema-formal.md | The peer-review-ready framework (§10.7–10.10 = hard-physics anchors) |
| complex.md | REPM — the frontier ontology |
| ochema.md | The original framework statement |
| ochema-landscape.md | Where we fit vs 7 existing frameworks |
| ochema-master.md | The five-tier organization of ALL ideas |
| project-inventory.md | The inventory (needs re-sync with current state) |
| levin-peer-review.md | What Levin actually establishes |
| csid-reconstruction.md | Doyle's science, cleaned |
| rendition.md | The sober synthesis of the whole architecture |
| the-moment.md | Orch-OR × Spanda × Ñāṇavīra × Proclus — the moment-triad |
| the-orchestration.md | Water bridge + frontier programs + the orchestration law |
| whattheheckis-spanda.md | The pulse doctrine |
| whattheheckis-loop-quantum-gravity(-math).md | The LQG pair with verified math |
| whattheheckis-merkabah.md | The chariot/star-tetrahedron geometry |
| the-unprovable-truth.md | The metaphysics without apology |

---

# PART 3: THE LIVING REGISTRIES (the git-object)

## 3.1 The Ochema Object (the-occhema-object/)

The canonical living research object — the thing that persists and
grows. Current version: **1.4.0**.

```
the-occhema-object/
├── meta/ro.json          — RO metadata: sections, confrontations, evidence, version
├── README.md             — the index: structure, update protocol, verdict table, frontier
├── sections/             — 9 editable working copies (one per thesis part)
│   ├── 00-introduction.md … 08-applications.md
├── confrontations/       — every theory run against the thesis
│   ├── REGISTRY.md       — master coverage table + backlog (325+ theories)
│   ├── tegmark-peer-review.md, ip-peer-review.md
│   ├── cimc-confrontation.md, iit4-validation.md
│   ├── orch-or-confrontation.md
│   ├── lee-degrees-2023.md, friesen-structure-2013.md
├── evidence/             — per-claim evidence
│   └── TREE.md           — every claim, supports/negations/gaps, strength-graded
└── updates/LOG.md        — versioned, dated, append-only
```

## 3.2 The Confrontation Registry (confrontations/REGISTRY.md)

**Purpose:** every theory in the field gets run against the thesis.
Verdicts: VALIDATES / ALIGNS / CHALLENGES / REFUTES / NEUTRAL, each
graded.

**Current coverage:** 14 confronted. Priority backlog:
1. Dual-aspect monism (Atmanspacher) — the closest relative
2. Global Workspace Theory (Dehaene/Baars)
3. Analytic idealism (Kastrup)
4. Predictive processing (Friston) — own record needed
5. Illusionism (Frankish/Dennett)

**Backlog:** 325+ theories from Kuhn's Landscape of Consciousness
taxonomy, organized by category (materialism, functionalism,
panpsychism, idealism, dualism, quantum, anomalous, challenge).

## 3.3 The Evidence Tree (evidence/TREE.md)

**Purpose:** every thesis claim, with supporting and negating evidence,
strength-graded (+++/++/+/0/−/−−/−−−). The asymmetry rule: a claim
with 3 supports and 1 strong negation is *contested*, not supported.

**Current state:**
- 9 claims at +++ (multiple independent confirmations)
- 2 rejected (−−−): the 576/570 numerology
- 2 strong negations (−−): quantum layer refuted-as-stated, water shield candidate-only
- **10 GAPS** (exposed claims — the research agenda):
  1. L1 bearer-identification
  2. L1 thermal time vs extrinsic time
  3. L3 collapse-as-experience (the central postulate, zero direct evidence)
  4. L5 water Λ test
  5. L5 subtle-body homology
  6. L6 phenomenology→physics bridge
  7. L7 identity vs correlation
  8. L7 CIMC finite-automaton test
  9. L8 orchestration law direct test
  10. L8 survival claims (unfalsifiable)

---

# PART 4: THE SKILLS (automation — blog/hermes/skills/)

The Hermes-agent skills that automate the pipeline. Each is a SKILL.md
with frontmatter (name, description, version) + procedure.

| Skill | What it does |
|---|---|
| **confrontation-registry** | Run any theory against the thesis: identify → confront per-invariant → write record → update REGISTRY.md → bump version. The batch confrontation pipeline. |
| **evidence-registry** | Attach supporting/negating evidence to any claim: identify claim → grade strength → write record → update TREE.md → bump version. |
| **peer-review** | General scientific paper review (multi-agent, split-then-aggregate: MARG/ASAP/FLAWS methodology). |
| **yogi-spotlight** | Yogi/philosopher spotlight profiles (PO system) + gold-standard narrative structure. Uses the yogi database. |
| **source-to-essay** | Convert source PDF → work JSON + essay JSON (for site/audio). |
| **publish-video-fablecut** | The video publishing pipeline. |
| **platinum-renderer / platinum-designer** | The essayviz/skia rendering. |
| **daily-research, market-scan, practice, site, writing, daimon, astrology, ops, engines, core** | Supporting ops skills. |

**The content pipeline (the vision):**
```
thesis → confrontation (skill) → whattheheckis doc → essayviz/skia
render → video → publish (FableCut) → YouTube
```

---

# PART 5: THE PLANS

## 5.1 The Active Research Vision

1. **Ongoing peer review** — every new theory/paper runs through the
   confrontation registry. The thesis is under constant attack; that's
   the point.
2. **Evidence accumulation** — every new dataset/paper attaches to the
   evidence tree. GAPS close one by one.
3. **Content production** — confrontations → whattheheckis documents →
   videos (essayviz + skia) → auto-publish.

## 5.2 The Queued/Planned Work

| Plan | Status | Where |
|---|---|---|
| Tibetan inspection | DONE (v1.2.0) | L5, L6, L8 |
| Confrontation registry | DONE (v1.3.0) | skills/confrontation-registry |
| Evidence registry | DONE (v1.4.0) | skills/evidence-registry |
| Proclus Timaeus commentary | QUEUED | blog/scholars/Proclus...Taylor_1816.md |
| Iamblichus theurgy integration | QUEUED | ro-iamblichean-theurgy + shaw texts |
| Subtle body formal docs | QUEUED | sanskritree/truth/subtle_body_formal.md |
| The myth/story (thesis as narrative) | PROPOSED | — |
| Yogi validation (Swami Rama, Satyamurti, Babaji) | PROPOSED | blog/data/yogis/ |
| The "whattheheckis" backlog | QUEUED | content-series-plan.md |
| neuSynth dataset as evidence | QUEUED | clean/neurodatasets/ |
| The 17 phases integration | QUEUED | sanskritree/truth/17phases_reframed.md |

## 5.3 The Unbuilt

- The myth/story (user's vision: a narrative where every mechanic is
  justified by the thesis — the intuitive telling)
- The yogi-validation layer (stories of famous yogis explained by the
  architecture: Swami Rama's heart at Menninger = the register's
  control; Satyamurti's burial = the resting place; Babaji = the
  invariant)
- The video pipeline end-to-end (skills exist; content doesn't yet)

---

# PART 6: HOW TO VALIDATE AND USE IT

## 6.1 Validation protocol (how to test the system)

1. **Confrontation test:** pick any theory from the backlog (REGISTRY.md
   → "Backlog"), run the confrontation-registry skill on it. Does the
   record follow the format? Does the verdict hold up against the
   evidence tree?
2. **Evidence test:** pick any GAP in TREE.md. Find the paper/dataset
   that closes it (or proves it can't close). Grade it honestly.
3. **Cross-validation:** after adding a confrontation, check the thesis
   sections it touches — does the section still hold, or does it need
   the refinement the confrontation demands? (The Friesen rule: a
   confrontation can force a thesis refinement — that's a success, not
   a failure.)
4. **The FLAWS discipline (from the peer-review skill):** periodically
   test the skills against known-bad inputs. Plant an error, confirm
   the skill surfaces it.
5. **The grading discipline (never relax):** theorems A, confirmed B,
   identifications C–E. The 576/570 stays rejected. No sympathy grades.

## 6.2 How to use it day-to-day

- **"Add this theory":** run confrontation-registry skill → record →
  REGISTRY.md → version bump.
- **"What's the evidence for X?":** read evidence/TREE.md → the claim's
  row → the records.
- **"Make a video about X":** X → confrontation (if new) → whattheheckis
  doc → render skill → publish.
- **"What's the frontier?":** the 10 GAPS in TREE.md + the χ-gap in the
  framework + the priority backlog in REGISTRY.md.
- **"Check the thesis":** the-unified-formal-framework.md is canonical;
  sections/ are working copies; LOG.md has the history.

## 6.3 The version protocol

- Patch (1.4.0 → 1.4.1): corrections, clarifications
- Minor (1.4 → 1.5): new confrontations, evidence, applications
- Major (1.x → 2.0): new layer, new theorem, structural change
- Every change logged in updates/LOG.md, dated

---

# PART 7: THE CORPORA (what feeds the system)

## 7.1 Physics (references/)

| Corpus | Contents | Feeds |
|---|---|---|
| 576lqg/ | 24 papers: LQG, causal sets, constructor theory, Wolfram, amplituhedron, packings + compute scripts + verification | L2 |
| tegmark/ | 24 papers: perceptronium, IIT 4.0, quantum Bayes, decoherence, multiverse | L3, L7 |
| orch-or/ | Hameroff 2014 chapter + McQueen 2023 | L3 |
| carr/ | Bernard Carr cosmology | L2 |
| cannon/ | 4 Convoluted Universe books, fully extracted (~4,500 passages) | L8 |
| paulselig/ | The Guides' channeled corpus | L8 |
| swedenborg/ urantia-book/ | Afterlife corpora | L8 |
| 576-thesis.md, lattice.md, 576-*.md | The lattice work (numerology REJECTED) | L2 |

## 7.2 The Traditions (tantraloka/, sanskritree/, blog/)

| Corpus | Contents | Feeds |
|---|---|---|
| tantraloka/texts-clean/ | Spandakārikā (4 commentaries), Doctrine of Vibration, Tantrāloka | L6 |
| tantraloka/notes/ | Proclus mapping, Ñāṇavīra comparison, My Big TOE, Egyptian–Tibetan death mapping, subtle body | L6, L8 |
| sanskritree/truth/ | COMPENDIUM, RASAANALYSIS, the whattheheckis originals, aperture specs, Shaw theurgy texts, subtle_body_formal.md, iamblichus_theurgy.md | L6, L7, L8 |
| blog/data/yogis/ | The yogi database (Swami Rama, Satyamurti, 50+ yogis, story/evidence scores) | Applications |
| blog/content/research-objects/ | 180 ROs (source extractions) | All |
| beings/ | Ra cosmology, Ecology of Souls, entity-density mapping | L8 |

## 7.3 The Datasets

| Dataset | Location | Use |
|---|---|---|
| neuSynth + neurodatasets | clean/neurodatasets/ | L5/L7 evidence (pending) |
| yogis.csv / yogis-master-list.md | blog/data/yogis/ | Yogi validation layer |

---

# PART 8: THE FRONTIER (what's next)

## 8.1 The 10 evidence GAPS (from TREE.md)

The research agenda, in priority order:
1. L3 collapse-as-experience (the central postulate)
2. L1 thermal time discrimination experiment
3. L7 identity vs correlation discrimination
4. L5 water Λ test (the decisive experiment)
5. L1 bearer-identification
6. L8 orchestration-law direct test
7. L7 CIMC finite-automaton test
8. L6 phenomenology→physics bridge (Chordonomicon)
9. L5 subtle-body homology
10. L8 survival claims (likely unfalsifiable — may be closed as N/A)

## 8.2 The confrontation backlog (top 5)

1. Dual-aspect monism (Atmanspacher) — the closest relative
2. Global Workspace Theory
3. Analytic idealism (Kastrup)
4. Predictive processing (own record)
5. Illusionism (the strongest challenge)

## 8.3 The unbuilt applications

1. **The myth** — a narrative where every mechanic is justified by the
   thesis (the user's vision; the "intuitive telling")
2. **The yogi validation layer** — Swami Rama (Menninger), Satyamurti
   (8-day burial), Babaji — explained by the architecture
3. **The Proclus/Iamblichus/subtle-body expansion** — the material
   exists, the integration doesn't
4. **The video pipeline** — skills exist, content doesn't

---

*Source Manual v1.0 — 2026-07-31. Canonical navigation document.
Update when the system changes. The thesis is under constant attack;
that's the point.*
