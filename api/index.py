from flask import Flask, render_template, request, redirect, url_for, session
import csv
import os
import re

app = Flask(__name__, template_folder="../templates") 
app.secret_key = "dlrjsduwnstoddlfdmfdnlgksdnpqtkdslxm"
app.config["SESSION_PERMANENT"] = False

session_initialized = False 

PASSWORD = {20243262, 20241962, 20241965, 20243272, 20241989, 20243264, 20243283, 20241971, 20241972, 20241974, 20241978, 20241984, 20243282, 20241982}

@app.before_request
def clear_session_on_restart():
    global session_initialized
    if not session_initialized:
        session.clear()
        session_initialized = True

@app.route('/')
def main():
    authenticated = session.get("authenticated", False)  # 👈 세션 값 저장
    return render_template('main.html', authenticated=authenticated)

@app.route("/gallery")
def gallery():
    if not session.get("authenticated"):
        return redirect(url_for("authentication"))
    image_folder = "static/images/gallery"
    image_files = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png", ".jpeg"))]
    
    image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]))

    photos = [{"src": f"/{image_folder}/{img}"} for img in image_files]

    return render_template("gallery.html", photos=photos)

def load_messages():
    messages = []
    with open("static/roll.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            messages.append(row)

    messages = sorted(messages, key=lambda x: (not bool(re.match(r"^[가-힣]", x["이름"])), x["이름"].strip()))

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
    return render_template("main.html")

# Vercel에서 Flask 실행을 위한 WSGI 핸들러 설정
# 여기서 app을 handler로 설정해야 함
handler = app
