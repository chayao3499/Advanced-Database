#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.1
import datetime
import time


def getTime():
    '''
    return time is format of time(unit is second)
    '''
    return time.time()


def getCPUClockTime():
    '''
    return time is CPU Clock time
    '''
    return time.clock()


def formatTime(timevalue):
    '''
    format the time numbers
    '''
    hour = 0
    minute = 0
    second = 0
    if timevalue > 0:
        #count hour
        hour = timevalue // 3600
        remain = timevalue % 3600
        #count minute
        minute = remain // 60
        remain = remain % 60
        #count second
        second = round(remain, 3)
    return '%.0fh:%.0fm:%.3fs'%(hour, minute, second)
        

if __name__=='__main__':
    value = 134.45632
    print value
    print formatTime(value)
    
