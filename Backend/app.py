# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from enhancer import enhance_prompt
from history_mananger import save_history, get_history
from prompt_library import get_library, search_library

app = Flask(__name__, static_folder="../frontend")
CORS(app)


# ── Serve Frontend Pages ──────────────────────────────
@app.route("/")
def index():
    return send_from_directory("../frontend/pages", "index.html")

@app.route("/history")
def history_page():
    return send_from_directory("../frontend/pages", "history.html")

@app.route("/library")
def library_page():
    return send_from_directory("../frontend/pages", "library.html")

# ── Serve Static Files (css, js, assets) ─────────────
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("../", filename)


# ── API: Enhance Prompt ───────────────────────────────
@app.route("/api/enhance", methods=["POST"])
def enhance():
    data = request.get_json()

    user_prompt = data.get("prompt", "")
    mode        = data.get("mode", "normal")

    if not user_prompt.strip():
        return jsonify({"success": False, "error": "Prompt is empty."}), 400

    result = enhance_prompt(user_prompt, mode)

    if result["success"]:
        save_history(user_prompt, result["enhanced_prompt"], mode)

    return jsonify(result)


# ── API: Get History ──────────────────────────────────
@app.route("/api/history", methods=["GET"])
def history():
    return jsonify(get_history())


# ── API: Clear History ────────────────────────────────
@app.route("/api/history/clear", methods=["DELETE"])
def clear_history():
    from history_mananger import clear_history as ch
    ch()
    return jsonify({"success": True, "message": "History cleared."})


# ── API: Prompt Library ───────────────────────────────
@app.route("/api/library", methods=["GET"])
def library():
    category = request.args.get("category", "all")
    return jsonify(get_library(category))

@app.route("/api/library/search", methods=["GET"])
def library_search():
    query = request.args.get("q", "")
    return jsonify(search_library(query))


# ── Run Server ────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)