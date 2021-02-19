import yaml

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
        self.habituation_time = edict['trial']['habituation_time']
        self.repetitions = edict['trial']['repetitions']
        self.timeout = edict['trial']['timeout']
        self.optimal_reward = edict['trial']['optimal_reward']
        self.suboptimal_reward = edict['trial']['suboptimal_reward']
        self.optimal_stimuluscolor = edict['trial']['optimal_stimuluscolor']
        self.suboptimal_stimuluscolor = edict['trial']['suboptimal_stimuluscolor']
        

class Database:
    '''
    Database class loads the sample and subject information form the database.yaml 
    config file. This information will be useful to help identifying subjects, as well as 
    for assigning subjects to the appropriate group in the experimental protocol.
    '''
    def __init__(self, ddict):
        self.samples = list(ddict.keys())
        self.description = ddict['sample1']['description']
        
class Metadata:
    '''
    Metadata class loads the progress form past trials in the loaded experiment from
    the metadata.yaml config file. This metadata will be helpful to display subjects' 
    progress during the experiment to guide the experimenter as well as to assign the
    subject to the upcoming scheduled trial, session, etc.
    '''
    def __init__(self, mdict):
        self.description = mdict['description']

        
class Parameters: # conisider RENAMING!
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
        with open(file, 'r') as f:
            files = yaml.safe_load(f)
        
        # hardware parameters
        hpath = files['hardware']['path']
        with open(hpath, 'r') as path:
            hparams = yaml.safe_load(path)
        hdict = hparams['hardware']
        self.hardware = Hardware(hdict)
        
        # experiment parameters
        epath = files['experiment']['path']
        with open(epath, 'r') as path:
            eparams = yaml.safe_load(path)
        edict = eparams['experiment']
        self.experiment = Experiment(edict)
        
        # database parameters
        dpath = files['database']['path']
        with open(dpath, 'r') as path:
            dparams = yaml.safe_load(path)
        ddict = dparams['database']
        self.database = Database(ddict)
        
        # metadata parameters
        mpath = files['metadata']['path']
        with open(mpath, 'r') as path:
            mparams = yaml.safe_load(path)
        mdict = mparams['metadata']
        self.metadata = Metadata(mdict)


# parameters file is written by experimenter clicking
#pm = Parameters('parameters.yaml')

#pm.hardware.stimulus_info
#pm.experiment.description
#pm.experiment.habituation_time
#pm.database.description
#pm.database.samples
#pm.metadata.description
