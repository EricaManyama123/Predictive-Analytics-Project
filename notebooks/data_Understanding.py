# %% 1.Importing the Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% 2. Loading the Dataset

df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Predictive Analytics Project\data\loan_approval_dataset.xls")
# Remove any hidden spaces from column names
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df.head()

# %% 3. Understanding the Dataset
# %% Dataset Shape
df.shape

# %% Dataset Information
df.info()
# %% Statistical Summary
df.describe()

# %% Column Names
df.columns.tolist()
# %% Unique Values
df.nunique()
# %% Categorical Variables
df.select_dtypes(include="object").columns
# %% Numerical Variables
df.select_dtypes(include="number").columns

# %% 4. Find Any Mess

# %% Missing Values
df.isnull().sum()
# %% Duplicate Records
df.duplicated().sum()
# %% Duplicate Records
df[df.duplicated()]
# %% Inconsistent Values
df["education"].value_counts()
# %% Inconsistent Values
df["self_employed"].value_counts()
# %% Cibil Score Min and Max
df["cibil_score"].min(), df["cibil_score"].max()

# %% 5.VISUALIZATIONS
# %% Loan Status Distribution
df["loan_status"].value_counts()
# %% Loan Status Distribution Visualization
sns.countplot(x="loan_status", data=df)
plt.title("Loan Approval Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applications")
plt.show()


# %% CIBIL score vs loan status
sns.boxplot(x="loan_status", y="cibil_score", data=df)
plt.title("CIBIL Score vs Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("CIBIL Score")
plt.show()
# Observation:The CIBIL score distribution shows potential outliers in both
# approved and rejected applications. These values will be investigated
# before deciding whether any treatment is necessary.


# %% income amount vs loan status
sns.boxplot(x="loan_status", y="income_annum", data=df)
plt.title("Applicant Income by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Annual Income")
plt.show()

# %% Loan Amount vs Loan Status
sns.boxplot(x="loan_status", y="loan_amount", data=df)
plt.title("Loan Amount by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Loan Amount")
plt.show()

# %% Education and Loan Approval
sns.countplot(x="education", hue="loan_status", data=df)
plt.title("Education and Loan Approval")
plt.xlabel("Education")
plt.ylabel("Number of Applications")
plt.show()
# Observation:
# The number of approved and rejected applications is fairly similar
# across Graduate and Not Graduate applicants. Education level does not
# show a strong difference in the approval counts in this dataset.

# %% Self-employment and loan approval
sns.countplot(x="self_employed", hue="loan_status", data=df)
plt.title("Self-employment and Loan Approval")
plt.xlabel("Self-employed")
plt.ylabel("Number of Applications")
plt.show()
# Observation:
# The approval and rejection counts are very similar for self-employed and non-self-employed applicants.
# Based on this visualization, self-employment does not show a large difference in loan approval counts.

# %% Correlation between numerical variables
corr = df[["cibil_score", "income_annum", "loan_amount"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation between Numerical Variables")
plt.show()

# %% Correlation between numerical variables (heatmap)
numeric_cols = df.select_dtypes(include="number").columns
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Numerical Variables")
plt.show()
# The correlation heatmap shows strong relationships between income, loan amount,
# and the different asset values. The strongest relationship is between annual income and loan amount (0.93).
#  CIBIL score, number of dependents, loan term, and loan ID have relatively weak correlations with the other numerical variables.
