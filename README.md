# Predictive modeling

The goal of this exercise is to assess your ability to develop a model that
predicts the energy expenditure (measured in METs) accurately from a collection
of 22 unique individuals each of whom were walking or running during the data
collection process. Each of the 943 rows in the training set consists of
feature values computed over a 15-second interval of time as well as a single
response variable stored in the column labeled “mets” and a unique test subject
identifier in the column labeled “uid”. Note that -99999 is used to represent
a missing value.

The features can be broadly divided into three categories:

1. Motion features derived from a three-axis accelerometer.
2. Heart rate features derived from an optical sensor.
3. Demographic and other features.

The accelerometer features are proprietary and will not be described here. You
can interpret the other features as follows:

| Name                | Meaning  |
| ------------------- | -------  |
| steps               | steps taken during the 15-second epoch  |
| age                 | age in years  |
| height              | height in meters  |
| weight              | weight in kg  |
| stride_length       | estimated stride length in inches  |
| mph                 | estimated speed in miles per hour |
| speed_mets          | estimated mets derived from mph using a textbook formula |
| baselineHR          | heart rate (HR) while sedentary |
| scaled_hr_mean_epoch| median_hr / (207 - (user_age * 0.7)) |
| hr_mean_epoch       | mean HR measurement in a 15-second epoch |
| hr_median_epoch     | median HR |
| hr_trend_epoch      | last HR - mean HR |
| hr_zscore_epoch     | (last HR - mean HR) / mean HR |
| hr_iqr_mean_epoch   | diff between mean HR at 25th percentile and mean HR at 75th |
| hr_iqr_median_epoch | diff between median HR at 25th percentile and mean HR at 75th |
| hr_iqr_max_epoch    | diff between max HR at 25th percentile and max HR at 75th |
| hr_iqr_min_epoch    | diff between min HR at 25th percentile and min HR at 75th |
| hr_idr_mean_epoch   | as above except 10th and 90th percentile |
| hr_idr_median_epoch | as above except 10th and 90th percentile |
| hr_idr_max_epoch    | as above except 10th and 90th percentile |
| hr_idr_min_epoch    | as above except 10th and 90th percentile |

## Procedure

First make a *private* copy of this repository in your own Github account.

Follow the [instructions
here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template).

Make absolutely sure your repository is *private* when you are doing this procedure; the option looks like this:

![](private_repo.png)

Clone your new copy of this template repository to your computer, and then
write notebook, code and other files to implement the requirements below.

Make sure you include instructions in this `README` file, or in another file,
clearly signaled, to run and reproduce your analysis.

## Requirements

1. Employ the modeling technique of your choice.
2. Use Python for implementation.
3. Use an existing package or implement something from scratch.
4. Any visualization would be good — plot away.
5. Please be as descriptive as possible about the approach you took and the
   reasoning behind it.
6. Along with the model, itself, provide an, estimate of the error rate of the
   model, along with the rationale for the choice of error estimation technique.
7. Please provide model validation.
