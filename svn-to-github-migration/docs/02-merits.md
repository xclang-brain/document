# 2. Git・GitHub のメリット

| メリット | 概要 |
| --- | --- |
| :material-link-variant: Issue と変更を紐づけて管理できる | なぜその変更をしたのかを後から追える |
| :material-source-branch: 作業ごとにブランチを分けやすい | 作業途中の変更を、他の人に影響させずに残せる |
| :material-source-pull: プルリクエストでレビューが記録に残る | 指摘と承認が、変更内容と一緒に残る |
| :material-cog-play: ビルドやテストを自動化できる | テストに通らない変更をマージできないようにできる |
| :material-earth: 業界標準である | 開発者の **93%** が Git を使っている |
| :material-robot-outline: AI 活用の幅が広がる | Issue からの実装やプルリクエストのレビューを AI に任せられる |

2.1〜2.4 は、GitHub での開発の流れの各段階に当たります。

```mermaid
flowchart LR
    A["Issue<br/>（2.1）"] --> B["ブランチ<br/>（2.2）"] --> C["プルリクエスト<br/>（2.3）"] --> D["自動テスト<br/>（2.4）"] --> E["マージ"]
```

## 2.1 Issue と変更を紐づけて管理できる

- **SVN**：課題管理は、Redmine などの別ツールと連携して行う
- **Git・GitHub**：Issue とプルリクエストが同じ場所にあり、マージすると Issue が自動で閉じる[^1]

## 2.2 作業ごとにブランチを分けやすい

- **SVN**：ブランチはサーバー上に作る。commit するとすぐサーバーに反映される
- **Git・GitHub**：ブランチを手元で作って切り替えられる。作業途中の変更も手元で commit できる

## 2.3 プルリクエストでレビューが記録に残る

- **SVN**：レビューには別のツールや手段が必要で、記録も変更とは別の場所に残る
- **Git・GitHub**：変更内容、指摘、承認がプルリクエストにまとめて残る[^2]

## 2.4 ビルドやテストを自動化できる

- **SVN**：Jenkins などの CI サーバーを別に用意して連携する
- **Git・GitHub**：GitHub Actions を使え、結果がプルリクエストに表示される[^3]

## 2.5 業界標準である

- Stack Overflow の開発者調査（2022年）では、回答者の **93%** が Git を使っている[^4]
- 情報、ツール、経験者が多い

## 2.6 AI 活用の幅が広がる

Copilot は今もエディタで使っています。移行すると、GitHub 上で AI に作業を任せられるようになります。

| GitHub 上で AI に任せられる作業 | 今の環境 | 移行後 |
| --- | :---: | :---: |
| Issue を割り当てて、実装させる | × | ○ |
| プルリクエストをレビュー・修正させる | × | ○ |
| 複数の作業を並行して進めさせる | △（準備が必要） | ○ |

- GitHub 上のプルリクエストの **40% 以上**が、AI の作成した下書きをもとにしている（2026年9月時点）[^5]
- 主要な AI ツール（Copilot、Claude Code、Codex など）の新機能は、ブランチとプルリクエストでの作業を前提にしている[^6]

[^1]: [プルリクエストを課題にリンクする（GitHub Docs）](https://docs.github.com/ja/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
[^2]: [Pull Request（GitHub Docs）](https://docs.github.com/ja/pull-requests/reference/pull-requests)
[^3]: [GitHub Actions について（GitHub Docs）](https://docs.github.com/ja/actions/get-started/understand-github-actions)
[^4]: [Beyond Git: The other version control systems developers use（Stack Overflow Blog）](https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use)
[^5]: [Octoverse 2026（GitHub Blog）](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
[^6]: [GitHub Copilot エージェントについて（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents) ／ [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) ／ [Codex: Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
