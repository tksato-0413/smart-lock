import sqlite3
import hashlib

def connect_db():
    """ユーザーデータベースにアクセスする関数
    Args:
        None
    Return:
        conn    (connection):データベースに接続するためのオブジェクト
        cursor  (cursor): データベースを操作するためのオブジェクト
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    """ユーザーデータベースを作成するための関数
    Args:
        None
    Return:
        None
    """
    conn, cursor = connect_db()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    print("\nCreated user database.")
    
    conn.commit()
    conn.close()

def add_user():
    """ユーザーを追加する関数
    Args:
        None
    Return:
        None
    """
    
    conn, cursor = connect_db() # データベースを取得
    username = input("Enter Student ID: ") # 学籍番号をユーザーネームとして使用
    password = input("Enter yourname: ") # 学生証での認証を前提としているため、名前をパスワードとして使用
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, hashed_password))
    
    conn.commit()
    conn.close()
    print(f"User {username} added successfully.")
    
def delete_user():
    """ユーザーを削除する関数
    Args:
        None
    Return:
        None
    """
    
    conn, cursor = connect_db() # データベースを取得
    
    username = input("Enter student ID to delete: ")
    password = input("Enter student name")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password)) 
    user = cursor.fetchone() # ユーザーが存在するか確認
    
    if user:
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        print(f"User '{username}' deleted successfully.")
    else:
        print("Incorrect username or password. Unable to delete user.")
    
    conn.close()

if __name__ == "__main__":
    while True:
        print("\nOptions:\n1. Add User\n2. Delete User\n3. Exit\n4. Create Table")
        choice = input("Chose Option: ")
        
        if choice == "1":
            add_user()
        elif choice =="2":
            delete_user()
        elif choice =="3":
            print("Exiting...")
            break
        elif choice =="4":
            create_table()
        else:
            print("Invalid choice. Please select again.")