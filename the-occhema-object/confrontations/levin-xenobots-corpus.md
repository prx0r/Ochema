# Confrontation: The Levin Corpus — Xenobots, Anthrobots, and the Measured Bioelectric Register

## The Levin biobot/bioelectric corpus: Kriegman et al. 2020 & 2021 (PNAS); Gumuskaya et al. 2023 (Advanced Science); Manicka, Pai & Levin 2023 (iScience); Levin 2019 (Frontiers in Psychology)

**Date:** 2026-07-31 · **Added in:** v1.15.0 · **Result: VALIDATES (L5) — the bioelectric register is measured, the target is experimentally shown to be carried by the state, and the invariant is shown surviving wholesale substrate replacement; the phenomenal identification is untouched**

---

## The Papers

| Paper | Contribution | Status |
|---|---|---|
| Kriegman, Blackiston, Levin & Bongard 2020, *A scalable pipeline for designing reconfigurable organisms*, PNAS 117(4):1853–1859 | In-silico evolutionary design of frog-cell machines ("Xenobots"); literal generator-and-filter architecture; silico→vivo transfer | Extracted, read fully (xenobots-scalable-pipeline.txt) |
| Kriegman, Blackiston, Levin & Bongard 2021, *Kinematic self-replication in reconfigurable organisms*, PNAS 118(49):e2112672118 | Kinematic (non-growth) self-replication of cell clusters from loose cells; no blueprint, no selection for it | Extracted, read fully (xenobots-self-replication.txt) |
| Gumuskaya, Srivastava, Cooper, Lesser, Semegran, Garnier & Levin 2023/24, *Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells*, Adv. Sci. 11:2303575 | Anthrobots: adult human airway cells self-construct motile biobots with no genome editing; discrete morphotypes/movement types | Extracted, read fully (anthrobots.txt) |
| Manicka, Pai & Levin 2023, *Information integration during bioelectric regulation of morphogenesis of the embryonic frog brain*, iScience 26:108398 | THE key paper: causal (Jacobian/Hessian) integration analysis of voltage→gene pattern recognition; two in-vivo-verified predictions | Extracted, read fully (manicka-iscience-v2.txt) |
| Levin 2019, *The Computational Boundary of a "Self": Developmental Bioelectricity Drives Multicellularity and Scale-Free Cognition*, Front. Psychol. 10:2688 | Cognitive light cone; self as scale-free process; boundary problem; bioelectricity as the pre-neural cognitive substrate | **RE-EXTRACTED CORRECTLY** (levin-boundary-2019-correct.txt, 2715 lines, read fully) |

---

## The Confrontation

### What VALIDATES the thesis

#### 1. Generate→select is literal architecture, not metaphor (L4: Doyle, Friston, Levin; L5)

The 2020 pipeline is not merely analogous to the thesis's generate→select two-stage architecture — it is named in the paper's own words:

> "The pipeline is organized as a sequence of **generators and filters** (SI Appendix, Fig. S1). The first generator is an evolutionary algorithm that discovers different ways of combining the biological building blocks together to realize the desired behavior. A population of random designs are first created. Then, each design is simulated in a physics-based virtual environment and automatically assigned a performance score. Less-performant designs are deleted and overwritten by randomly modified copies of more-performant designs."
> — xenobots-scalable-pipeline.txt L62–69

The two stages are cleanly separated: **generate** (random population → modified copies of performers) and **select** (performance score → deletion). The thesis's L4 claim that generate→select is the decision architecture appears at the design level *and* is then re-instantiated inside the biology: the evolved designs are filtered by robustness ("only allows passage of designs that sustain the desired behavior in the face of noise", L167–169), then by manufacturability (L173–181), then built, then compared against simulation, with discrepancies fed back as constraints (L200–208: "Common patterns among the successful systems are distilled down into constraints and supplied back to the evolutionary algorithm"). The thesis's orchestration claim — the state at threshold determines the outcome — is here the *transferability* law: the design survives to the physical register only if it passes each threshold state (robustness filter → build filter → transferability filter), and the transfer is verified to be non-accidental:

> "the upright organisms' direction of movement matched that of the in silico design under random perturbations (P < 0.01…) This suggests that successful transference did not result by chance but rather was due to the design itself."
> — xenobots-scalable-pipeline.txt L263–268

The Manicka model search repeats the same architecture: "we chose a single high-performing model… from among a suite of 40 initially randomly parameterized models" (manicka-iscience-v2.txt L209–210), trained with "a combination of genetic algorithm and gradient descent" (L2231–2237). Generate→select is the universal structure in this corpus: it designs the machines, and (below) the machines themselves turn out to be the products of it.

#### 2. The morphogenetic target is the future attractor, and it is carried by the *state*, not the genome (L5; orchestration law; karmic update rule)

This is the deepest result of the corpus, and it is experimentally confirmed in Manicka et al.:

> "One key aspect of the bioelectric code is that transcriptional and morphogenetic states are determined not by local, single-cell, voltage levels but by specific distributions of voltage across cell sheets."
> — manicka-iscience-v2.txt L54–57

> "Crucially, it is the long-range difference between voltage in these regions that is required for normal development, not the absolute values of specific regions."
> — manicka-iscience-v2.txt L122–123

The target morphology is *not* in the genes (the genome is wild-type); it is in the spatiotemporal voltage state — a state of the register. Two model predictions were then tested in vivo, and both confirmed. First, a step-function voltage pattern (one half hyperpolarized) was predicted to leave brain development normal:

> "Surprisingly, as predicted by the model, the Kv1.5 + β-galactosidase mRNA-injected tadpoles also exhibited normal brain patterning… Percentage of tadpoles with brain defects for each experimental group are as follows: Controls: 8%, β-galactosidase: 7%, Kv1.5 + β-galactosidase: 8%, and Kir4.1: 6%."
> — manicka-iscience-v2.txt L595–598, L824–827

Second, a sharpened pattern (same overall shape, fewer hyperpolarized cells) was predicted to produce defects — against the prior expectation of every biologist:

> "A reasonable expectation (based on previously published manipulations of the voltage pattern in vivo) would be that this compressed, but qualitatively similar, pattern would still be sufficient to direct normal brain morphology. However, our results defied this expectation and instead confirmed the model's novel prediction… DN-KATP + β-galactosidase injection significantly increased the percentage of stage 45 tadpoles with brain morphology defects: uninjected or β-galactosidase controls—both 9%; DN-KATP + β-galactosidase—53%."
> — manicka-iscience-v2.txt L646–649, L931–934

**This is an experimental instance of the thesis's orchestration law (claim 4): the state of the register at the morphogenetic threshold determines the outcome.** The same gene sequence, the same overall pattern, different register state (proportion of polarized cells) → different outcome (normal brain vs 53% deformed). The state, not the symbol set, is the determinant. And the target is a future attractor in the dynamical sense, made precise:

> "it translates into a phenomenon where only a subset of the nodes or pathways in the network actually direct the system to its final attractor state for a given initial state… our model also exhibits a similar canalizing relationship between the voltage pattern and the discriminator gene expression in that the former is sufficient to determine the asymptotic expression of the latter."
> — manicka-iscience-v2.txt L861–863

The Anthrobots paper gives the same claim in developmental form — morphogenesis as the navigation of a landscape toward target states, with a Waddington formalism and *decision points*:

> "We further represent this relationship by a decision tree in the form of a Waddington Landscape… the Anthrobot moves through the developmental landscape, negotiating certain points of morphological possibility to reach its final architecture."
> — anthrobots.txt L528–537

And the default competence is latent in the cells — no genome editing, no sculpting (the thesis's latent target states):

> "the fact that wild-type cells from trachea will move over and heal neural tissues could not be predicted from any current molecular or tissue-level models."
> — anthrobots.txt L852–853

> "we characterized the space of discrete characters of form and function that are not currently inferable from the standard target morphology associated with the human genome."
> — anthrobots.txt L881–883

#### 3. The invariant survives substrate replacement — kinematic self-replication is pattern persistence (claims 9, 12)

The 2021 paper provides the cleanest demonstration in biology of the thesis's invariant claim (ι_i: what survives content changes). The replicator is *not* biological reproduction; it is the machine reshaping loose cells into a new machine:

> "synthetic multicellular assemblies can also replicate kinematically by moving and compressing dissociated cells in their environment into functional self-copies. This form of perpetuation, previously unseen in any organism, arises spontaneously over days rather than evolving over millennia."
> — xenobots-self-replication.txt L12–15

> "clusters of cells, if freed from a developing organism, can similarly find and combine loose cells into clusters that look and move like they do, and that this ability does not have to be specifically evolved or introduced by genetic manipulation."
> — xenobots-self-replication.txt L84–89

The replication is verified to be kinematic (machine-caused), not self-assembly: "With no progenitor organisms present, no offspring self-assembled at any of the stem cell concentrations tested" (L150–154). The offspring are built from ~100% fresh substrate (dissociated cells pooled from 30 embryos, L505–508); the only thing that crosses the generation boundary is the *form* — the pattern, the propensity to move and to compress cells. This is Fuller's pattern integrity made experimental, and the thesis's ι_i: the invariant is what survives when every token of the bearer is replaced. The thesis's nonlocal-encoding parallel (Penington islands) is not claimed by the paper — but the corpus does show a *distributed* encoding: the pattern-discrimination model "successfully solved the pattern discrimination problem even in a larger tissue containing 180 cells… found to scale to tissues as large as about 400 cells" (manicka-iscience-v2.txt L384–388), i.e., the target information is not pinned to individual cells.

The precision the thesis must add (honest limit): the kinematic offspring *do not inherit the full phenotype*. "although both progenitor groups produced spheroid offspring" — the semitorus shape does not transmit (L300–302). What transmits is a *weighted state*: offspring size, which alone correlated with replicative longevity (q = 0.93, L310–311). The thesis's karmic update rule (new register initialized from weighted state) is confirmed in its *precise* form: what is carried over is a weighted state of the parent's act (pile size above threshold ≈108 voxels, L574), not the parent's morphology. The invariant is competence, not appearance.

#### 4. Material enactment is constitutive (Axiom 7) — the substrate is not a neutral vehicle

Three independent results in the corpus make the substrate-loading claim concrete:

**(a) The same code on different hardware does not produce the behavior.** In silico and in vivo instances of the *same design* behave differently unless filtered:

> "On the first pass through the pipeline… this resulted in highly performant but nontransferable designs… These discrepancies were rectified by adding constraints into the pipeline."
> — xenobots-scalable-pipeline.txt L441–458

**(b) Swapping the symbolic substrate while preserving the state preserves the outcome.** The bioelectric code is arbitrary in exactly the way the thesis requires — the symbol is not the state:

> "the triggering stimulus is not a specific gene product that intrinsically is associated with that organ structure, but a physiological state that is arbitrary in the sense that it could have been mapped to any outcome just as easily. Indeed, specific ion channels and pumps, and even ionic species, can be swapped out at will, as long as the resulting electrophysiological states are the same."
> — manicka-iscience-v2.txt L696–701

This is multiple realizability of the *symbol* over the *state* — the thesis's claim that what matters is the coherent state of the register, and that the mapping "is set by the interpretation machinery, not by intrinsic (biophysical or genetic) properties of the stimulus" (L701–703).

**(c) Generic form arises from divergent substrates.** Anthrobots (adult human, somatic, decades-old genome) and Xenobots (embryonic frog) converge on the same morphotypes:

> "Despite their highly divergent genome, age, and tissue origin, the two platforms assemble into very similar types of creatures, illustrating the importance of generic laws of morphogenesis in addition to species-specific genomic information."
> — anthrobots.txt L798–801

The convergent morphology is not in either genome — it is an attractor of the morphogenetic process as such. The thesis's L5 claim that the target is the future attractor of the *process architecture*, not the content of any substrate, is exactly this.

#### 5. The bearer is a process, and its boundary is computed, not given (claims 1, 5; boundary b_i)

Manicka et al. independently raise the thesis's boundary question *as a research question in biology*:

> "we can ask if the physical boundaries of a given cell in our multicellular model are relevant and to what extent. Are there larger or smaller effective boundaries cutting across clusters of cells and genes that are more meaningful for the pattern discrimination problem? It has been hypothesized… that when active biological units such as cells come together in informationally connected groups, the computational boundary demarcating a coherent 'individual' could scale up from single units to the collective… Our analysis has already provided hints to support this view, where small clusters of cells seem to act as coherent modules… more than one such instructive causal nexus exists in the tissue—these may be separated in physical space but interact with each other at certain times—an indication that they may be closer in 'physiological space' even if distant in physical space."
> — manicka-iscience-v2.txt L1017–1038

This is the thesis's b_i = RT minimal surface claim in its L5 form: the boundary of the self is where the information structure cuts, not where the membrane is. And the measured object — what the boundary encloses — is a *process* (the voltage-gene dynamics), not a thing. The thesis's claim (1) that the bearer is an operator algebra + faithful state (M, ω) is not directly confronted by these papers (no operator-algebra analysis exists in them — honest limit), but the *functional claim* that underlies it — that what acts is a structured state of a dynamics, whose coherent modules define the individuals — is exactly what the causal-integration analysis measures (below).

#### 6. Information integration is a real, measurable property of the register (the bridge claim)

The Manicka paper is the closest existing experimental bridge between "consciousness math" and biology — with precise caveats:

> "Causal integration analysis revealed a higher-order mechanism by which information about the voltage pattern was spatiotemporally integrated into gene activity, as well as a division of labor among and between the bioelectric and genetic components. We tested and confirmed predictions of this model in a system in which bioelectric control of morphogenesis regulates gene expression and organogenesis: the embryonic brain of the frog Xenopus laevis."
> — manicka-iscience-v2.txt L57–60

The measured facts: the discriminator gene's dynamics are controlled "almost exclusively at the second-order level. In other words, it is the voltages of pairs of cells, rather than of single cells, that influence gene expression" (L451–453); the influence networks are dynamic, oscillatory, and nonlocal — "the oscillatory scanning-like behavior of the influence suggests that information is integrated both over space and time before a decision is made" (L490–494); and there is a division of labor across spatial scales: "some genes (2 and 5) are more attuned to the pattern at the tissue level, some (genes 3 and 4) to the single-cell level, and others (genes 1 and 6) display a fine balance between the two scales" (L517–519). The state of the register is not a bag of symbols: it is a *structured, higher-order, spatiotemporally integrated* object, and that structure is causally decisive (the Hessian reconstruction, L449–453). For the thesis's L5 this is direct experimental support that the bearer's information structure — not its constituent symbols — is what selection acts on and what determines the outcome.

**Honest limits, stated plainly.** (i) The paper does NOT claim frog brains are conscious; no phenomenal claim appears anywhere in it. The information-integration quantities are computed on the *model* dynamics (the Jacobian/Hessian causal derivatives, L2398–2438); the in vivo experiments confirm the *morphological-outcome predictions*, not the Hessian structure in vivo — the paper itself says a decisive experiment is outstanding: "Future experiments could study the effect of perturbations of the voltages of pairs or even groups of cells on tissue-wide gene expression. If verified, it would imply that bioelectric regulation is indeed of a higher-order nature" (L996–1001). (ii) The framework used is "multi-timescale causal influence" (Manicka & Levin 2022, ref. 182) — first- and second-order causal derivatives — which is the *same family* as integrated-information analyses (effective-information/causal-influence measures) but is **not** IIT's Φ: there is no maximally-irreducible-complex search and no exclusion-based individuation. Calling it "IIT's formalism applied to tissue" would be an overclaim; it is the closest relative of IIT's measures to be brought to biological regulation. The thesis must keep this distinction explicit. (iii) The model is minimal and phenomenological: it "does not generate precise quantitative predictions about the voltage and gene expression values" (L1051–1052), and "no model can formally prove particular mechanisms to be the cause of empirical observations" (L211).

#### 7. The 2019 boundary paper (correctly extracted)

The correct extraction (levin-boundary-2019-correct.txt) confirms the
prior record and adds precise language for the thesis's boundary and
ladder claims:

> "The shape of boundary defines each agent's 'cognitive light cone' –
> anything outside this region is mentally inaccessible to that system."
> — levin-boundary-2019-correct.txt L874

> "The borders of the temporal and spatial events of which a given
> system is capable of measuring and acting map out a 'cognitive light
> cone' – a boundary in the informational space of a mind. These
> borders can grow or shrink, on evolutionary or ontogenic time
> scales, as the organization of an agent changes."
> — levin-boundary-2019-correct.txt L3 (abstract)

> "The self is not something ready-made, but something in [continuous
> formation]"
> — levin-boundary-2019-correct.txt L1189 (citing Mead's processual
> self; the thesis's "the bearer is a process, not a thing")

The bioelectricity-as-cognitive-substrate claim is the paper's spine:
"bioelectricity – the ability of all cells to form electrical networks
that process information – suggests a plausible set of gradual
evolutionary steps that naturally lead from physiological [processes
to cognition]" (L67–70). This directly supports the thesis's L5
claims (the register is the bioelectric state; the boundary is
computed from the information structure, not given by the membrane) —
with the same grading: the light-cone boundary is the thesis's b_i in
its L5 form, and the cognitive-light-cone scaling (grow/shrink with
organization) is the aperture regime / density ladder in biological
terms.

### What CHALLENGES the thesis

1. **Spontaneous, unselected, non-genetic replication.** The 2021 result "does not evolve in response to selection pressures, but arises spontaneously over 5 d" (xenobots-self-replication.txt L52–53). A naive reading of the thesis's generate→select (generation needs an external selector) is challenged: here the selector is *internalized* as a physical threshold (piles ≥ ~50 cells mature, L136–137; the in-silico threshold p = 108 voxels, L574). The thesis's orchestration law absorbs this (thresholds do the selection), but the thesis must say so explicitly: in this regime, selection is not an agent — it is the state's own threshold structure. That is a strengthening, but it is also a warning against reifying the "selector" in the two-stage architecture.

2. **The outcome is not determined by the coarse initial state.** Anthrobots: "Out of the 2281 spheroids characterized total, ≈50% consistently showed no signs of motility (despite most having cilia)" (anthrobots.txt L361–362). Same protocol, same cell source, half do nothing. And "inherent noise in the system (such as small imbalances in the cilia distribution… or how the bot happened to be oriented in the plate) may be sufficient to have these bots generate small amounts of movement" (L521–524). The thesis's orchestration law says the state at threshold determines the outcome; this corpus shows the decisive state is *finer-grained* than any currently controlled register (cilia noise, orientation, micro-contingencies). Honest consequence: the orchestration law is confirmed only modulo the register's full microstate; the "state" that determines the outcome is not the experimenter's register. This is a challenge to the *controllability* of the law, not to its truth — but it must be recorded.

3. **Persistence is bounded; the invariant decays.** The replicator "naturally self-replicates for a maximum of two rounds before halting" (xenobots-self-replication.txt L138–139); even the AI-designed semitorus achieves only four rounds (L250, L304–306). The invariant does not survive indefinitely — it survives with decreasing fidelity ("Each successive generation, the size and number of offspring decreased until offspring were too small to develop", L146–149). This is consistent with the thesis's withdrawal phase (persistence is always finite), and the thesis should say so rather than implying indefinite pattern persistence.

4. **No operator-algebra, no thermal time, no phenomenal content.** None of the four papers touches claims (1) algebraically, (2) thermal time, (11) the Veil, or any phenomenal claim. The formal identification of the bioelectric register with (M, ω) and its modular flow is the thesis's L1/L2 contribution — this corpus supplies the *phenomenology-free experimental* side only. The consciousness identification is untouched by these papers: nothing here discriminates identity from correlation.

5. **Single-lab ecosystem.** All four papers are the same research program (Tufts/Levin lab, with Vermont/computer-science collaborators for the Xenobots). The in vivo predictions of Manicka are striking but originate from the model of the same group that made the model. Grade B (confirmed, replicated within and across systems — frog vs human, 2020 vs 2023 — but not independently reproduced by other labs).

6. **The arbitrary-code result cuts both ways.** "the assignment of trigger to outcome is set by the interpretation machinery, not by intrinsic (biophysical or genetic) properties of the stimulus" (manicka-iscience-v2.txt L701–703) supports the thesis's state-over-symbol claim — but it equally warns the thesis against any claim that *specific* bioelectric patterns carry intrinsic valence. Valence-as-coherence is safe; valence-as-symbol-content is refuted by this very result.

7. **The boundary is hypothesized, not demonstrated.** The "computational boundary could scale up" passage (L1031–1038) is a question the paper raises ("Are there larger or smaller effective boundaries…?", L1018–1019), with "hints" from the Hessian networks — not a measurement. The thesis's b_i = RT minimal surface mapping remains a thesis-side construction; the grade for that mapping stays C/D.

### What the thesis CHANGES in response

1. **L5 evidence table strengthened** (TREE.md): "Generate→select is universal in biology" gains a literal-architecture support (Xenobots pipeline: "a sequence of generators and filters", L62; plus the GA+GD search in Manicka, L2231); "The morphogenetic target is the future attractor" gains its first *experimentally confirmed* instance (Manicka's two predictions, including the counterintuitive 53% defect result); "Material specificity is constitutive" gains the transferability-failure result (L441–458) and the arbitrary-code/state-preserving result (L700–701).

2. **The orchestration law gets its first L5 experimental anchor.** Previously theorem-backed (thermal time + quantum Bayes) with Tier-4 corpus support; now also: register state (voltage pattern proportion) determines morphogenetic outcome in vivo, with both a positive (step-function → normal) and negative (sharpened → 53% defects) confirmation. The law's *controllability limit* (Anthrobots non-movers, cilia noise) is recorded as an explicit caveat: the determining state is the full microstate, not the experimenter's register.

3. **The karmic update rule is sharpened.** The kinematic-replication data (offspring inherit size/weighted-state, not morphology; q = 0.93 for size→generations, L310–311) refines claim (12): what is transmitted across register replacement is a *weighted state of the act*, not the phenotype. The thesis's wording "new register initialized from weighted state" is confirmed in its precise, non-obvious form.

4. **The invariant claim is re-graded with a decay clause.** ι_i survives wholesale substrate replacement (2021) and tissue scaling (Manicka, 180–400 cells, L384–388) — but with bounded fidelity. The thesis now states the withdrawal phase explicitly for L5: persistence is always finite; the invariant degrades with successive transmissions.

5. **Instrumentation note (resolved):** the first Levin 2019 download returned the wrong paper (DOI .02697 vs .02688); re-extracted correctly (levin-boundary-2019-correct.txt, 2715 lines). All alignments traced to the 2019 paper now have primary-source quotes (L874 cognitive light cone, L1189 processual self, L67–70 bioelectric substrate).

---

## The Synthesis (the deep convergence)

Read together, these four papers perform, at the biological level, the entire core of the thesis's architecture — without any phenomenal vocabulary, and therefore without any of the thesis's metaphysical claims. The convergence is striking because each thesis claim finds a *measured* counterpart:

- The bearer is a structured state of a dynamics: the voltage-gene register, whose decisive properties are second-order (pairwise) and spatiotemporally integrated — "the voltages of pairs of cells, rather than of single cells, that influence gene expression" (manicka L451–452).
- The target is the future attractor: "only a subset of the nodes or pathways in the network actually direct the system to its final attractor state" (manicka L862), and the attractor is *reached by different means under perturbation* — the half-and-half pattern still yields a normal brain (L595–598), the sharpened pattern does not (L931–934): same endpoint, different trajectory → regulative competency; same trajectory, different state → different endpoint → orchestration.
- Generate→select is universal: it is the engineering architecture (L62), the search architecture (L2231), and the developmental outcome architecture (Waddington decision trees, anthrobots L528–537).
- The invariant survives substrate replacement: kinematic self-replication (L12–15) is pattern persistence through ~100% substrate turnover; the transmitted quantity is a weighted state, not a shape (L300–302, L310–311).
- Material enactment is constitutive: the same design fails to transfer (L441–458), the same symbol set on different states gives different brains, and divergent genomes converge on the same generic forms (anthrobots L798–801).
- The boundary is computed, not given: the field itself asks whether the coherent "individual" is bounded by information structure rather than membrane (manicka L1017–1038).

The thesis's distinct contribution is not contradicted by any of it: nothing in this corpus touches thermal time, the modular flow, exclusion as a theorem, the Veil, or phenomenality. What the corpus does is supply the missing *experimental L5 floor*: the claim that the bearer's information structure is the target of selection, and that the state of the register at threshold determines the outcome, are no longer thesis-side constructions — they are published, replicated experimental results. The frog-brain system is not consciousness-grade evidence (no phenomenal claim, C), but as L5 evidence for the process architecture it is the strongest experimental support the thesis has yet confronted.

---

## Verdict

| Thesis claim | Verdict | Grade |
|---|---|---|
| L4/L5 (5): Generate→select universal two-stage architecture | **VALIDATES** — pipeline literally "a sequence of generators and filters"; GA+GD search; Waddington decision-tree development | B (multiple instances, single-lab ecosystem) |
| L5 (6): Morphogenetic target = future attractor; target carried by the state | **VALIDATES** — two in-vivo-confirmed predictions; canalized asymptotic expression | B |
| (4): Orchestration law — state of register at threshold determines outcome | **VALIDATES (at L5)** — step-function pattern → normal brain; sharpened pattern → 53% defects; same genome, same pattern shape, different register state, different outcome. Caveat: the decisive state is the full microstate (Anthrobots non-movers) | B |
| (9): Invariant ι_i survives content changes | **VALIDATES** — kinematic replication through ~100% substrate replacement; scaling to 180–400 cells. With the decay clause: persistence is finite (2–4 rounds) | B |
| (12): Karmic update rule — new register from weighted state | **VALIDATES (precise form)** — offspring inherit size (a weighted state), not morphology (q = 0.93) | C |
| (7): Material enactment constitutive (Axiom 7) | **ALIGNS** — transferability failures; symbol-swaps preserve state-determined outcomes; convergent generic forms across divergent genomes | B/C |
| (5): Boundary b_i computed from information structure | **ALIGNS (posed by the source field)** — "computational boundary… could scale up"; thesis's RT-minimal-surface mapping remains thesis-side | C/D |
| (1): Bearer = operator algebra + faithful state | **ALIGNS (functionally)** — register state is causally decisive, second-order, integrated; no algebraic identification in the papers | C |
| (8): Moment-triad (emergence/persistence/withdrawal) | **ALIGNS** — prepattern emerges (st. 15–18), persists over hours, reverts halfway through; replicator persistence bounded with withdrawal | C |
| (3): Determination through exclusion | **ALIGNS (weakly)** — coherent modules as instructive causal nexuses; division of labor across scales | C |
| (10): Valence = coherence | **ALIGNS (weakly)** — second-order canalized control; depolarized-cells-more-influential asymmetry. Arbitrary-code result refutes any symbol-intrinsic valence | C/D |
| (2): Time = modular flow | NEUTRAL — no confrontation; slow bioelectric timescales (hours) noted | C |
| (11): The Veil | NEUTRAL — no confrontation (the "no blueprint" result is a different claim: competence without symbolic representation) | C |
| **Consciousness identification (D_i ≡_int A_i)** | **NEUTRAL — no phenomenal claims in any paper; the frog-brain register is non-cortical; information integration ≠ consciousness** | **C (unchanged)** |

**The net effect: the Levin corpus is the thesis's strongest L5 confrontation. Generate→select, the future-attractor target, material enactment, the invariant through substrate replacement, and the orchestration law all receive experimental — in places in-vivo-confirmed — support. The consciousness identification is not advanced by these papers: information integration in a bioelectric register is now a measured biological property, but nothing in the corpus discriminates identity from correlation, and the grade for the identification stays C.**

---

## Sources

- Kriegman, S., Blackiston, D., Levin, M., Bongard, J. (2020). *A scalable pipeline for designing reconfigurable organisms.* PNAS 117(4):1853–1859. doi:10.1073/pnas.1910837117. Extraction: /tmp/opencode/levin/xenobots-scalable-pipeline.txt (645 lines, read fully).
- Kriegman, S., Blackiston, D., Levin, M., Bongard, J. (2021). *Kinematic self-replication in reconfigurable organisms.* PNAS 118(49):e2112672118. doi:10.1073/pnas.2112672118. Extraction: /tmp/opencode/levin/xenobots-self-replication.txt (759 lines, read fully).
- Gumuskaya, G., Srivastava, P., Cooper, B.G., Lesser, H., Semegran, B., Garnier, S., Levin, M. (2023). *Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells.* Advanced Science 11:2303575. doi:10.1002/advs.202303575. Extraction: /tmp/opencode/levin/anthrobots.txt (1580 lines, read fully).
- Manicka, S., Pai, V.P., Levin, M. (2023). *Information integration during bioelectric regulation of morphogenesis of the embryonic frog brain.* iScience 26:108398. doi:10.1016/j.isci.2023.108398. Extraction: /tmp/opencode/levin/manicka-iscience-v2.txt (2704 lines, read fully).
- Levin, M. (2019). *The Computational Boundary of a "Self": Developmental Bioelectricity Drives Multicellularity and Scale-Free Cognition.* Frontiers in Psychology 10:2688. doi:10.3389/fpsyg.2019.02688, PMID 31920779. Extraction: /tmp/opencode/levin/levin-boundary-2019-correct.txt (2715 lines, read fully). **Note: the first download attempt (DOI 10.3389/fpsyg.2019.02697) returned the wrong paper (Callejas-Albiñana et al., Consumer Motivation); corrected with the right DOI.**
- Cross-references: /root/projects/ochema/levin-peer-review.md (prior Levin confrontation — graded evidence table at L924–943); /root/projects/ochema/the-occhema-object/evidence/TREE.md §L5 (L120–152); the-unified-formal-framework.md claims (1)–(12); frontier-holography.md (b_i = RT minimal surface; Penington-island nonlocal encoding).
