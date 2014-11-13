# Goldwave #

* المطورون: Joseph Lee ومساهمون آخرون في NVDA
* Download [stable version][1]
* Download [development version][2]

هذه الوحدات البرمجية تعمل على تحسين استخدام برنامج محرر الصوت GoldWave

## مفاتيح الاختصار ##

* Control+Shift+P: للإعلان عن موضع المسار أو التراك الحالي.
* Control+NvDA+3: لإعطاء ملخص معلومات عن الجزء الصوتي الذي تم تحديده.
* Control+NVDA+2: الإعلان عن الطول الإجمالي للملف الصوتي.
* Control+NVDA+1: الإعلان عن القناة التي يتم تعديلها
* NVDA+shift+c: تعطيل أو تشغيل نطق الأوامر أثناء تحرير الصوت
* Control+NVDA+4: للإعلان عن مستوى الزوم.

للمزيد من المعلومات حول برنامج GoldWave وأوامره يرجى مراجعة دليل استخدامه.

Note: GoldWave 6 requires 64-bit version of Windows 7 or later. NVDA 2014.1
or later is required to use add-on 2.0.

## Changes for 2.0

* Support for GoldWave 6, including 64-bit version of GoldWave (see note
  above).
* Add-on help can now be accessed from add-ons manager (NVDA 2014.3 and
  later).
* NVDA now announces selected channel if you press channel selection
  commands such as Control+Shift+L for the left channel.
* Various issues with numeric edit fields such as censor field and time
  selector in mix dialog has been fixed, including selecting text, updating
  values and so on.
* Command announcement setting will be remembered when switching to other
  programs.

## مستجدات الإصدار 1.2

* إصلاح خطأ برمجي حيث كان يواجه NVDA صعوبة في الإعلان عن بعض مربعات التحرير.
* ترجمة الإضافة للغات جديدة وتحديث اللغات الأخرى
* يرجى الملاحظة أنه نظرا للتعديلات التي تمت في الإصدارات الأخيرة من NVDA,
  فإن بعض أوامر الحالة كأمر الإعلان عن الجزء الصوتي المحدد لم تعمل كما ينبغي
  في بعض الأنظمة.

## تعديلات الإصدار 1.1 ##

* دعم ظهور الرسائل على الأسطر الإلكترونية
* عرض الأجزاء الصوتية المحددة باللغات الأخرى غير الإنجليزية
* الإعلان عن مزيد من الأوامر بما في ذلك: موضع حركة الإشارة وعمليات
  التزيين/والحذف
* Fixed an issue in numeric edit fields such as various effects dialogs
  where nothing or wrong field name was announced.
* ترجمة الإضافة للغات جديدة وتحديث اللغات الأخرى

## تعديلات الإصدار 1.0 ##

* إصدار أولي

[[!tag devstable]]

[1]: http://addons.nvda-project.org/files/get.php?file=gwv

[2]: http://addons.nvda-project.org/files/get.php?file=gwv
