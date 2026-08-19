"""
Initial AI Drug Screening Pipeline — Pre-ADMET Ranking
AI-Assisted Molecular Docking for Repurposing Drugs Targeting NDM-1 in E. Coli
--------------------------------------------------------------------------------
This script performs the INITIAL AutoGluon Tabular screening of drug candidates
based on docking scores and drug-likeness properties, BEFORE ADMET analysis.

The pipeline:
1. Loads drug dataset with docking scores and molecular properties
2. Explores and preprocesses the data
3. Splits into 70% training / 30% testing (as used in the thesis)
4. Uses AutoGluon Tabular to benchmark multiple ML models
5. Ranks drug candidates by AI score
6. Outputs the initial ranked list (before ADMET refinement)

Results: See results/initial_ranking_pre_admet.md
"""

import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split

# ── 1. Load Dataset ──────────────────────────────────────────────────────────
df = pd.read_excel("data/AI-DATASETS-TABLE.xlsx")

# Clean column names (removes hidden spaces from Excel headers)
df.columns = df.columns.str.strip()

# Display first 10 rows
print("First 10 rows:\n")
print(df.head(10))

# Display column names
print("\nColumn names:\n")
print(df.columns.tolist())

# Display dataset info
print("\nDataset info:\n")
df.info()

# Select important columns for analysis
important_cols = ["Drugs", "Docking score", "BBB permeability", "Absorption",
                  "Toxicity"]

print("\nImportant columns for analysis:\n")
print(df[important_cols].head(10))

# ── 2. Preprocessing ─────────────────────────────────────────────────────────
# Drop drug name column for ML training (non-numeric identifier)
features = df.drop(columns=["Drugs"])

# Fill missing values with median
features = features.fillna(features.median(numeric_only=True))

# ── 3. Define Target ──────────────────────────────────────────────────────────
# Target: Docking score (lower = better binding affinity to NDM-1)
label = "Docking score"

# ── 4. Train-Test Split (70:30) ───────────────────────────────────────────────
# Note: Thesis used 70/30 split for initial screening
train_data, test_data = train_test_split(features, test_size=0.3, random_state=42)

print(f"\nTraining samples : {len(train_data)}")
print(f"Testing samples  : {len(test_data)}")

# ── 5. AutoGluon Tabular Training ─────────────────────────────────────────────
# AutoGluon benchmarks: LightGBM, XGBoost, Weighted Ensemble, etc.
# AUC-ROC validation: 0.9-1.0 = accurate, 0.5-0.7 = not accurate
predictor = TabularPredictor(
    label=label,
    path="results/autogluon_initial_screening",
    eval_metric="rmse"
).fit(
    train_data=train_data,
    presets="best_quality",   # trains multiple models + ensembles
    time_limit=600            # 10 minutes max training time
)

# ── 6. Evaluate & Leaderboard ─────────────────────────────────────────────────
print("\n── Model Leaderboard ──")
leaderboard = predictor.leaderboard(test_data, silent=False)

print("\n── Feature Importance ──")
feature_importance = predictor.feature_importance(test_data)
print(feature_importance)

# ── 7. Initial Ranking — All Drug Candidates ──────────────────────────────────
# Predict AI scores for all compounds
all_features = df.drop(columns=["Drugs"])
all_features = all_features.fillna(all_features.median(numeric_only=True))

df["AI_Score"] = predictor.predict(all_features)

# Rank by AI score (descending = better candidate)
ranked_df = df[["Drugs", "Docking score", "BBB permeability",
                "Absorption", "Toxicity", "AI_Score"]].copy()
ranked_df = ranked_df.sort_values("AI_Score", ascending=False)
ranked_df["Rank"] = range(1, len(ranked_df) + 1)

print("\n── Top 10 Initial Drug Candidates (Pre-ADMET) ──")
print(ranked_df.head(10))

# Save initial ranked results
ranked_df.to_csv("results/initial_ranked_candidates.csv", index=False)
print("\nInitial ranked candidates saved to results/initial_ranked_candidates.csv")
print("\nNOTE: These results are BEFORE ADMET analysis.")
print("Run drug_ranking_pipeline_final.py for post-ADMET refined ranking.")
