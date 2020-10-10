from flask import Flask, request, make_response, send_file, render_template, request, jsonify
import os
import io
import zipfile

app = Flask(__name__)

@app.route("/download")
def download():
    fo = io.BytesIO()
    with zipfile.ZipFile(fo, "w") as zf:
        zf.write("memo.md", "memo.md")

    fo.seek(0)

    response = make_response(fo.read())
    response.headers.set('Content-Type', 'zip')
    response.headers.set('Content-Disposition', 'attachment', filename="Time.zip")

    return response

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)