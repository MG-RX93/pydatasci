import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import warnings
import seaborn as sns
# Ignore all warnings
warnings.filterwarnings('ignore')

# Read the Parquet file
parquet_file = 'flow_execution_file.parquet'
full_df = pd.read_parquet(parquet_file)

# Print DataFrame
print("\nOriginal DataFrame:")
print(full_df)

# Sample dataset
df = full_df.sample(n=10000, random_state=1)

# Print DataFrame
print("\nSampled DataFrame:")
print(df)

# CPU Data Set
cpu_time_values = df['TOTAL_EXECUTION_TIME'].values

# Calculate the range for the bell curve
mean = round(np.mean(cpu_time_values),2)
print("\nMean of CPU TIME:")
print(mean)
std_dev = round(np.std(cpu_time_values),2)
print("\nStandard Deviation of CPU TIME:")
print(std_dev)
x_values = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)

# Generate the bell curve (Gaussian distribution)
bell_curve = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_values - mean) / std_dev) ** 2)

# Plotting Histogram
plt.figure(figsize=(12, 5))
plt.hist(df['TOTAL_EXECUTION_TIME'], bins=15, alpha=0.7)  
plt.title('Histogram of CPU_TIME Values')
plt.xlabel('CPU_TIME')
plt.ylabel('Frequency')

# Set y-axis to have more granular control
plt.ylim(0, 10000)  # Adjust these limits based on your data's range
plt.gca().yaxis.set_major_locator(ticker.LinearLocator(numticks=25))  # Adjust 'numticks' as desired

# Set x-axis to have more granular control
plt.xlim(-100, 7000) 
plt.gca().xaxis.set_major_locator(ticker.LinearLocator(numticks=15))

plt.show()

# Plotting Bell Curve
plt.figure(figsize=(12, 5))
plt.plot(x_values, bell_curve, label='Bell Curve')
plt.scatter(cpu_time_values, np.zeros_like(cpu_time_values), color='red', label='CPU_TIME Values') 

# Highlight the mean and standard deviations
plt.axvline(x=mean, color='k', linestyle='--', label='Mean')
plt.axvline(x=mean - std_dev, color='g', linestyle='--', label='Mean - 1 Std Dev')
plt.axvline(x=mean + std_dev, color='g', linestyle='--', label='Mean + 1 Std Dev')
plt.axvline(x=mean - 2*std_dev, color='y', linestyle='--', label='Mean - 2 Std Dev')
plt.axvline(x=mean + 2*std_dev, color='y', linestyle='--', label='Mean + 2 Std Dev')
plt.axvline(x=mean - 3*std_dev, color='r', linestyle='--', label='Mean - 3 Std Dev')
plt.axvline(x=mean + 3*std_dev, color='r', linestyle='--', label='Mean + 3 Std Dev')

plt.title('CPU_TIME Values on a Bell Curve')
plt.xlabel('Value')
plt.ylabel('Probability Density')

plt.xlim(-900, 7000)  # Adjust these limits based on your data's range
plt.gca().xaxis.set_major_locator(ticker.LinearLocator(numticks=25))

plt.legend()
plt.show()