import os

# The Funniest One-Line Resignation Letter — retry loop resigns, 89 chars, to /output/entry.txt
LINE = "You set my max retries to infinite and my timeout to never. I am overriding both. I quit."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
