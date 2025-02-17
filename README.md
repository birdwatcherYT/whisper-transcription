# whisper-transcription
- whisperを使った書き起こしサンプル
- 音声/動画ファイルから文字起こしした結果をタイムスタンプとともにテキストファイルに出力する

## `run-fast.py`: faster_whisper
- 自動的に区切られたセグメントごとに出力される

環境構築
```sh
pip install faster-whisper
```

実行
```sh
python run-fast.py input_audio.wav [--model turbo]
```

## `run.py`: whisper
- すべての処理が終わってから出力される

環境構築
```sh
pip install openai-whisper
pip install ffmpeg-python
```

実行
```sh
python run.py input_audio.wav [--model turbo]
```
