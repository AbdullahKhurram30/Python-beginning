import scipy
from scipy import stats

#Geometric Distribution
p = 0.3
n = 2
print("Probability of first success on the",n,"th trial:",stats.geom.pmf(n,p),"\n")

#Binomial Distribution
p = 0.3
n = 100
k = 50
print("Probability of ",k,"successes in",n,"trials:",stats.binom.pmf(k,n,p))

#formula 3.30
x = ((1 - 0.3) ** (2 - 1)) * (p)
print(x)