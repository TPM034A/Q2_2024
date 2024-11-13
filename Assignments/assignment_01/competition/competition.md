
# Competition in Machine learning for socio-technical systems (TPM034a)

Welcome to the technical guidelines for the competition in Machine Learning for Socio-technical Systems (TMP034a). Assignment 01 includes an internal competition in pedicting `bike_speed`. For doing so, you have to train and predicts the bike speed given the dataset you have been working in this assigment. We have prepare the dataset in a slight different format, bu the data is the same as the `first_campaign.gpkg`.

In this competition, you have access to two data files in CSV format: 
- (1) **train.csv**: This data file includes everything. The dependent variable `bike_speed`, many explanatory variables (as you discuvered in the assignment), and a `ROW_ID` column. The latter is just a unique identification for the row.
- (2) **predict.csv**: This data file has the exact same format as *train.csv*, but the `bike_speed` values where removed (i.e., the column is filled with NaN values).

**==================> [DOWNLOAD FILES](https://github.com/TPM034A/Q2_2024/raw/refs/heads/main/Assignments/assignment_01/competition/train_predict_files.zip) <==================**

**The competition closes: 25-11-2024 9:00 am**

You have to use the data provided in **train.csv** to train a model that can predict the `bike_speed`. Then, you have to use this model to predict the `bike_speed` in the **predict.csv** file and fill-in the `bike_speed` column with your predictions. The evaluation metric will be the mean squared error ([RMSE](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_squared_error.html)) between your prediction and the true bike speed. It is very important that you provide a prediction for all rows in the **predict.csv**. If you do not provide a prediction, the submission is not considered.

This competition can give you up to 0.5 grading BONUS points in the final grade of the assignment 01. The Bonus obtained will be based on the ranking of the RMSE of your predictions, and the ranking position will be based on the RMSE of the predictions in the **predict.csv** file. The RMSE is calculated using the true values of the `bike_speed` of the **predict.csv** file. The top 10 participants will receive Bonus grading points according to the following table:

| Rank | Bonus |
|------|-------|
| 1    | 0.5   |
| 2    | 0.45  |
| 3    | 0.4   |
| 4    | 0.35  |
| 5    | 0.3   |
| 6    | 0.25  |
| 7    | 0.2   |
| 8    | 0.15  |
| 9    | 0.1   |
| 10   | 0.05  |

The competiton have a web interface where you can submit your predictions and check the ranking. The web interface is available at: [https://class-competitor.tpm.tudelft.nl](https://class-competitor.tpm.tudelft.nl). Please read carefully the technical guidelines below to understand how to submit your predictions.

## Technical Guidelines

1. **Data Files**: You have access to two data files in CSV ([DOWNLOAD](https://github.com/TPM034A/Q2_2024/raw/refs/heads/main/Assignments/assignment_01/competition/train_predict_files.zip))
    - (1) **train.csv**: This data file includes everything. The dependent variable `bike_speed`, many explanatory variables (as you discuvered in the assignment), and a `ROW_ID` column. The latter is just a unique identification for the row.
    - (2) **predict.csv**: This data file has the exact same format as *train.csv*, but the `bike_speed` values where removed (i.e., the column is filled with NaN values).

2. **Training**: You have to use the data provided in **train.csv** to train a model that can predict the `bike_speed`. You can use any model you want, and any transformation you think is necessary. You can use any library you want, such as `scikit-learn`, `pandas`, `numpy`, etc.

3. **Submission File**: You have to submit a CSV file with the same format as the **predict.csv** file, but with the `bike_speed` column filled with your predictions. Use comma as the delimiter. Your file should look like this:

    ```csv
    ROW_ID,oneway,highway,maxspeed,...,n_observations,bike_speed
    0,True,cycleway,50,...,163.0,54.1
    1,True,primary,50,...,5.0,13.2
    ...
    ````

4. **Submission platform**: You have to submit your predictions in the web interface available at: [https://class-competitor.tpm.tudelft.nl](https://class-competitor.tpm.tudelft.nl). **You can submit up to 10 different predictions**. Please, go to the web platform and follow the instructions for registering and submitting your predictions. The platform will be open for submission till **25-11-2024 9:00 am**.

5. **Ranking**: You can check the ranking of the competition in the web interface. The ranking will be based on the RMSE of the predictions in the **predict.csv** file. The RMSE will be calculated by the Competiton team using the true values of the `bike_speed` of the **predict.csv** file.

6. **Grading**: The top 10 participants will receive bonus grading points according to the table mentioned above. The grading will be based on the ranking of the RMSE of your predictions.

Good Luck!
