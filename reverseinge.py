import re

def extract_patterns(file_path):
    results = {
        "urls": [],
        "ips": [],
        "tokens": [],
        "webhooks": [],
        "emails": [],
        "aws_keys": [],
        "jwt": []
    }

    with open(file_path, 'rb') as f:
        data = f.read().decode('latin1', errors='ignore')

    # Regex bien propres
    results["urls"] = list(set(re.findall(r'https?://[^\s\'"<>]+', data)))
    results["ips"] = list(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)))
    results["webhooks"] = list(set(re.findall(r'https://discord(?:app)?\.com/api/webhooks/[^\s\'"<>]+', data)))
    results["tokens"] = list(set(re.findall(r'[A-Za-z0-9_\-]{24,}', data)))
    results["emails"] = list(set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', data)))
    results["aws_keys"] = list(set(re.findall(r'AKIA[0-9A-Z]{16}', data)))
    results["jwt"] = list(set(re.findall(r'eyJ[a-zA-Z0-9\-_]+?\.[a-zA-Z0-9\-_]+?\.[a-zA-Z0-9\-_]+', data)))

    return results
