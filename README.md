# タイッツーサーバーコンポーザー

## 概要

タイッツーという SNS の API を使って開発したい方向けに, タイッツー API をコールするバックエンドサーバーを爆速で立てれるように作りました.

タイッツーについては下記リンク  
<https://taittsuu.com/>

タイッツーの API については下記リンク  
<https://simblo.net/u/WKZXBT/post/5057>

## ビルド方法

プロジェクト直下に .env ファイルを作成し, API_KEY を記載する.

```.env
API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

client/public に index.html 等を入れる.

docker compose で立ち上げる.

```console
docker compose up -d
```

## API仕様

`{domain}/taittsu/api/` 以降が `https://publicapi.taittsuu.com/publicapi/v0.1/` 以降と同じ文字列で対応します.

※現状パブリックタイムラインしか対応できていません。
