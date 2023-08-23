from collections import defaultdict
def calc_wqi(row, 
             standardValues=None,
             pureValues=None
            ):
    if standardValues is None:
        standardValues= {'COD': 20, 'DO': 6, 'BOD':7, 'EC': 1000, 'NO3': 20,'N2': 10,'TSS': 500,'TEMP': 28,'PH': 8.5}
    if pureValues is None:
        pureValues=defaultdict(lambda : 0)
        pureValues['PH']=7
        pureValues['DO']=14.6
        pureValues['BOD']=16
    return 100 * sum([1/standardValues[col] * 
                      (row[col]-pureValues[col])/
                      (standardValues[col]-pureValues[col])
                         for col in row.index if col!='WQI'])/sum(map(lambda x:1/x, standardValues.values()))

def populate_wqi(df, pos= 0, standardValues={}):
    '''Populates dataframe with WQI based on WAWQI model'''
    
    return df.insert(pos, 'WQI', df.apply(calc_wqi,axis=1))