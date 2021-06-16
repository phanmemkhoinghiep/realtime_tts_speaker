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

2.1. Kích hoạt môi trường
Sử dụng các tính năng sau:
```sh
cd /home/pi/realtime_tts_speaker/src
```
2.2. Kích hoạt Flask

```sh
export FLASK_APP=tts.py
python3 -m flask run --host=X.X.X.X 
```
Với X.X.X là địa chỉ IP của Mạch phần cứng chạy TTS, ví dụ ở đây là: 192.168.1.109

Nếu hiện các thông báo sau:

```sh
 * Serving Flask app "tts.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
pygame 1.9.4.post1
Hello from the pygame community. https://www.pygame.org/contribute.html
 * Running on http://192.168.1.109:5000/ (Press CTRL+C to quit)
```
Là Webhook Server đã chạy thành công

### STEP3. Truyền tín hiệu vào TTS để phát thông báo

3.1. Mô tả về API

Tại nguồn truyền, sử dụng tính năng webhook, phát bản tin với định dạng json là {"data":"Nội dung cần phát"} vào địa chỉ là http://192.168.1.109:5000/webhook

```sh
[BOT-TTS-GOOGLE-CLOUD]: Cộng hòa xã hội chủ nghĩa Việt Nam. Độc lập tự do hạnh phúc
Delayed: 5(s)
192.168.1.106 - - [27/Apr/2021 10:16:04] "POST /webhook HTTP/1.1" 200 -
```
Trong trường hợp thành công, TTS sẽ trả về nội dung 'Playback OK', không thành công sẽ trả về nội dung 'Playback not OK' trên Client

3.2. Ví dụ với Home Assistant

Khai báo trong configuration.yaml
```sh
rest_command:
  vietbot_tts:
    url: http://192.168.1.109:5000/webhook
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

4.1. Tự động bằng crontab

4.1.1. Tạo nơi lưu log

```sh
cd ~
mkdir logs
```
4.1.2. Khai báo crontab

```sh
crontab -e
```
Chọn 1 để edit bằng nano 
Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi gõ

```sh
@reboot sh /home/pi/realtime_tts_speaker/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

4.1.3. Khởi động lại Pi 

```sh
sudo reboot
```
TTS sẽ tự động chạy khi khởi động Pi 

4.1.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
4.1.5. Gỡ tự động chạy khi khởi động Pi (Nếu cần)

```sh
crontab -e
```
Chọn 1 để edit bằng nano 

Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi xóa dòng sau

```sh
@reboot sh /home/pi/realtime_tts_speaker/src/start.sh >/home/pi/logs/cronlog 2>&1i
```
Bấm Ctrl + X, Y, Enter

Khởi động lại Pi 

```sh
sudo reboot
```
TTS sẽ không tự động chạy khi khởi động Pi nữa


