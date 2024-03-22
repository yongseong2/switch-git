import tkinter as tk
from tkinter import simpledialog
import subprocess
import platform

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
        log_text.insert(tk.END, f"Failed to delete credentials: {e}\n")

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
    choice = simpledialog.askinteger("Input", "Choose user type (1 for Personal, 2 for Company, 3 for Custom):")
    success = False  # 성공 여부를 추적하는 변수

    if choice == 1:
        success = set_git_user("#CUSTOM", "#CUSTOM")
    elif choice == 2:
        success = set_git_user("#CUSTOM", "#CUSTOM")
    elif choice == 3:
        user_name = simpledialog.askstring("Input", "Enter your name:")
        user_email = simpledialog.askstring("Input", "Enter your email:")
        if user_name and user_email:
            success = set_git_user(user_name, user_email)
        else:
            log_text.insert(tk.END, "Invalid input. Please enter both name and email.\n")
    else:
        log_text.insert(tk.END, "Invalid choice, please enter 1, 2, or 3.\n")

    if success:
        delete_git_credentials()  # 성공적으로 사용자 정보가 설정된 후에만 자격증명 삭제를 실행

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

    delete_button = tk.Button(frame, text="Delete Git Credentials", command=delete_git_credentials)
    delete_button.pack(fill=tk.X)

    user_info_button = tk.Button(frame, text="Set Git User Info", command=choose_user_info)
    user_info_button.pack(fill=tk.X)

    list_config_button = tk.Button(frame, text="List Git Config", command=list_git_config)
    list_config_button.pack(fill=tk.X)

    log_text = tk.Text(frame, height=20, width=100)
    log_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
