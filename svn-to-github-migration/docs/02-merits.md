# 2. Git・GitHub のメリット

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
