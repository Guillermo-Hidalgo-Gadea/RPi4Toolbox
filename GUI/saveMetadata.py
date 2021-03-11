# save metadata as yaml 

#import pandas as pd
import yaml
import datetime
import time

try:
    # if metadata exists, read keys to initialize dictionary
    with open('/home/hidalggc/Documents/metadata.yaml', 'r') as yamlfile:
        metadata = yaml.safe_load(yamlfile)
        dictionary = dict.fromkeys(metadata.keys(), [])
except IOError:
    # if no metadata file exists initialize new empty ditionary
    dictionary = {'subject':[],'date':[],'session':[],'trial':[],'repetition':[],
                   'start_habituation':[],'start_stimulus':[],'reactiontime_keypeck':[],
                   'optimal_stimulus':[],'key_choice':[],'reward':[],'col1':[]}

for i in range(5):
    
    # timestamps
    start_session = datetime.datetime.now()
    time.sleep(1)
    start_stimulus = datetime.datetime.now()
    time.sleep(1)
    start_key = datetime.datetime.now()
    diff = start_key - start_stimulus
    
    # run trial and save metadata
    subject = 'p009'
    date = start_session.strftime('%Y-%m-%d')
    session = 3
    trial = 'training_autoshape'
    repetition = 8
    start_habituation = start_session.strftime('%H:%M:%S.%f')
    start_stimulus = start_stimulus.strftime('%H:%M:%S.%f')
    reactiontime_keypeck = str(diff)
    optimal_stimulus = 'left'
    key_choice = 'right' 
    reward = 2
    
    # update dictionary 
    dictionary['subject'].append(subject)
    dictionary['date'].append(date)
    dictionary['session'].append(session)
    dictionary['trial'].append(trial)
    dictionary['repetition'].append(repetition)
    dictionary['start_habituation'].append(start_habituation)
    dictionary['start_stimulus'].append(start_stimulus)
    dictionary['reactiontime_keypeck'].append(reactiontime_keypeck)
    dictionary['optimal_stimulus'].append(optimal_stimulus)
    dictionary['key_choice'].append(key_choice)
    dictionary['reward'].append(reward)



    
# SAVE TO YAML at the end of session
try:
    # if metadata exists, append
    with open('/home/hidalggc/Documents/metadata.yaml', 'r') as yamlfile:
        metadata = yaml.safe_load(yamlfile)
        metadata.update(dictionary)
    
    with open('/home/hidalggc/Documents/metadata.yaml', 'w') as file:
        yaml.safe_dump(metadata, file, sort_keys=False)

except IOError:
    # if no metadata exists, create new
    with open('/home/hidalggc/Documents/metadata.yaml', 'w') as file:
        yaml.dump(dictionary, file, sort_keys=False)
