import time
import subprocess
import sys
def replace_file_content(original_file_path, replacement_file_path):
  with open(replacement_file_path, 'r') as replacement:
    content = replacement.read()
    with open(original_file_path, 'w') as original:
      original.write(content)
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
def paste_from_clipboard_to_file(file_path):
  completed_process = subprocess.run(['pbpaste'], stdout=subprocess.PIPE)
  clipboard_contents = completed_process.stdout.decode('utf-8')
  with open(file_path, 'w') as file:
    file.write(clipboard_contents)
    print()
def type_code_to_file(code, file_path):
  with open(file_path, 'w') as file:
    file.write(code)
print("")
type_text(" *** APERTURETERMINAL SETUP ***")
time.sleep(1.0)
type_text("This will automatically set up your terminal to become the ultimate aperture laboratories experience.")
type_text("IMPORTANT: YOU MUST BE IN THE REPOSITORY DIRECTORY BEFORE RUNNING") 
consent = input("Do you want to continue (y/n)?: ")
if consent == "y":
  print("")
  type_text("Customizing...")
  replace_file_content(/etc/motd, motd.txt)
  subprocess.run(["pbcopy","<", "zshprompt.sh])
  subprocess.run(["cd", "~"])
  paste_from_clipboard_to_file(zshprompt.sh)
  write = 'source ~/zshprompt.sh\nexport TERM=xterm-256color'
  filepath = '.zshrc'
  type_code_to_file(write, filepath)
  print("")
  type_text("Done! Just close out of the terminal and reopen to see the changes!")
  sys.exit()
elif consent == "n":
  print("")
  type_text("Aborted")
  sys.exit()
else:
  type_text("invalid option.")
  sys.exit()
