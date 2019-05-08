**Mod 2 Project Submission Please fill out:**

* Student name: John Naujoks & Laura E Shummon Maass
* Student pace: Full Time
* Scheduled project review date/time: 5/10/2019
* Instructor name: Miles Erickson, Greg Damico


## Project Overview
* The data set is based on Pitchfork review data. 
* The goal of the project is to answer 4 hypothesis statements about the data. 


### Hypothesis Test #1: Pop vs Electro Ratings

* **Null:** There is no statistically significant difference between the reviews for pop/R&B albums and electronic music albums.
* **Alternative:** The reviews for pop/R&B albums and electronic albums have a statistically significant difference between how they are reviewed, either positively or negatively.

* **Findings:**
* The distribution of ratings for both pop & electronic lined up very closely: **(insert image here)**
* The sample means were very close (less than a 0.16 difference) (# refers to rating)
* And the t-stat was below 0.37  (-0.3642)
* The p-value came to 0.7157 which far exceeded our threshold of 0.05
* We also did a bootstrap test and found:
    * Almost identical standard deviations for both samples
    * Almost identical 2.5 and 97.5 mean percentiles for both samples
* With all of the evidence above we accepted our null hypothesis that there is no statistically significant difference between the rating of pop/R&B and electronic albums.
**consider duplicating analysis for other genres**


### Hypothesis Test #2: Self-Released vs Label Ratings

* **Null:** There is no statistically significant difference between self-released album ratings and all others. 
* **Alternative:** Self-released albums have a statistically significant decrease in ratings compared to other labels.

* **Findings:**
* The distribution of ratings between self-released albums and albums with labels is not quite as closely lined up as pop and electro ratings, however they still overlap quite well: **(insert image here)**
* The sample means had a difference of 0.09 (# refers to rating)
* However, the t-stat was -1.44 **talk about the cutoff for our sample size and 0.05**
* Our p-value was also much lower at 0.1499. This still exceeds our threshold of 0.05
* With the evidence above, we accepted our null hypothesis that there is no statistically significant difference between self-released album ratings and albums with labels. 

### Hypothesis Test #3: Top Reviewer Ratings

* **Null Hypothesis:** There is no statistical difference between the top album reviewers and all others.
* **Alternative:** Top album reviewers have a statistically significant different in their review scores. 

* **Findings:**
* Viewed distributions of the top 5 reviewers (in terms of volume): **(insert image here)**
* As you can see 3 of the reviewers have very similar distributions, 2 stand out (Ian-orange and Mark-purple)
* Compared Ian to Joe AND compared Mark to Joe:
    * Ian to Joe:
        * Difference in means = 0.9
        * T-stat = 10.66
        * P-value = 0.000...3936
        * With the evidence above we rejected our null hypothesis and accept the alternative between 2 of the 5 top reviewers
    * Mark to Joe:
        * Difference in means = -0.46
        * T-stat = -4.92
        * P-value = 0.000...1075
        * With the evidence above we rejected our null hypothesis and accept the alternative between 2 of the 5 top reviewers
        * Note: Mark is an executive editor which may be the reason that his reviews are, on average, so much higher than others.
            * He may be handed albums from popular artists more often than other reviewers. 

### Hypothesis Test #4: Album Genres with Best and Worst Reviews 

* **Null:** In sampling the 500 worst and 500 best reviewed albums, there is no statistically significant difference in the genres each represents with regards to score. 
* **Alternative:** The 500 worst reviewed and 500 best reviewed albums have a statistically significant difference in the genres they have. 

* **Findings:**
* Conducted an ANOVA test on the 500 best & worst reviewed albums.
* We found trends amoung genres in the 500 best reviewed albums, but no trends emerged in the worst reviewed.
* In the 500 best reviewed albums, pop/r&b and rap had p-values of 0.0013 and 0.026 respectively. Rock had a p-value of 0.0546
* Based on the 3 lowest p-value genres, we reject the null for pop & rap, but not for rock (since it doesn't meet our 0.05 cutoff)
    * Pop & Rap have a statistically significant difference in showing up in the top 500 album reviews list. 


