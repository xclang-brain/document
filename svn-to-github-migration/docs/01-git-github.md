# 1. Git と GitHub の概要

## 1.1 Git とは

- ファイルの変更履歴を管理するツール（SVN と同じ種類のツール）

出典：[Pro Git（日本語版）](https://git-scm.com/book/ja/v2)

## 1.2 GitHub とは

- Git のリポジトリを置いて共有するサービス
- プルリクエスト、Issue、GitHub Actions、GitHub Copilot など、開発を支える機能がある

出典：[GitHub とは（GitHub Docs）](https://docs.github.com/ja/get-started/start-your-journey/what-is-github)

## 1.3 SVN との仕組みの違い

SVN は履歴をサーバーだけが持ちます。Git は各開発者が全履歴を手元に持ち、GitHub で共有します。

```mermaid
flowchart TB
    subgraph GIT["Git（分散型）"]
        direction TB
        GH[("GitHub<br/>共有リポジトリ")]
        GA["開発者 A<br/>ローカルリポジトリ<br/>（全履歴あり）"] -->|push| GH
        GB["開発者 B<br/>ローカルリポジトリ<br/>（全履歴あり）"] -->|push| GH
    end
    subgraph SVN["SVN（集中型）"]
        direction TB
        SS[("SVN サーバー<br/>履歴はここだけ")]
        SA["開発者 A<br/>作業コピー"] -->|commit| SS
        SB["開発者 B<br/>作業コピー"] -->|commit| SS
    end
```

## 1.4 SVN との作業の流れの違い

SVN の commit はすぐにサーバーへ反映されます。Git の commit は手元に記録するだけで、push して初めて GitHub に反映されます。GitHub では、作業用のブランチで変更し、プルリクエストでレビューを受けてからマージします。

```mermaid
flowchart LR
    subgraph SV["サーバー（SVN）"]
        R[("SVN リポジトリ")]
    end
    subgraph PC["ローカル PC"]
        W["作業コピー<br/>② 編集"]
    end
    R -->|"① update"| W
    W -->|"③ commit"| R
```

```mermaid
flowchart LR
    subgraph GH["サーバー（GitHub）"]
        R[("リモートリポジトリ<br/>⑥ プルリクエストで<br/>レビューしてマージ")]
    end
    subgraph PC["ローカル PC"]
        L["ローカルリポジトリ<br/>② ブランチ作成<br/>③ 編集<br/>④ commit（手元に記録）"]
    end
    R -->|"① pull"| L
    L -->|"⑤ push"| R
```
