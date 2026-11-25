# Python 101

Python 3'e giriş için yazılmış kısa örnekler: değişkenler, kullanıcıdan veri alma, operatörler, karar yapıları, döngüler, listeler, matematik ve rastgele sayı fonksiyonları, metin işlemleri.

> **Not:** Bu depo 2017 yılında eğitim amaçlı yazıldı ve artık güncellenmiyor.

## İçerik

Her örnek `HellWorld/` altında kendi klasöründe, `__init__.py` dosyasındadır.

| Klasör | Konu |
|---|---|
| `Example1Hello` | Ekrana yazdırma |
| `Example2VariableType` | Değişken türleri |
| `Example3InputValue` | Kullanıcıdan veri alma |
| `Example4BasicOperators` | Aritmetik, karşılaştırma ve atama operatörleri |
| `Example5Decision` | `if` / `elif` / `else` |
| `Example5Loops` | `while` ve `for` döngüleri |
| `Example6Lists` | Liste işlemleri |
| `Example7MathematicalFunctions` | `math` modülü |
| `Example8RandomNumberFunctions` | `random` modülü |
| `Example9LoopList` | Metin ve liste üzerinde döngü |
| `Example10LoopBreak` | `for` ve `while` döngülerinde `break` |
| `Example11String` | Metin dilimleme, kaçış karakterleri, metin birleştirme |

## Teknolojiler

- Python 3.6 (başlangıçta Eclipse PyDev ile yazıldı)
- Dış bağımlılık yok

## Çalıştırma

Her örnek tek başına çalışır:

```
python HellWorld/Example1Hello/__init__.py
```

`Example2VariableType` ve `Example3InputValue` dosyalarının başında IDE'nin otomatik eklediği gereksiz `import` satırları var (`test.pickletester`, `pip._vendor...`). Bu modüller ortamınızda yoksa o satırı silin; `Example3` için `raw_input` yerine Python 3'teki `input` kullanılabilir.
