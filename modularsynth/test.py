from modularsynth import csoundwriter, units, sequencers
import os

sine = units.Sine_unit()
env = units.AD_unit()
sequencer = sequencers.SequencerBase('frequency', 'amplitude')

sine.connect('frequency', sequencer, 'frequency')
sequencer.add(start=0, duration=1, frequency=440, amplitude=1)
sequencer.add(start=1, duration=1, frequency=880, amplitude=1)

env.connect('source', sine, 'out')

instrument = units.Instrument(env, sequencer)

csoundwriter.write('test.csd', instrument)
#os.system('csound test.csd')
#os.system('aplay test.wav')

