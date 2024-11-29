import tkinter as tk
from tkinter import messagebox
import requests
import json


def fetch_repository_info():
    repo_name = entry.get()

    if not repo_name:
        messagebox.showerror("Error", "Please enter a repository name.")
        return

    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        result = {
            'company': data.get('owner', {}).get('company', None),
            'created_at': data.get('created_at'),
            'email': data.get('owner', {}).get('email', None),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('html_url'),
        }
        with open('repository_info.json', 'w') as f:
            json.dump(result, f, indent=4)

        messagebox.showinfo("Success", "Repository information saved successfully!")
    else:
        messagebox.showerror("Error", "Failed to fetch repository data. Please check the repository name.")

root = tk.Tk()
root.title("GitHub Repository Info Fetcher")

label = tk.Label(root, text="Enter repository name (e.g., user/repo):")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Get Info", command=fetch_repository_info)
button.pack(pady=20)

root.mainloop()


