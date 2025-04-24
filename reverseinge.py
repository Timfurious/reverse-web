import re

def extract_patterns(file_path):
    results = {
        "urls": [],
        "ips": [],
        "tokens": [],
        "webhooks": [],
        "emails": [],
        "aws_keys": [],
        "jwt": [],
        "api_keys": [],
        "discord_tokens": [],
        "slack_hooks": [],
        "github_tokens": []
    }

    try:
        # Open the file and read its content
        with open(file_path, 'rb') as f:
            data = f.read().decode('latin1', errors='ignore')

        # --- Enhanced Regex Patterns ---
        results["urls"] = list(set(re.findall(r'https?://[^\s\'"<>]+', data)))
        results["ips"] = list(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)))
        results["webhooks"] = list(set(re.findall(r'https://discord(?:app)?\.com/api/webhooks/[^\s\'"<>]+', data)))
        results["tokens"] = list(set(re.findall(r'[A-Za-z0-9_\-]{24,}', data)))
        results["emails"] = list(set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', data)))
        results["aws_keys"] = list(set(re.findall(r'AKIA[0-9A-Z]{16}', data)))
        results["jwt"] = list(set(re.findall(r'eyJ[a-zA-Z0-9\-_]+?\.[a-zA-Z0-9\-_]+?\.[a-zA-Z0-9\-_]+', data)))

        # --- Additional Enhanced Patterns ---
        results["api_keys"] = list(set(re.findall(r'(?i)(api[_\-]?key|token)[^\s]{0,5}[:=][^\s\'"]{10,}', data)))  # Generic API keys
        results["discord_tokens"] = list(set(re.findall(r'([MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27})', data)))  # Discord Bot tokens
        results["slack_hooks"] = list(set(re.findall(r'https://hooks.slack.com/services/[A-Za-z0-9]+/[A-Za-z0-9]+/[A-Za-z0-9]+', data)))  # Slack Webhooks
        results["github_tokens"] = list(set(re.findall(r'ghp_[0-9a-zA-Z]{36}', data)))  # GitHub Tokens

    except Exception as e:
        print(f"Error occurred while processing the file: {e}")

    return results
