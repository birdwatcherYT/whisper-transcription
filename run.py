# pip install git+https://github.com/openai/whisper.git
# pip install ffmpeg-python

import os
import argparse
import time
from datetime import timedelta
import whisper


def transcribe_audio(input_file, model_name):
    start_time = time.time()

    # Whisperモデルをロード
    model = whisper.load_model(model_name)

    # 音声ファイルの文字起こし
    # ここの処理が重い
    result = model.transcribe(input_file)

    # 結果をファイルに書き出す
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            sentence = f"[{timedelta(seconds=int(start))} - {timedelta(seconds=int(end))}] {text}"
            print(sentence)
            f.write(f"{sentence}\n")

    print(f"Output saved to {output_file}")

    end_time = time.time()
    print(f"elapsed time: {end_time - start_time} sec")


# python run.py input_audio.wav [--model small]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using Whisper models."
    )
    parser.add_argument("input_file", help="Path to the input audio file")
    parser.add_argument(
        "--model",
        default="turbo",
        help="Model size to use (e.g., tiny, base, small, medium, large, turbo). Default is 'base'.",
    )

    args = parser.parse_args()

    transcribe_audio(args.input_file, args.model)
