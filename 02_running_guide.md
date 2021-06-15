### HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG

### STEP1. Cài đặt 

1.1. Download Code về Pi theo cách sau:

Truy cập vào Git
Trên console của Pi, sử dụng lệnh sau

```sh
cd ~ 
```
1.2. Kết nối vào Git TTS bằng lệnh sau:

```sh
git clone https://github.com/phanmemkhoinghiep/realtime_tts_speaker.git
Cloning into 'realtime_tts_speaker'...
```
1.3. Nhập username và password cho github

```sh
Username for 'https://github.com': your_username
Password for 'your_password': 
remote: Enumerating objects: 80, done.
remote: Counting objects: 100% (80/80), done.
remote: Compressing objects: 100% (80/80), done.
remote: Total 1597 (delta 37), reused 0 (delta 0), pack-reused 1517
Receiving objects: 100% (1597/1597), 74.75 MiB | 819.00 KiB/s, done.
Resolving deltas: 100% (766/766), done.
Checking out files: 100% (102/102), done.
```

### STEP2.  Truy nhập vào thư mục TTS

2.1. Truy cập vào thư mục realtime_tts_speaker

Sử dụng lệnh sau

```sh
cd realtime_tts_speaker/src
```
2.2. Edit File config

```sh
sudo nano create_config.py
```
Điền các giá trị phù hợp cho các loại TTS cần dùng. Lưu ý, tại 1 thời điểm chỉ được Active 1 TTS

2.3. Tạo File config

```sh
python3 create_config.py
```


### STEP2. Kích hoạt Webhook

Sử dụng các tính năng sau:
```sh
cd /home/pi/realtime_tts_speaker/src
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

Tại nguồn truyền, sử dụng tính năng webhook, phát bản tin với định dạng json là {"data":"Nội dung cần phát"} vào địa chỉ là http://192.168.1.109:5000/webhook

```sh
[BOT-TTS-GOOGLE-CLOUD]: Cộng hòa xã hội chủ nghĩa Việt Nam. Độc lập tự do hạnh phúc
Delayed: 5(s)
192.168.1.106 - - [27/Apr/2021 10:16:04] "POST /webhook HTTP/1.1" 200 -
```
Trong trường hợp thành công, TTS sẽ trả về nội dung 'Playback OK', không thành công sẽ trả về nội dung 'Playback not OK' trên Client

Ví dụ với Home Assistant

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


