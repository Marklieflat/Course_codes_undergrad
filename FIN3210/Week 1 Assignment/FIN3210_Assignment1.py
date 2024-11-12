import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm


# Load and preprocess and check the data
data = pd.read_csv('FIN3210 Week 1 Data.csv', encoding='gbk')
df = data[['age','gender','instalments_amount','nominalrates','tencentscore','highcontact20s','deal','default']].copy()
df['gender'] = df['gender'].astype('int')
df['default'] = np.where(df['default'] == False, 0, df['default'])
df['default'] = np.where(df['default'] == True, 1, df['default'])
df['default'] = np.where(df['default'] == 'NaN', np.nan, df['default'])
df['highcontact20s'] = df['highcontact20s'].astype('int')
df['default'] = df['default'].astype('Int64')

# Check missing values
print(df.isna().sum())

'''
Q1.Present a table of summary statistics for the key variables including the borrowers' age, 
    gender, loan amount, interest rate, credit scores, a dummy whether the borrower has a frequent contact, 
    approval dummy, and delinquency dummy
'''
print(df.describe().T)

# Take natural log and run the following regression
df['log_amount'] = df['instalments_amount'].apply(np.log)
df['log_tencentscore'] = df['tencentscore'].apply(np.log)

"""
Q2. Perform a logit regression and examine the relation between the delinquency likelihood and credit scores
"""
df1 = df.dropna().copy()
X = df1[['age','gender','log_amount','nominalrates','log_tencentscore','highcontact20s']]
y = df1[['default']].astype('int')
X = sm.add_constant(X)
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

"""
Q3. Perform a logit regression and examine the relation between the loan approval likelihood and credit scores
"""
df1 = df[df['nominalrates'].notna()].copy()
X = df1[['age','gender','log_amount','nominalrates','log_tencentscore','highcontact20s']]
y = df1[['deal']].astype('int')
X = sm.add_constant(X)
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

"""
Q4. Perform a logit regression and examine the relation between the loan approval likelihood and the dummy 
    whether the borrower has a frequent contact
"""
df1 = df[df['nominalrates'].notna()].copy()
X = df1[['age','gender','log_amount','nominalrates','log_tencentscore','highcontact20s']]
y = df1[['deal']].astype('int')
X = sm.add_constant(X)
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())