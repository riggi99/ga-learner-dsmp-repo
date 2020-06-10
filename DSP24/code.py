# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
total=(len(df))
#Calculate the probability p(A)for the event that fico credit score is greater than 700
pa=np.sum(df['fico'] > 700)

p_a=pa/total
print(p_a)

#Calculate the probabilityp(B) for the event that purpose == 'debt_consolation'
pb=np.sum(df['purpose'] == 'debt_consolidation')

p_b=pb/total
print(p_b)

df1=df[df['purpose']=='debt_consolidation']
total1=len(df1)

pa1=np.sum(df1['fico'] > 700)
p_a_b=pa1/total1
print(p_a_b)

result=p_a_b == p_a

print(result)
# code ends here


# --------------
# code starts here
prob_lp=np.sum(df['paid.back.loan'] == 'Yes')/total

prob_cs=np.sum(df['credit.policy']=='Yes')/total
print(prob_cs)

new_df=df[df['paid.back.loan']=='Yes']
total2=len(new_df)
prob_pd_cs=np.sum(new_df['credit.policy']=='Yes')/total2

bayes=(prob_pd_cs*prob_lp)/prob_cs

print(bayes)
# code ends here


# --------------
# code starts here
df1=df[df['paid.back.loan']=='No']

df1.purpose.value_counts(normalize=True).plot(kind='bar')
# code ends here


# --------------
# Calculate median 
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()


# histogram for installment
df['installment'].hist(normed = True, bins=50)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')

plt.show()

#histogram for log anual income
df['log.annual.inc'].hist(normed = True, bins=50)
plt.show()


