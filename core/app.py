from flask import Flask, request, render_template, Response

app = Flask(__name__, template_folder='templates', static_folder='static')
