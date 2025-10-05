#@title #**TTS 뽑기**
import torch
from TTS.api import TTS
from pydub import AudioSegment
from pathlib import Path
import warnings
import gc

import argparse


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='AI RVC COVER', add_help=True)
  parser.add_argument('-txt', '--text', type=str, required=True, help='TEXT TO SAY')
  parser.add_argument('-spk', '--speaker', type=str, required=True, help='WHO')
  args = parser.parse_args()
  text = args.text
  speaker = args.speaker

  warnings.filterwarnings("ignore")
  
  import os
  os.environ["COQUI_TOS_AGREED"] = "1"

  
  # Get device
  device = "cuda" if torch.cuda.is_available() else "cpu"
  print(f"Using device: {device}")
  
  try:
      tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to(device)
      print("✅TTS Loaded")
  except Exception as e:
      import traceback
      print(f"❌ TTS 로드 중 오류 발생: {e}")
      print("\n--- 상세 오류 추적(Traceback) ---")
      traceback.print_exc() # 전체 Traceback 출력

  try:
      tts.tts_to_file(
          text=text,
          speaker_wav=speaker,
          language="ko",
          file_path="tts_generated.mp3",
          enable_text_splitting=True,
          temperature=0.7,
          top_k=50,
          repetition_penalty=5.0,
      )
      print("✅TTS Generation Complete")
  
  except Exception as e:
      print(f"❌ TTS 생성 중 오류 발생: {e}")
  
  finally:
      # 메모리 해제
      if torch.cuda.is_available():
          torch.cuda.empty_cache()
      del tts
      gc.collect()
      print("✅END")
