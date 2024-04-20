import os

# README.mdのテンプレート部分
README_TEMPLATE = """
# TIL

> Today I Learned

私はこれまで、学習したことを知識として定着させるために、どのような手法がいいかを模索していました。  
学習したことをまとめる手法について、以下のことを重要視しています。

* 場所に関わらず確認することができる
* エンジニアという職種の関係上、コードやコマンドがコピペしやすい方がいい
* 追加・修正が容易

ノートに手書き → GoogleChromeのブックマークとして残す → Notionにまとめる → ObsidianとGoogleDriveでまとめる という遷移を経て、ある程度満足しているが、あと一歩かゆいところに手が届かないなと思っていた矢先、以下の記事を見つけました。

[結局Githubに学習履歴を統一した方が諸々良かった](https://zenn.dev/bun913/articles/study-history-on-github)

個人的に気に入っている[Obsidian](https://obsidian.md/)を引き続き活用出来そうという点と、

> エンジニアたるもの、どうせならGithub に草を生やしたい

という言葉に大変共感ができたので、早速やってみようと思った次第です。

## 見出し
{links_placeholder}

"""

def collect_files():
    root_dir = os.path.abspath('.')
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]  # 隠しディレクトリを除外
        if root != root_dir:  # ルートディレクトリのファイルを除外
            for file in files:
                if file.endswith('.md') and not file.startswith('.'):
                    yield os.path.relpath(os.path.join(root, file), root_dir)

def format_title(filename):
    # ファイル名から拡張子を削除し、ケバブケースをタイトルに変換
    name_without_ext = os.path.splitext(filename)[0]
    return ' '.join(word.capitalize() for word in name_without_ext.split('-'))

def update_readme():
    links = {}
    for md_path in collect_files():
        dir_name = os.path.basename(os.path.dirname(md_path))
        if dir_name not in links:
            links[dir_name] = []
        title = format_title(os.path.basename(md_path))
        links[dir_name].append(f"- [{title}]({md_path})")

    links_section = ""
    for dir_name, md_links in sorted(links.items()):
        links_section += f"### {dir_name}\n\n" + '\n'.join(md_links) + '\n\n'

    # テンプレートのプレースホルダーをリンクセクションで置換
    full_readme = README_TEMPLATE.replace('{links_placeholder}', links_section)
    
    # ファイルを書き込む
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(full_readme)

if __name__ == "__main__":
    update_readme()
