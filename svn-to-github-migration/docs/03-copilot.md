# 3. GitHub Copilot の活用範囲の拡大

Copilot は今の環境でもエディタで使っています。GitHub に移行すると、GitHub 上で動く Copilot の機能も使えるようになります。

## 3.1 今の環境と移行後で使える機能の比較

| 機能 | 今の環境（SVN） | 移行後（GitHub） |
| --- | --- | --- |
| エディタでのコード補完、チャット | 使える | 使える |
| Issue を割り当てて実装を任せる | 使えない | 使える |
| プルリクエストのレビュー | 使えない | 使える |

## 3.2 Issue を割り当てて実装を任せられる

- Issue を Copilot に割り当てると、Copilot が実装してプルリクエストを作成する
- マージするかどうかは、開発者がレビューして判断する

![Copilot に実装を任せる流れ](img/03-copilot-1.png)

出典：[GitHub Copilot エージェントについて（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents)

## 3.3 プルリクエストのレビューに使える

- プルリクエストのレビュー担当に Copilot を指定すると、変更内容へのコメントが付く
- 人のレビューの前に、見落としを減らせる

出典：[GitHub Copilot コード レビュー（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/code-review)
