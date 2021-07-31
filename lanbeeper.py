#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# based on https://stackoverflow.com/q/19794695

from flask import Flask, render_template, request

import subprocess
def beep():
    subprocess.call([
        b'notify-send',
        b'-u', b'critical',
        b'LanBeeper',
        b'X' * 140
    ])

uitxt = {
    'html_dir': 'ltr',
    'html_lang': 'en',
    'send_beep': 'Send Beep!',
}
beep_sent_msg = 'Beep Sent!'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'beep' in request.form:
            beep()
            return render_template('lanbeeper.html', **uitxt, msg=beep_sent_msg)
    return render_template('lanbeeper.html', **uitxt)


if __name__ == '__main__':
    # app.run(host='192.168.1.2', port='8000')
    app.run(host='0.0.0.0')

