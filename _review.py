#pip install python-frontmatter
import os
import pathlib
import frontmatter

root = pathlib.Path().resolve()
for path, subdirs, files in os.walk(root):
    for name in files:
        if (name.startswith('_') or name.startswith('.') or not name.endswith('.md')):
            continue
        file_path = os.path.join(path, name)
        print(file_path)
        url = (file_path
            .replace('C:\\Projects\\bs', 'https://blendedfeelings.com/software')
            .replace('\\', '/')
            )
        
        print(url)
        article = frontmatter.load(file_path)
        if article.content.strip() == '':
            raise Exception(f'File {file_path} has empty content.')
        lines = article.content.split('\n')
        if not lines[0].startswith('# '):
            raise Exception(f'File {file_path} has no title.')
        if lines[1].strip() == '':
            raise Exception(f'File {file_path} has empty line after title.')
        if lines[0][2].isupper() == False:
            raise Exception(f'File {file_path} has title that does not start with uppercase letter.')
        for line_index, line in enumerate(lines):
            if line.lower().startswith('!include'):
                line = '[!INCLUDE ' + line.split(' ')[1] + ']'
                lines[line_index] = line
        article['b'] = url
        article.content = '\n'.join(lines)
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(frontmatter.dumps(article))