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
    user_token = simpledialog.askstring("Input", "Enter your token:")

    if user_name and user_email and user_token:  # 이름, 이메일, 토큰 값이 모두 입력된 경우
        user_info = load_user_info()
        new_key = f"User{len(user_info) + 1}"  # 새로운 키 생성
        user_info[new_key] = {
            'name': user_name,
            'email': user_email,
            'token': user_token  # 토큰 값 저장
        }
        save_user_info(user_info)  # 수정된 정보 저장
    else:
        log_text.insert(tk.END, "Invalid input. Please enter name, email, and token.\n")



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

def set_git_user(name, email, token):
    try:
        subprocess.run(["git", "config", "--global", "user.name", name], check=True)
        subprocess.run(["git", "config", "--global", "user.email", email], check=True)
        log_text.insert(tk.END, "Git user info set successfully.\n")
        
        if platform.system() == 'Windows':
            add_git_credentials(name, token)
        return True
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Failed to set user info: {e}\n")
        return False

def add_git_credentials(username, token):
    try:
        if platform.system() == 'Windows':
            subprocess.run(["cmdkey", "/generic:git:https://github.com", "/user:" + username, "/pass:" + token], check=True)
            log_text.insert(tk.END, "Git credentials added successfully.\n")
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Failed to add credentials: {e}\n")


def choose_user_info():
    user_info = load_user_info()
    choices = []
    for key, value in user_info.items():
        choices.append(f"ID: {value['name']} / Email: {value['email']}")
    
    choice_str = "\n".join(f"{i+1}. {choice}" for i, choice in enumerate(choices))
    choice_str += f"\n{len(choices)+1}. Enter new user"
    user_choice = simpledialog.askstring("Choose User Info", f"Choose user number:\n{choice_str}")
    
    try:
        user_choice = int(user_choice) - 1
    except (ValueError, TypeError):
        log_text.insert(tk.END, "Invalid choice, please enter a valid number.\n")
        return
    
    if user_choice < len(choices):
        selected_key = list(user_info.keys())[user_choice]
        set_git_user(user_info[selected_key]['name'], user_info[selected_key]['email'], user_info[selected_key]['token'])
    elif user_choice == len(choices):
        create_git_user()
    else:
        log_text.insert(tk.END, "Invalid choice.\n")


def list_git_config():
    try:
        result = subprocess.run(["git", "config", "--global", "--list"], capture_output=True, text=True)
        log_text.insert(tk.END, result.stdout + "\n")
    except subprocess.CalledProcessError as e:
        log_text.insert(tk.END, f"Failed to list git config --global --list: {e}\n")


def create_ui():
    global log_text
    window = tk.Tk()
    window.title("Git Configuration Tool")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    create_user_button = tk.Button(frame, text="계정 생성", command=create_git_user)  # 새 버튼 추가
    create_user_button.pack(fill=tk.X)


    user_info_button = tk.Button(frame, text="계정 설정", command=choose_user_info)
    user_info_button.pack(fill=tk.X)


    list_config_button = tk.Button(frame, text="계정 정보 보기", command=list_git_config)
    list_config_button.pack(fill=tk.X)

    delete_button = tk.Button(frame, text="로컬에 등록된 계정 삭제", command=delete_git_credentials)
    delete_button.pack(fill=tk.X)

    log_text = tk.Text(frame, height=20, width=100)
    log_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
