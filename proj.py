# -*- coding: utf-8 -*-
""".
Created on Mon Jun 24 17:58:24 2019


Note: Right now, the Pvalue is 0.0 when it should proably be: 0 < pval < 1
      If any one can verify that answer or fix the issue then we are all set
      for the code part of the project. Thanks,
      - Miles



(Complete) 1. From our Blackboard Downloads Folder, download the ESS7e02_1.dta file and the ESS7_codebook.

(Complete) 2. The Dta extension is for Stata files and Pandas has a method for reading Dta files.

(Complete) 3. Create a program that reads the European Social Survey data you just downloaded and using gender
partition two sets: 1. Men; 2. Women.

(Complete) 4. Plot the histograms for weekend alcohol consumption for men and women. In the codebook, alcohol
consumption is in the Health and inequality set of variables, and the weekend series is named
alcwknd.

(Complete) 5. For weekend alcohol consumption, print the mean, variance and difference between the means for
men and women

(Complete) 6. Print the Cohen effect size between men and women regarding weekend alcohol consumption

(Complete) 7. Compare the weekend alcohol consumption relative frequency for the two datasets, men and women,
using probability mass function in a bar graph

(Complete) 8. Compare the weekend alcohol consumption relative frequency for the two datasets, men and women,,
using probability mass function using step functions

(Complete) 9. Plot to compare the cdfs the two sets (men and women) and explain the graph.

(Complete) 10. Get two data series from each of the sets: one for the weekend alcohol consumption for women and
one for men. Combine them into a tuple.

(Complete) 11. Instantiate your permutations test subclass using your data tuple. Use your instance to calculate the pvalue for the hypothesis that there is no difference between the means between the two groups.

(Complete) 12. Use the PlotCDF method of HypothesisTest to graph your test statistic’s CDF. 

Group 4:
    Miles Franklin
    Pranav Maniktala
    Nidhi Naik
    Omar Almazrouei
    Mohamed Alkindi
"""

import pandas as pd
#import math
import numpy as np
import thinkstats2
import thinkplot
import hypothesis

def main():
    df = readFile()
    df = cleanDF(df)
    men, women = makeFrames(df)
    makeHists(men, women)
    variousStats(men, women)
    makePMFs(men, women)
    makeCDFs(men, women)
    testStats(men, women)
    
def readFile(dat_file='ESS7e02_1.dta'):
    """Reads data
    
    dat_file: string file name

    returns: DataFrame
    """
    #Read Data
    df_CAT_TRUE = pd.read_stata(dat_file, columns=['alcwknd', 'icgndra', 'gndr'])
    df = pd.read_stata(dat_file, columns=['alcwknd', 'icgndra', 'gndr'], \
                       convert_categoricals=False) 
    print df_CAT_TRUE
    print df
    return df

def cleanDF(df):
    """ Gets rid of NAN data
    
    df: DataFrame

    returns: DataFrame
    """
    df = df[df.alcwknd!=6666]
    df = df[df.alcwknd!=7777]
    df = df[df.alcwknd!=8888]
    df = df[df.alcwknd!=9999]
    
    return df

def makeFrames(df):
    """Gender Partition

    df: DataFrame
    
    returns: DataFrames by gender
    """
    
    # if cconvert == False, then gndr is  1 or 2
    men = df[df.gndr == 1]
    women = df[df.gndr == 2]
    return men, women

def makeHists(men, women):
    """Prints Histograms of Mens and Womens drinking habits.

    men:   DataFrame
    women: DataFrame
        
    returns: N/A
    """
    
    # Men
    hist_men = thinkstats2.Hist(men.alcwknd, label='Men')
    thinkplot.Hist(hist_men, align='left')
    thinkplot.config(title='Mens Histogram',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 200.0, 0, 700.0])
    thinkplot.show()
    
    # Women
    hist_women = thinkstats2.Hist(women.alcwknd, label='Women')
    thinkplot.Hist(hist_women, align='left')
    thinkplot.config(title='Womens Histogram',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 200.0, 0, 700.0])
    thinkplot.show()

def makePMFs(men, women):
    """Prints PMFs of Mens and Womens drinking habits.

    men:   DataFrame
    women: DataFrame
        
    returns: N/A
    """
    
    # Mens Step Graphs
    pmf_men = thinkstats2.Pmf(men.alcwknd, label='Men')
    thinkplot.pmf(pmf_men, align='left')
    thinkplot.config(title='Mens PMF Step',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 125.0, 0, .2])
    thinkplot.show()
    
    # Women Step Graphs
    pmf_women = thinkstats2.Pmf(women.alcwknd, label='Women')
    thinkplot.pmf(pmf_women, align='left')
    thinkplot.config(title='Womens PMF Step',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 125.0, 0, .2])
    thinkplot.show()
    
    # Mens Bar Graphs
    pmf_men = thinkstats2.Pmf(men.alcwknd, label='Men')
    thinkplot.Hist(pmf_men, align='left')
    thinkplot.config(title='Mens PMF Bar',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 125.0, 0, .2])
    thinkplot.show()
    
    # Womens Bar Graphs
    pmf_women = thinkstats2.Pmf(women.alcwknd, label='Women')
    thinkplot.Hist(pmf_women, align='left')
    thinkplot.config(title='Womens PMF Bar',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 125.0, 0, .2])
    thinkplot.show()

def makeCDFs(men, women):
    """Prints CDFs of Mens and Womens drinking habits.

    men:   DataFrame
    women: DataFrame
        
    returns: N/A
    """
    
    cdf_men = thinkstats2.Cdf(men.alcwknd, label='Men')
    cdf_women = thinkstats2.Cdf(women.alcwknd, label='Women')
    
    thinkplot.Cdfs([cdf_men, cdf_women])
    thinkplot.config(title='CDFs',
                   xlabel='Grams',
                   ylabel='Frequency',
                   axis=[0, 125.0, 0, 1.1])
    thinkplot.show()
    
def variousStats(men, women):
    """ Prints some statistics of interest

    men:   DataFrame
    women: DataFrame
        
    returns: N/A
    """
    # Mean
    mean_men = men.alcwknd.mean()
    mean_women = women.alcwknd.mean()
    print "The average weekend consumption of alcohol (in grams)"
    print "Men:", mean_men
    print "Women:", mean_women
    print
    
    # Variance
    print "The variance in weekend consumption of alcohol (in grams)"
    print "Men:", men.alcwknd.var()
    print "Women:", women.alcwknd.var()
    print 
    
    # Diff. in means
    diff = mean_men - mean_women 
    print "Men, on average, drank", diff , "more grams than women."
    print 
    
    # Cohen Effect Size
    print "The Cohen effect size between men and women is", \
          thinkstats2.CohenEffectSize(men.alcwknd, women.alcwknd)
    print

def testStats(men, women):
    """ Prints some statistics of interest

    men:   DataFrame
    women: DataFrame
        
    returns: N/A
    """
    data = men.alcwknd.dropna(), women.alcwknd.dropna() #tuple
    ht = DiffMeansPermute(data)
    pvalue = ht.PValue()
    
    print "pvalue:", pvalue
    print "The diff between means:", ht.actual
    
    ht.PlotCdf()
    thinkplot.config(root='hypothesis1',
                   title='Permutation test',
                   xlabel='Difference in means (weeks)',
                   ylabel='CDF',
                   legend=False,
                   axis=[0, 2.6, 0, 1.1])
    thinkplot.show()

###############################################################################
###########################################################

class HypothesisTest(object):

    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)

    def PValue(self, iters=1000):
        self.test_stats = [self.TestStatistic(self.RunModel()) 
                           for _ in range(iters)]

        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count / iters

    def TestStatistic(self, data):
        raise UnimplementedMethodException()

    def MakeModel(self):
        pass

    def RunModel(self):
        raise UnimplementedMethodException()


# In[3]:


class DiffMeansPermute(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data

###########################################################
###############################################################################
    
    
main()