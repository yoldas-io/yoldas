# Yoldaş güvenli mi?

Aracınıza kurduğunuz bir uygulamanın ne yaptığını bilmeniz gerekir. Bu sayfada Yoldaş'ın hangi verileri topladığını, nereye gönderdiğini ve nasıl koruduğunu sade bir dille anlatıyoruz.

Son güncelleme: 15 Ekim 2026

## Hangi veriler gönderilir?

Ölçüm gönderimi **sizin onayınızla** açılır; konum için ayrıca onay istenir. Onay verirseniz şunlar Yoldaş'ın sunucusuna gider:

- Araç ölçümleri: batarya, menzil, hız, lastik basıncı, 12 V akü, tüketim gibi değerler.
- Olaylar: kilit, kapı, bagaj, park ve sürüş geçişi, şarj başlangıcı ve bitişi.
- Nöbetçi olayları: zamanı, türü, yönü, yaklaşık açısı, yakınlık sınıfı, nöbetçi durumu, model sürümü ve dosya özeti.
- Konum (ayrı onayla): yolculuk rotası ve "aracım nerede" için.
- Araç profili: model kodu ve yazılım sürümü.
- Bağlantı tanısı için Wi-Fi ağ adı ve aracın yerel ağ adresi.

Kurulum, onay, yardımcı ve geçiş adımları gibi kısa tanı olayları, sorunların nedenini bulmak için onay beklemeden gönderilir. Kişisel veriler bu olaylardan süzülür.

## Neler gönderilmez?

- **Şasi numarası (VIN).** Araçta kalır. Lisans için yalnız ondan üretilen, geri çevrilemeyen bir özet kullanılır.
- **Kamera kayıtları.** Araçta kalır ve kendiliğinden sunucuya yüklenmez. Telefonda istediğinizde yalnız seçtiğiniz kayıt araçtan alınır.
- **Canlı görüntü.** Sunucudan geçer ama saklanmaz.
- **Nöbetçi görüntüleri.** İncelenen küçük görüntüler diske veya buluta yazılmaz; sunucuya yalnız olayın bilgileri gider (yukarıdaki liste). Yüz, görüntü kutusu ya da kişi kimliği gönderilmez.

## Veriler nasıl korunur?

- Bütün bağlantılar HTTPS ile şifrelenir; tarayıcılara yalnız HTTPS kullanmaları söylenir (HSTS).
- Hesap parolaları açık metin olarak saklanmaz; güçlü bir özetleme yöntemiyle (PBKDF2) saklanır.
- Telefona giden bildirimlerin içeriği, telefona özel anahtarla şifrelenir.
- Yönetim paneli internete kapalıdır; yalnız sunucuya güvenli tünelle bağlanarak açılır.
- Her hesap yalnız kendi aracının verisini görür.

## Canlı kamera ve telefon komutları

- Kameraları yalnız aracın sahibi olan hesap izler; aynı anda tek izleme, en çok 10 dakika.
- İzleme için araç internete bağlı, "Telefondan kontrol" açık ve lisansı etkin olmalı; kamera ve ekran üstü gösterme izni de verilmiş olmalıdır.
- Araç ekranındaki kırmızı "canlı izleniyor" işareti ve Durdur düğmesi varsayılan olarak gizlidir. Güvenlik › Kayıt ve koruma bölümünden açarsanız izleme sürerken çizilir.
- Kabin sesini dinleme ve araca konuşma ayrı izinle açılır.
- Telefon komutları tek kullanımlıktır ve en çok 60 saniye geçerlidir. Her komut ve sonucu kayda geçer.
- Telefondan araç kontrol komutları için güvenli kullanım onayı gerekir; onay yoksa komut reddedilir (durdurma komutları hariç). Onayın sürümü, metin özeti ve zamanı kaydedilir; geçmişi silmek bu kaydı silmez.
- Telefondan kontrol ve Yoldaş yardımcısı açıkken bağlantı kontak kapandıktan sonra da sürer; isterseniz koyduğunuz pil ya da 12 V akü alt sınırının altına inince bırakılır (varsayılan olarak sınır yoktur).
- Araçta Sistem › Telefondan kontrol kapatılırsa hiçbir telefon komutu çalışmaz.

## İmzalı güncellemeler

Yoldaş'ın bütün sürümleri aynı anahtarla imzalanır. Otomatik güncelleme, kurmadan önce dosyanın bütünlüğünü, paket adını, sürüm numarasını ve imzasını denetler; eski bir sürümü yeniymiş gibi kurmaz. Güncellemeler yalnız HTTPS üzerinden, Wi-Fi'de ya da aracın kendi mobil verisinde iner (dolaşımdayken mobil veriyle inmez). Güncel APK her zaman [indirme sayfasında](https://yoldas.io/indir); dosyanın özetini [SHA-256 rehberiyle](https://yoldas.io/rehber/apk-sha256-dogrulama) doğrulayabilirsiniz.

## Uygulamanın istediği izinler
İzinNe için KameraKamera görüntüsü, kayıt, canlı izleme ve nöbetçi. MikrofonKabin sesini dinlemeyi ya da konuşmayı siz açarsanız; sesli dashcam kaydında da. KonumYolculuk rotası ve aracın son konumu. Ayrı onayla. Diğer uygulamaların üzerinde göstermeCanlı izleme işareti, sinyal kamerası ve bilgi şeridi. BildirimArka planda çalıştığını gösteren kalıcı bildirim. Uygulama yüklemeKendini güncellerken indirilen yeni sürümü kurmak. Pil kısıtlaması dışında kalmaArka planda kesilmeden çalışmak. Telefon durumuAracın mobil veri bağlantısının durumunu (dolaşım dahil) görüp bağlantı sorunlarını tanımak. Açılışta başlama, uyanık kalmaAraç açılınca Yoldaş'ı başlatmak ve işlemler sürerken cihazı kısa süre uyanık tutmak. Erişilebilirlik hizmetleri (iki adet)Biri, araç güncellemesinden sonra sıfırlanan otomatik başlatma iznini düzeltir. Diğeri yalnız siz bağlantı hazırlamayı başlatınca araçtaki doğrulama ekranını okuyup kurulumu yapar. Hiçbir kimlik bilgisi kaydedilmez ya da gönderilmez.

Araç ekranında Yoldaş'ı PIN ile kilitleyebilirsiniz (Sistem › Uygulama kilidi).

## Verilerinizi silme

Telefon uygulamasında Hesap bölümündeki **"Bu aracın geçmişini sil"** ile sunucudaki ölçümler, yolculuk özetleri ve rotaları, aracın son durumu, olaylar ve şarj kayıtları silinir; yedekleme ve konum onayınız da kapanır. Tercihleriniz, komut günlüğü, bildirim geçmişi, tanı günlüğü ve onay kayıtları bu işlemle silinmez. Hesabınızın tamamen silinmesi için bize yazın: [iletisim@yoldas.io](mailto:iletisim@yoldas.io). Kişisel verilerle ilgili haklarınız [gizlilik sayfasında](https://yoldas.io/gizlilik).

Bir güvenlik açığı bulduysanız lütfen önce bize bildirin: [iletisim@yoldas.io](mailto:iletisim@yoldas.io).

## Sık sorulan sorular

### Yoldaş aracımın şasi numarasını (VIN) gönderiyor mu?

Hayır. Şasi numarası araçta kalır. Lisans için yalnız şasi numarasından üretilen, geri çevrilemeyen bir özet kullanılır.

### Kamera görüntüleri sunucuya gidiyor mu?

Kayıtlar araçta kalır ve kendiliğinden yüklenmez. Canlı izlemede görüntü sunucudan yalnız geçer, saklanmaz. Nöbetçi modunun incelediği küçük görüntüler hiçbir yere yazılmaz.

### Verilerimi nasıl silerim?

Telefon uygulamasında Hesap bölümündeki "Bu aracın geçmişini sil" ile ölçümler, yolculuklar, olaylar ve şarj kayıtları sunucudan silinir. Hesabınızın tamamen silinmesi için bize yazın.
