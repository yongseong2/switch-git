import tkinter as tk
from tkinter import simpledialog
import subprocess
import platform
import json

# 사용자 정보 저장
def save_user_info(info_dict):
    try:
        with open('./git_user_info.json', 'w') as file:
            json.dump(info_dict, file)
    except Exception as e:
        print(f"Error saving user info: {e}")

# 사용자 정보 불러오기
def load_user_info():
    try:
        with open('./git_user_info.json', 'r') as file:
            data = file.read()
            # 파일 내용이 비어있는 경우 빈 딕셔너리 반환
            if not data:
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

    
def create_git_user():
    user_name = simpledialog.askstring("Input", "Enter your name:")
    user_email = simpledialog.askstring("Input", "Enter your email:")
    if user_name and user_email:
        user_info = load_user_info()
        new_key = f"User{len(user_info) + 1}"  # 새로운 키 생성
        user_info[new_key] = {'name': user_name, 'email': user_email}
        save_user_info(user_info)  # 수정된 정보 저장
    else:
        log_text.insert(tk.END, "Invalid input. Please enter both name and email.\n")


def delete_git_credentials():
    os_name = platform.system()
    try:
        if os_name == 'Windows':
            subprocess.run(["cmdkey", "/delete:git:https://github.com"], check=True)
        elif os_name == 'Darwin':
            subprocess.run(["security", "delete-generic-password", "-s", "github.com"], check=True)
        elif os_name == 'Linux':
            # Linux용 자격증명 삭제 코드
            pass
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Already deleted: {e}\n")

def set_git_user(name, email):
    try:
        subprocess.run(["git", "config", "--global", "user.name", name], check=True)
        subprocess.run(["git", "config", "--global", "user.email", email], check=True)
        log_text.insert(tk.END, "Git user info set successfully.\n")
        return True  # 성공적으로 설정되었음을 나타내는 True 반환
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Failed to set user info: {e}\n")
        return False  # 실패했음을 나타내는 False 반환

def choose_user_info():
    user_info = load_user_info()
    choices = []
    for key, value in user_info.items():
        name_email_str = f"ID: {value['name']} / Email: {value['email']}"  # 사용자 정보를 문자열로 포맷팅
        choices.append(name_email_str)
    
    choice_str = "\n".join(f"{i+1}. {choice}" for i, choice in enumerate(choices))
    choice_str += f"\n{len(choices)+1}. Enter new user field name"
    user_choice = simpledialog.askstring("Choose User Info", f"Choose user number:\n{choice_str}")
    
    try:
        user_choice = int(user_choice) - 1
    except (ValueError, TypeError):
        log_text.insert(tk.END, "Invalid choice, please enter a valid number.\n")
        return
    
    if user_choice < len(choices):
        selected_key = list(user_info.keys())[user_choice]
        success = set_git_user(user_info[selected_key]['name'], user_info[selected_key]['email'])
        if success:
            delete_git_credentials()
    elif user_choice == len(choices):  # 새로운 사용자 정보 입력
        create_git_user()  # 사용자 생성 함수 호출
    else:
        log_text.insert(tk.END, "Invalid choice.\n")


def list_git_config():
    try:
        result = subprocess.run(["git", "config", "--list"], capture_output=True, text=True)
        log_text.insert(tk.END, result.stdout + "\n")
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Failed to list git config: {e}\n")


def create_ui():
    global log_text
    window = tk.Tk()
    window.title("Git Configuration Tool")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    create_user_button = tk.Button(frame, text="Create Git User", command=create_git_user)  # 새 버튼 추가
    create_user_button.pack(fill=tk.X)


    user_info_button = tk.Button(frame, text="Set Git User Info", command=choose_user_info)
    user_info_button.pack(fill=tk.X)


    list_config_button = tk.Button(frame, text="List Git Config", command=list_git_config)
    list_config_button.pack(fill=tk.X)

    delete_button = tk.Button(frame, text="Delete Git Credentials", command=delete_git_credentials)
    delete_button.pack(fill=tk.X)

    log_text = tk.Text(frame, height=20, width=100)
    log_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
