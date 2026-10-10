"""Bundle src/ into one self-contained HTML file (two flavours: standalone + artifact)."""
import base64, re, pathlib

root = pathlib.Path(__file__).parent
src = root / 'src'
dist = root / 'dist'
dist.mkdir(exist_ok=True)

def uri(path, mime):
    return f"data:{mime};base64,{base64.b64encode((root / path).read_bytes()).decode()}"

parts = []
THREE_IMPORT = "import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';"
for name in ['core.js', 'scan.js', 'audio.js', 'glsl.js', 'env.js', 'engine.js', 'app.js']:
    code = (src / name).read_text()
    code = re.sub(r"import\s*\{[^}]*\}\s*from\s*'\./[a-z]+\.js';\n", '', code, flags=re.S)
    code = re.sub(r'^export (const|function|class) ', r'\1 ', code, flags=re.M)
    code = code.replace(THREE_IMPORT + '\n', '')
    assert './' not in re.findall(r"from '([^']+)'", code).__str__(), name
    parts.append(f'// ===== {name} =====\n{code}')
script = THREE_IMPORT + '\n' + '\n'.join(parts)

shell = (src / 'shell.html').read_text()
page = (shell.replace('__LOGO__', uri('assets/logo.webp', 'image/webp'))
             .replace('__MARK__', uri('assets/mark.webp', 'image/webp'))
             .replace('__SCRIPT__', script))

(dist / 'artifact.html').write_text(page)
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<link rel="icon" href="{uri("assets/fav.png", "image/png")}">\n')
standalone = head + page.replace('<div id="app">', '</head>\n<body>\n<div id="app">', 1) + '\n</body>\n</html>\n'
(dist / 'afterimage.html').write_text(standalone)
print('built', len(standalone) // 1024, 'KB')
