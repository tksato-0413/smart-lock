# ベースとなるイメージを指定（例: python 3.10）
FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Djangoプロジェクトのソースコードをコピー
COPY . .

# サーバーの起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

