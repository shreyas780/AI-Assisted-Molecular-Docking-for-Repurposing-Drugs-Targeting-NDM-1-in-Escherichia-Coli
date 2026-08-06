# AI-Assisted Molecular Docking for Repurposing Drugs Targeting NDM-1 in Escherichia Coli

An AI-assisted computational drug screening project aimed at identifying potential
drug candidates for repurposing against NDM-1 (New Delhi Metallo-beta-lactamase-1),
a key enzyme responsible for antibiotic resistance in Escherichia Coli, using
molecular docking and an AutoGluon Tabular-based drug ranking pipeline.

---

## Overview

NDM-1 is a metallo-beta-lactamase enzyme produced by certain strains of E. Coli
that confers resistance to nearly all beta-lactam antibiotics, making it a critical
target in the fight against antimicrobial resistance (AMR). This project combines
computational molecular docking with an AI-based ranking pipeline to screen
FDA-approved and investigational compounds for potential repurposing as NDM-1
inhibitors.

The project combined two approaches:
- **Molecular Docking** — protein-ligand interaction analysis using Schrödinger
  Maestro to screen compounds against the NDM-1 active site
- **AI Drug Ranking Pipeline** — AutoGluon Tabular used to rank and shortlist
  the most promising drug candidates based on docking scores and molecular
  properties

---

## Key Contributions

- Developed an AI-assisted computational drug screening framework targeting
  the NDM-1 enzyme in antibiotic-resistant E. Coli
- Performed molecular docking and protein-ligand interaction analysis using
  **Schrödinger Maestro**
- Screened and optimized **200+ FDA-approved and investigational compounds**,
  shortlisting drug candidates using **Lipinski's Rule of Five**
- Built an AI-based drug ranking pipeline using **Python** and
  **AutoGluon Tabular** to identify the most promising repurposing candidates

---

## Technical Breakdown

### Molecular Docking (Schrödinger Maestro)
The NDM-1 protein structure was prepared and optimized in Schrödinger Maestro.
Ligand structures for 200+ FDA-approved and investigational compounds were
retrieved, prepared, and docked against the NDM-1 active site using Glide
docking. Protein-ligand interaction analysis was performed to evaluate binding
affinity and interaction patterns.

### Lipinski's Rule of Five Filtering
Compounds were filtered using Lipinski's Rule of Five to shortlist drug-like
candidates with favorable oral bioavailability and pharmacokinetic properties,
reducing the compound pool to the most viable candidates.

### AI Drug Ranking Pipeline
An AutoGluon Tabular-based pipeline was built in Python to rank shortlisted
compounds based on docking scores, binding energy, and molecular descriptors.
AutoGluon automatically benchmarked multiple ML models to identify the
best-performing ranker for the dataset.

---

## Folder Structure

AI-Assisted-Molecular-Docking-for-Repurposing-Drugs-Targeting-NDM-1-in-Escherichia-Coli/
├── data/ # Compound datasets and docking input files
├── pipeline/ # AutoGluon Tabular drug ranking pipeline scripts
├── results/ # Docking scores, ranked compound lists, interaction analysis
├── media/ # Docking visualizations, interaction diagrams, screenshots
└── README.md


---

## Outcomes & Learnings

- Gained hands-on experience with computational drug discovery workflows,
  combining molecular docking with AI-based ranking
- Understood how Lipinski's Rule of Five filters drug-like compounds and why
  pharmacokinetic properties matter in early drug screening
- Developed cross-domain skills bridging bioinformatics, cheminformatics,
  and machine learning — relevant to computational biology and drug discovery
- This project demonstrated the potential of AI to accelerate drug repurposing
  pipelines for antibiotic resistance targets

---

## Disclaimer

This was an academic/personal computational biology project for learning purposes.
Results are based on in-silico screening only and have not been validated through
wet lab experiments or clinical trials.

---

## Tech / Tools Used

`Schrödinger Maestro` · `Python` · `AutoGluon Tabular` · `Molecular Docking` ·
`Lipinski's Rule of Five` · `Drug Repurposing` · `NDM-1` · `Antibiotic Resistance`