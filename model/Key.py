class Key(object):

    def __init__(self, *args):
        self.context = ''
        self.key = ''
        self.action = ''
        self.duration = ''
        self.axis = ''
        self.type = ''

    def populate(self, context, key):
        self.context = context
        self.key, action = key.split('=(')
        if ("Pad" in self.key):
            self.type = 'controller'
        elif ('PS4' in self.key):
            self.type = 'PS4'
        else:
            self.type = 'keyboard'
        action = action[:-1]
        values = action.split(',')
        self.action = values[0][7:]
        if (len(values) > 1):
            if ("Axis" in values[1]):
                self.axis = values[2][6:]
            elif ("Duration" in values[1]):
                self.duration = values[2][9:]

    def __str__(self):
        str = ""
        str += self.key + "=(Action=" + self.action
        if (self.duration or self.axis):
            if (self.duration):
                str += ",State=Duration,IdleTime=" + self.duration
            else:
                str += ",State=Axis,Value=" + self.axis
        str += ")"
        return str
