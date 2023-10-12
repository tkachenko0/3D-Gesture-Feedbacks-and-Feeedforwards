from jproperties import Properties

configs = Properties()

with open('.properties', 'rb') as config_file:
    configs.load(config_file)


CAMERA_INDEX = int(configs.get('CAMERA_INDEX').data)