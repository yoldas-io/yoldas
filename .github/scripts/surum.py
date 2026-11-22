"""Yoldaş GitHub deposu: yoldas.io'daki canlı sürümü GitHub sürümü olarak yayınlar (GitHub Actions'ta çalışır).

Kaynak kod yok; yalnız herkese açık bilgiler okunur:
- https://yoldas.io/en/download : sürüm adı (data-apk="surum"), sürüm kodu (APK bağlantısı), SHA-256 (data-apk="sha256")
- https://yoldas.io/indir/yoldas-arac-<kod>.apk : APK
- https://yoldas.io/surum-notlari.json : sürüm notları (13 dil)

APK'nın SHA-256'sı siteyle, imza sertifikası beklenen parmak iziyle eşleşmezse hiçbir şey yayınlanmaz.
Çıktı: README.md / README.tr.md sürüm tablosu, CHANGELOG.md / CHANGELOG.tr.md, release/ (APK, .sha256, notes.md)
ve GITHUB_OUTPUT'a tag/ad/yeni bayrağı. Üreten: scripts/github/github_deposu.py (ana depo, özel).
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request

SITE = "https://yoldas.io"
IMZA = "dd695000acb1d946491b04d2f5f69a019c57c0b6c45588562044fec255a1277e"
UA = {"User-Agent": "yoldas-github-release/1.0"}


def al(yol, ham=False):
    with urllib.request.urlopen(urllib.request.Request(SITE + yol, headers=UA), timeout=120) as y:
        veri = y.read()
    return veri if ham else veri.decode("utf-8")


def cikti(ad, deger):
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"{ad}={deger}\n")
    print(f"{ad}={deger}")


def madde(m):
    if not isinstance(m, dict):
        return f"- {m}"
    v, t = (m.get("vurgu") or "").strip(), (m.get("metin") or "").strip()
    return f"- **{v}** {t}" if v else f"- {t}"


def changelog(notlar, dil, bas):
    out = [bas]
    for n in notlar:
        out.append(f"\n## {n['surumAdi']} ({n['tarih']})\n")
        out += [madde(m) for m in (n["diller"].get(dil) or n["diller"].get("en") or n["diller"]["tr"])]
    return "\n".join(out).strip() + "\n"


def main():
    sayfa = al("/en/download")
    surum = re.search(r'data-apk="surum">([0-9.]+)<', sayfa).group(1)
    kod = re.search(r'href="/indir/yoldas-arac-([0-9]+)\.apk"', sayfa).group(1)
    sha = re.search(r'data-apk="sha256">([0-9a-f]{64})<', sayfa).group(1)
    tag = f"v{surum}"
    var = subprocess.run(["gh", "release", "view", tag], capture_output=True).returncode == 0
    if var and "--zorla" not in sys.argv:
        print(f"{tag} zaten yayında; yapılacak bir şey yok.")
        cikti("yeni", "hayir")
        return

    apk_ad = f"yoldas-arac-{kod}.apk"
    os.makedirs("release", exist_ok=True)
    for eski in glob.glob("release/*"):
        os.remove(eski)
    apk = al(f"/indir/{apk_ad}", ham=True)
    if hashlib.sha256(apk).hexdigest() != sha:
        sys.exit("APK'nın SHA-256'sı sitedekiyle uyuşmuyor; yayın durduruldu.")
    with open(f"release/{apk_ad}", "wb") as f:
        f.write(apk)
    with open(f"release/{apk_ad}.sha256", "w", encoding="utf-8", newline="\n") as f:
        f.write(f"{sha}  {apk_ad}\n")
    araclar = sorted(glob.glob(os.path.join(os.environ.get("ANDROID_HOME", "/usr/local/lib/android/sdk"), "build-tools", "*", "apksigner")))
    if not araclar:
        sys.exit("apksigner bulunamadı; imza doğrulanamadı.")
    imza = subprocess.run([araclar[-1], "verify", "--print-certs", f"release/{apk_ad}"], capture_output=True, text=True).stdout
    if f"certificate SHA-256 digest: {IMZA}" not in imza:
        sys.exit("APK imza sertifikası beklenenle uyuşmuyor; yayın durduruldu.")

    notlar = json.loads(al("/surum-notlari.json"))["notlar"]
    bu = next((n for n in notlar if n["surumAdi"] == surum), None)
    en = "\n".join(madde(m) for m in bu["diller"]["en"]) if bu else "See https://yoldas.io/en/release-notes"
    tr = "\n".join(madde(m) for m in bu["diller"]["tr"]) if bu else "Bkz. https://yoldas.io/surum-notlari"
    with open("release/notes.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(f"""{en}

<details><summary>Türkçe</summary>

{tr}

</details>

| | |
|---|---|
| File | `{apk_ad}` |
| SHA-256 | `{sha}` |
| Signing certificate SHA-256 | `{IMZA}` |

Install guide: https://yoldas.io/en/install · Kurulum: https://yoldas.io/byd-uygulama-yukleme
""")

    for dosya in ("README.md", "README.tr.md"):
        if not os.path.exists(dosya):
            continue
        s = open(dosya, encoding="utf-8").read()
        s = re.sub(r"^\| APK \| `[^`]*` \([0-9]+\) \|$", f"| APK | `{surum}` ({kod}) |", s, flags=re.M)
        s = re.sub(r"^\| SHA-256 \| `[0-9a-f]{64}` \|$", f"| SHA-256 | `{sha}` |", s, flags=re.M)
        open(dosya, "w", encoding="utf-8", newline="\n").write(s)
    open("CHANGELOG.md", "w", encoding="utf-8", newline="\n").write(changelog(
        notlar, "en", "# Release notes\n\nThe same notes appear in the app after an update and on [yoldas.io](https://yoldas.io/en/release-notes).\n"))
    open("CHANGELOG.tr.md", "w", encoding="utf-8", newline="\n").write(changelog(
        notlar, "tr", "# Sürüm notları\n\nAynı notlar güncellemeden sonra uygulamada ve [yoldas.io](https://yoldas.io/surum-notlari) adresinde de görünür.\n"))

    cikti("yeni", "evet")
    cikti("tag", tag)
    cikti("ad", f"Yoldaş {surum} ({kod})")
    cikti("apk", apk_ad)


if __name__ == "__main__":
    main()
