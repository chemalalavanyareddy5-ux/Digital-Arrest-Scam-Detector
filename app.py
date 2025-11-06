from flask import Flask, render_template, request, jsonify
from scanner import analyze_text, check_email_sender, check_website_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/message')
def message_page():
    return render_template('message.html')

@app.route('/email')
def email_page():
    return render_template('email.html')

@app.route('/website')
def website_page():
    return render_template('website.html')

# ---------- API ENDPOINTS ----------
@app.route('/api/message', methods=['POST'])
def api_message():
    text = request.form.get('message', '').strip()
    if not text:
        return jsonify({'result': '⚠️ Please enter a message to scan!'})
    return jsonify({'result': analyze_text(text)})

@app.route('/api/email', methods=['POST'])
def api_email():
    email = request.form.get('email', '').strip()
    if not email:
        return jsonify({'result': '⚠️ Please enter an email address!'})
    return jsonify({'result': check_email_sender(email)})

@app.route('/api/website', methods=['POST'])
def api_website():
    url = request.form.get('url', '').strip()
    if not url:
        return jsonify({'result': '⚠️ Please enter a website URL!'})
    return jsonify({'result': check_website_url(url)})

if __name__ == '__main__':
    app.run(debug=True)

