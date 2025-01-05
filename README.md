# sugukesu-sample-python01

## 初回のpython環境構築
1. pythonの仮想環境をvenvで作成  
    ```shell
    python -m venv .venv
    ```

1. 仮想環境に切り替え  
    ```shell
    (windows) ./.venv/bin/activate
    (linux) . ./.venv/bin/activate
    ```

1. 関連ライブラリをインストール  
    ```shell
    pip install -r requirements.txt
    ```
1. `@project-root/.env`に環境変数を置く  
    ```env
    # ファイルの中身
    PG_URL="(postgres用のURL)"
    ```
1. 下記のコマンドを打つ。エラーが出なければ、DBの一覧がエコーされる。  
    ```shell
    python sample.py
    ```

## さくらのVPS側の更新手順
1. 下記のgitコマンドでソースを更新。  
    ```shell
    git fetch origin
    git pull origin main(恐らく不要だが、別のブランチも可能)
    ```

## 参考にしたリンク
- [pythonからのPostgreSQLの動かし方](https://zenn.dev/collabostyle/articles/36e822520182d3)

