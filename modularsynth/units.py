# Author:  Martin McBride
# Created: 2020-04-19
# Copyright (C) 2020, Martin McBride
# License: MIT

from modularsynth import namestore
import pystache


class Unit:

    def __init__(self):
        self.output = dict()
        self.params = dict()
        self.children = []

    def get_output(self, name='out'):
        return self.output[name]

    def get_code(self):
        return []

    def get_function_tables(self):
        return []

    def get_input(self, name):
        return str(self.params[name])

    def set_input(self, name, value):
        self.params[name] = value

    def connect(self, in_name, source, source_out='out'):
        self.params[in_name] = source.get_output(source_out)
        self.children.append(source)

    def join_params(self, *args):
        return ', '.join(args)


class Instrument:

    def __init__(self, source, sequencer):
        self.source = source
        self.sequencer = sequencer
        self.id = namestore.get_instrument()

    def get_code(self):
        code = []
        code.append(pystache.render('instr {{id}}',
                                    {'id': str(self.id)}))
        sources = self.source.get_code()
        code += sources
        code.append(pystache.render('out {{output}}',
                                    {'output': self.source.get_output()}))
        code.append('endin')
        return code

    def get_function_tables(self):
        return self.source.get_function_tables()

    def get_score(self):
        return self.sequencer.get_events(self.id)


class Sine_unit(Unit):

    def __init__(self):
        super().__init__()
        self.output['out'] = namestore.get_audio_variable()
        self.params['amplitude'] = '1'
        self.params['frequency'] = '440'
        self.params['offset'] = '0'
        self.function_table = [namestore.get_function_table()]

    def get_code(self):
        code = []
        for source in self.children:
            code += source.get_code()
        code.append(pystache.render('{{out}} oscil {{amp}}, {{freq}}, {{f0}}',
                                    {'out': self.output['out'],
                                     'amp': self.params['amplitude'],
                                     'freq': self.params['frequency'],
                                     'f0': self.function_table[0]}))
        return code

    def get_function_tables(self):
        ftable = []
        for source in self.children:
            ftable += source.get_function_tables()
        ftable.append(pystache.render('f {{f0}} 0 32768 10 1', {'f0': self.function_table[0]}))
        return ftable

class AD_unit(Unit):

    def __init__(self):
        super().__init__()
        self.output['out'] = namestore.get_audio_variable()
        self.envelope = namestore.get_audio_variable()
        self.params['source'] = '0'
        self.params['attack'] = '.1'
        self.function_table = [namestore.get_function_table()]

    def get_code(self):
        code = []
        for source in self.children:
            code += source.get_code()
        code.append(pystache.render('{{env}} adsr {{attack}}, .5, 0, 0\n{{out}} = {{env}} * {{source}}',
                                    {'out': self.output['out'],
                                     'source': self.params['source'],
                                     'env': self.envelope,
                                     'attack': self.params['attack']}))
        return code

    def get_function_tables(self):
        ftable = []
        for source in self.children:
            print(source, source.get_function_tables())
            ftable += source.get_function_tables()
        return ftable

