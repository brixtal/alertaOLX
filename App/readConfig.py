class ReadConfig:

    global config
    config = {}

    def getConfig (self, path_file):
        with open(path_file, 'r') as f:
            for line in f:
                attrib = line.split('=')
                key = attrib[0].strip()
                parameter = attrib[1].strip()
                config.update({key : parameter})
        return config

