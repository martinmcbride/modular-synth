# Author:  Martin McBride
# Created: 2020-04-19
# Copyright (C) 2020, Martin McBride
# License: MIT

__INSTRUMENTS__ = 0
__AUDIO_VARIABLE__ = 0
__CONTROL_VARIABLE__ = 0
__FUNCTION_TABLE__ = 0

def get_instrument():
    '''
    Get next instrument
    :return: int instrument number
    '''
    global __INSTRUMENTS__
    __INSTRUMENTS__ += 1
    return __INSTRUMENTS__

def get_function_table():
    '''
    Get next f table
    :return: int f tabe#le number
    '''
    global __FUNCTION_TABLE__
    __FUNCTION_TABLE__ += 1
    return str(__FUNCTION_TABLE__)

def get_audio_variable():
    '''
    Get next audio variable name
    :return: str audio variable name
    '''
    global __AUDIO_VARIABLE__
    __AUDIO_VARIABLE__ += 1
    return 'a' + str(__AUDIO_VARIABLE__)

def get_control_variable():
    '''
    Get next control variable name
    :return: str control variable name
    '''
    global __CONTROL_VARIABLE__
    __CONTROL_VARIABLE__ += 1
    return 'a' + str(__CONTROL_VARIABLE__)

