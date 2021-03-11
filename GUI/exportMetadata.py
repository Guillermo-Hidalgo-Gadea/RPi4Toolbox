# export metadata version 
import yaml
import pandas as pd
import datetime

with open('/home/hidalggc/Documents/metadata.yaml', 'r') as yamlfile:
    data = yaml.safe_load(yamlfile)

metadata = pd.DataFrame.from_dict(data, orient='index')
metadata = metadata.transpose()

filename = '/home/hidalggc/Documents/metadata_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.csv'

metadata.to_csv(filename, index = False, header=True, encoding='utf-8')

# move metadata csv and yaml file to backup

# erase yaml file to keep it slim