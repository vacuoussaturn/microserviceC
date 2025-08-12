from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

posts = []

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.json
    author = data.get('author', 'Anonymous')
    content = data.get('content', '').strip()

    if not content:
        return jsonify({"error": "Content is required"}), 400

    post = {"author": author, "content": content}
    posts.append(post)
    return jsonify(post), 201

if __name__ == '__main__':
    app.run(port=7011, debug=True)
