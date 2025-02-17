# pip install faster-whisper

import os
import argparse
import time
from datetime import timedelta
from faster_whisper import WhisperModel


def transcribe_audio(input_file, model_name):
    start_time = time.time()

    # Whisperモデルをロード
    model = WhisperModel(model_name)

    # 音声ファイルの文字起こし
    # generatorが返ってくるため、ここの処理自体は軽い
    segments, info = model.transcribe(input_file, language="ja", vad_filter=True)

    # 結果をファイルに書き出す
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            start = segment.start
            end = segment.end
            text = segment.text
            sentence = f"[{timedelta(seconds=int(start))} - {timedelta(seconds=int(end))}] {text}"
            print(sentence)
            f.write(f"{sentence}\n")

    print(f"Output saved to {output_file}")

    end_time = time.time()
    print(f"elapsed time: {end_time - start_time} sec")


# python run-fast.py input_audio.wav [--model small]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using Whisper models."
    )
    parser.add_argument("input_file", help="Path to the input audio file")
    parser.add_argument(
        "--model",
        default="turbo",
        help="Model size to use (e.g., tiny, base, small, medium, large, large-v2, turbo). Default is 'base'.",
    )

    args = parser.parse_args()

    transcribe_audio(args.input_file, args.model)
