# بَيَان — منصة القرائية العربية · Bayan — Arabic Literacy Platform

> حين تصبح القراءةُ فهمًا · Where reading becomes understanding
> من تطوير **مجموعة المتحدة للتعليم** · Developed by **Almotahida Education Group**

هذا الملف يوثّق موقع بَيَان التعريفي بالكامل: محتواه (عربي/إنجليزي)، بنيته، هويّته البصرية، وملاحظاته التقنية — لمشاركته مع الزملاء والشركاء وفرق التطوير والتصميم.

---

## ١. نظرة عامة

بَيَان منصةٌ تعليمية تركّز على **القرائية** لا على تعليم اللغة فحسب؛ هدفها بناء القارئ المفكّر القادر على الفهم والتحليل والنقد، عبر رحلةٍ متدرّجة على ستة مستويات من رياض الأطفال إلى الجامعة، ومحتوًى يصل المتعلّم بهويّته وحضارته ومعرفته ومرجعيّته.

الموقع الحالي **موقعٌ تعريفي (Marketing site)** صفحةٌ واحدة طويلة، ثنائي اللغة بالكامل (عربي RTL ↔ إنجليزي LTR) مع زرّ تبديلٍ عامل. ليس منصة التعلّم نفسها، بل واجهة التعريف بها وطلب العروض.

---

## ٢. محتويات المجلد

| الملف | الوصف |
|---|---|
| `index.html` | نسخة المشروع: ملف HTML خفيف (~٩١ كيلوبايت) يشير إلى الصور في مجلد `assets/`. الأنسب للتعديل والاستضافة. |
| `bayan-standalone.html` | نسخة الملف الواحد المدمج (~١.٢ ميجابايت): كل الصور مضمّنة داخله. تُفتح مباشرةً وتعمل دون إنترنت ودون مجلد الصور — الأنسب للمشاركة السريعة. |
| `assets/` | الشعار (`logo.png`) وعشر صور للموقع. |
| `build-standalone.py` | سكربت بايثون يعيد توليد `bayan-standalone.html` من `index.html` بتضمين الصور base64. شغّله بعد أيّ تعديل على `index.html`: `python build-standalone.py`. |
| `README.md` | هذا الملف. |

**كلا النسختين متطابقتان في المظهر والمحتوى تمامًا**، والفرق فقط في طريقة تضمين الصور.

> ⚠️ ملاحظة تحديث: أُضيفت إلى `index.html` أقسامٌ ومزايا جديدة (انظر القسم ٥ و٨). **يلزم إعادة توليد `bayan-standalone.html`** بتشغيل `build-standalone.py` حتى تتطابق النسختان.

---

## ٣. كيفية الفتح والاستخدام

- **للعرض السريع:** افتح `bayan-standalone.html` بأي متصفّح (نقرة مزدوجة). يعمل دون إنترنت.
- **للتعديل/الاستضافة:** استخدم `index.html` مع مجلد `assets/` بجواره؛ ارفع المجلد كاملًا إلى أي استضافة ويب.
- **زرّ اللغة:** في أعلى يمين الصفحة زرّ (`EN` / `ع`) يقلب الموقع كاملًا — اللغة، الاتجاه، الخطوط، الأرقام، وحقول النموذج. يفتح الموقع على العربية افتراضيًّا.
- **نموذج طلب العرض:** **توضيحيّ فقط** — لا يُرسل بيانات إلى أي خادم. عند الإطلاق الفعلي يلزم ربطه بخدمة بريد/قاعدة بيانات.
- **الخطوط:** تُحمَّل من Google Fonts عند الاتصال بالإنترنت؛ وبدونه يستعمل المتصفّح خطوطًا بديلة قريبة.

---

## ٤. الهوية البصرية

- **الألوان:** الأحمر `#EC2127` (لكنة وتمييز)، الأسود `#0E0B0A` (الأقسام الداكنة والتذييل)، وقاعدة عاجية/ورقية فاتحة هي الغالبة.
- **الخطوط:** Cairo (العناوين)، Tajawal (المتن)، Aref Ruqaa (اقتباس عرضي)، وInter للنصوص اللاتينية في الوضع الإنجليزي.
- **الشعار:** علامة خطّية حمراء لكلمة «بَيَان» على خلفية شفافة (`assets/logo.png`).
- **الأسلوب:** طباعةٌ ومساحاتٌ بيضاء وأيقوناتٌ خطّية، مع تصوير تحريري دافئ بدرجات العاج والفحم ولمسة حمراء مضبوطة.

> ملاحظة: الموجز الأصلي اقترح لوحة خضراء/ذهبية؛ اعتُمدت بدلًا منها لوحةُ الشعار (أحمر/أسود/عاجي) بناءً على توجيه العميل.

---

## ٥. خريطة الأقسام (صفحة واحدة)

الرأس الثابت ← البطل (`#top`) ← شريط الثقة ← المشكلة (`#problem`) ← القراءة مقابل القرائية (`#literacy`، داكن) ← كيف تعمل (`#how`) ← المنهجية (`#methodology`) ← المحتوى والمحاور (`#content`) ← المنصة والمزايا (`#platform`) ← الحلول (`#solutions`) ← **الأثر بالأرقام (`#impact`، عدّادات متحركة)** ← عن بَيَان (`#about`) ← الأسئلة الشائعة (`#faq`) ← ابدأ الآن/التواصل (`#contact`، داكن، مع تفاصيل تواصل وروابط تواصل اجتماعي) ← التذييل.

> 🆕 **أُضيف في هذا التحديث:**
> - قسم **الأثر بالأرقام** بعدّادات تتصاعد عند الظهور (تحترم `prefers-reduced-motion` وتتبدّل أرقامها بين العربية والإنجليزية).
> - **تفاصيل تواصل** (بريد/هاتف/عنوان) وروابط تواصل اجتماعي في قسم التواصل والتذييل — *القيم الحالية مؤقّتة؛ استبدِلها بالبريد والهاتف والعنوان وروابط الشبكات الحقيقية.*
> - **لمسات فنية راقية** مرسومة SVG بلا صور خارجية: زخارف هندسية إسلامية خفيفة (نجمة ثمانية) خلف البطل والأقسام الداكنة وقسم الأرقام، فواصل زخرفية بين الأقسام، ملمس ورقي خفيف، وحركات دقيقة (خطّ متحرّك تحت روابط القائمة، لمعان لطيف على البطاقات، حركة بارالاكس هادئة في البطل) — كلّها تحترم `prefers-reduced-motion`.
> - تحسينات تقنية: وسوم **OpenGraph/Twitter** و**JSON-LD** (منظمة/منتج/أسئلة)، **أيقونة موقع (favicon)**، **شريط تقدّم التمرير**، **زر العودة للأعلى**، **تظليل القسم النشط** في القائمة، **رابط تخطٍّ للمحتوى** وتحسينات تركيز للوصولية، و**حفظ اختيار اللغة** (localStorage) مع كشف لغة المتصفّح أول زيارة.

---

## ٦. المحتوى الكامل (عربي · English)

### البطل · Hero
- **عربي:** منصة القرائية العربية — *حين تصبح القراءةُ فهمًا.*
  منصة بَيَان للقرائية العربية — رحلةٌ متدرّجة عبر ستة مستويات، من رياض الأطفال إلى الجامعة، تبني القارئ المفكّر لا الناطق فحسب، بمحتوًى يصل المتعلّم بهويّته وعالمه.
  أزرار: «اطلب عرضًا تعريفيًّا» · «استكشف المنهجية». مؤشّرات: ٦ مستويات قرائية · ٤ محاور معرفية · ١٠ أقسام للدرس.
- **English:** Arabic Literacy Platform — *Where reading becomes understanding.*
  Bayan is an Arabic-literacy platform — a graded journey across six levels, from kindergarten to university, building readers who think rather than merely decode, through content that connects learners to their identity and world.
  Buttons: “Request a demo” · “Explore the methodology”. Stats: 6 reading levels · 4 knowledge axes · 10 lesson parts.

### شريط الثقة · Trust strip
| عربي | English |
|---|---|
| ٦ مستويات قرائية متدرّجة | Six graded levels |
| ٤ محاور معرفية متكاملة | Four knowledge axes |
| ٢ مساران: مؤلَّف وأصيل | Authored & authentic |
| ✓ عربية فصحى مراجَعة علميًّا | Academically reviewed |

### المشكلة · The gap
- **عربي:** يُتقن كثيرٌ من المتعلّمين فكّ الرموز ونطقها، لكنّهم يعجزون عن *فهم* ما يقرؤون أو تحليله أو الإفادة منه. هذه الفجوة — بين القراءة الآلية والفهم الحقيقي — لا تُضعف اللغة وحدها، بل تمتدّ إلى كلّ مادةٍ تُدرَّس بالعربية. ويضاعف من حدّتها ندرةُ المحتوى العربيّ المتدرّج المبنيّ على أسسٍ علمية.
- **English:** Many learners can decode and pronounce words, yet cannot *understand*, analyse or use what they read. This gap — between mechanical reading and genuine comprehension — weakens not only language but every subject taught in Arabic. It is widened by a scarcity of graded, research-based Arabic content.

### القراءة مقابل القرائية · Reading vs Literacy
- **القراءة / Reading:** مهارةٌ آلية — فكّ رموز الكلمات ونطقها سليمةً؛ شرطٌ لازمٌ غير كافٍ. · A mechanical skill — decoding and pronouncing words correctly; necessary but not sufficient.
- **القرائية / Literacy:** القدرة على فهم النصّ وتحليله ونقده وتوظيفه. · The ability to understand, analyse, critique and use a text.

| وجه المقارنة / Aspect | القراءة / Reading | القرائية / Literacy |
|---|---|---|
| الطبيعة / Nature | مهارة آلية / Mechanical skill | كفاية معرفية وعقلية / Cognitive competence |
| الهدف / Goal | نطق الكلمات / Pronouncing words | فهم وتحليل ونقد / Understand, analyse & critique |
| المخرَج / Output | قارئٌ ناطق / A reader who pronounces | قارئٌ مفكّرٌ ومنتِج / A thinking, producing reader |
| بالمعنى / Meaning | قد تنفصل عن المعنى / May detach from meaning | تقوم على المعنى والسياق / Built on meaning & context |
| في بَيَان / In Bayan | نقطة الانطلاق / The starting point | الغاية المقصودة / The intended goal |

> اقتباس: «القراءة شرطٌ لازم، والقرائية هي **الثمرة**. بَيَان لا تُعلّم الطفل أن يقرأ فحسب، بل أن يفهم ويحاور ويبني.»
> “Reading is necessary; literacy is the **fruit**. Bayan teaches a child not only to read, but to understand, question and build.”

### كيف تعمل · How it works
1. **اختر المسار والموضوع** — تختار المحور والموضوع والشخصية، فيُبنى الدرس حول اهتمام المتعلّم وهويّته. / **Choose the track and topic** — the lesson is built around the learner's interest and identity.
2. **يقدّم بَيَان النصّ** — بمستوى المتعلّم تمامًا، مع المفردات والإعراب والأساليب والتحليل البلاغي. / **Bayan presents the text** — at exactly the learner's level, with vocabulary, parsing, styles and rhetorical analysis.
3. **يُقاس الفهم ويُتابَع** — أنشطةٌ واختبارٌ بعديّ، ومتابعةٌ للنتائج عبر المستويات. / **Comprehension is measured & tracked** — activities and a post-test, with progress tracked across levels.

### المنهجية · Methodology
**ستة مستويات قرائية / Six reading levels:**

| المستوى/Level | المرحلة/Stage | النصّ السائد/Dominant text | الضبط بالشكل/Vocalisation |
|---|---|---|---|
| ١ / 1 | رياض الأطفال/مبكّر · Kindergarten/early | سردي · Narrative | كامل · Full |
| ٢ / 2 | ابتدائي مبكّر · Early primary | سردي · Narrative | كامل · Full |
| ٣ / 3 | ابتدائي · Primary | سردي · Narrative | كامل · Full |
| ٤ / 4 | إعدادي · Preparatory | تفسيري/معلوماتي · Expository/informational | إلزامي · Required |
| ٥ / 5 | ثانوي · Secondary | تفسيري · Expository | منطقة وسطى · Mid-range |
| ٦ / 6 | جامعي · University | حجاجي/نقدي · Argumentative/critical | مخفّف · Light |

> تبقى النصوص القرآنية مضبوطةً كما وردت في مصدرها دون أيّ تخفيفٍ للشكل في أيّ مستوى. · Qur'anic texts remain fully vocalised as in their source, with no reduction at any level.

**مساران للمحتوى / Two content tracks:**

| | المسار التوليدي / Generative track | المسار الأصيل / Authentic track |
|---|---|---|
| الطبيعة/Nature | محتوًى مؤلَّف تربويًّا · Pedagogically authored | نصوص مصدرية موثّقة · Documented source texts |
| التغطية/Coverage | الموضوع عبر المستويات الستة · One topic across all six levels | درسٌ بمستوًى واحد يختاره المتخصّص · A single-level lesson chosen by a specialist |
| الأمثلة/Examples | موضوعات علمية وإنسانية · Scientific & humanities topics | قرآن، حديث، شعر، نثر تراثي، حكايات · Qur'an, hadith, poetry, classical prose, tales |
| النصّ/Text | يُصاغ تربويًّا لكل مستوى · Composed for each level | يُصان كما ورد دون تعديل · Preserved as received |

**بناء الدرس في عشرة أقسام / The 10-part lesson:**
١ النصّ الأصلي · ٢ النصّ مضبوطًا بالشكل · ٣ أسئلة ما قبل القراءة · ٤ المفردات وأمثلتها · ٥ الإعراب · ٦ الأساليب اللغوية · ٧ التحليل البلاغي · ٨ عناصر بناء الموضوع · ٩ الاختبار البعدي · ١٠ الأنشطة التطبيقية.
(1 Source text · 2 Fully vocalised text · 3 Pre-reading questions · 4 Vocabulary & examples · 5 Parsing/iʿrāb · 6 Linguistic styles · 7 Rhetorical analysis · 8 Composition elements · 9 Post-test · 10 Applied activities.)

### المحتوى والمحاور · Content & Axes
يُعالَج كلُّ موضوعٍ من خلال أربعة محاورٍ متكاملة. · Every topic is treated through four integrated axes.

- **المحلي / Local:** يربط المتعلّم بهويّته القُطرية والعربية. · Connects the learner to national and Arab identity.
  وسوم: الحضارة والعادات، الأعياد، المعالم، الملابس، العملة، شخصيات، التاريخ والجغرافيا، الأطعمة والمهن، الفنون والآداب المحلية.
- **الحضاري / Historical:** نوافذُ على الحضارات الكبرى. · Windows onto the great civilisations.
  وسوم: العربي الإسلامي، الفرعوني، الروماني، اليوناني، الصيني، الهندي، العصر الحديث.
- **الموضوعي / Subject:** المعرفة المنظَّمة عبر العلوم والتقنية، والإنسانيات والاجتماعيات والفنون والآداب. · Organised knowledge across STEM and HASS.
  وسوم: STEM — علوم، رياضيات، تكنولوجيا، هندسة، HASS — إنسانيات، فنون، آداب.
- **الإسلامي / Islamic:** يصل المتعلّم بمرجعيّته الإسلامية عبر نصوصها الأصيلة وفق ضوابط دقيقة. · Connects the learner to the Islamic reference through authentic texts under precise controls.
  وسوم: القرآن الكريم، الحديث النبوي، الفقه الإسلامي، السيرة النبوية.

**طبقة الشخصيات / Personalities layer:** تتقاطع مع المحاور طبقةٌ من الشخصيات المصنّفة تقرن كلّ موضوعٍ بشخصيةٍ ذات صلة، فيغدو التعلّم أقرب إلى القصة منه إلى التلقين. · A cross-cutting layer of classified figures pairs each topic with a relevant figure, making learning closer to a story than to rote.

### المنصة والمزايا · Platform & Features
بيئةٌ رقمية متكاملة تخدم كل دورٍ بما يناسبه. · An integrated digital environment serving every role.

| الدور / Role | الوظيفة / Function |
|---|---|
| الطالب / Student | يقرأ ويتفاعل، يؤدّي الأنشطة والاختبارات، ويتابع تقدّمه. · Reads, engages, completes activities/tests, tracks progress. |
| المعلّم / Teacher | يختار النصوص ويكلّف، يصحّح ويترك ملاحظات، ويطّلع على لوحة صفّه. · Assigns texts, grades & gives feedback, views a class dashboard. |
| إدارة المدرسة / School admin | تتابع الصفوف والمعلمين وتدير الحسابات والاشتراكات. · Tracks classes & teachers, manages accounts & subscriptions. |
| الوزارة/الجهة · Ministry/authority | لوحاتٌ تجميعية عبر المدارس ومعايير موحّدة على نطاقٍ واسع. · Aggregate dashboards across schools with unified standards at scale. |

المزايا / Features: لوحات التتبّع والتقارير (قابلة للتصدير) · التكامل مع أنظمة إدارة التعلّم (LMS) والدخول الموحّد (SSO) · استجابةٌ كاملة وإتاحة (Accessibility) عبر قارئ الشاشة ولوحة المفاتيح.
(Dashboards & exportable reporting · LMS integration & SSO · Fully responsive & accessible via screen readers and keyboard.)

### الحلول · Solutions (رسالةٌ مخصّصة لكل جهة / A tailored message for every audience)

- **للمدارس الخاصة / For Private Schools** — الحاجة: ما يميّز المدرسة ويرفع نتائجها، وضعف القرائية يقلق أولياء الأمور. الاستجابة: منهجٌ قرائيٌّ جاهز يُدمَج مع منهجك ويحوّل القرائية إلى ميزةٍ تسويقية.
  *Need:* distinction + stronger outcomes; weak literacy worries parents. *Response:* a ready, graded curriculum that integrates with your programme and turns literacy into a competitive advantage.
- **لوزارات التعليم / For Ministries** — الحاجة: تحدٍّ على مستوى النظام يصعب علاجه بحلولٍ متفرّقة. الاستجابة: حلٌّ منهجيٌّ قابل للتوسّع يُواءَم مع المراحل الوطنية ويدعم السياسات بمعايير موحّدة.
  *Need:* a system-wide challenge. *Response:* a scalable, methodical solution alignable to national stages with unified standards.
- **للمعلمين / For Teachers** — الحاجة: وقتٌ طويل في الإعداد والضبط والتصحيح. الاستجابة: محتوًى جاهز، بناءٌ واضح للدرس، تصحيحٌ تلقائي، وأدوات تكليفٍ ومتابعة.
  *Need:* hours lost to prep, levelling, grading. *Response:* ready content, clear lesson structure, auto-graded tests, assignment & tracking tools.
- **للطلبة / For Students** — الحاجة: نصٌّ أعلى أو أدنى من المستوى، وانفصالٌ عن القراءة. الاستجابة: رحلةٌ بمستواك تمامًا، ومحتوًى يربطك بهويّتك، وكل موضوعٍ بشخصيةٍ مُلهمة.
  *Need:* texts mismatched to level, disengagement. *Response:* a journey at exactly your level, content tied to your identity, every topic paired with an inspiring figure.

### عن بَيَان · About
وُلدت بَيَان من ملاحظةٍ بسيطة: أنّ تعليم الطفل أن *يقرأ* شيءٌ، وأن نعلّمه أن *يفهم* شيءٌ آخر. القراءة وسيلة، والقرائية غاية.
*Bayan was born of a simple observation: teaching a child to read is one thing; teaching them to understand is another. Reading is the means, literacy the end.*

**المبادئ الثلاثة / Three principles:**
- صون النصّ الأصيل (خاصةً المقدّس والتراثي) دون تعديل. · Preserving the authentic text without alteration.
- التدرّج مع نموّ المتعلّم نصًّا ومفرداتٍ وأسلوبًا. · Progression with the learner's growth in text, vocabulary and style.
- ربط القرائية بالمعنى والهوية. · Linking literacy to meaning and identity.

**الجهة المطوّرة والمراجعة العلمية / Developer & academic review:** تطوّر المنصة **مجموعة المتحدة للتعليم** اعتمادًا على فريقٍ تربويٍّ ولغويّ، ويخضع كلُّ محتوًى قبل نشره لمراجعةٍ علمية متخصّصة. · Developed by **Almotahida Education Group** with an educational & linguistic team; every piece of content undergoes specialised academic review before publication.

### الأسئلة الشائعة · FAQ
1. **ما الفرق بين بَيَان وغيرها؟** تركّز على القرائية لا تعليم اللغة فحسب. · *How is Bayan different?* It focuses on literacy, not language teaching alone.
2. **لمن صُمّمت؟** للمدارس الخاصة والوزارات والمعلمين والطلبة من الروضة إلى الجامعة. · *Who is it for?* Private schools, ministries, teachers and students, KG to university.
3. **كيف تُضمَن دقّة المحتوى؟** مراجعةٌ علمية قبل النشر، وصونُ النصوص المقدّسة والتراثية. · *How is accuracy ensured?* Academic review before publication; sacred/classical texts preserved.
4. **هل يحلّ محلّ منهج المدرسة؟** لا؛ يتكامل ويواءم لا يزاحم. · *Does it replace the curriculum?* No; it integrates and aligns rather than competes.
5. **بأيّ لغة المحتوى؟** المحتوى التعليمي بالعربية الفصحى، وواجهة الموقع التعريفي ثنائية اللغة. · *What language?* Content in standard Arabic; the marketing site is bilingual.
6. **كيف نبدأ؟** بطلب عرضٍ تعريفيّ من نموذج التواصل. · *How do we start?* Request a demo from the contact form.

### ابدأ الآن · Get started
- **عربي:** ابدأ ببناء جيلٍ *يقرأ ليفهم*. اطلب عرضًا تعريفيًّا، وسيتواصل فريق بَيَان لتحديد احتياج جهتك.
- **English:** Start building a generation that *reads to understand*. Request a demo and the Bayan team will reach out to identify your needs.
- حقول النموذج / Form fields: الاسم · الجهة · نوع الجهة (مدرسة خاصة / وزارة / معلّم / طالب أو وليّ أمر / أخرى) · البريد الإلكتروني. *(Name · Organisation · Type · Email)* — نموذج توضيحي لا يُرسل بيانات. *(Demo form — sends nothing.)*

### التذييل · Footer
روابط سريعة، روابط للجهات، تواصل، وحقوق: © ٢٠٢٦ مجموعة المتحدة للتعليم — جميع الحقوق محفوظة. روابط سياسة الخصوصية/الشروط حاليًّا عناصر نائبة (placeholders).
*Quick links, audience links, contact, and: © 2026 Almotahida Education Group — All rights reserved. Privacy/Terms links are placeholders.*

---

## ٧. قائمة الصور (`assets/`)

| الملف | القسم | الوصف (النص البديل) |
|---|---|---|
| `logo.png` | الرأس/التذييل/علامات مائية | شعار بَيَان (علامة حمراء، خلفية شفافة) |
| `hero.jpg` | البطل | طفلٌ منهمكٌ في قراءة كتاب |
| `axis-local.jpg` | المحور المحلي | نافذة مشربية وبوابة مقوّسة |
| `axis-civilizations.jpg` | المحور الحضاري | عمود يوناني ونقش مصري وأسطرلاب وخريطة |
| `axis-subject.jpg` | المحور الموضوعي | فرجار ونموذج جزيئي وكتاب وقلم |
| `axis-islamic.jpg` | المحور الإسلامي | مصحفٌ على حاملٍ خشبي بجوار زخارف |
| `about-calligraphy.jpg` | عن بَيَان | يدٌ تكتب خطًّا عربيًّا بالقلم |
| `sol-schools.jpg` | الحلول — المدارس | فصلٌ دراسيٌّ مشمس |
| `sol-ministries.jpg` | الحلول — الوزارات | واجهةٌ حجرية بأعمدة |
| `sol-teachers.jpg` | الحلول — المعلمون | معلّمٌ يرشد طالبًا |
| `sol-students.jpg` | الحلول — الطلبة | طالبٌ يقرأ مبتسمًا |

جميع الصور عولجت بتدرّجٍ لوني موحّد وضُغطت للويب، ولكلٍّ منها نصٌّ بديل عربي وتحميلٌ كسول (عدا البطل يُحمّل فورًا).

---

## ٨. ملاحظات تقنية

- **ثنائية اللغة:** كل نصٍّ له نسختان (`.t-ar` / `.t-en`) تُظهر إحداهما عبر CSS حسب `lang` على عنصر `<html>`؛ والزرّ يقلب `lang` و`dir` والأرقام والخطوط وحقول النموذج وعنوان الصفحة. لا يحتاج خادمًا.
- **مستقلٌّ ذاتيًّا:** نسخة `bayan-standalone.html` تضمّن كل الصور (base64) فتعمل دون إنترنت ودون ملفات خارجية.
- **الاستجابة:** تخطيطٌ متجاوب لشاشات الحاسوب واللوح والجوال، مع قائمةٍ منسدلة للجوال.
- **الحركة والإتاحة:** ظهورٌ تدريجي عند التمرير يحترم `prefers-reduced-motion`، ونصوصٌ بديلة، وعناصر `details` أصيلة للأسئلة.
- **لا واجهة خلفية:** نموذج طلب العرض توضيحيّ؛ يلزم ربطه عند الإطلاق. روابط الخصوصية/الشروط نائبة.
- **اعتماد خارجي وحيد:** خطوط Google Fonts (تُحمّل عند الاتصال؛ وإلا تُستخدم بدائل).

---

## ٩. الحقوق

© ٢٠٢٦ **مجموعة المتحدة للتعليم** — جميع الحقوق محفوظة.
الصور المستخدمة في الموقع مُولّدة/مجهّزة لأغراض العرض؛ يُرجى التحقّق من حقوق الاستخدام قبل النشر التجاري.
