from datetime import datetime as dt

def phone_number(st):
    time = dt.today().strftime('%D/%m/%y.%H.%M')
    with open('log.csv', 'a') as p_file:
        p_file.write('{}; New_contact: {}\n'
                     .format(time,st))
        
