# 【株JSON】全銘柄JSONデータ

日本株の全銘柄一覧を毎日更新してJSONで公開しています

[![badge](https://github.com/umihico/kabu-json-all-stock-list/actions/workflows/auto-update.yml/badge.svg)](https://github.com/umihico/kabu-json-all-stock-list/actions/workflows/auto-update.yml)

## 概要

[その他統計資料 | 日本取引所グループ](https://www.jpx.co.jp/markets/statistics-equities/misc/01.html)に公開されている「東証上場銘柄一覧（20XX年Y月末）」というExcelファイルをダウンロード月次でパーズして、JSONで公開しています。

加えて、[新規上場銘柄一覧 | 日本取引所グループ](https://www.jpx.co.jp/listing/stocks/new/index.html)をスクレイピングして新規上場銘柄を取得して、JSONで公開しています。

最後に、それらを統合して全銘柄のJSONデータとして公開しています。

## 公開データ

- [全銘柄JSONデータ](https://umihico.github.io/kabu-json-all-stock-list/all_stocks.json)
- [新規上場銘柄JSONデータ](https://umihico.github.io/kabu-json-all-stock-list/new_listings.json)
- [月次全銘柄JSONデータ](https://umihico.github.io/kabu-json-all-stock-list/monthly.json)

## 記事

[日本株の全銘柄一覧をJSON形式で毎日更新・配信する「株JSON」をリリース | UMIHICO BLOG](https://umihi.co/blog/20240908-kabu-json-release)
