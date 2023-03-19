# Search Shortcut

## Requirements
- Python

## Instructions

To search Google while in the directory that contains *google.py*, you can run
```
python3 google.py <Google search query>
```

To visit a website while in the directory that contains *website.py*, you can run
```
python3 website.py <website domain>
```

To query ChatGPT while in the directory that contains *chatgpt.py*, you can run
```
python3 chatgpt.py <ChatGPT query>
```

## Speed Increases

Create an alias for each of the scripts so they can be run from any directory with a single character.

On Linux, create or edit the .bash_aliases file in the home (~) directory and add the following lines.
```
alias s='python3 ~/path/to/google.py'
alias w='python3 ~/path/to/website.py'
alias gpt='python3 ~/path/to/chatgpt.py'
```

When using website.py, the full domain name does not have to be typed for all websites. The following table shows a list of shortcuts that can be used.
| Shortcut | Website |
| --- | --- |
| a | amazon.com |
| g | github.com |
| gm | gmail.com |
| y | youtube.com |