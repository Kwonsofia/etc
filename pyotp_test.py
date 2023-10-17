import pyotp
from datetime import datetime

# Test 1 - pyotp (https://github.com/pyauth/pyotp)
secret_key = pyotp.random_base32()  # secret_key를 유저마다 다르게 해야하기 때문에 발급된 secret_key를 저장할 필드 추가 필요함
print(secret_key)
totp = pyotp.TOTP(secret_key).provisioning_uri(name='test@google.com', issuer_name='OtpTest')  # name에는 각 유저의 email 넣기
print(totp)
# terminal : qrcode otpauth://totp/OtpTest:test%40google.com?secret=GFHNHFPYGBAL3D5K74OJ5YDISAQR6FXN&issuer=OtpTest

secret_key = 'GFHNHFPYGBAL3D5K74OJ5YDISAQR6FXN'
totp = pyotp.TOTP(secret_key)
now = datetime.now()  # 현재 시간
print("now otp: " + totp.now())  # 현재 값
print('next otp : ', totp.at(int(now.timestamp()) + 30))  # 30초후 변경되는 값
