import subprocess
import os
 
urls = [
    "https://m365.cloud.microsoft/chat/",
    "https://www.perplexity.ai/search",
    "https://gemini.google.com/u/1/app",
    "https://chat.deepseek.com/"
]
 
edge_path = os.path.join(
    os.environ.get("PROGRAMFILES(x86)", "C:\\Program Files (x86)"),
    "Microsoft\\Edge\\Application\\msedge.exe"
)

subprocess.Popen([edge_path, "--new-window"] + urls)