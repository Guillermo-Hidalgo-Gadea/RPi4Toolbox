import yaml
from pathlib import Path

class Hardware:
    '''
    Hardware class loads the configured stimulus, sensors and effectors form the 
    hardware.yaml config file. Note that the class attributes are hard-coded and 
    need to be adapted to the yaml file structure (i.e., nesting).
    '''
    def __init__(self, hdict):
        self.stimulus_info = hdict['stimulus']['info']
        self.stimulus1 = hdict['stimulus']['stimulus1']['name']
        self.stimulus1_id = hdict['stimulus']['stimulus1']['id']
        self.stimulus2 = hdict['stimulus']['stimulus2']['name']
        self.stimulus2_id = hdict['stimulus']['stimulus2']['id'] 
        self.stimulus3 = hdict['stimulus']['stimulus3']['name']
        self.stimulus3_id = hdict['stimulus']['stimulus3']['id']
        
        self.sensor_info = hdict['sensor']['info']
        self.sensor1 = hdict['sensor']['sensor1']['name']
        self.sensor1_id = hdict['sensor']['sensor1']['id']
        self.sensor2 = hdict['sensor']['sensor2']['name']
        self.sensor2_id = hdict['sensor']['sensor2']['id'] 
        self.sensor3 = hdict['sensor']['sensor3']['name']
        self.sensor3_id = hdict['sensor']['sensor3']['id'] 
        
        self.effector_info = hdict['effector']['info']
        self.effector1 = hdict['effector']['effector1']['name']
        self.effector1_id = hdict['effector']['effector1']['id']
        self.effector2 = hdict['effector']['effector2']['name']
        self.effector2_id = hdict['effector']['effector2']['id'] 
        self.effector3 = hdict['effector']['effector3']['name']
        self.effector3_id = hdict['effector']['effector3']['id'] 
        
class Experiment:
    '''
    Experiment class loads the planed experimental protocol form the experiment.yaml 
    config file. 
    '''
    def __init__(self, edict):
        self.description = edict['description']
        self.groups = '' #list keys with description
        self.conditions = ''#list keys with description
        self.trial = 'trial_training_quantity' # TODO assigned from session outside class
        self.trials_persession = edict[self.trial]['trials_persession']
        self.min_sessions = edict[self.trial]['min_sessions']
        self.criterion = edict[self.trial]['criterion']
        self.repetitions_pertrial = edict[self.trial]['repetitions_pertrial']
        self.habituation_time = edict[self.trial]['habituation_time']
        self.timeout_interval = edict[self.trial]['timeout_interval']
        self.optimal_key_position = edict[self.trial]['optimal_key_position']
        self.optimal_key_depth = edict[self.trial]['optimal_key_depth']
        self.optimal_stimuluscolor = edict[self.trial]['optimal_stimuluscolor']
        self.suboptimal_key_depth = edict[self.trial]['suboptimal_key_depth']
        self.suboptimal_stimuluscolor = edict[self.trial]['suboptimal_stimuluscolor']
        self.optimal_reward = edict[self.trial]['optimal_reward']
        self.suboptimal_reward = edict[self.trial]['suboptimal_reward']
        

class Database:
    '''
    Database class loads the sample and subject information form the database.yaml 
    config file. This information will be useful to help identifying subjects, as well as 
    for assigning subjects to the appropriate group in the experimental protocol.
    '''
    def __init__(self, ddict):
        self.samples = list(ddict.keys())
        self.description = ddict['sample1']['description']
        

        
class Parameters: # TODO conisider RENAMING!
    '''
    This class is a wrapper for all the objects above. Hardware, Experiment, 
    Database and Metadata are passed as attributes of Parameters. The specific 
    config files are intentionally distributed in separate yaml files for ease of 
    use by the experimenter i.e., avoiding long config files with inconsistent structure.
    The Parameters object is initialized with an overview parameters.yaml file that
    contains paths to the specific classes to be extracted. Then, attributes are 
    passed on from objects defined above.
    '''
    def __init__(self, file):
        
        # distribution to separate yaml files for convenience
        #with open(file, 'r') as f:
        #    files = yaml.safe_load(f)
        
        # hardware parameters
        hpath = (Path().parent / "Toolbox/hardware.yaml").resolve()
        #hpath = files['hardware']['path']
        with open(hpath, 'r') as path:
            hparams = yaml.safe_load(path)
        hdict = hparams['hardware']
        self.hardware = Hardware(hdict)
        
        # experiment parameters
        epath = (Path().parent / "Toolbox/experiment.yaml").resolve()
        #epath = files['experiment']['path']
        with open(epath, 'r') as path:
            eparams = yaml.safe_load(path)
        edict = eparams['experiment']
        self.experiment = Experiment(edict)
        
        # database parameters
        dpath = (Path().parent / "Toolbox/database.yaml").resolve()
        #dpath = files['database']['path']
        with open(dpath, 'r') as path:
            dparams = yaml.safe_load(path)
        ddict = dparams['database']
        self.database = Database(ddict)
        


# parameters file is written by experimenter clicking
#pm = Parameters('parameters.yaml')

#pm.hardware.stimulus_info
#pm.experiment.description
#pm.experiment.habituation_time
#pm.database.description
#pm.database.samples
#pm.metadata.description
