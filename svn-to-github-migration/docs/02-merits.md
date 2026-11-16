# 2. Git・GitHub のメリット

<div class="grid cards" markdown>

-   :material-source-branch:{ .lg .middle } **ブランチの作成とマージが容易になる**

    ---

    作業途中の変更を手元に置いたまま、作業ごとに分けて進められる

-   :material-source-pull:{ .lg .middle } **プルリクエストでレビューが記録に残る**

    ---

    レビューの指摘と承認が、変更内容と一緒に残る

-   :material-link-variant:{ .lg .middle } **Issue と変更を紐づけて管理できる**

    ---

    なぜその変更をしたのかを、後から追える

-   :material-cog-play:{ .lg .middle } **ビルドやテストを自動化できる**

    ---

    テストに通らない変更は、マージできないようにできる

-   :material-earth:{ .lg .middle } **業界標準である**

    ---

    開発者の **93%** が Git を使っている

-   :material-robot-outline:{ .lg .middle } **AI 活用の幅が広がる**

    ---

    Issue からの実装やプルリクエストのレビューを AI に任せられる

</div>

2.1〜2.4 は、GitHub での開発の流れの各段階に当たります。

```mermaid
flowchart LR
    A["Issue"] --> B["ブランチ"] --> D["プルリクエスト"] --> E["自動テスト"] --> F["レビュー"] --> G["マージ"]
```

## 2.1 ブランチの作成とマージが容易になる

- **SVN**：ブランチはサーバー上に作る。作業途中の変更も、commit するとサーバーに反映される
- **Git・GitHub**：ブランチを手元ですぐに作れる。作業途中の変更は手元で commit し、終わってから共有できる

## 2.2 プルリクエストでレビューが記録に残る

- **SVN**：レビューの仕組みがないため、レビューは別の手段で行い、記録も別に管理する
- **Git・GitHub**：変更内容、指摘、承認がプルリクエストにまとめて残る。承認されるまでマージできないようにも設定できる[^1]

## 2.3 Issue と変更を紐づけて管理できる

- **SVN**：課題を管理する機能がないため、課題と変更の対応は手作業で管理する
- **Git・GitHub**：Issue（課題）と、それを解決したプルリクエストを紐づけられる[^2]

## 2.4 ビルドやテストを自動化できる

- **SVN**：自動化には、別途 CI サーバーを用意する必要がある
- **Git・GitHub**：GitHub Actions で、push やプルリクエストのたびにビルドとテストを実行できる。結果はプルリクエストに表示され、失敗した変更はマージできないようにできる[^3]

## 2.5 業界標準である

- Stack Overflow の開発者調査（2022年）では、回答者の **93%** が Git を使っている[^4]
- 情報、ツール、経験者が多い

## 2.6 AI 活用の幅が広がる

Copilot は今もエディタで使っています。移行すると、GitHub 上で AI に任せられる作業が増えます。

| AI に任せられる作業 | SVN | Git・GitHub |
| --- | :---: | :---: |
| 複数の作業を並行して任せる | :material-minus: 一部 | :material-check: |
| Issue から実装を任せる | :material-close: | :material-check: |
| プルリクエストのレビューと修正を任せる | :material-close: | :material-check: |

- GitHub 上のプルリクエストの **40% 以上**が、AI の作成した下書きをもとにしている（2026年9月時点）[^5]
- 主要な AI ツール（Copilot、Claude Code、Codex など）の新機能は、ブランチとプルリクエストでの作業を前提にしている[^6]

[^1]: [Pull Request（GitHub Docs）](https://docs.github.com/ja/pull-requests/reference/pull-requests)
[^2]: [プルリクエストを課題にリンクする（GitHub Docs）](https://docs.github.com/ja/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
[^3]: [GitHub Actions について（GitHub Docs）](https://docs.github.com/ja/actions/get-started/understand-github-actions)
[^4]: [Beyond Git: The other version control systems developers use（Stack Overflow Blog）](https://stackoverflow.blog/2023/01/09/beyond-git-the-other-version-control-systems-developers-use)
[^5]: [Octoverse 2026（GitHub Blog）](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
[^6]: [GitHub Copilot エージェントについて（GitHub Docs）](https://docs.github.com/ja/copilot/concepts/agent-capabilities/about-agents/about-github-copilot-agents) ／ [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) ／ [Codex: Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
