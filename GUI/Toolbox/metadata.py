# Metadata module to save metadata as dictionary, save trial metadata as yaml and export metadata as csv

import yaml
import datetime
import pandas as pd
from pathlib import Path

class Metadata:
    def __init__(self):
        base_path = Path().parent
        self.metadata_dir = (base_path / "RPi4Toolbox/GUI/Toolbox/metadata.yaml").resolve()
        self.subject = ''
        self.experimenter = ''
        self.date = ''
        self.session = 0
        self.condition = ''
        self.trial = 0
        self.repetition = 0
        self.start_habituation = ''
        self.start_stimulus = ''
        self.reactiontime_keypeck = ''
        self.optimal_stimulus = ''
        self.key_choice = ''
        self.reward = 0

        # Initialize dictionary from existing metadata or create new
        try:
            # if metadata exists, read keys to initialize dictionary
            with open(self.metadata_dir, 'r') as yamlfile:
                metadata = yaml.safe_load(yamlfile)
                self.dictionary = dict.fromkeys(metadata.keys(), [])
        except IOError:
            # if no metadata file exists initialize new empty ditionary
            self.dictionary = {'subject':[],'experimenter':[],'date':[],'condition':[],'session':[],'trial':[],'repetition':[],
                        'start_habituation':[],'start_stimulus':[],'reactiontime_keypeck':[],
                        'optimal_stimulus':[],'key_choice':[],'reward':[],'col1':[]}

    def append(self):
        # update dictionary with session related metadata
        self.dictionary['subject'].append(self.subject)
        self.dictionary['experimenter'].append(self.experimenter)
        self.dictionary['date'].append(self.date)
        self.dictionary['condition'].append(self.condition)
        self.dictionary['session'].append(self.session)
        # update dictionary with trial related metadata
        self.dictionary['trial'].append(self.trial)
        self.dictionary['repetition'].append(self.repetition)
        self.dictionary['start_habituation'].append(self.start_habituation)
        self.dictionary['start_stimulus'].append(self.start_stimulus)
        self.dictionary['reactiontime_keypeck'].append(self.reactiontime_keypeck)
        self.dictionary['optimal_stimulus'].append(self.optimal_stimulus)
        self.dictionary['key_choice'].append(self.key_choice)
        self.dictionary['reward'].append(self.reward)

    def save(self):
        # SAVE TO YAML at the end of session
        try:
            # if metadata exists, append new data
            with open(self.metadata_dir, 'r') as yamlfile:
                metadata = yaml.safe_load(yamlfile)
                metadata.update(self.dictionary)
            with open(self.metadata_dir, 'w') as file:
                yaml.safe_dump(metadata, file, sort_keys=False)
        except IOError:
            # if no metadata exists, create new file
            with open(self.metadata_dir, 'w') as file:
                yaml.dump(self.dictionary, file, sort_keys=False)

def export():
    """
    This function exports the metadata.yaml file to a standard metadata.csv and cleans the
    metadata.yaml history after moving it to backup.
    """

    ## EXPORT METADATA
    base_path = Path().parent
    file_path = (base_path / "../RPi4Toolbox/GUI/Toolbox/metadata.yaml").resolve()
    with open(file_path, 'r') as yamlfile:
        data = yaml.safe_load(yamlfile)
    metadata = pd.DataFrame.from_dict(data, orient='index')
    metadata = metadata.transpose()
    filename = str(file_path)[0:-5]+'_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.csv'
    metadata.to_csv(filename, index = False, header=True, encoding='utf-8')

    # move metadata csv and yaml file to sciebo backup
    # erase yaml file to keep it slim