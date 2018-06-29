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
Must be "fld1" ... "fldN", but actual information can contain anything.
```python
ns.sync()
ns.send_event('evt_', label="event", timestamp=egi.ms_localtime(),
              table = {'fld1' : "BeginTrial","fld2" : "Nothing"})
```

## End Routine
```python
ns.send_event('evt_', label="event", timestamp=egi.ms_localtime(),
              table = {'fld1' : "EndTrial","fld2" : "Nothing2"})
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
pass

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
pass

---

# Eyetracking Calibration

## Begin Experiment
```python
import pylinkwrapper
tracker = pylinkwrapper.Connect(win, 'test822') #TODO: expInfo
```

## Begin routine
```python
tracker.calibrate(cnum=9)
```
## Experiment
```python
tracker.end_experiment('.')
```
