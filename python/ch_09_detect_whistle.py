# Adapted from: https://github.com/tensorflow/examples/tree/master/lite/examples/sound_classification/raspberry_pi
# by Simon Monk

import time
from audio_classifier import AudioClassifier
from audio_classifier import AudioClassifierOptions

# Initialize the audio classification model.
options = AudioClassifierOptions(
    num_threads = 4,
    max_results = 1,
    score_threshold = 0.6,
    enable_edgetpu = False)
# other options
model = 'yamnet.tflite'
overlapping_factor = 0.5

classifier = AudioClassifier(model, options)

# Initialize the audio recorder and a tensor to store the audio input.
audio_record = classifier.create_audio_record()
tensor_audio = classifier.create_input_tensor_audio()

# Calculate the optimnal pause time
# We'll try to run inference every interval_between_inference seconds.
# This is usually half of the model's input length to create an overlapping
# between incoming audio segments to improve classification accuracy.
input_length_in_second = float(len(
    tensor_audio.buffer)) / tensor_audio.format.sample_rate
interval_between_inference = input_length_in_second * (1 - overlapping_factor)
pause_time = interval_between_inference / 10.0

audio_record.start_recording()

print('Listening for Whistles...')

while True:
  tensor_audio.load_from_audio_record(audio_record)
  categories = classifier.classify(tensor_audio)
  if len(categories) > 0:
    top_category = categories[0]
    if top_category.label == 'Whistling':
      print('Whistling Detected')
  time.sleep(pause_time)
