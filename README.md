# Hardware Control
The `hardware` directory contains a module for controlling Eyelink and Netstation hardware from a PsychoPy experiment. This can be done using either the coder or builder approach

- If using the coder, follow the example in hardware/code.md (just an example of using existing libraries)
- If using the builder, follow the directions under "Using Builder Components", and/or see the included .psyexp for a modified version of the StroopDemo.

---
## Prerequisites
- PsychoPy2 (version 1.9 or higher)
- For Eyelink: https://github.com/ndiquattro/pylinkwrapper
- For Nestation: https://github.com/gaelen/python-egi

To install these modules in PsychoPy (standalone version), clone or download the repositories and place them in PsychoPy/lib/site-libraries (eg: `C:\Program Files\PsychoPy2\lib\site-libraries`)

To install these modules in PsychoPy (environment version), clone or download and install with the respective setup.py files.

---
## Installation
1. Download the repositories be either:
  - "Download Zip" and placing wherever you desire
  - Cloning into wherever you desire.
2. Open PsychoPy, and go to File > Preferences > Builder > Component path
3. In the text box, add the full path to wherever you placed the repository
4. Restart PsychoPy

---
## Using the Builder components
The installation creates two new builder components "startHardware" and "syncHardware". You must include each of these in your experiment in order for the system to work.

- startHardware:
  - Include **only one** of these components in the entire experiment, preferably in a routine just before the experiment starts, but after any subject instructions.
  - There are 4 parameters to pay attention to:
    - *ifNet*: Whether or not to record EEG
    - *ifEye*: Whether or not to record eyetracking
    - *netIP*: IP address of your nestation computer
    - *netPort*: Port to communicate with Netstation
  - **Note:** `ifNet` and `ifEye` will turn off (and on) all code related to their hardware. So, you can add all syncHardware components, and toggle off when running behavioral only studies (eg: piloting, or debugging behavioral experiment on a non-recording computer)

- syncHardware:
  - This is the main component you will be placing in all of your trial and calibration routines.
  - Parameters:
    - *ifCalibrate* Whether or not to run calibration (typically NOT desired every trial)
    - *RecordEye* Whether or not to record eye movement during this routine (eg, may not want on during ITI)
    - *startMessage*: Message to stamp onto the EEG at begining of routine (eg "BTRL", "BITI")
    - *endMessage*: Message to stamp onto EEG at end of routine (eg: "ETRL", "EITI")
  - **Note:** `startMessage` and `endMessage` must be exactly 4 characters long, per EGI requirements.
