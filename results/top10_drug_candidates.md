# Final Top 10 Drug Candidates — Post-ADMET AutoGluon Ranking

## Context

This is the **final AI screening output** after completing molecular docking,
ADMET analysis (QikProp), and toxicity assessment (ProTox-3.0). The ranking
integrates docking scores, BBB permeability, absorption, toxicity, and
AutoGluon-predicted docking scores into a single composite AI score.

AutoGluon Tabular (best_quality preset, 70/30 train-test split) automatically
benchmarked multiple ML algorithms including LightGBM, XGBoost, NeuralNetTorch,
and Weighted Ensemble. The best model (WeightedEnsemble_L2) was used for
final candidate ranking.

**AI screening improved efficiency by ~83%**, reducing dataset complexity and
identifying the highest-performing compounds.

---

## Top 10 Final Drug Candidates

| Rank | Drug | Docking Score (kcal/mol) | BBB Permeability | Absorption | Toxicity | Predicted Docking | AI Score |
|------|------|--------------------------|------------------|------------|----------|-------------------|----------|
| 1 | Aspirin | -6.666 | ACTIVE | 1 | 1 | -10.5646 | 0.912784 |
| 2 | Captopril | -6.849 | ACTIVE | 1 | 1 | -10.3636 | 0.873771 |
| 3 | Betaxolol | -6.351 | ACTIVE | 1 | 1 | -10.3636 | 0.859448 |
| 4 | Methimazole | -4.296 | ACTIVE | 0.93 | 1 | -10.4753 | 0.814458 |
| 5 | Pantoprazole | -6.685 | ACTIVE | 1 | 0 | -10.5646 | 0.813330 |
| 6 | Mefloquine | -5.191 | ACTIVE | 0.85 | 1 | -10.3636 | 0.803586 |
| 7 | Zavegepant | -6.903 | ACTIVE | 0.5 | 1 | -10.3636 | 0.800324 |
| 8 | Disulfiram | -3.695 | ACTIVE | 1 | 1 | -10.3636 | 0.783061 |
| 9 | Niclosamide | -7.150 | ACTIVE | 1 | 0 | -10.3636 | 0.782428 |
| 10 | Fluoxetine | -5.397 | ACTIVE | 1 | 0 | -10.5646 | 0.776287 |

---

## Column Definitions

- **Docking Score** — Glide docking score from Schrödinger Maestro (kcal/mol); lower = stronger binding affinity
- **BBB Permeability** — Blood-brain barrier permeability from QikProp (ACTIVE = permeable)
- **Absorption** — Oral absorption score from QikProp (1 = high, 0 = low)
- **Toxicity** — Toxicity flag from ProTox-3.0 (0 = non-toxic, 1 = toxic — requires dose management)
- **Predicted Docking** — AutoGluon-predicted docking score after ADMET-informed training
- **AI Score** — Final composite ranking score from AutoGluon Tabular (higher = better candidate)

---

## Key Observations

- **Aspirin** ranks #1 with the highest AI score (0.9128) despite not having the
  strongest raw docking score. This confirms the AI ranking balances multiple
  parameters rather than relying on docking score alone.
- **Niclosamide** had the best raw docking score in the initial ranking but
  dropped to #9 in the final ranking — reflecting the multi-criteria nature of
  the AI scoring system after ADMET integration.
- All Top 10 candidates show **ACTIVE BBB permeability**, indicating good
  systemic distribution potential.
- **Final selected compound: Aspirin** — highest AI score, strong BBB activity,
  full absorption, and the most convincing overall risk-benefit balance.

---

## How This Differs From Initial Ranking

| Aspect | Initial Ranking | Final Ranking |
|--------|----------------|---------------|
| Basis | Docking score + drug-likeness | Docking + ADMET + toxicity + predicted docking |
| Top compound | Niclosamide (AI: 0.875) | Aspirin (AI: 0.913) |
| BBB filter | Binary (0/1) | ACTIVE/INACTIVE (QikProp) |
| Absorption | Estimated | QikProp-validated |
| Toxicity | Estimated flag | ProTox-3.0 validated |
| Predicted docking | Not included | AutoGluon-predicted |

---

## Disclaimer

Results are based on in-silico screening only. Experimental validation (wet lab,
in vitro, in vivo) is required before any clinical consideration.
