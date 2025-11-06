from urllib.parse import urlparse

def analyze_text(text):
    scam_words = ["arrest", "warrant", "fine", "pay now", "cyber cell", "legal notice"]
    hits = [w for w in scam_words if w in text.lower()]
    if hits:
        return f"🚨 Scam Detected! Found: {', '.join(hits)}"
    return "✅ Message appears safe."

def check_email_sender(email):
    fake_domains = ["gov-in.net", "cybercell-gov.com", "police-secure.in"]
    if any(d in email.lower() for d in fake_domains):
        return "🚨 Fake or phishing email detected!"
    if email.endswith(".gov.in"):
        return "✅ Verified government domain."
    return "⚠️ Unknown domain — please verify manually."

def check_website_url(url):
    try:
        domain = urlparse(url).netloc.lower()
        if domain.endswith(".gov.in"):
            return "✅ Official government website detected."
        elif any(x in domain for x in ["secure", "verify", "govin-security"]):
            return f"⚠️ Suspicious website: {domain}"
        else:
            return f"⚠️ Non-official domain: {domain}"
    except:
        return "⚠️ Invalid website format."
