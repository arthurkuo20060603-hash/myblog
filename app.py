from flask import Flask, render_template

app = Flask(__name__)

# 模擬部落格文章資料
posts = [
    {
        "id": 1,
        "title": "第一篇文章：開始寫作！",
        "author": "郭庭瑋",
        "content": "這是我的第一篇部落格文章。使用 Flask 真的很有趣！"
    },
    {
        "id": 2,
        "title": "Flask 模板教學",
        "author": "郭庭瑋",
        "content": "Flask 的 Jinja2 模板讓我們能輕鬆將後端資料渲染到前端。"
    },
    {
        "id": 3,
        "title": "Python 真香",
        "author": "郭庭瑋",
        "content": "今天來聊聊為什麼我喜歡用 Python 來做專案。"
    }
]

@app.route("/")
def index():
    # 首頁：顯示所有文章標題
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    # 根據 id 顯示單篇文章
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
