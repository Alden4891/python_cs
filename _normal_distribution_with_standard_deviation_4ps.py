# Scenario: Beneficiary Compliance Monitoring

# Observation:
#    * On average, 2,400 beneficiaries are not compliant with the family development sessions every month due to absence.
#    * The total number of beneficiaries you are monitoring is 240,000.

# Objective:
#    * To visualize the distribution of non-compliant beneficiaries and predict how many may fall into different ranges of absences each month.

# Key Details:
#    * Mean absences (mu): 2,400 beneficiaries per month.
#    * Standard deviation (sigma): Let's assume a standard deviation of 400 beneficiaries based on historical data (this can be adjusted based on actual records).

# Questions You May Want to Answer:
#    1. How many beneficiaries are expected to be slightly above or below the average absence?
#       * Between 2,000 and 2,800 absences (within 1 standard deviation).
#    2. What percentage of beneficiaries are expected to have significantly higher absences (more than 3,200)?
#       * These beneficiaries might need more targeted interventions.
#    3. How rare are exceptionally low non-compliance rates (fewer than 1,600 beneficiaries)?
#       * This could indicate a highly compliant month.

# Explanation:
#    1. Mean (mu = 2400): Represents the average number of beneficiaries who are absent (2,400).
#    2. Standard deviation (sigma = 400): A spread of 400 beneficiaries indicates variability in non-compliance from month to month.
#    3. Filled areas: Show the probability of how many beneficiaries are expected to fall within each range of absences:
#       * 68% of months will have absences between 2,000 and 2,800 (within 1 standard deviation).
#       * 95% of months will have absences between 1,600 and 3,200 (within 2 standard deviations).
#       * 99.7% of months will have absences between 1,200 and 3,600 (within 3 standard deviations).

# Interpretation:
#    * Most months will have absences ranging between 2,000 and 2,800 beneficiaries.
#    * If absences are greater than 3,200 in a particular month, this would be considered a higher-than-usual non-compliance, possibly requiring intervention.
#    * Exceptionally low absence rates (fewer than 1,600 beneficiaries) would indicate very high compliance, which may be a signal of effective program implementation or external factors affecting compliance.


# Practical Use:
#    * Track trends in non-compliance across months.
#    * Predict future compliance levels and allocate resources for intervention based on the number of non-compliant beneficiaries.
#    * Identify outliers or months where absences are unusually high or low, prompting investigation into specific regions or events that may have caused a deviation in the trend.


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data for each month (non-compliant beneficiaries, including an outlier in January)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
non_compliant_beneficiaries = [3000, 2200, 2800, 2600, 2400, 2100, 2900, 2000, 3000, 1900, 2500, 2300]

# Calculate the mean and standard deviation of non-compliance
mu = np.mean(non_compliant_beneficiaries)
sigma = np.std(non_compliant_beneficiaries)

# Calculate the bounds for each standard deviation range, setting the lower bound to 0 if negative
one_std_lower, one_std_upper = max(mu - sigma, 0), mu + sigma
two_std_lower, two_std_upper = max(mu - 2*sigma, 0), mu + 2*sigma
three_std_lower, three_std_upper = max(mu - 3*sigma, 0), mu + 3*sigma

# Print the ranges for each standard deviation
print(f"68% of months will have absences between {one_std_lower:.0f} and {one_std_upper:.0f} (within 1 standard deviation).")
print(f"95% of months will have absences between {two_std_lower:.0f} and {two_std_upper:.0f} (within 2 standard deviations).")
print(f"99.7% of months will have absences between {three_std_lower:.0f} and {three_std_upper:.0f} (within 3 standard deviations).")

# Generate points for the normal distribution curve
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

# Create the figure and axis for the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# First plot: Normal Distribution Plot
ax1.plot(x, y, label='Beneficiary Non-Compliance Distribution', color='blue')

# Fill the areas for each standard deviation
ax1.fill_between(x, y, where=(x >= mu - sigma) & (x <= mu + sigma), color='red', alpha=0.5)
ax1.fill_between(x, y, where=(x >= mu - 2*sigma) & (x < mu - sigma), color='blue', alpha=0.5)
ax1.fill_between(x, y, where=(x > mu + sigma) & (x <= mu + 2*sigma), color='blue', alpha=0.5)
ax1.fill_between(x, y, where=(x >= mu - 3*sigma) & (x < mu - 2*sigma), color='lightgreen', alpha=0.5)
ax1.fill_between(x, y, where=(x > mu + 2*sigma) & (x <= mu + 3*sigma), color='lightgreen', alpha=0.5)

# Add vertical lines for each standard deviation
for i in range(-3, 4):
    ax1.axvline(mu + i*sigma, color='white', linestyle='--', alpha=0.8)

# Annotate the percentages
ax1.text(mu, 0.00001, '34.1%', horizontalalignment='center', fontsize=12)
ax1.text(mu - 1.5*sigma, 0.00001, '13.6%', horizontalalignment='center', fontsize=12)
ax1.text(mu + 1.5*sigma, 0.00001, '13.6%', horizontalalignment='center', fontsize=12)
ax1.text(mu - 2.5*sigma, 0.000005, '2.1%', horizontalalignment='center', fontsize=12)
ax1.text(mu + 2.5*sigma, 0.000005, '2.1%', horizontalalignment='center', fontsize=12)
ax1.text(mu - 3.5*sigma, 0.000002, '0.1%', horizontalalignment='center', fontsize=12)
ax1.text(mu + 3.5*sigma, 0.000002, '0.1%', horizontalalignment='center', fontsize=12)

# Label axes and title for the first plot
ax1.set_title('Distribution of Non-Compliant Beneficiaries in Family Development Sessions')
ax1.set_xlabel('Number of Non-Compliant Beneficiaries')
ax1.set_ylabel('Probability Density')

# Second plot: Bar chart for Monthly Non-Compliance
ax2.bar(months, non_compliant_beneficiaries, color='lightcoral', alpha=0.7)
ax2.axhline(y=mu, color='blue', linestyle='--', label=f'Average ({mu:.0f})')

# Label axes and title for the second plot
ax2.set_title('Monthly Non-Compliant Beneficiaries with Average Line')
ax2.set_xlabel('Month')
ax2.set_ylabel('Number of Non-Compliant Beneficiaries')

# Show the average value as a line
ax2.legend()

# Adjust the layout and show both plots
plt.tight_layout()
plt.show()
