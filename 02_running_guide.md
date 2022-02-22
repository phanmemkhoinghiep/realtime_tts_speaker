### HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG

### STEP1.  Truy nhập vào thư mục TTS

1.1. Truy cập vào thư mục realtime_tts_speaker

Sử dụng lệnh sau

```sh
cd realtime_tts_speaker/src
```
1.2. Edit File config

```sh
sudo nano create_config.py
```
Điền các giá trị phù hợp cho các loại TTS cần dùng. Lưu ý, tại 1 thời điểm chỉ được Active 1 TTS

1.3. Tạo File config

```sh
python3 create_config.py
```


### STEP2. Kích hoạt Webhook

2.1.Chạy
Sử dụng các tính năng sau:
```sh
cd /home/pi/realtime_tts_speaker/src
python3 start.py
```

2.2 Kiểm tra thông báo
Nếu hiện các thông báo sau:

```sh
 * Serving Flask app "start.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
 * Running on http://X.X.X.X:5000/ (Press CTRL+C to quit)
```
Là Webhook Server đã chạy thành công

### STEP3. Truyền text vào TTS để phát thông báo

3.1 Truyền trực tiếp
Truyền trực tiếp qua giao diện
 http://X.X.X.X:5000/
 
 Gõ Text, sau đó bấm Submit

3.2. Truyền qua API

3.2.1. Mô tả API

Địa chỉ: http://X.X.1.X:5000/api

Phương thức: POST

Định dạng bản tin: json

Cấu trúc bản tin: {"data":"Nội dung cần phát"} 

Phản hồi thành công: TTS sẽ trả về nội dung 'Playback OK'

Phản hồi không thành công: Trả về nội dung 'Playback not OK'

```sh
[BOT-TTS-GOOGLE-CLOUD]: Cộng hòa xã hội chủ nghĩa Việt Nam. Độc lập tự do hạnh phúc
Delayed: 5(s)
192.168.1.106 - - [27/Apr/2021 10:16:04] "POST /webhook HTTP/1.1" 200 -
```

3.2.2. Ví dụ với Home Assistant

Khai báo trong configuration.yaml
```sh
rest_command:
  vietbot_tts:
    url: http://192.168.1.109:5000/api
    method: POST
    payload: '{"data":"{{ data }}"}'
    content_type: 'application/json; charset=utf-8'
automation:
  alias: test
  description: ''
  trigger:
    - platform: device
      type: turned_off
      device_id: cc94e4e74c8e7bcf0a9f2649637d3734
      entity_id: switch.0x588e81fffede3767_switch_l2
      domain: switch
  condition: []
  action:
    - service: rest_command.vietbot_tts
      data:
        data: Đã tắt đèn rồi nhé anh 
  mode: single
```

### STEP4. Chạy tự động

4.1. Chạy bằng Systemd

4.1.1. Tạo file tts_speaker.service bằng lệnh

```sh
sudo nano /etc/systemd/system/tts_speaker.service
```
Tại cửa sổ Nano, gõ dòng lệnh sau

```sh
[Unit]
Description=tts_speaker
After=alsa-state.service

[Service]
ExecStart = /usr/bin/python3.9  /home/pi/tts_speaker/src/start.py
WorkingDirectory=/home/pi/tts_speaker/src
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```
Bấm Ctrl + X, Y, Enter

4.1.2. Gõ lệnh sau

```sh
sudo systemctl enable tts_speaker.service
```
Hệ thống sẽ hiện ra
```sh
Created symlink /etc/systemd/system/multi-user.target.wants/tts_speaker.service → /etc/systemd/system/vtts_speaker.service.
```
Hệ thống đã sẵn sàng tự động chạy tu dong tts_speaker

4.1.3. Gõ lệnh sau để chạy tự động tts_speaker
```sh
sudo systemctl start tts_speaker
```
hoặc
```sh
sudo reboot
```
4.1.4. Gõ lệnh sau để xem log
```sh
 sudo journalctl -u tts_speaker.service -f
```
4.1.5. Gõ lệnh sau để stop chạy tự động 

Gõ lệnh để stop

```sh
sudo systemctl stop tts_speaker.service
```
tts_speaker sẽ stop không chạy

Gõ lệnh để disable

```sh
sudo systemctl disable tts_speaker.service
```

Hệ thống sẽ hiện ra
```sh
Removed /etc/systemd/system/multi-user.target.wants/tts_speaker.service
```
Hệ thống đã stop tts_speaker không chạy tự động nữa
