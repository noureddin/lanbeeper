#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# based on https://stackoverflow.com/q/19794695

from flask import Flask, render_template, request
from configparser import RawConfigParser
import subprocess
import sys
import os

def render(**kw):
    return render_template('lanbeeper.html', **tr, **kw)

def notify(msg=None):
    subprocess.call([
        b'notify-send',
        b'-u', b'critical',
        b'LanBeeper',
        b'X' * 140 if msg is None else msg.encode('utf-8')
    ])


# 4 cases for the first cli argument:
# - no argument: use ./translation/en.ini
# - a file: read it.
# - a language code: read ./translation/{arg}.ini
# - otherwise: warning and use ./translation/en.ini

def translation_file_of_language(lang):
    return os.path.join(os.path.dirname(__file__), f'translation/{lang}.ini')

def read_translation_file(file):
    conf = RawConfigParser()
    conf.read(file)
    return dict(conf['DEFAULT'])


try:
    firstarg = sys.argv[1]
except:
    firstarg = None

tr = None
if firstarg is not None:
    if os.path.exists(firstarg):
        tr = read_translation_file(firstarg)
    else:
        file = translation_file_of_language(firstarg)
        if os.path.exists(file):
            tr = read_translation_file(file)
        else:
            print(f'Warning: the given argument `{firstarg}` is neither a file nor a supported language code. Using English.', file=sys.stderr)

if tr is None:
    tr = read_translation_file(translation_file_of_language('en'))


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'beep' in request.form:
            notify()
            return render(msg=tr['beep_sent_msg'])
        if 'text' in request.form:
            notify(request.form['textarea'])
            return render(msg=tr['text_sent_msg'])
    return render()


if __name__ == '__main__':
    # https://stackoverflow.com/q/7023052
    app.run(host='0.0.0.0', port=5000)

