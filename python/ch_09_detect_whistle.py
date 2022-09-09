# Adapted from: https://github.com/tensorflow/examples/tree/master/lite/examples/sound_classification/raspberry_pi
# by Simon Monk

import time
from tflite_support.task import audio
from tflite_support.task import core
from tflite_support.task import processor

model = 'yamnet.tflite'
num_threads = 4
score_threshold = 0.6
overlapping_factor = 0.5

# Initialize the audio classification model.
base_options = core.BaseOptions(
      file_name=model, use_coral=False, num_threads=num_threads)
classification_options = processor.ClassificationOptions(
      max_results=1, score_threshold=score_threshold)
options = audio.AudioClassifierOptions(
      base_options=base_options, classification_options=classification_options)
classifier = audio.AudioClassifier.create_from_options(options)

# Initialize the audio recorder and a tensor to store the audio input.
audio_record = classifier.create_audio_record()
tensor_audio = classifier.create_input_tensor_audio()

# We'll try to run inference every interval_between_inference seconds.
# This is usually half of the model's input length to create an overlapping
# between incoming audio segments to improve classification accuracy.
input_length_in_second = float(len(
    tensor_audio.buffer)) / tensor_audio.format.sample_rate
interval_between_inference = input_length_in_second * (1 - overlapping_factor)
pause_time = interval_between_inference * 0.1
last_inference_time = time.time()

# Start audio recording in the background.
audio_record.start_recording()

print('Listening for Whistles...')

while True:
  tensor_audio.load_from_audio_record(audio_record)
  results = classifier.classify(tensor_audio)
  if len(results.classifications) > 0:
    classification = results.classifications[0]
    if len(classification.categories) > 0:
      top_category = classification.categories[0]
      if top_category.category_name == 'Whistling':
        print('Whistling Detected')
  time.sleep(pause_time)

