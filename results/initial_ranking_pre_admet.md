# Initial Drug Ranking — Pre-ADMET AutoGluon Screening

## Context

This is the **initial AI screening output** from AutoGluon Tabular, performed
**before** ADMET analysis and toxicity assessment. At this stage, compounds were
ranked based on docking scores, BBB permeability, absorption, and toxicity flags
derived from molecular docking results only.

AutoGluon Tabular was trained on a 70/30 train-test split and benchmarked multiple
ML algorithms including LightGBM, XGBoost, and Weighted Ensemble. Models were
validated using AUC-ROC (0.9–1.0 = accurate, 0.5–0.7 = not accurate).

---

## Initial Ranking — All 53 Screened Compounds

| Rank | Drug Name | Docking Score (kcal/mol) | BBB Permeability | Absorption | Toxicity | AI Score |
|------|-----------|--------------------------|------------------|------------|----------|----------|
| 1 | Niclosamide | -7.15 | 1 | 1 | 0 | 0.874978 |
| 2 | Pantoprazole | -6.685 | 1 | 1 | 0 | 0.844888 |
| 3 | Pentamidine | -7.801 | 1 | 0.5 | 0 | 0.817105 |
| 4 | Verapamil | -5.965 | 1 | 1 | 0 | 0.798296 |
| 5 | Albendazole | -5.79 | 1 | 1 | 0 | 0.786972 |
| 6 | Fluoxetine | -5.397 | 1 | 1 | 0 | 0.761540 |
| 7 | Chlorpromazine | -5.313 | 1 | 1 | 0 | 0.756104 |
| 8 | Captopril | -6.849 | 1 | 1 | 1 | 0.755500 |
| 9 | Imipenem | -6.817 | 1 | - | 0 | 0.753430 |
| 10 | Aspirin | -6.666 | 1 | 1 | 1 | 0.743658 |
| 11 | Auranofin | - | 1 | - | 0 | 0.741588 |
| 12 | Betaxolol | -6.351 | 1 | 1 | 1 | 0.723274 |
| 13 | Risedronate | -7.711 | 1 | 0 | 0 | 0.711281 |
| 14 | Methotrexate | -8.346 | 0 | 1 | 0 | 0.702373 |
| 15 | Zidovudine | -5.411 | 1 | 0.5 | 0 | 0.662446 |
| 16 | Zavegepant | -6.903 | 1 | 0.5 | 1 | 0.658995 |
| 17 | Fluorouracil | -6.634 | 1 | 0.5 | 1 | 0.641588 |
| 18 | Cefiderocol | -8.709 | 0 | - | 0 | 0.625863 |
| 19 | Mefloquine | -5.191 | 1 | 0.85 | 1 | 0.618210 |
| 20 | Ceftazidime | -7.636 | 0 | 0.8 | 0 | 0.616428 |
| 21 | Nitazoxanide | -3.152 | 1 | 1 | 0 | 0.616264 |
| 22 | Methimazole | -4.296 | 1 | 0.93 | 1 | 0.576293 |
| 23 | Cefuroxime | -7.676 | 0 | 0.5 | 0 | 0.559016 |
| 24 | Disulfiram | -3.695 | 1 | 1 | 1 | 0.551402 |
| 25 | Fosfomycin | -7.505 | 0 | - | 0 | 0.547951 |
| 26 | Tucatinib | -6.031 | 1 | 0 | 1 | 0.502567 |
| 27 | Cefoxitin | -8.204 | 0 | - | 1 | 0.493184 |
| 28 | Dimercaprol | -4.242 | 1 | 0 | 0 | 0.486799 |
| 29 | Atogepant | -3.895 | 1 | 0 | 0 | 0.464344 |
| 30 | Cefepime | -7.726 | 0 | 0 | 0 | 0.462252 |
| 31 | Ubrogepant | -2.128 | 1 | 1 | 1 | 0.450000 |
| 31 | Ceftriaxone | -9.082 | 0 | 0 | 1 | 0.450000 |
| 32 | Fendiline | -4.446 | 0 | 1 | 0 | 0.450000 |
| 33 | Ciprofloxacin | -6.734 | 0 | 0.7 | 1 | 0.438059 |
| 34 | Vaborbactam | -7.301 | 0 | - | 1 | 0.434750 |
| 35 | Ticarcillin | -7.16 | 0 | - | 1 | 0.425626 |
| 35 | Doripenem | -7.16 | 0 | - | 1 | 0.425626 |
| 36 | Cefotaxime | -7.139 | 0 | - | 1 | 0.424267 |
| 37 | Piperacillin | -8.505 | 0 | 0 | 1 | 0.412662 |
| 38 | Aztreonam | -6.722 | 0 | 0 | 0 | 0.397282 |
| 39 | Rifampicin | - | 0 | - | 1 | 0.391588 |
| 40 | Carbenicillin | -6.601 | 0 | - | 1 | 0.389452 |
| 41 | Ertapenem | -8.114 | 0 | 0 | 1 | 0.387360 |
| 42 | Ampicillin | -6.373 | 0 | 0.5 | 1 | 0.374698 |
| 43 | Amoxicillin | -5.919 | 0 | 0.6 | 1 | 0.365319 |
| 44 | Nitrofurantoin | -6.219 | - | - | - | 0.364733 |
| 45 | Meropenem | -7.449 | 0 | 0 | 1 | 0.344327 |
| 46 | Amikacin | -7.158 | 0 | 0 | 1 | 0.325496 |
| 47 | Celecoxib | -4.224 | 0 | 0.4 | 0 | 0.315634 |
| 48 | Adapalene | -5.073 | 0 | 0 | 0 | 0.290574 |
| 49 | Sulbactam | -6.069 | 0 | 0 | 1 | 0.255026 |
| 50 | Gentamicin | -5.856 | 0 | 0 | 1 | 0.241242 |
| 51 | Loperamide | -5.114 | 0 | 0 | 1 | 0.193227 |
| 52 | Clofazimine | -3.237 | 0 | 0 | 0 | 0.171764 |
| 53 | Ivermectin | -2.3 | - | 0 | - | 0.011130 |

---

## Notes

- 7 compounds from the original 60 were excluded due to failed docking, poor data
  quality, or insufficient molecular descriptors for AI scoring
- BBB permeability: 1 = permeable, 0 = not permeable
- Absorption: 1 = high, 0 = low, 0.5/0.85/0.93 = partial
- Toxicity: 0 = non-toxic, 1 = toxic
- AI Score: composite AutoGluon ranking score (higher = better candidate)
- This ranking was performed **before** ADMET and toxicity refinement
- The final ranking (see `top10_drug_candidates.md`) reflects post-ADMET analysis
