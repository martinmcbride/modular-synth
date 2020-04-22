# Author:  Martin McBride
# Created: 2020-04-19
# Copyright (C) 2020, Martin McBride
# License: MIT

def write(fname, instrument):
    with open(fname, 'w') as outfile:
        outfile.write('<CsoundSynthesizer>\n')
        outfile.write('<CsOptions>\n')
        outfile.write('-odac\n')
        outfile.write('</CsOptions>\n')
        outfile.write('<CsInstruments>\n')
        outfile.write('sr = 44100\n')
        outfile.write('ksmps = 32\n')
        outfile.write('nchnls = 2\n')
        outfile.write('0dbfs  = 1\n')

        for s in instrument.get_code():
            outfile.write(s +'\n')
        outfile.write('\n')
        outfile.write('</CsInstruments>\n')
        outfile.write('<CsScore>\n')
        outfile.write('; sine wave.\n')
        for s in instrument.get_function_tables():
            outfile.write(s +'\n')
        outfile.write('\n')
        for s in instrument.get_score():
            outfile.write(s +'\n')
        outfile.write('e\n')
        outfile.write('</CsScore>\n')
        outfile.write('</CsoundSynthesizer>\n')
