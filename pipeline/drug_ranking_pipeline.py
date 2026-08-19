"""
AI-Based Drug Ranking Pipeline
AI-Assisted Molecular Docking for Repurposing Drugs Targeting NDM-1 in E. Coli
--------------------------------------------------------------------------------
This script loads the drug dataset with docking scores and pharmacokinetic
parameters, preprocesses it, and uses AutoGluon Tabular to automatically
rank the most promising drug candidates for NDM-1 inhibition.
"""

import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split

# ── 1. Load Dataset ──────────────────────────────────────────────────────────
df = pd.read_excel("data/AI-DATASETS-TABLE.xlsx")

# Clean column names
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

# Select important columns
important_cols = ["Drugs", "Docking score", "BBB permeability", "Absorption",
"Toxicity"]

print("\nImportant columns for analysis:\n")
print(df[important_cols].head(10))

# ── 2. Feature Engineering ────────────────────────────────────────────────────
# Drop drug name column for ML training (non-numeric)
features = df.drop(columns=["Drugs"])

# ── 3. Define Target ──────────────────────────────────────────────────────────
# Target: Docking score (lower = better binding affinity)
label = "Docking score"

# ── 4. Train-Test Split (80:20) ───────────────────────────────────────────────
train_data, test_data = train_test_split(features, test_size=0.2, random_state=42)

print(f"\nTraining samples : {len(train_data)}")
print(f"Testing samples  : {len(test_data)}")

# ── 5. AutoGluon Tabular Training ─────────────────────────────────────────────
predictor = TabularPredictor(
    label=label,
    path="results/autogluon_drug_ranking",
    eval_metric="rmse"
).fit(
    train_data=train_data,
    presets="best_quality",
    time_limit=600
)

# ── 6. Evaluate & Leaderboard ─────────────────────────────────────────────────
print("\n── Model Leaderboard ──")
leaderboard = predictor.leaderboard(test_data, silent=False)

print("\n── Feature Importance ──")
feature_importance = predictor.feature_importance(test_data)
print(feature_importance)

# ── 7. Rank Drug Candidates ───────────────────────────────────────────────────
# Predict docking scores for all compounds
all_features = df.drop(columns=["Drugs"])
df["Predicted_Docking_Score"] = predictor.predict(all_features)

# Rank by predicted docking score (ascending = better binding)
ranked_df = df[["Drugs", "Docking score", "Predicted_Docking_Score",
                "BBB permeability", "Absorption", "Toxicity"]].copy()
ranked_df = ranked_df.sort_values("Predicted_Docking_Score", ascending=True)
ranked_df["Rank"] = range(1, len(ranked_df) + 1)

print("\n── Top 10 Drug Candidates ──")
print(ranked_df.head(10))

# Save ranked results
ranked_df.to_csv("results/ranked_drug_candidates.csv", index=False)
print("\nRanked drug candidates saved to results/ranked_drug_candidates.csv")
