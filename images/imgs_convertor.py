import sys
from pathlib import Path
from PIL import Image

try:
    src_dir, dst_dir = sys.argv[1:3]
except ValueError as err:
    print("Please enter SRC and DST folders...")

if not Path(dst_dir).exists():
    Path(dst_dir).mkdir()

for pic in Path(src_dir).iterdir():
    file_name = pic.name.split('.')[0]
    im = Image.open(pic)
    im.convert('RGB').save(f"{dst_dir}/{file_name}.jpg", "JPEG")

