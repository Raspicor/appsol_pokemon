import struct, sys, os, zlib

f = open('/Users/ezcaretech/Downloads/PikaPet.exe','rb')
data = f.read()
MAGIC = b'MEI\014\013\012\013\016'
pos = data.rfind(MAGIC)
print("cookie at", pos)
# PyInstaller 2.1+ cookie: 8s magic, !i lengthofPackage, !i toc, !i tocLen, !i pyver, 64s pylibname
cookie = data[pos:pos+88]
magic, lengthofPackage, toc, tocLen, pyver = struct.unpack('!8siiii', cookie[:24])
pylib = cookie[24:88].rstrip(b'\0').decode()
print("pkgLen",lengthofPackage,"tocOff",toc,"tocLen",tocLen,"pyver",pyver,"pylib",pylib)

overlayPos = pos + 88 - lengthofPackage   # start of the CArchive
tocPos = overlayPos + toc
print("archive starts at", overlayPos)

entries=[]
p = tocPos
end = tocPos + tocLen
while p < end:
    (entrySize,) = struct.unpack('!i', data[p:p+4])
    nameLen = entrySize - 18
    entryPos, cmprsdSize, uncmprsdSize, cmprsFlag, typeCmprsData, name = struct.unpack(
        '!iiiBc{}s'.format(nameLen), data[p+4:p+entrySize])
    name = name.rstrip(b'\0').decode('utf-8','replace')
    entries.append((entryPos, cmprsdSize, uncmprsdSize, cmprsFlag, typeCmprsData.decode(), name))
    p += entrySize

print("entries:", len(entries))
from collections import Counter
print(Counter(t for *_ , t, n in entries))

out='extracted'
os.makedirs(out, exist_ok=True)
for entryPos, csz, usz, flag, typ, name in entries:
    blob = data[overlayPos+entryPos : overlayPos+entryPos+csz]
    if flag:
        try: blob = zlib.decompress(blob)
        except Exception as e: print("ERR", name, e); continue
    safe = name.replace('\\','/').lstrip('/')
    dest = os.path.join(out, safe)
    os.makedirs(os.path.dirname(dest) or out, exist_ok=True)
    if typ in ('s','m','M'):
        dest += '.pyc'
    with open(dest,'wb') as g: g.write(blob)

print("\n=== PYSOURCE (main scripts) ===")
for e in entries:
    if e[4]=='s': print("  ", e[5], e[2], "bytes")
print("\n=== PYZ ===")
for e in entries:
    if e[4] in ('z','Z'): print("  ", e[5], e[2])
