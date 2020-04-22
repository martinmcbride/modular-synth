# Author:  Martin McBride
# Created: 2020-04-19
# Copyright (C) 2020, Martin McBride
# License: MIT

class SequencerBase():

    def __init__(self, *names):
        self.fields = ['start', 'duration', *names]
        self.output = {s:'p'+str(i) for i, s in enumerate(self.fields, 2)}
        self.contents = []

    def get_code(self):
        return []

    def get_output(self, name='out'):
        return self.output[name]

    def get_events(self, instrument_id):
        events = []
        for event in self.contents:
            params = [str(event[s]) for s in self.fields]
            events.append(' '.join([
                'i',
                str(instrument_id),
                *params
            ]))
        return events

    def add(self, **values):
        self.contents.append(values)

    def get_function_tables(self):
        return []
