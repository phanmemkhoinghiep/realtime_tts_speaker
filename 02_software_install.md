### HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER

### STEP1. Cài đặt hệ điều hành Raspbian

1.1. Download Raspberry Pi OS
Tối ưu cho phần cứng Pi Zero Wireless nên Vietbot chỉ cần bản OS Buster Lite

Download đúng phiên bản sau tại địa chỉ:

https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-01-12/2021-01-11-raspios-buster-armhf-lite.zip

1.2. Flash vào thẻ nhớ
Sử dụng tool của Raspberry hoặc Etcher

1.3. Config để vào được SSH qua WiFi

1.3.1. Cắm lại thẻ nhớ vào máy

1.3.2. Sử dụng Notepad ++ để tạo file có tên là wpa_supplicant.conf trong thư mục boot của thẻ nhớ với  định dạng file Unix (Edit -> EOL converion -> UNIX/OSX Format là Unix (LF)), nội dung là các tham số tên SSID và mật khẩu tương ứng
Chú ý, tham số country có thể đổi sang us hoặc vn tùy theo cài đặt tại bộ phát WiFi
```sh
country=vn
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="testing"
    psk="testingPassword"
}
```
1.3.3. Tạo file rỗng có tên là SSH trong thư mục boot 

1.4. Truy cập ssh vào Pi Zero Wirless

1.4.1. Cắm thẻ nhớ vào Pi Zero Wireless, chờ Pi boot up xong, xác định IP của Pi từ Modem, Access Pint

1.4.2. Sử dụng putty truy cập ssh vào địa chỉ IP của Pi với username là pi, password là raspberry


### STEP2. Cài đặt các thư viện chung cho Vietbot và thư viện cho Python trên OS

2.1. Cài đặt các thư viện chung cho Vietbot

Chạy lần lượt các lệnh sau
2.1.1.
```sh
sudo apt-get update -y
```
sau đó 
```sh
sudo apt-get upgrade -y
```
2.1.2.

```sh
sudo apt-get install libportaudio2 libatlas-base-dev libsdl2-mixer-2.0-0 libpq-dev libssl-dev libffi-dev zlib1g-dev libportaudio-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev libmpg123-dev -y

```
2.1.3.

```sh
sudo apt-get install git wget openssl vlc ffmpeg flac -y
```

2.2. Khởi động lại
```sh
sudo reboot

```
2.3. Cài đặt các thư viện cho Python

Chạy lần lượt các lệnh sau
```sh
sudo apt-get install python3-pip python3-setuptools python3-psutil python3-bottle python3-requests python3-dev python3-pyaudio python3-numpy python3-pip python3-wheel python3-dev python3-pygame python3-bs4 -y
```

### STEP3. Cài đặt các gói Python

3.1. Nâng cấp PIP

Chạy lần lượt các lệnh sau
```sh
python3 -m pip install --upgrade pip

```
3.2. Cài đặt các gói Python cơ bản

```sh
python3 -m pip install python-Levenshtein PyAudio pygame pyalsaaudio pyyaml pyusb pyalsaaudio pyyaml pydub pyglet

```

3.3. Cài đặt các gói Python liên quan 
```sh
python3 -m pip install ffmpeg termcolor datefinder mutagen playsound wget enums untangle html5lib BeautifulSoup4 python-vlc pathlib2 urllib3 sounddevice click tenacity futures setuptools wheel spidev  snumpy google-trans-new

python3 -m pip install --upgrade google-assistant-library==1.0.1  --upgrade google-assistant-grpc --upgrade google-assistant-sdk[samples]==0.5.1 --upgrade google-auth-oauthlib[tool]

python3 -m pip install google-cloud googletrans google-cloud-texttospeech

```


### STEP4. Config MSpeaker


4.1. Thống kê ID của Mic và Loa 

4.1.1. Lấy ID của Mic & Loa

Chạy lệnh sau để biết ID của Mic USB
```sh
arecord -l
```
sau đó chạy lệnh sau để biết ID của Loa

```sh
aplay -l
```
Lưu lại thông tin về card_id và device_id ở mỗi kết quả lệnh

4.2. Khai báo 

4.2.1. Cài Pulseaudio

Chạy lệnh sau 
```sh
sudo apt-get install pulseaudio -y
```
4.2.2. Khai báo Asoundrc

```sh
sudo nano /home/pi/.asoundrc
```
Cửa sổ nano hiện lên, paste dòng sau, thay thế <card_id> và <device_id> bằng kết quả đã lưu ví dụ 0:0 hoặc 1:0 hoặc 1:1:

```sh
pcm.!default {
  type asym
  capture.pcm "mic"  
  playback.pcm "speaker"  
}
pcm.mic {
  type plug
  slave {
    pcm "hw:<card_id>,<device_id>"
  }
}
pcm.speaker {
  type plug
  slave {
    pcm "hw:<card_id>,<device_id>"
  }
}
```
Bấm lần lượt Ctrl + X, sau đó Y rồi Enter

4.3. Copy file thiết lập cho mọi account (Nếu chỉ dùng Account Pi thì bỏ qua bước này)

Chạy lệnh sau
```sh
sudo cp /home/pi/.asoundrc /etc/asound.conf
```
4.4. Reboot lại Pi
Chạy lệnh sau
```sh
sudo reboot
```

### STEP5. Cấu hình thời gian, tối ưu cho Pi (Nếu dùng Raspberry Pi)

5.1. Chạy config
Chạy lệnh sau
```sh
sudo raspi-config
```
5.2. Cài đặt thời gian với múi giờ VN

```sh
Chọn mục số 5 Localisation Options, Select rồi Enter

Chọn L2 Time Zone

Chọn Asia

Chọn Ho Chi Minh City, OK rồi Enter

5.3. Cài đặt Pi khởi động với Command line để tiết kiệm bộ nhớ

Chọn mục System Options, Select rồi Enter

Chọn S5 Boot/ Auto Login, Select rồi Enter

Chọn B2, OK

5.4. Giảm bộ nhớ RAM dùng cho đồ họa

Chọn mục Performance Options, Select rồi Enter

Chọn P2 GPU Memory, Select rồi Enter

Chọn 16, OK

5.5. Khởi động lại Pi

Khi thoát khỏi Raspi Config, chọn Yes để khởi động lại

```
