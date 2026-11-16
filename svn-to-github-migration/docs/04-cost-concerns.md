# 4. 移行のコストと懸念

## 4.1 移行にかかるコスト

- Git と GitHub の操作を覚える時間
- リポジトリの移行と CI の構築作業
- 既存の手順書やツールの見直し

## 4.2 よくある懸念と回答

| 懸念 | 回答 |
| --- | --- |
| 覚えることが多いのでは | 日常的に使う操作は pull、commit、push、プルリクエストに限られる |
| 移行中に開発が止まらないか | 一度に移行せず、段階的に進める（5章） |
| SVN の過去の履歴は残るか | （記載予定） |
| ソースコードの置き場所は安全か | （記載予定） |

## 4.3 SVN のほうが向いていること

| SVN が向いていること | Git・GitHub での対応 |
| --- | --- |
| 大きなバイナリファイルの管理 | Git LFS を使う |
| ファイルのロック | Git LFS のロック機能を使う |

出典：[Git Large File Storage について（GitHub Docs）](https://docs.github.com/ja/repositories/working-with-files/managing-large-files/about-git-large-file-storage) ／ [File Locking（Git LFS Wiki）](https://github.com/git-lfs/git-lfs/wiki/File-Locking)
