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


class startHardwareComponent(components.BaseComponent):
    """For initializing (and closing) hardware connections"""

    def __init__(self, exp, parentName, name='startHardware',
                 netIP='10.0.0.42',
                 netPort=55513):
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

        # these inherited params are harmless but might as well trim:
        for p in ('startType', 'startVal', 'startEstim', 'stopVal',
                  'stopType', 'durationEstim'):
            del self.params[p]

    def writeInitCode(self, buff):
        inits = components.getInitVals(self.params)
        depth = -self.getPosInRoutine()

        code = ("import egi.simple as egi \n" +
                "import pylinkwrapper \n" +
                "tracker = pylinkwrapper.Connect(win, test822) \n" +
                "ms_localtime = egi.ms_localtime \n" +
                "ns = egi.Netstation() \n" +
                "ns.connect() \n"
                "ns.BeginSession() \n" +
                "ns.sync() \n" +
                "ns.StartRecording() \n")
        buff.writeIndentedLines(code)

    def writeExperimentEndCode(self, buff):
        code = ("ns.StopRecording() \n" +
                "ns.EndSession() \n" +
                "ns.disconnect() \n" +
                "tracker.end_experiment('.')")

        buff.writeIndentedLines(code)
