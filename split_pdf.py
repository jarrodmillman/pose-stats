import subprocess
import sys
import re
import pathlib
from collections import defaultdict

if not len(sys.argv) > 1:
    print('Usage: split_pdf.py filename.pdf')
    sys.exit(1)
else:
    input_file = sys.argv[1]

p = subprocess.run(['pdftk',  input_file, 'dump_data_utf8'], stdout=subprocess.PIPE)
out = p.stdout.decode('utf-8').split('\n')

current_section = 'default'
data = defaultdict(list)

for line in out:
    line = line.strip()
    if not line:
        continue

    if line.endswith('Begin'):
        current_section = line.replace('Begin', '')
    elif ':' in line and not line.endswith(':'):
        field, val = line.split(': ', maxsplit=1)
        if field.startswith(current_section):
            field = field[len(current_section):]
        data[current_section].append((field, val))
    else:
        print("Hrm, didn't expect this:")
        print(line)

bmdata = data['Bookmark']
bookmarks = [dict(bmdata[i:i + 3]) for i in range(0, len(bmdata), 3)]

files = []

for bm in bookmarks:
    if bm['Level'] != '1':
        continue
    title = bm['Title']
    page = int(bm['PageNumber'])

    file_nr = len(files)
    if file_nr > 0:
        files[-1][-1].append(page - 1)

    title_loweralpha = ''.join(ch if ch.isalnum() else '_' for ch in title.lower())
    title_loweralpha = title_loweralpha.replace(' ', '_')
    title_loweralpha = re.sub('\_+', '_', title_loweralpha)
    fn = f'{file_nr:02d}_{title_loweralpha}.pdf'

    files.append((fn, [str(page),]))


print(f'Splitting {input_file} into chapters')
pathlib.Path("build").mkdir(exist_ok=True)
for (fn, pages) in files:
    if len(pages) != 2:
        pages.append("")

    print(f" {fn} ({pages[0]}--{pages[1]})")
    subprocess.run(["pdftk", input_file, "cat", f"{pages[0]}-{pages[1]}", "output", f"build/{fn}"])
