#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بناء النسخة المدمجة · Build the single-file standalone

يقرأ index.html ويضمّن كل صور مجلد assets/ بصيغة base64 داخل الملف،
فينتج bayan-standalone.html الذي يعمل دون إنترنت ودون مجلد الصور.

Reads index.html, inlines every assets/ image as a base64 data URI,
and writes bayan-standalone.html (opens offline, no assets folder needed).

التشغيل · Run:   python build-standalone.py
"""
import re, os, base64, mimetypes, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "index.html")
OUT  = os.path.join(HERE, "bayan-standalone.html")

def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

def main():
    if not os.path.exists(SRC):
        sys.exit("index.html not found next to this script.")
    html = open(SRC, encoding="utf-8").read()
    # safety: refuse to build from a truncated/incomplete source
    if "</html>" not in html:
        sys.exit("index.html looks incomplete (no </html>); aborting.")

    cache = {}
    def repl(m):
        pre, path, post = m.group(1), m.group(2), m.group(3)
        full = os.path.join(HERE, path)
        if path not in cache:
            cache[path] = data_uri(full) if os.path.exists(full) else path
        return pre + cache[path] + post

    # inline both src="assets/..." and href="assets/..." (favicon, apple-touch-icon)
    html = re.sub(r'(src=")(assets/[^"]+)(")',  repl, html)
    html = re.sub(r'(href=")(assets/[^"]+)(")', repl, html)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {OUT} ({os.path.getsize(OUT):,} bytes), {len(cache)} assets inlined.")

if __name__ == "__main__":
    main()
