# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import twitter_tweet
import numpy as np

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    # NumPy の random.choice で配列からランダムに取り出し
    return np.random.choice(messages)
    #return messages

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = "ようこそ"
    # message = picked_up()
    message = ""
    # index.html をレンダリングする
    return render_template('index.html',message=message, title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        text = request.form['text']
        consumer_key = request.form['consumer_key']
        consumer_secret = request.form['consumer_secret']
        token = request.form['token']
        token_secret = request.form['token_secret']
        # index.html をレンダリングする
        twitter_tweet.postTweet(consumer_key,consumer_secret,token,token_secret,text)
        #return render_template('index.html',name=name, title=title)
        return render_template('index.html',consumer_key=consumer_key,consumer_secret=consumer_secret,token=token,token_secret=token_secret)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に  
