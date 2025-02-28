from flask import Flask, render_template, request, redirect, url_for, session, Flask
import csv
import os
import re
from flask_static_digest import FlaskStaticDigest


app = Flask(__name__, static_folder="../static", template_folder="../templates")
# static/images/gallery 폴더가 없으면 자동 생성
gallery_path = "static/images/gallery"
if not os.path.exists(gallery_path):
    os.makedirs(gallery_path)
# FlaskStaticDigest(app)
app.secret_key = "dlrjsduwnstoddlfdmfdnlgksdnpqtkdslxm"
app.config["SESSION_PERMANENT"] = False

session_initialized = False

PASSWORD = {20243262, 20241962, 20241965, 20243272, 20241989, 20243264, 20243283, 20241971, 20241972, 20241974, 20241978, 20241984, 20243282, 20241982}

@app.before_request
def clear_session_on_restart():
    global session_initialized
    if not session_initialized:
        session.clear()
        session.permanent = False
        session_initialized = True

@app.route('/')
def main():
    authenticated = session.get("authenticated", False)
    return render_template('main.html', authenticated=authenticated)

@app.route("/gallery")
def gallery():
    if not session.get("authenticated"):
        return redirect(url_for("authentication"))
    image_folder = os.path.join(app.static_folder, "images/gallery")
    image_files = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png", ".jpeg"))]
    
    image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]))

    photos = [{"src": url_for('static', filename=f"images/gallery/{img}")} for img in image_files]

    return render_template("gallery.html", photos=photos)

def load_messages():
    messages = []
    with open("static/roll.csv", "r", encoding="utf-8", errors="ignore") as file:
        reader = csv.DictReader(file)
        for row in reader:
            messages.append(row)

    messages = sorted(messages, key=lambda x: (not re.match(r"^[가-힣]", x["이름"] or ""), x["이름"].strip()))

    return messages

@app.route("/rolling_paper")
def rolling_paper():
    messages = load_messages()
    return render_template("rolling_paper.html", messages=messages)

@app.route("/authentication", methods=["GET", "POST"])
def authentication():
    if request.method == "POST":
        entered_password = request.form.get("password")
        next_page = request.form.get("next", "/")
        try:
            entered_password = int(entered_password)
        except ValueError:
            return render_template("authentication.html", error="숫자만 입력하세요!", next=next_page)

        if entered_password in PASSWORD:
            session["authenticated"] = True
            return redirect(next_page)
        else:
            return render_template("authentication.html", error="비밀번호가 틀렸습니다!", next=next_page)
    return render_template("authentication.html", next=request.args.get("next", "/"))

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return redirect(url_for("main"))

# Vercel에서 Flask 실행을 위한 WSGI 핸들러 설정
handler = app

from flask import send_from_directory

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

