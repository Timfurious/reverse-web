# reverse-web

reverse-web is a simple reverse engineering tool designed to extract information such as IP addresses or URLs from executable files.
It uses pattern matching with regular expressions to detect potential indicators of compromise.

The core script, reverseinge.py, reads the binary content of the selected executable and looks for common patterns.

![image](https://github.com/user-attachments/assets/e7dab5b8-fa0e-4dd5-ad7a-3abcfbaf4a0f)

git clone https://github.com/Timfurious/reverse-web.git

cd reverse-web

pip install -r requirements.txt

python3 app.py

and go to 127.0.0.1:5000 in your browser

How It Works

1. The script reverseinge.py opens the selected executable file.

2. It reads the binary content.

3. It scans for specific patterns (e.g. IP addresses, URLs) using regular expressions.

4. Matches are extracted and displayed in the web interface.
