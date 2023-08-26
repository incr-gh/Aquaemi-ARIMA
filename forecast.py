import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
warnings.filterwarnings("ignore")
import pandas as pd
import statsmodels.api as sm
import matplotlib
from sktime.performance_metrics.forecasting import *
from scipy import stats

def print_metrics(ref, comp, model_name='Model'):
    mae_ = mean_absolute_error(ref, comp)
    rmse_ = mean_squared_error(ref, comp, square_root = True)
    mape_ = mean_absolute_percentage_error(ref, comp)
    smape_ = mean_absolute_percentage_error(ref, comp, symmetric = True)
    
    dict_ = {'Mean Absolute Error': mae_, 'Root Mean Squared Error': rmse_,
             'Mean Absolute Percentage Error': mape_, 'Mean Squared Absolute Percentage Error': smape_ }
    
    df = pd.DataFrame(dict_, index = [model_name])
    return(df.round(decimals = 2))

def can_tho():
    df= pd.read_csv('Data\Mekong Can Tho Data.csv')
    df=df.set_index('Date')
    df=df.convert_dtypes()
    df.index=df.index=pd.DatetimeIndex(df.index) #m= Month, w= Week, d= Day

def __getmodels():
    __models= pd.read_csv('models.csv')
    __models=__models.convert_dtypes()
    __models=__models.drop(__models.columns[0],axis=1)
    __models=__models.drop(__models.columns[0],axis=1)
    __models=__models.apply(lambda k: k.apply(eval))
    #best_models={c:__models[c][r] for c,r in zip(__models.columns,[0,1,3,3,9,23,2,1])}
    return __models

def find_optimal_model(ser, pdqmax:int=3, iterations:int=12):
    '''
    Best to use newer data to ensure highest speed and accuracy (from 2016 onwards)
    Applies seasonal ARIMA to series with DatetimeRangeIndex
    ReturnType: Returns a sorted list of models ranked by lowest aicc
    
    '''
    warnings.filterwarnings('ignore')
    p = d = q = range(0, pdqmax)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], iterations) for x in list(itertools.product(p, d, q))]
    train=ser.astype('float')
    aicl=[]
    k=None
    print(f'---------------------{ser.name if (ser.name is not None) else "Training"}---------------------')
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(train,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)
                results = mod.fit()
                aicl.append((param,param_seasonal, results.aicc))
                if k==None or results.aic < k[2]:
                    k=(param,param_seasonal,results.aicc)
                    print(f'Current Best: SARIMA{k[0]}x{k[1]}12 - AICC:{k[2]}')
            except e:
                print('baka')
                continue
    print(f'Best: ARIMA{k[0]}x{k[1]}12 - AIC:{k[2]}')
    return sorted(aicl,key=lambda x:x[2])

best_models=\
{'COD': ((1, 0, 0), (2, 2, 0, 12)),
 'DO': ((2, 0, 2), (2, 2, 0, 12)),
 'EC': ((1, 2, 2), (0, 2, 2, 12)),
 'NO3': ((1, 0, 0), (1, 0, 1, 12)),
 'N2': ((2, 0, 2), (0, 2, 2, 12)),
 'TSS': ((0, 1, 2), (1, 2, 2, 12)),
 'TEMP': ((0, 1, 2), (0, 2, 2, 12)),
 'PH': ((1, 1, 2), (0, 1, 2, 12))}
def get_best_model(key, data):
    '''Get best model using data as training'''
    return sm.tsa.statespace.SARIMAX(data, 
                                     order=(l:=best_models[key])[0], 
                                     seasonal_order=l[1],
                                     enforce_stationarity=False,
                                     enforce_invertibility=False).fit()

def forecast(model, steps=36):
    '''Returns (Forecast, Lower bound forecast, Upper bound forecast)'''
    return ((r:=model.get_forecast(steps=steps)).predicted_mean,  r.conf_int().iloc[:, 0], r.conf_int().iloc[:, 1])

def predict_shorterm(x,y, terms=7):
    slope, intercept, r, p, std_err = stats.linregress(range(len(x)), y)
    return [slope*xi + intercept for xi in range(len(x))]

#x = [23,22,24]
#y = [0,1,2]



#predict_shorterm(23,22,24)