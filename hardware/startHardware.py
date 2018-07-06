# Part of the PsychoPy library
# Copyright (C) 2015 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

from os import path
from psychopy.app.builder.builder import components
#BaseVisualComponent, Param, getInitVals, _translate

#[u'C:\\Users\\William Chapman\\Documents\\GitHub\\stunning-octo-telegram\\hardwareControl\\hardwareControl', ]

# the absolute path to the folder containing this path
thisFolder = path.abspath(path.dirname(__file__))
iconFile = path.join(thisFolder, 'startHardware.png')


class startHardwareComponent(components.BaseComponent):
    """For initializing (and closing) hardware connections"""

    def __init__(self, exp, parentName, name='startHardware',
                 netIP='10.0.0.42',
                 netPort=55513,
                 ifNet=False,
                 ifEye=False):
        super(startHardwareComponent, self).__init__(
            exp, parentName, name=name)

        self.type = 'startHardware'
        self.url = "http://www.psychopy.org/builder/components/dots.html"

        # params
        self.params['netIP'] = components.Param(
            netIP, valType='string',
            updates='constant',
            hint='IP of netstation computer',
            label='netIP')

        self.params['netPort'] = components.Param(
            netPort, valType='code',
            updates='constant',
            hint='port of netstation computer',
            label='netPort')

        self.params['ifNet']=components.Param(ifNet, valType='bool', allowedTypes=[],
            updates='constant', allowedUpdates=[])

        self.params['ifEye']=components.Param(ifEye, valType='bool', allowedTypes=[],
            updates='constant', allowedUpdates=[])

        # these inherited params are harmless but might as well trim:
        for p in ('startType', 'startVal', 'startEstim', 'stopVal',
                  'stopType', 'durationEstim'):
            del self.params[p]

    def writeInitCode(self, buff):
        inits = components.getInitVals(self.params)
        depth = -self.getPosInRoutine()

        if self.params['ifNet'].val:
            netCode = ("import egi.simple as egi \n" +
                    "ms_localtime = egi.ms_localtime \n" +
                    "ns = egi.Netstation() \n" +
                    "ns.connect() \n"
                    "ns.BeginSession() \n" +
                    "ns.sync() \n" +
                    "ns.StartRecording() \n" +
                    "ifNet = True")
        else:
            netCode = ("ifNet = False")

        buff.writeIndentedLines(netCode)

        if self.params['ifEye'].val:
            eyeCode = ("import pylinkwrapper \n" +
                    "tracker = pylinkwrapper.Connect(win, filename) \n" +
                    "ifEye = True")
        else:
            eyeCode = ("ifEye = False")

        buff.writeIndentedLines(eyeCode)


    def writeExperimentEndCode(self, buff):
        if self.params['ifNet'].val:
            netCode = ("ns.StopRecording() \n" +
                "ns.EndSession() \n" +
                "ns.disconnect() \n")
            buff.writeIndentedLines(netCode)
        if self.params['ifEye'].val:
            eyeCode = ("tracker.end_experiment('.')")
            buff.writeIndentedLines(eyeCode)
