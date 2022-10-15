<p align="center"> 
  <img src="images/banner.png" alt="Banner">
</p>

In this project, I have attempted to analyze the retail sales dataset of Rossmann stores and build a predictive model to forecast the sales over the next 6 weeks. No personal information of customer is provided in this dataset.

## :floppy_disk: Project Files Description</h2>

<p>This project contains an executable iPython Notebook and a presentation as follows:</p>
<h4>Executable Files:</h4>
<ul>
  <li><b>Rossmann_Sales_Prediction_Capstone_Project.ipynb</b> - Google Colab notebook containing data summary, exploration, visualisations, feature engineering, modelling, performance evaluation and conclusion.</li>
</ul>

<h4>Documentation:</h4>
<ul>
  <li><b>Presentation PDF - Supervised Machine Learning - Regression - Rossmann Retail Sales - Capstone Project.pdf</b> - Presentation slideshow of the project.</li>
</ul>

<h4>Source Directory:</h4>
<ul>
  <li><b>Data & Resources.zip</b> - Includes sales data and store data for various Rossmann stores.</li>
</ul>

## :book: Problem Statement

Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied.
Two datasets are given: one with store data and the other with historical sales data of 1115 stores from January 2013 to July 2015. The main objective is to understand existing data and after identifying the key factors that will predict future sales, a predictive model will be built for making forecasts about future sales.

## :book: Approach

1.	Understanding the business task.
2.	Import relevant libraries and define useful functions.
3.	Reading data from files given.
4.	Data pre-processing, which involves inspection of both datasets and data cleaning.
5.	Exploratory data analysis, to find which factors affect sales and how they affect it.
6.	Feature engineering, to prepare data for modelling.
7.	Modelling data and comparing the models to find out most suitable one for forecasting.
8.	Conclusion and recommendations to boost sales.

## :book: Exploratory Data Analysis

The following insights were gained from EDA:
<li>Mondays have most sales since most of the Sundays are closed.</li>
<li>Promotions seem to have a significant effect on sales but not for the number of customers. It is advisable to spend more on promos to get higher returns.</li>
<li>Store type b has higher sales and customers per store than other store types. More Store type b must be opened.</li>
<li>Assortment b is available only at store type b and it has more sales and customers than any other assortment. More assortment b must be stocked to meet the demands of customers.</li>
<li>Weekly sales and customers peak at the mid-December. It may be guessed that people buy drugs in advance just before the shops close for the holiday season.</li>

## :book: Modelling

<img src="images/Result_light.png" alt="Result">

## 📘: Conclusion

The following conclusions were drawn from Modelling:
<li>The model built using XGBoost algorithm gives unusually high accuracy. This may lead to overfitting. Therefore, it is advisable to not use this model.</li>
<li>Among the remaining, the model built using random forest algorithm is the most accurate one. This can be attributed to higher number of categorical features in the data.</li>
<li>If model interpretability is more important than accuracy, model built using decision tree algorithm should be chosen over the one using random forest algorithm. Since the difference between accuracy of these two models is less than 1%, there won't be a large difference in the result.</li>
<li>Decision tree based algorithms are slightly more accurate than linear regression based algorithms. Decision tree based algorithm gives an accuracy of ~93% while linear regression based algorithms given ~50%.</li>

## :scroll: Credits

Midhun R | Avid Learner | Data Analyst | Data Scientist | Machine Learning Enthusiast
<p> <i> Contact me for Data Science Project Collaborations</i></p>


[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/connectmidhunr/)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/connect-midhunr/)
[![Medium Badge](https://img.shields.io/badge/Medium-1DA1F2?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@connect.midhunr/)
[![Resume Badge](https://img.shields.io/badge/resume-0077B5?style=for-the-badge&logo=resume&logoColor=white)](https://drive.google.com/file/d/1Bho0SK8U3PMCK5UEyVEYnrNM9IYUUzcV/view?usp=sharing)

## :books: References
<ul>
  <li><p>GeeksforGeeks, 'Feature Encoding Techniques – Machine Learning'. [Online].</p>
      <p>Available: https://www.geeksforgeeks.org/feature-encoding-techniques-machine-learning/</p>
  </li>
  <li><p>Medium, 'Which evaluation metric should you choose for evaluating your Classification and Regression models?'. [Online].</p>
      <p>Available: https://medium.com/almabetter/which-evaluation-metric-should-you-choose-for-evaluating-your-classification-and-regression-models-1df8237f9a24</p>
  </li>
  <li><p>Analytics Vidhya, 'Decision Tree Algorithm – A Complete Guide'. [Online].</p>
      <p>Available: https://www.analyticsvidhya.com/blog/2021/08/decision-tree-algorithm/</p>
  </li>
</ul>
