# 5. marketplaceとは

## 5.1 定義

- plugin の一覧（marketplace.json）を持つ、plugin 配布用のリポジトリ

```text
リポジトリ/
├── .github/
│   └── plugin/
│       └── marketplace.json   # plugin の一覧を書くファイル（必須）
└── plugins/
    ├── plugin-a/              # plugin 本体
    └── plugin-b/
```

```json title=".github/plugin/marketplace.json"
{
  "name": "my-marketplace",
  "owner": { "name": "Your Organization" },
  "plugins": [
    {
      "name": "plugin-a",
      "description": "plugin-a の説明",
      "version": "1.0.0",
      "source": "./plugins/plugin-a"
    },
    {
      "name": "plugin-b",
      "description": "plugin-b の説明",
      "version": "1.0.0",
      "source": "./plugins/plugin-b"
    }
  ]
}
```

出典：[Creating a plugin marketplace（GitHub Docs）](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace)

## 5.2 何のために使うか

| | marketplace なし | marketplace あり |
|---|---|---|
| 管理 | plugin が個人・リポジトリごとに散在する | 1 つのリポジトリで一元管理できる |
| 入手 | 配布元を個別に探す | marketplace から検索してインストールできる |

出典：[Plugins for GitHub Copilot（GitHub Docs）](https://docs.github.com/en/copilot/concepts/customizations/plugins)

## 5.3 plugin の公開手順

1. skill・MCP 設定を作る
2. plugin にまとめる
3. marketplace のリポジトリの `plugins/` に置き、`marketplace.json` の一覧に追記する

出典：[Creating a plugin marketplace（GitHub Docs）](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace)

## 5.4 plugin の導入手順

1. **marketplace を登録する**
    - **Copilot CLI**：セッションで `/plugin marketplace add OWNER/REPO` を実行
    - **VS Code**：Agent Customizations エディターで marketplace を追加

2. **plugin を探してインストールする**
    - **Copilot CLI**：セッションで `/plugin` を実行し、一覧から選んでインストール
    - **VS Code**：Agent Customizations エディターで plugin を選び、Install を押す

出典：[Agent plugins in VS Code（VS Code Docs）](https://code.visualstudio.com/docs/agent-customization/agent-plugins) ／ [Finding and installing plugins for Copilot CLI（GitHub Docs）](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing) ／ [Copilot CLI new terminal interface is generally available（GitHub Changelog）](https://github.blog/changelog/2026-06-23-copilot-cli-new-terminal-interface-is-generally-available/)
