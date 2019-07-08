#!/usr/bin/env python3

#In case of OSError: [Errno 8]
#https://stackoverflow.com/questions/55271912/flask-cli-throws-oserror-errno-8-exec-format-error-when-run-through-docker

#Reading data from a file, displaying and updating the display periodically. Got quite a bit of inspiration from https://github.com/alysivji/talks/blob/master/data-science-workflows-using-docker-containers/workflow3-data-driven-app/plot_timeseries.py


import pandas


def tail_file(filename, nlines):
    '''Return last nlines of file
    Adapted from https://gist.github.com/amitsaha/5990310
    '''
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        endf = position = qfile.tell()
        linecnt = 0
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n" and position != endf-1:
                linecnt += 1

            if linecnt == nlines:
                break
            position -= 1

        if position < 0:
            qfile.seek(0)

        return qfile.read()


def get_data(filename, nlines=20):
    '''Get data from tail of text file into pandas df
    '''

    # read in file
    input_data = tail_file(filename, nlines)
    x = []
    y = []
    with io.StringIO(input_data) as f:
        for line in f:
            items = line.strip().split(', ')
            x.append(items[0])
            y.append(items[1])

return TwoDPlot(x, y)