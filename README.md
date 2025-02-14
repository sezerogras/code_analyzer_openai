🚀 Code Analyzer with OpenAI
Bu proje, Python kodlarını analiz ederek performanslarını ölçen ve OpenAI API kullanarak iyileştirme önerileri sunan bir araçtır. Streamlit tabanlı bir web uygulaması olarak geliştirilmiştir.









📌 Özellikler
Kullanıcı tarafından girilen Python kodunun çalışma süresini ölçer
Bellek kullanımını analiz eder
Kodun karmaşıklığını belirler
OpenAI API ile kod hakkında yorum ve iyileştirme önerileri sunar









🛠 Kullanılan Teknolojiler
Python 3.x
Streamlit (Web Arayüzü)
Timeit (Çalışma süresi ölçümü)
Memory Profiler (Bellek analizi)
Radon (Kod karmaşıklık analizi)
OpenAI API (Kod inceleme ve öneriler)











📦 Kurulum
Öncelikle gerekli bağımlılıkları yükleyin:






pip install streamlit memory-profiler radon openai








Ardından, app.py dosyasını çalıştırarak uygulamayı başlatabilirsiniz:









streamlit run app.py









📊 Kullanım
Uygulama açıldıktan sonra, kodunuzu metin alanına girin
"Analiz Et" butonuna tıklayın
Kodunuzun çalışma süresi, bellek kullanımı ve karmaşıklık seviyesi hesaplanır
OpenAI API, kodunuzu değerlendirir ve iyileştirme önerileri sunar








📁 Dosya Açıklamaları
app.py → Ana uygulama dosyası (Streamlit arayüzünü çalıştırır)
code_analyzer.py → Kodun performans analizini yapan modül
openai_review.py → OpenAI API ile kod incelemesi yapan modül









🔑 API Anahtarı
OpenAI API'yi kullanabilmek için openai_review.py içinde API anahtarınızı ayarlamanız gerekmektedir:








OPENAI_API_KEY = "Your_OPENAI_API_Key"







📜 Lisans
Bu proje, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.















