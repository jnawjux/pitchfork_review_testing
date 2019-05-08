import psycopg2
import pandas as pd
import numpy as np
from  scipy.stats import ttest_ind
conn = psycopg2.connect("dbname=musicdatabase")

def query_to_df(query):
    """Taking an SQL query, executing it on the database, returning the results in a Pandas Dataframe"""
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    names = [description[0] for description in cur.description]
    return pd.DataFrame(results, columns=names)

def sample_size_calc(var1, var2, moe=1):
    """For Two Sample T-Test, find the best sample size, based on our two categories"""
    std_var1 = var1.std()
    std_var2 = var2.std()
    count_var1 = len(var1)
    count_var2 = len(var2)

    std_p = (( (count_var1-1) * (std_var1**2) ) + ( (count_var2-1) * (std_var2**2) )) / (count_var1 + count_var2 - 2)
    return 2*( ((1.96 * std_p)/moe)**2 )


def bootstrap_mean_stats(array, sample_size=0, n_tests=100, low_p=2.5, high_p=97.5):
    """Take a sample array, preferred size of bootstrap sample, and number of tests to return statistics
    for the sample mean, including standard deviation and percentiles around mean"""
    #samples = []
    bootstrap_sample_means = np.zeros(n_tests)

    for i in range(n_tests):
        bootstrap_sample = np.random.choice(array, size=sample_size, replace=True)
        #samples.append(bootstrap_sample)
        bootstrap_sample_means[i] = bootstrap_sample.mean()

    std = round(bootstrap_sample_means.std(), 4)
    low_p = round(np.percentile(a=bootstrap_sample_means, q=low_p), 4)
    high_p = round(np.percentile(a=bootstrap_sample_means, q=high_p), 4)
    return std, low_p, high_p

def two_sample_ttest_stats(series1, series2):
    """Gives us the means for each Series and performs a two sample T-Test on them and returns the statistics"""
    print('Sample 1 Review Mean: ', series1.mean())
    print('Sampe 2 Review Mean: ', series2.mean())
    print('Difference: ', series1.mean() - series2.mean())
    t_stat, p_val = ttest_ind(series1,series2)
    print(f"T-Statistic: {t_stat}\nP-Value: {p_val}")