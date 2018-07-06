# Part of the PsychoPy library
# Copyright (C) 2015 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

from os import path
from psychopy.app.builder.builder import components
#BaseVisualComponent, Param, getInitVals, _translate

#[u'C:\\Users\\William Chapman\\Documents\\GitHub\\stunning-octo-telegram\\hardwareControl\\hardwareControl', ]

# the absolute path to the folder containing this path
thisFolder = path.abspath(path.dirname(__file__))
iconFile = path.join(thisFolder, 'syncHardware.png')


class syncHardwareComponent(components.BaseComponent):
    """An event class for presenting Random Dot stimuli"""

    def __init__(self, exp, parentName, name='syncHardware',
                 startMessage='BeginTrial',
                 endMessage='EndTrial',
                 ifCalibrate=False,
                 RecordEye=True):
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

        self.params['RecordEye'] = components.Param(
            RecordEye,
            valType='bool', allowedTypes=[],
            updates='constant', allowedUpdates=[]
        )
        self.params['ifCalibrate'] = components.Param(
            ifCalibrate,
            valType='bool', allowedTypes=[],
            updates='constant', allowedUpdates=[]
            )

        # these inherited params are harmless but might as well trim:
        for p in ('startType', 'startVal', 'startEstim', 'stopVal',
                  'stopType', 'durationEstim'):
            del self.params[p]


    def writeRoutineStartCode(self,buff):
        code = ("if ifNet: \n" +
                "   ns.sync() \n" +
                "   ns.send_event() \n" +    #TODO
                "if ifEye: \n" +
                "   tracker.set_status('TrialActive') \n" +    #TODO:
                "   tracker.set_trialid() \n" +
                "   tracker.send_message('BeginTrial') \n" +   #TODO
                "   tracker.record_on() \n")

        buff.writeIndented(code)

    def writeRoutineEndCode(self, buff):
        code = ("if ifNet: \n" +
                "   ns.send_event() \n" +
                " if ifEye: \n" +
                "   tracker.record_off() \n")
        buff.writeIndented(code)
