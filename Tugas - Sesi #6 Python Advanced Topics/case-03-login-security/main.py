# Studi Kasus 3: Sistem Keamanan Akun dan Audit Log Login

import re
from datetime import datetime
from functools import wraps


# Pola username: minimal 5 karakter dan hanya huruf/angka.
POLA_USERNAME = r"[A-Za-z0-9]{5,}"

# Pola password: minimal 8 karakter dan harus mengandung setidaknya satu angka.
POLA_PASSWORD = r"(?=.*\d).{8,}"


class User:
    """Model pengguna dengan atribut yang dikelola melalui property."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nilai):
        if not isinstance(nilai, str) or re.fullmatch(POLA_USERNAME, nilai) is None:
            raise ValueError(
                "Format username tidak valid: minimal 5 karakter dan hanya huruf/angka."
            )
        self._username = nilai

    @property
    def password(self):
        # Property ini dipakai oleh logika program, tetapi password tidak pernah
        # dimasukkan ke dalam audit log atau dicetak ke terminal.
        return self._password

    @password.setter
    def password(self, nilai):
        if not isinstance(nilai, str) or re.fullmatch(POLA_PASSWORD, nilai) is None:
            if isinstance(nilai, str) and len(nilai) < 8:
                raise ValueError("Password ditolak: panjang password minimal 8 karakter.")
            raise ValueError("Password ditolak: password wajib minimal 8 karakter dan mengandung angka.")
        self._password = nilai


def audit_login(fungsi_login):
    """Decorator untuk mencatat hasil login tanpa mencampuri validasi inti."""

    @wraps(fungsi_login)
    def pembungkus(username, password, akun_terdaftar):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            hasil = fungsi_login(username, password, akun_terdaftar)
            print(
                f"[AUDIT] {timestamp} | Username: {username} | "
                "Status: BERHASIL"
            )
            return hasil
        except ValueError as error:
            # Hanya alasan dan username yang dicatat. Password tidak pernah dicatat.
            print(
                f"[AUDIT] {timestamp} | Username: {username} | "
                f"Status: DITOLAK | Alasan: {error}"
            )
            return False

    return pembungkus


@audit_login
def login(username, password, akun_terdaftar):
    """Validasi kredensial lalu cocokkan dengan akun yang terdaftar."""
    pengguna_percobaan = User(username, password)

    if pengguna_percobaan.username != akun_terdaftar.username:
        raise ValueError("Username tidak terdaftar atau tidak cocok.")

    if pengguna_percobaan.password != akun_terdaftar.password:
        raise ValueError("Password tidak cocok.")

    return True


def main():
    # Akun demo untuk pengujian. Jangan gunakan password pribadi.
    akun_terdaftar = User("Reezd123", "Aman12345")

    print("=" * 76)
    print("              SISTEM LOGIN DAN AUDIT LOG")
    print("=" * 76)
    print("Pengujian 1: username mengandung simbol/spasi yang tidak diperbolehkan")
    login("Reez! 123", "Aman12345", akun_terdaftar)

    print("\nPengujian 2: password terlalu pendek")
    login("Reezd123", "abc123", akun_terdaftar)

    print("\nPengujian 3: password tidak mengandung angka")
    login("Reezd123", "passwordaman", akun_terdaftar)

    print("\nPengujian 4: kredensial sesuai")
    login("Reezd123", "Aman12345", akun_terdaftar)
    print("=" * 76)


if __name__ == "__main__":
    main()