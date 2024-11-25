from pathlib import Path
Path = Path('pi_digits.txt')
Path.write_text("zhaoysuhi00")
contents = Path.read_text()
print(contents)