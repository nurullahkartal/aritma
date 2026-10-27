/**
 * GÜVEN Su Arıtma Sistemleri - Gaziantep
 * Otomatik WhatsApp Servis & Talep Yönlendirme
 * İletişim: 0541 515 30 10
 */

document.addEventListener("DOMContentLoaded", function () {
  var forms = document.querySelectorAll("form");
  forms.forEach(function (form) {
    var submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
    if (!submitBtn) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var isim = (form.querySelector('input[name="isim"]') || {}).value || "";
      var tel = (form.querySelector('input[name="tel"]') || {}).value || "";
      var mail = (form.querySelector('input[name="mail"]') || {}).value || "";
      var konu = (form.querySelector('input[name="konu"]') || {}).value || "";
      var tarih = (form.querySelector('input[name="taleptarih"]') || {}).value || "";
      var adres = (form.querySelector('input[name="talepadres"]') || {}).value || "";
      var mesaj = (form.querySelector('textarea[name="mesaj"], input[name="mesaj"]') || {}).value || "";

      isim = isim.trim();
      tel = tel.trim();
      konu = konu.trim();
      adres = adres.trim();
      mesaj = mesaj.trim();

      if (!isim && !tel) {
        alert("Lütfen adınızı ve telefon numaranızı giriniz.");
        return;
      }

      var text = "💧 *GÜVEN SU ARITMA SERVİS TALEBİ* 💧\n" +
                 "━━━━━━━━━━━━━━━━━━━━━\n" +
                 "👤 *Müşteri:* " + (isim || "Belirtilmedi") + "\n" +
                 "📞 *Telefon:* " + (tel || "Belirtilmedi") + "\n";

      if (konu) {
        text += "📌 *Hizmet / Konu:* " + konu + "\n";
      }
      if (tarih) {
        text += "📅 *İstenen Tarih:* " + tarih + "\n";
      }
      if (adres) {
        text += "📍 *Adres / Bölge:* " + adres + "\n";
      }
      if (mesaj) {
        text += "📝 *Mesaj / Not:* " + mesaj + "\n";
      }

      text += "━━━━━━━━━━━━━━━━━━━━━\n" +
              "🌐 _Gaziantep Şehitkamil & Şahinbey Su Arıtma Hattı_";

      var waUrl = "https://api.whatsapp.com/send?phone=905415153010&text=" + encodeURIComponent(text);

      // WhatsApp'a yönlendir
      window.open(waUrl, "_blank");

      // Buton durumunu güncelle
      var originalHtml = submitBtn.innerHTML;
      submitBtn.innerHTML = "<i class='fas fa-check'></i> Talebiniz WhatsApp'a İletiliyor...";
      submitBtn.style.backgroundColor = "#25D366";
      submitBtn.style.color = "#ffffff";

      setTimeout(function () {
        submitBtn.innerHTML = originalHtml;
        submitBtn.style.backgroundColor = "";
        submitBtn.style.color = "";
      }, 4000);
    });
  });
});
