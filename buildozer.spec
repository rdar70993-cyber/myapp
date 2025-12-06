[app]
# نام اپلیکیشن
title = TestApp
# نام پکیج (یونیک باشه)
package.name = testapp
package.domain = org.test

# فایل اصلی پروژه
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# فایل entry point
main.py = main.py

# آیکون اپ (اختیاری)
icon.filename = %(source.dir)s/icon.png

# نسخه اپ
version = 0.1

# نیازمندی‌های پایتون
requirements = python3,kivy

# تنظیمات مجوزها
android.permissions = INTERNET

# خروجی APK
android.arch = armeabi-v7a

[buildozer]
# پلتفرم هدف
log_level = 2
warn_on_root = 1
