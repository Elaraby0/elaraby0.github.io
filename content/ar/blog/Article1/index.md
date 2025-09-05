---
title: تابِع المجلات العلمية والكلمات المفتاحية علي PubMed بذكاء
date: 2025-08-16T19:21:24+03:00
lastmod: 2025-08-16T19:21:24+03:00
draft: false
lang: ar
translationKey: "1755353729-Never Miss a Paper Again: PubMed-Scopus RSS → Telegram in 10 Minutes"
description: دليل عملي للباحثين الذين يريدون أن تصلهم الأوراق الجديدة تلقائيًا—سواء في قارئ RSS أو مباشرةً إلى قناة/مجموعة على تيليجرام.
summary: ""
tags: 
  - RSS
  - البحث السريري
  - PubMed
  - Scopus
  - مجلات_علمية
  - تيليجرام
  - حيل_حياتية
categories: 
series: 
showToc: true
TocOpen: false
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowReadingTime: true
ShowShareButtons: true
ShowWordCount: false
comments: false
hidemeta: false
disableShare: false
cover:
  image: group_12552.png
  alt: ""
  caption: ""
  relative: true
math: false
mermaid: false
canonicalURL: ""
aliases: 
weight: 1
---

## لماذا لا تزال خلاصات RSS رائعة للباحثين

 هو انتقال التحديثات او المقالات الجديده من مصدرٍ ما (مجلة، نتيجة بحث، مؤلف… إلخ). إلى قناتك على تيليجرام او مجموعتك او قارئ الخلاصات الخاص بك.
 سريع، خفيف، ويعمل عبر معظم المواقع الأكاديمية.

![Pastedimage20250816184034.png](/Pastedimage20250816184034.png)

## ما الذي ستحتاجه

- **مكان واحد لاستقبال التحديثات:**
    
    - **قارئ RSS** (مثل Inoreader، وFeedly، وNewsBlur، وNetNewsWire، وReeder).
        
    - **أو** إعداد **تيليجرام** (Feed Reader Bot / RSS bot) لدفع التحديثات إلى **قناة** أو **مجموعة**.
        
- **مصادرك:** عمليات بحث PubMed وScopus أو صفحات المجلات العلمية.
    

## في PubMed: حوِّل أي بحث إلى خلاصة RSS

1. **أجرِ بحثك على PubMed** وطبّق الفلاتر (تجارب سريره فقط، مراجعات، الأحدث، أنواع المقالات، اللغة… إلخ).
    
2. انقر **Create RSS** أسفل صندوق البحث مباشرة.
    
3. قم بتسمية الخلاصة، ثم انقر **Create RSS**.
    
4. انسخ رابط **RSS Feed**.  
    ![Pasted image 20250816184853.png](/Pastedimage20250816184853.png)
    

### بالنسبة إلى Scopus وWeb of Science وبقية قواعد البيانات

غالبًا ستتّبع الخطوات نفسها التي اتّبعناها في PubMed، وسترى علامة خلاصة RSS في صفحة نتائج البحث.

---

## مجلات ومواقع بلا خلاصة ظاهرة

- كثيرٌ من المجلات يوفّر خلاصات **Latest / Early View / In Press**—ابحث عن أيقونة RSS البرتقالية أو رابط “RSS/XML” في التذييل.  
    إليك مثالًا من [JAMA Network](https://jamanetwork.com/)  
    - ![Pasted image 20250816185412.png](/Pastedimage20250816185412.png)
		- ![Pasted image 20250816185432.png|355](/Pastedimage20250816185432.png)
    
- إذا لم يوفّر الموقع خلاصة، يمكنك توليد واحدة بإضافة كروم مفتوحة المصدر [**RSSHub Radar**](https://chromewebstore.google.com/detail/rsshub-radar/kefjpfngnndepjbopdmoebkipbgkggaa).
    

---

## أين تقرأ المقالات الجديدة

### 1) قارئ RSS تقليدي

استخدم [Inoreader](https://www.inoreader.com/)/[Feedly](https://feedly.com/): الصق رابط الخلاصة.  
![Pasted image 20250816185939.png](/Pastedimage20250816185939.png)
![Pasted image 20250816190004.png](/Pastedimage20250816190004.png)

### 2) تيليجرام (للمتابعين أو للمتابعه الشخصيه)

**[RSS Bot](https://t.me/rss2tg_bot) (@rss2tg_bot)**

- للنشر داخل **قناة** أو **مجموعة**:
    
    1. أضِف البوت كـ **مشرف (Admin)** في القناة/المجموعة.
        
    2. داخل البوت: استخدم `/channel` (أو `/group`) → اختر الوجهة → ثم `/add <feed_url>`.
        
        ![Pasted image 20250816190347.png|280](/Pastedimage20250816190347.png) 
        ![Pasted image 20250816190436.png|252](/Pastedimage20250816190436.png)
        ![Pasted image 20250816190456.png|219](/Pastedimage20250816190456.png)
        ![Pasted image 20250816191342.png](/Pastedimage20250816191342.png)
        
        لقد أضفتُ خلاصتين من مدونتي إلى القناة بكتابة الأمر التالي:
       <div dir="ltr"> 
        `@rss2tg_bot https://<رابط_خلاصة_RSS_الذي_نسخته_من_المصدر>`
       </div> 
        ولتعديل الإعدادات، اكتب الأمر:
        
        `/settings@rss2tg_bot`