from flask import Flask
import os

app = Flask(name)

@app.route("/")
def home():
    return "Flask + Docker + GHCR + Terraform + Render"

@app.route("/health")
def health():
    return {"status": "Tout est ok ou pas"}

@app.route("/info")
def info():
    return {
        "app": "Flask Render",
        "student": "Ndeye Gnamou Faye",
        "version": "v1"
    }

@app.route("/env")
def env():
    return {"env": os.getenv("ENV")}
