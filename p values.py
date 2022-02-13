# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
#levels of cholestrol for a person with heart disease
chol_hd = yes_hd.chol
chol_hd_mean = np.mean(chol_hd)

# one sided t-test for person with heart disease of having average cholestrol level significantly more than 240
tstst, pval=ttest_1samp(chol_hd, 240 )
print(pval/2)
#dividing by 2 gives one sided p value

# since p value is 0.003 and less than our significance threshold 0.05 we conclude our null hypothesis to be wrong and the average cholestrol level of person with a heart disease isnt significantly greater than 240.

###########################################

# p value test to find average cholestrol level for sample who do not have heart disease

chol_hd_no = no_hd.chol
chol_hd_no_mean = np.mean(chol_hd_no)

tstst, pval=ttest_1samp(chol_hd_no, 240 )
print(pval/2)

# here p value is greater than our significance threshold therefore we can reasonably conclude that average cholestrol level for a person without heart disease is greater than 240.

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = len(heart.fbs[heart.fbs==1])
print(num_highfbs_patients)
print(num_patients*0.08)
from scipy.stats import binom_test

p_value = binom_test(num_highfbs_patients, num_patients, 0.08, alternative="greater")

print(p_value)

# here p value is less than significance threshold of 0.05 so we can safely assume that the sample was taken from a population having more than 8% of peope with fasting blood sugar > 120mg/dl
