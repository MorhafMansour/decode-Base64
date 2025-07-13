from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# فتح الملف المشفر وقراءته كـ bytes
# استخدم r"" لتجنب مشاكل escape في مسار الملف
with open(r"C:\the\path\for\encrypted\file", 'rb') as f:
    content = f.read()
    # تحويل محتوى الملف إلى تمثيل hex لسهولة التقسيم
    content_hex = content.hex()

# استخراج الـ IV (initialization vector) من أول 12 بايت (24 حرف hex)
iv = bytes.fromhex(content_hex[:24])
# استخراج التاج (tag) من آخر 16 بايت (32 حرف hex)
tag = bytes.fromhex(content_hex[-32:])
# استخراج النص المشفر (ciphertext) بين الـ IV والتاج
ciphertext = bytes.fromhex(content_hex[24:-32])

# المفتاح الخاص بفك التشفير (يجب أن يكون بنفس الطول المستخدم عند التشفير)
key_hex = "6433616462333366643361646233336664336164623333666433616462333366"
key = bytes.fromhex(key_hex)

# تهيئة كائن التشفير باستخدام AES في وضع GCM مع المفتاح، IV والتاج
cipher = Cipher(
    algorithms.AES(key),
    modes.GCM(iv, tag),
    backend=default_backend()
)
decryptor = cipher.decryptor()

try:
    # محاولة فك التشفير
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    # طباعة النص المفكوك مع تجاهل الأخطاء في الترميز
    print("Decrypted Text:")
    print(plaintext.decode('utf-8', errors='ignore'))
except Exception as e:
    # في حال حدوث أي خطأ أثناء فك التشفير، طباعة رسالة الخطأ
    print("Failed to decrypt:", e)

