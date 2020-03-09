# 自動イラスト閲覧アプリ
## ローカル環境での実行
1. このリポジトリをダウンロードする。
   ```git clone ```

# 参考
- [Developing a Single Page App with Flask and Vue.js | TestDriven.io](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)

- [Vue.js を vue-cli を使ってシンプルにはじめてみる - Qiita](https://qiita.com/567000/items/dde495d6a8ad1c25fa43)

- [imlinus/vue-magic-grid: ??♂?? Responsive Magic Grid for Vue](https://github.com/imlinus/vue-magic-grid)

- [HTML/CSSの覚え方　WEB制作に役立つ便利なチートシートまとめ - Minimal Green](https://www.atmarkit.co.jp/fdotnet/chushin/cheatsheet_02/cheatsheet_02_01.html)  
<img src="https://www.atmarkit.co.jp/fdotnet/chushin/cheatsheet_02/cheatsheet_02_01.gif" width=100>

- [TwitterのAPI制限 [2019/11/17現在] - Qiita](https://qiita.com/mpyw/items/32d44a063389236c0a65)  
```/favorites/list```は15分当たり75リクエスト(=5[リクエスト/分])の制限があるので可能な限りキャッシングする。また1リクエストで1～200ツイートを取得できるので、常に最大の200ツイートを取得することでRate Limitを避ける。