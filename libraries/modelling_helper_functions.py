import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt
import seaborn as sns

#################################################################################################################

def metrics_summary(model,obs,pred):
    
    mape = round(mean_absolute_percentage_error(y_true=obs,y_pred=pred)*100,3)
    
    print(f'Results for the test data:')
    print(f'\tModel: {model}')
    print(f'\tMAPE = {mape}%')

#################################################################################################################

def lin_reg_plot(train,train_pred,test,test_pred):
    plt.figure(figsize=(25,10))
    plt.plot(train,color='blue')
    plt.plot(train_pred,color='green')
    plt.plot(test_pred,label='Predicted', color='green')
    plt.plot(test, label='Actual',color='blue')
    plt.axvline(x=pd.to_datetime('2019-01-01'),label='Train/Test Boundary',color='red')
    sns.despine()
    plt.title('GMSL Linear Regression Predicted vs Actual')
    plt.ylabel('GMSL Change (mm)')
    plt.legend()
    plt.show()

#################################################################################################################