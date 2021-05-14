# stream-on-mq-example
Simple repo to demo streaming via redis

# Instructions
- install dependencies in `requirements.txt`
- start redis container using `bash run_redis.sh`
- on 1 terminal run `python publisher.py`
- open another terminal and run `python subscriber.py`

note: run `export OPENCV_FFMPEG_CAPTURE_OPTIONS="rtsp_transport;udp"` on the publisher terminal if you are viewing a UDP rtsp stream