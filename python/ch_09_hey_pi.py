import sys
import signal
from edge_impulse_linux.audio import AudioImpulseRunner

modelfile = '/home/pi/modelfile.eim'
audio_device_id = 2

runner = None

def signal_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


with AudioImpulseRunner(modelfile) as runner:
    try:
        model_info = runner.init()
        labels = model_info['model_parameters']['labels']
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')

        for res, audio in runner.classifier(device_id=audio_device_id):
            score = res['result']['classification']['hey_pi']
            if (score > 0.7):
                print('Hello you!')

    finally:
        if (runner):
            runner.stop()