#def save_info (a,b):
    #return {b: a}
    
import pandas as pd
    
def save_info (a,b,c):
    d ={'Имя абонента': [b],
            'Телефон': [a],
                'Город': [c]}
    return(pd.DataFrame(data=d))

    