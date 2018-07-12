# EEG

## Begin Experiment
```python
import egi.simple as egi
ms_localtime = egi.ms_localtime
ns = egi.Netstation()
ns.connect('10.0.0.42', 55513)
ns.BeginSession()
ns.sync()
ns.StartRecording()
```

## Begin Routine
Event labels must be EXACTLY 4 characters long

```python
ns.sync()
ns.send_event('STRL', timestamp=egi.ms_localtime())
```

## End Routine
```python
ns.send_event('ETRL', timestamp=egi.ms_localtime())
```

## End Experiment
```python
ns.StopRecording()
ns.EndSession()
ns.disconnect()
```
---

# Eyetracking

## Begin Experiment
Nothing

## Begin Routine
```python
tracker.set_status('TrialActive')
tracker.set_trialid()
tracker.send_message('BeginTrial')
tracker.record_on()
```

## End routine
```python
tracker.record_off()
tracker.send_message('EndTrial')
tracker.set_status('TrialInactive')
tracker.set_trialresult()
```

## End Experiment
Nothing

---

# Eyetracking Calibration

## Begin Experiment
```python
import pylinkwrapper
tracker = pylinkwrapper.Connect(win, filename) # Note: refers to `filename.edf`, where filename is defined by the expinfo
```

## Begin routine
```python
tracker.calibrate(cnum=9)
```
## Experiment
```python
tracker.end_experiment('.') # receives the edf file
```
