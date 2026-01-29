[app]

# اسم التطبيق
title = تطبيقي

# اسم الحزمة
package.name = myapp

# نطاق الحزمة
package.domain = org.myapp

# مجلد الكود المصدري
source.dir = .

# امتدادات الملفات المطلوبة
source.include_exts = py,png,jpg,kv,atlas,txt,json

# رقم الإصدار
version = 0.1

# المكتبات المطلوبة
requirements = python3,kivy==2.3.0

# اتجاه الشاشة (portrait للعمودي، landscape للأفقي)
orientation = portrait

# شاشة كاملة
fullscreen = 0

# الصلاحيات
android.permissions = INTERNET

# إصدار Android API
android.api = 33

# الحد الأدنى للـ API
android.minapi = 21

# إصدار SDK
android.sdk = 33

# إصدار NDK
android.ndk = 25b

# المعماريات المدعومة
android.archs = arm64-v8a,armeabi-v7a

[buildozer]

# مستوى السجلات (2 للتفصيل الكامل)
log_level = 2

warn_on_root = 1
