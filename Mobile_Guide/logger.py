from datetime import datetime as dt

def phone_number(st):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as p_file:
        p_file.write('{}; Number_Phone: {}\n'
                     .format(time,st))
        
