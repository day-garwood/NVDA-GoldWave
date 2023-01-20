# GoldWave #

* المطورون: Joseph Lee ومساهمون آخرون في NVDA
* تحميل [الإصدار النهائي][1][1]
* NVDA compatibility: 2022.4 and later

This app module enhances access and usage of GoldWave audio editor.

## مفاتيح الاختصار ##

* NVDA+Shift+C: Toggles speaking of commands during audio editing.
* Control+Shift+P: للإعلان عن موضع المسار أو التراك الحالي.
* NVDA+Shift+R: الإعلان عن الوقت المتبقي من المسار الجاري تحريره.
* Control+NVDA+1: الإعلان عن القناة التي يتم تعديلها
* Control+NVDA+2: الإعلان عن الطول الإجمالي للملف الصوتي.
* Control+NVDA+3: announces a summary on audio selection information.
* Control+NVDA+4: للإعلان عن مستوى الزوم.

For more information about GoldWave and keyboard commands, refer to GoldWave
Manual.

Note: GoldWave 6 or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.
* In GoldWave 6.57 and later, NVDA will no longer repeat the name of the
  loaded file when pressing play/rewind/stop keys.

## Version 21.06

* Resolved additional coding style issues and potential bugs with Flake8.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Added input help messages for remainig time command (NVDA+Shift+R).
* Toggle command announcement command (NVDA+Shift+C) will now show up under
  "GoldWave" category in NVDA's input gestures dialog.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 19.11

* Windows 7 SP1, GoldWave 6.x, and NVDA 2019.1 or later is required.
* Added help message for sound window (accessible if Control Usage Assistant
  add-on is installed).

## Version 18.12

* NVDA will no longer appear to do nothing or play error tones when
  performing certain GoldWave commands with command announcement set to off
  (this may result in odd behaviors in some cases).
* Internal changes to support future NVDA releases.

## Version 18.07

* Fixed an issue where leading zeroes would not be displayed when trying to
  obtain remaining time for a trakc.

## Version 17.05

* Added ability to provide debug information when NVDA is running with debug
  logging enabled (NVDA 2017.1 or later).
* Updated translations.

## Version 16.12

* Version scheme is now year.month instead of major.minor.

## Changes for 4.0

* Add-on repository has moved to GitHub (now located at
  https://github.com/josephsl/goldwave).
* Performance improvements when looking up information such as channel name
  and other status information.

## مستجدات الإصدار 3.0

* Added a command to announce remaining time for the current track
  (NVDA+Shift+R).
* تحسينات طفيفة عند الإعلان عن معلومات الحالة كالإعلان عن معلومات القناة.

## مستجدات الإصدار 2.0

* دعم gold wave 6 ويشمل ذلك الإصدار 64 من goldwave (انظر الملحوظة أعلاه).
* يمكن الوصول لملف المساعدة الخاص بالإضافة من مدير الإضافات البرمجية.
* سيعلن NVDA الآن عن السماعة المختارة إذا قمت بالضغط على أي من اختصارات
  اختيار السماعات كالضغط على Control+Shift+L لاختيار السماعة اليسرى.
* معالجة العديد من الأخطاء بالحقول الرقمية كما في حقل المراقبة وحقل اختيار
  الوقت بمحاورة المزج, ويشمل ذلك تحديد النص وتحديث القيم وهكذا.
* تذكر إعداد الإعلان عن الأمر عند الانتقال للبرامج الأخرى.

## مستجدات الإصدار 1.2

* إصلاح خطأ برمجي حيث كان يواجه NVDA صعوبة في الإعلان عن بعض مربعات التحرير.
* ترجمة الإضافة للغات جديدة وتحديث اللغات الأخرى
* يرجى الملاحظة أنه نظرا للتعديلات التي تمت في الإصدارات الأخيرة من NVDA,
  فإن بعض أوامر الحالة كأمر الإعلان عن الجزء الصوتي المحدد لم تعمل كما ينبغي
  في بعض الأنظمة.

## تعديلات الإصدار 1.1

* دعم ظهور الرسائل على الأسطر الإلكترونية
* عرض الأجزاء الصوتية المحددة باللغات الأخرى غير الإنجليزية
* الإعلان عن مزيد من الأوامر بما في ذلك: موضع حركة الإشارة وعمليات
  التزيين/والحذف
* معالجة مشكلة مربعات التحرير الرقمية كتلك الموجودة في العديد من محاورات
  المؤثرات التي كان NVDA لا يعلن فيها عن شيء أو يقرأ أسماء الحقول بطريقة
  خاطئة.
* ترجمة الإضافة للغات جديدة وتحديث اللغات الأخرى

## تعديلات الإصدار 1.0

* إصدار أولي

[[!tag devstable]]

[1]: https://addons.nvda-project.org/files/get.php?file=gwv
