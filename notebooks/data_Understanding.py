# %% 1.Importing the Libraries
import pandas as pd

# %% 2. Loading the Dataset

df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Predictive Analytics Project\data\loan_approval_dataset.xls")
# Remove any hidden spaces from column names
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df.head()
# %% 3. Dataset Shape
df.shape

# %% 4. Dataset Information
df.info()
# %% 5. Statistical Summary
df.describe()

# %% 6. Missing Values
df.isnull().sum()
# %% 7. Duplicate Records
df.duplicated().sum()

# %% 8. Column Names
df.columns.tolist()

# %% 9. Unique Values
df.nunique()
# %% 10. Categorical Variables
df.select_dtypes(include="object").columns
# %% 11. Numerical Variables
df.select_dtypes(include="number").columns
