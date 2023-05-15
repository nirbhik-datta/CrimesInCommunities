# Overview

Social data often necessitates large amounts of preprocessing and data exploration to make plausible data driven inferences. In this project, we explore the utility of UCI's ML Repository "Crommunities and Crime" dataset in predicting crime indcidences. Given socioeconomic data from different communities compiled through Census Bureau data, we seek to predict the number of crime incidences per 100,000 in population for eight individual sub-categories of crime (arson, larcenies, murders, etc.)

The notebook is generally structured as the following:
* Pulling and parsing data from Amazon S3
* High level exploratory data analysis through data summaries and visualizations (seaborn, pandas)
* Data imputation for missing values using the MICE algorithm (Multiple Imputation by Chained Equations)
* Further feature and target transformations (PowerTransformer, PCA)
* Training and evaluation of an MLP implemented using Keras
* Comparison with Linear Regression models trained on individual crime types


In totality, we show the viability of using a Multivariate Principle Component Regression model in order to utilize the relationship of our target variables during the weigh updates in our training procedure. The utilization of multiple signals is especially pronounced when looking at crimes with lower number of incidences.

# Tableau Notebook Summarizing and Visualizing Dataset Statistics and Varialbe Relationships

https://public.tableau.com/app/profile/nirbhik.datta/viz/CrimesInCommunities/Dashboard1

