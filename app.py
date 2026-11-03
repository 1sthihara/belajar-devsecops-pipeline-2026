
"""Sentinel Flask Application.

Aplikasi portal sederhana untuk mengakses halaman Sentinel.
Tidak menggunakan autentikasi maupun database.
"""

from flask import Flask,jsonify, render_template

APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def portal():
    """Menampilkan halaman utama Sentinel Portal."""
    return render_template("portal.html")


@APP.route("/dashboard", methods=["GET"])
def dashboard():
    """Menampilkan halaman dashboard."""
    return render_template("dashboard.html")


@APP.route("/index", methods=["GET"])
def index():
    """Menampilkan halaman index."""
    return render_template("index.html")


@APP.route("/register", methods=["GET"])
def register():
    """Menampilkan halaman registrasi."""
    return render_template("register.html")

@APP.route("/sentinel/pulse", methods=["GET"])
def sentinel_pulse():
    """Menyediakan informasi heartbeat aplikasi."""
    return jsonify({
        "service": "Sentinel Flask Application",
        "status": "operational",
        "environment": "docker",
        "pipeline": "github-actions",
    })


@APP.route("/deployment-manifest", methods=["GET"])
def deployment_manifest():
    """Menyediakan informasi deployment aplikasi."""
    return jsonify({
        "application": "Sentinel Flask",
        "version": "PBL-CICD-03",
        "container": "secure-flask-app",
        "deployment": "automatic",
        "pipeline": "GitHub Actions",
    })

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
