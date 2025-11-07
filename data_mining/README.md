# Spam Detection Using ML Algorithms

This project demonstrates the implementation of three machine learning algorithms — Decision Tree, K-Nearest Neighbors (KNN), and Naive Bayes — to classify emails as spam or not spam. The pipeline includes data preprocessing, training, and evaluation, along with a comparison of model performances.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Dependencies](#dependencies)
5. [Pipeline](#pipeline)
6. [Modules](#modules)
7. [How to Run](#how-to-run)
8. [Results and Visualizations](#results-and-visualizations)
9. [Future Enhancements](#future-enhancements)

---

## Project Overview

Spam emails are a significant challenge in communication systems. This project uses classic supervised learning algorithms to classify emails as spam or not spam. It implements:
- **Decision Tree**
- **K-Nearest Neighbors (KNN)**
- **Naive Bayes**

These models are evaluated and compared based on their accuracy and performance metrics.

---

## Features

- **Data Preprocessing**:
  - Cleaning, tokenization, stopword removal, and stemming.
  - Addressing class imbalance using SMOTE.
  
- **Algorithms Implemented**:
  - Decision Tree
  - KNN
  - Naive Bayes

- **Visualizations**:
  - Class distribution of emails.
  - Email length before and after preprocessing.
  - Confusion matrices for each algorithm.
  - Accuracy comparison of all models.

---

## Dataset

The dataset `spam_dataset.csv` contains two main columns:
- **message_content**: Text content of the email.
- **is_spam**: Label indicating whether the email is spam (1) or not spam (0).

---

## Dependencies

Install the required Python libraries using the following command:

```bash
pip install -r requirements.txt
```
