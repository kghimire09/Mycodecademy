import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
vein_pack_lifespans = familiar.lifespans(package='vein')
tstat, pval = ttest_1samp(vein_pack_lifespans,71)
vein_pack_test = pval
if (pval < 0.05):
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print("The Vein Pack is Probably Good For You Somehow!")
artery_package_lifespan= familiar.lifespans(package='artery')
tstatistic, pval1 = ttest_ind(artery_package_lifespan, vein_pack_lifespans)
package_comparison_results = pval1
if pval1 < 0.05:
  print("The Artery Package guarentees even stronger results!")
else:
  print("The Artery Package is also a great product!")
iron_contingency_table = familiar.iron_counts_for_package()
iron_pvalue = chi2_contingency(iron_contingency_table)
if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!!")



    