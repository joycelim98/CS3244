"""
Import the relevant libraries here
"""

import numpy as np 
import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
import seaborn as sn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import confusion_matrix
import random
from imblearn.over_sampling import RandomOverSampler



def plot_cm_n_calculate_F1_score(confusion_matrix, normalise = True, save_fig = True, method_name = ""):

    TN = confusion_matrix[0][0]
    TP = confusion_matrix[1][1]
    FP = confusion_matrix[0][1]
    FN = confusion_matrix[1][0]
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1_score = 2 * precision * recall / (precision + recall)
    print("The F1 score is:", F1_score)
    
    cm = [[0,0],[0,0]]
    if normalise:
        cm[0][0] = TN / (TN + FP)
        cm[0][1] = FP / (TN + FP)
        cm[1][0] = FN / (FN + TP)
        cm[1][1] = TP / (FN + TP)
        plt.title('Normalised Confusion matrix ' + method_name, fontsize = 14)
    else:
        cm[0][0] = TN
        cm[0][1] = FP
        cm[1][0] = FN
        cm[1][1] = TP
        plt.title('Confusion matrix ' + method_name, fontsize = 14)
        
    labels = ['Non-Clickbait', 'Clickbait']
    df_cm = pd.DataFrame(cm, index = labels, columns = labels,)
    sns_plot = sn.heatmap(df_cm, annot=True, cmap=plt.cm.Blues, annot_kws={"size": 14})
    fig = sns_plot.get_figure()
    plt.xlabel('Predicted value', fontsize = 16)
    plt.ylabel('True value', fontsize = 14)
    # plt.show()
    
    if save_fig:
        figname = "Normalised Confusion Matrix " if normalise else "Confusion Matrix "
        figname += "(" + method_name + ")"
        fig.savefig(figname)
        print("figure saved")

    plt.clf()


##cm_rf = [[2397, 511], [1340, 1612]]
##cm_knn = [[2054, 854], [1112, 1840]]
##cm_bag = [[2653,253], [1858, 1094]]

cm_rf = [[753, 235], [450, 550]]
cm_knn = [[753, 235], [450, 550]]
cm_bag = [[686, 302], [319, 681]]


labelled = [(cm_rf, "Random Forest"), (cm_knn, "k-Nearest-Neighbours"), (cm_bag, "Bagging")]

for i in labelled:
    plot_cm_n_calculate_F1_score(i[0], method_name = i[1])

##cm_log_reg = [[0.01143451,0.98856549],[0.02863203,0.97136797]]
##plot_cm_n_calculate_F1_score(cm_log_reg, method_name = "Logistic Regression", normalise = False)
