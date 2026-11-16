# 3. GitHub Copilot 活用のメリット

## 3.1 SVN でも使える機能と GitHub が必要な機能

| 機能 | SVN のまま | GitHub 移行後 |
| --- | --- | --- |
| エディタでのコード補完、チャット | 使える | 使える |
| Issue を割り当てて実装させる | 使えない | 使える |
| プルリクエストをレビューさせる | 使えない | 使える |

## 3.2 Issue を Copilot に割り当てて実装させる

- Issue を Copilot に割り当てると、Copilot が実装してプルリクエストを作成する
- マージするかどうかは、開発者がレビューして判断する

![Copilot に実装させる流れ](img/03-copilot-1.png)

出典：[GitHub Copilot エージェントについて（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents)

## 3.3 プルリクエストを Copilot にレビューさせる

- プルリクエストのレビュー担当に Copilot を指定すると、変更内容へのコメントが付く
- 人のレビューの前に、見落としを減らせる

出典：[GitHub Copilot コード レビュー（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/code-review)
