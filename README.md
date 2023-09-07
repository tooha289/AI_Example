- [Introduce](#introduce)
- [Library](#library)
  - [preprocessing](#preprocessing)
- [Examples](#examples)
  - [Covid\_prediction 1](#covid_prediction-1)
    - [Goal](#goal)
    - [File](#file)
    - [Data source](#data-source)
      - [Kaggle](#kaggle)
    - [Duration : 2023-09-01](#duration--2023-09-01)
  - [Covid\_prediction 2](#covid_prediction-2)
    - [Goal](#goal-1)
    - [File](#file-1)
    - [Data source](#data-source-1)
      - [Kaggle](#kaggle-1)
    - [Duration : 2023-09-01](#duration--2023-09-01-1)
  - [Car price](#car-price)
    - [Goal](#goal-2)
    - [File](#file-2)
    - [Data source](#data-source-2)
      - [Dacon](#dacon)
    - [Duration : 2023-09-04](#duration--2023-09-04)
  - [Titanic VIF](#titanic-vif)
    - [Goal](#goal-3)
    - [File](#file-3)
    - [Data source](#data-source-3)
      - [Dacon](#dacon-1)
    - [Duration : 2023-09-05](#duration--2023-09-05)
  - [Internet subscription](#internet-subscription)
    - [Goal](#goal-4)
    - [File](#file-4)
    - [Data source](#data-source-4)
      - [Site](#site)
    - [Duration : 2023-09-07](#duration--2023-09-07)
  - [BMI obesity prediction](#bmi-obesity-prediction)
    - [Goal](#goal-5)
    - [File](#file-5)
    - [Data source](#data-source-5)
      - [Site](#site-1)
    - [Duration : 2023-09-07](#duration--2023-09-07-1)

# Introduce
The goal is to use various AI models from various data and practice their use.

# Library
These are libraries that can be used when performing analysis.
## [preprocessing](https://github.com/tooha289/AI_Example/blob/main/Library/preprocessing.py)
This class helps perform preprocessing on data frames. Through this class, you can perform scaling or encoding operations on data frames.
* The currently verified transformers are as follows. MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder

# Examples
## Covid_prediction 1 
### Goal
Predicting COVID confirmation from pre-COVID symptoms.

### File
* [covid.ipynb](https://github.com/tooha289/AI_Example/blob/main/covid(other_data).ipynb)

### Data source
#### Kaggle
* https://www.kaggle.com/code/mykeysid10/detection-of-covid19-cases-using-ml/input

### Duration : 2023-09-01

## Covid_prediction 2
### Goal
Predicting COVID confirmation from pre-COVID symptoms.

### File
* [covid(other).ipynb](https://github.com/tooha289/AI_Example/blob/main/covid(other_data).ipynb)

### Data source
#### Kaggle
* https://www.kaggle.com/datasets/hemanthhari/symptoms-and-covid-presence
  
### Duration : 2023-09-01

## Car price
### Goal
This example uses various machine learning models to predict used car prices.

### File
* [car_price.ipynb](https://github.com/tooha289/AI_Example/blob/main/car_price.ipynb)

### Data source
#### Dacon
* https://dacon.io/competitions/official/236114/data
  
### Duration : 2023-09-04

## Titanic VIF
### Goal
This example analyzes the impact of high VIF columns on learning on Titanic data.

### File
* [titanic_vif.ipynb](https://github.com/tooha289/AI_Example/blob/main/titanic_vif.ipynb)

### Data source
#### Dacon
* https://www.kaggle.com/competitions/titanic/data?select=train.csv

### Duration : 2023-09-05

## Internet subscription
### Goal
In this example, we predict new sign-ups based on information from new internet subscribers.

### File
* [internet_subscription.ipynb](https://github.com/tooha289/AI_Example/blob/main/internet_subscription.ipynb)

### Data source
#### Site
* http://www-stat.wharton.upenn.edu/~waterman/Teaching/701f98/logistic/logistic.html

### Duration : 2023-09-07

## BMI obesity prediction
### Goal
In this example, predicting obesity based on height and weight data.

### File
* [bmi.ipynb](https://github.com/tooha289/AI_Example/blob/main/bmi.ipynb)

### Data source
#### Site
* https://hoony-gunputer.tistory.com/entry/%ED%85%90%EC%84%9C%ED%94%8C%EB%A1%9C%EC%9A%B0%EB%A1%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%95%98%EA%B8%B0bmi-%EA%B5%AC%ED%95%98%EA%B8%B0

### Duration : 2023-09-07