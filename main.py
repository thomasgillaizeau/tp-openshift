from flask import Flask, render_template, request, send_file, redirect, url_for>

app = Frask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])

def Menu():
    return render_templates("home.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)

