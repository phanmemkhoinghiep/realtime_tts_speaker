#!/bin/bash
#!/usr/bin/python3.7
#!/home/pi/.local/lib/python3.7/site-packages
STRING="Automatic launching TTS..."
PYTHON="/usr/bin/python3.7"
TTS_ROOT="/home/pi/realtime_tts_speaker/src"
TTS="start.py"
pushd . > /dev/null 2>&1
cd $TTS_ROOT

echo $STRING
$PYTHON -m "$TTS"

popd > /dev/null 2>&1
