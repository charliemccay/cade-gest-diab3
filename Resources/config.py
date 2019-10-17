### Running CADE ###
# ignoreWarnings
# True - warnings will be displayed but the user will not be prompted to ask if they wish to continue.
# False - the user will not be prompted to ask if they wish to continue on any warning.
ignoreWarnings = True
event_count_limit = 10000
# runTimeSelections indicates how many options the user wishes to be presented with at run time. Exit option will be
# available at every prompt. Positive numbers will present more options as they increase. Negative numbers cawn be use
# for special case options (eg. a config setup option where every option is presented before running)
# 0 - no run time options are available. All variables must be set through the config. This is the default.
# 1 - Y/N questions only will be presented for config values not set TBD
# 2 - questions only will be presented for config values needed(Y/N, file locations) but not set TBD
# 3 - all Y/N questions will be presented in addition to option 2
# 4 - questions will be presented for all config values needed(Y/N, file locations)
# Yet to be implemented, leave as 0
runTimeSelections = 0

informationItemsFile = 'InformationItems.csv'
setAttributesFile = 'AttributesSet.csv'

### Choose what will be executed
# populationGenBool will indicate if a population is to be created in this run.
populationGenBool = True
# populationGenBool will indicate if a chosen set of pathways will be validated.
pathwayValidationBool = True
# executeEngineBool will indicate if a simulation is to be executed this run.
# This implies that pathway validation will be run. Overrides pathwayValidation if false.
executeEngineBool = True
# populationGenBool will indicate if a visualisation is to be created in this run.
visualisationBool = True
# visulisationDisplay not working currently - should be left as False
visualisationDisplay = False


### Directories ###
# defaultDirLocation indicates where the Resources directory is located.
defaultDirLocation = ''
pathwayFileLocation = 'Resources/Files/Pathway/'


### Logging ###
# languageFileLocation indicates where the language file to be used is located.
languageFileLocation = 'PyCode/Logging/logDetails.csv'
# messageSet will be the header value of the set of messages to be used from the language file.
messageSet = 'message'
# individualLogs indicates whether the simulation will keep individual logs of patients at run time.
individualLogs = True
delete_logs = True


### Exhausts ###
# digitalExhaustDir indicates where the templates for a digital exhaust are located.
digitalExhaustTemplateDir = 'Resources/Files/ExhaustTemplates/'
# digitalExhaustFile will be the name of the file in the digitalExhaustDir location that details how the templates are
# to be used.
digitalExhaustFile = 'ExhaustConfig.csv'
# digital exhaust directory
digital_exhaust_directory = 'Resources/Outputs/Exhaust/'
# clear the exhaust directory
delete_exhaust = True
# number of seconds per tick
tickValue = 900


### Population creation ###
# populationSize will indicate the desired number of persons. May end up off slightly
populationSize = 50
# location of population file to load in
# populationFilePath = 'Resources/Files/Populations/start_population 2.csv'
populationFilePath = 'Resources/Files/Populations/start_population 50.csv'
# todo delete_end_population


### Execution engine ###
# Time between checks of the case for changed variables allowing sentries to be passed
# TBD: Only check case when change is made. This variable is a temporary fix.
caseTime = 'Hours'


### Visualisation ###
# Location of a list of nodes that will be used to filter the data shown in built figures
# TBD: Generate this list from pathway files with indicators on nodes of interest
nodesListFile = 'Resources/Files/Visualisations/NodesList.csv'
# Log to be used for building the visualisations
visLog = None

### FHIR exhaust ###
# fhir_base = ""
fhir_base = 'http://localhost:8080/baseDstu2/'
# fhir_base = 'http://localhost:8080/baseDstu3/'
# fhir_base = 'https://nhs.smilecdr.com/fhir-request/'
fhir_headers = {'Content-Type': 'application/json'}



