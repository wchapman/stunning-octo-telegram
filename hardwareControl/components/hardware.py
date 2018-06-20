from _base import *
from os import path
from psychopy.app.builder.experiment import Param
from psychopy import prefs

thisFolder = path.abspath(path.dirname(__file__))#the absolute path to the folder containing this path
iconFile = path.join(thisFolder,'hardware.png')
tooltip = _translate('hardware: Control EEG and eyetracker')


class hardware(BaseComponent):
    """A class for controlling EEG and Eyetracking"""
    categories = ['custom']
    def __init__(self, exp, parentName, name='hardware',
                startType='time (s)', startVal=0.0,
                stopType='duration (s)', stopVal=1.0):
        super(hardware, self).__init__(exp, parentName, name,
            startType=startType, startVal=startVal,
            stopType=stopType, stopVal=stopVal,
            startEstim=startEstim, durationEstim=durationEstim)
        self.type='Hardware'
        self.url="https://github.com/wchapman/stunning-octo-telegram"
        self.categories=['custom']
        #self.exp.requirePsychopyLibs(['parallel']) #TODO
        self.order=['startVal','stopVal']

        # Main parameters
        self.params['address'] = Param(address, valType='str')

    def writeInitCode(self, buff):
        buff.writeIndented("1+1")

    def writeRoutineStartCode(self, buff):
        buff.writeIndented("1+1")

    def writeFrameCode(self, buff):
        buff.writeIndented("1+1")

    def writeRoutineEndCode(self, buff):
        buff.writeIndented("1+1")
