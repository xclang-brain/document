# 2. Git・GitHub のメリット

| メリット | 概要 |
| --- | --- |
| ブランチの作成とマージが容易になる | 作業ごとにブランチを分け、作業途中の変更が他の人に影響しない |
| プルリクエストでレビューが記録に残る | 変更内容、レビューのコメント、承認の記録がまとめて残る |
| Issue と変更を紐づけて管理できる | なぜその変更をしたかを後から追える |
| ビルドやテストを自動化できる | push やプルリクエストのたびに、ビルドとテストが自動で実行される |
| 業界標準である | 開発者の 93% が Git を使用しており、情報や経験者が多い |
| AI 活用の幅が広がる | Issue からの実装やプルリクエストのレビューを AI に任せられる |

## 2.1 ブランチの作成とマージが容易になる

- ブランチは手元ですぐに作れ、作業ごとに分けやすい
- 作業途中の変更も手元のブランチに commit でき、他の人の作業に影響しない

## 2.2 プルリクエストでレビューが記録に残る

- 変更内容、レビューのコメント、承認の記録がプルリクエストにまとめて残る
- 承認されるまでマージできないように設定できる

出典：[Pull Request（GitHub Docs）](https://docs.github.com/ja/pull-requests/reference/pull-requests)

## 2.3 Issue と変更を紐づけて管理できる

- Issue（課題）と、それを解決したプルリクエストを紐づけられる
- 「なぜこの変更をしたか」を後から追える

出典：[プルリクエストを課題にリンクする（GitHub Docs）](https://docs.github.com/ja/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

## 2.4 ビルドやテストを自動化できる

- GitHub Actions で、push やプルリクエストのたびにビルドとテストを自動で実行できる
- 結果はプルリクエストに表示され、失敗した変更はマージできないように設定できる

出典：[GitHub Actions について（GitHub Docs）](https://docs.github.com/ja/actions/get-started/understand-github-actions)

## 2.5 業界標準である

- Stack Overflow の開発者調査（2022年）では、回答者の 93% が Git を使用
- 情報、ツール、経験者が多い

出典：[Beyond Git: The other version control systems developers use（Stack Overflow Blog）](https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use)

## 2.6 AI 活用の幅が広がる

Copilot は今もエディタで使っています。移行すると、GitHub 上で AI に任せられる作業が増えます。

| 機能 | 今の環境（SVN） | 移行後（GitHub） |
| --- | --- | --- |
| 複数の作業を AI に並行して任せる | 一部できる | できる |
| Issue を割り当てて実装を任せる | できない | できる |
| プルリクエストのレビューと修正を任せる | できない | できる |

- 主要な AI ツール（Copilot、Claude Code、Codex など）の新機能は、ブランチとプルリクエストでの作業を前提にしている
- GitHub 上のプルリクエストの 40% 以上は、AI が作成した下書きをもとにしている（2026年9月時点）

出典：[Octoverse 2026（GitHub Blog）](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) ／ [GitHub Copilot エージェントについて（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents) ／ [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) ／ [Codex: Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
