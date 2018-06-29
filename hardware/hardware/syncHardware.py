# Part of the PsychoPy library
# Copyright (C) 2015 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

from os import path
from psychopy.app.builder.builder import components
#BaseVisualComponent, Param, getInitVals, _translate

#[u'C:\\Users\\William Chapman\\Documents\\GitHub\\stunning-octo-telegram\\hardwareControl\\hardwareControl', ]

# the absolute path to the folder containing this path

thisFolder = path.abspath(path.dirname(__file__))
iconFile = path.join(thisFolder, 'hardware.png')
#tooltip = components._translate('Dots: Random Dot Kinematogram')
# only use _localized values for label values, nothing functional:
#_localized = {'nDots': components._translate('Number of dots'),
#              'dir': components._translate('Direction'),
#              'speed': components._translate('Speed'),
#              'coherence': components._translate('Coherence'),
#              'dotSize': components._translate('Dot size'),
#              'dotLife': components._translate('Dot life-time'),
#              'signalDots': components._translate('Signal dots'),
#              'noiseDots': components._translate('Noise dots'),
#              'fieldShape': components._translate('Field shape'),
#              'fieldSize': components._translate('Field size'),
#              'fieldPos': components._translate('Field position'),
#              'refreshDots':components._translate('Dot refresh rule')}


class syncHardwareComponent(components.BaseComponent):
    """An event class for presenting Random Dot stimuli"""

    def __init__(self, exp, parentName, name='syncHardware',
                 startMessage='BeginTrial',
                 endMessage='EndTrial'):
        super(syncHardwareComponent, self).__init__(
            exp, parentName, name=name)

        self.type = 'syncHardware'
        self.url = "http://www.psychopy.org/builder/components/dots.html"

        # params
        self.params['startMessage'] = components.Param(
            startMessage, valType='string',
            updates='constant',
            hint='Code for begining of routine',
            label='startMessage')

        self.params['endMessage'] = components.Param(
            endMessage, valType='string',
            updates='constant',
            hint='Code for end of Routine',
            label='endMessage')
        # these inherited params are harmless but might as well trim:
        for p in ('startType', 'startVal', 'startEstim', 'stopVal',
                  'stopType', 'durationEstim'):
            del self.params[p]


    def writeRoutineStartCode(self,buff):
        code = ("ns.sync() \n" +
                "ns.send_event() \n" +
                "tracker.set_status('TrialActive') \n" +
                "tracker.set_trialid() \n" +
                "tracker.send_message('BeginTrial') \n" +
                "tracker.record_on() \n")

        buff.writeIndented(code)

    def writeRoutineEndCode(self, buff):
        code = ("ns.send_event() \n")
        buff.writeIndented(code)
