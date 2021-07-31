#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# based on https://stackoverflow.com/q/19794695

from flask import Flask, render_template, request
import subprocess

def render(**kw):
    return render_template('lanbeeper.html', **uitxt, **kw)

def notify(msg=None):
    subprocess.call([
        b'notify-send',
        b'-u', b'critical',
        b'LanBeeper',
        b'X' * 140 if msg is None else msg.encode('utf-8')
    ])

uitxt = {
    'html_dir': 'ltr',
    'html_lang': 'en',
    'head_msg': '', # 'Welcome to LanBeeper!',
    'send_beep': 'Send Beep!',
    'send_text': 'Send Text!',
    'send_text_lbl': 'Or, send a text message instead:',
}
beep_sent_msg = 'Beep Sent!'
text_sent_msg = 'Text Sent!'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'beep' in request.form:
            notify()
            return render(msg=beep_sent_msg)
        if 'text' in request.form:
            notify(request.form['textarea'])
            return render(msg=text_sent_msg)
    return render()


if __name__ == '__main__':
    # app.run(host='192.168.1.2', port='8000')
    app.run(host='0.0.0.0')

