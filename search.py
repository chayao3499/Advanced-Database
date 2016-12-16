#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2012-07-04
#version 1.0
import re
import sys
import os
#http://newcenturycomputers.net/projects/wconio.html
import WConio
import countTime


def getParameters():
    '''
    get parameters from console command
    '''
    ret = []
    if len(sys.argv) < 3 or len(sys.argv) > 4:    
        print 'Please input correct parameter, for example:'
        print 'No1. python search.py keyword filepath'
        print 'No2. python search.py keyword folderpath txt'
    else:
        for i in range(1, len(sys.argv)):
            #print i, sys.argv[i]
            ret.append(sys.argv[i])
        print '+============================================================================+'
        print '  Keyword = %s'%sys.argv[1]
    return ret


def isFileExists(strfile):
    '''
    check the file whether exists
    '''
    return os.path.isfile(strfile)


def isDirExists(strdir):
    '''
    check the dir whether exists
    '''
    return os.path.exists(strdir)


def getFileList(strdir, filetype):
    '''
    get a type of file list in a folder
    '''
    flist = []
    for root, dirs, fileNames in os.walk(strdir):
        if fileNames:
            for filename in fileNames:
                if (filetype == filename.split('.')[1]):
                    filepath = os.path.join(root, filename)
                    flist.append(filepath)
    return flist


def Search(keyword, filename):
    '''
    search the keyword in a assign file
    '''
    if(isFileExists(filename) == False):
        print 'Input filepath is wrong,please check again!'
        sys.exit()
    print '+----------------------------------------------------------------------------+'
    print '  Filename = %s'%filename
    print '+----------------------------------------------------------------------------+'
    linenum = 1
    findtime = 0
    orginalcolor = WConio.gettextinfo()[4]
    with open(filename, 'r') as fread:
        lines = fread.readlines()
        for line in lines:
            rs = re.search(keyword, line)
            if rs:
                #output linenum of keyword place 
                WConio.textcolor(WConio.MAGENTA)
                sys.stdout.write('line:%d '%linenum)
                WConio.textcolor(orginalcolor)
                lsstr = line.split(keyword)
                strlength = len(lsstr)
                findtime = findtime + (strlength - 1)
                #print strlength
                for i in range(strlength):
                    if(i < (strlength - 1)):
                        sys.stdout.write(lsstr[i].strip())
                        WConio.textcolor(WConio.LIGHTGREEN)
                        sys.stdout.write(keyword)
                        WConio.textcolor(orginalcolor)
                    else:
                        sys.stdout.write(lsstr[i].strip() + '\n')
            linenum = linenum + 1
    if findtime > 0:
       print '+----------------------------------------------------------------------------+'
    print '  Search result: find keyword %d times'%findtime
            

def SearchAll(keyword, strdir, filetype):
    '''
    search the keyword in a assign dir
    '''
    if(isDirExists(strdir) == False):
        print 'Input folderpath is wrong,please check again!'
        sys.exit()
    filels = getFileList(strdir, filetype)
    for item in filels:
        Search(keyword, item)
        print '\n'

def executeSearch():
    '''
    this is a execute search method
    '''
    ls = getParameters()
    start = countTime.getTime()
    if(len(ls) == 2):
        Search(ls[0], ls[1])
    elif(len(ls) == 3):
        SearchAll(ls[0], ls[1], ls[2])
    else:
        print 'There is a parameter error occured in executeSearch()!'
    end = countTime.getTime()
    print '+----------------------------------------------------------------------------+'
    print '  Total cost time: %s'%countTime.formatTime(end - start)
    print '+============================================================================+'
    
if __name__=='__main__':
    executeSearch()