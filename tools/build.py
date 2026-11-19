"""Generate the Blossom static site. Run: python3 -I build.py <output_dir>
Shared header/footer live here so every page stays consistent."""
import sys, os

OUT = sys.argv[1]
EMAIL = "hello@blossomtherapy.au"
FB = "https://www.facebook.com/profile.php?id=61581113236421"
IG = "https://www.instagram.com/blossomtherapyandsupports/"
SITE = "https://blossomtherapyandsupport.com.au"

NAV = [
    ("/", "Home"),
    ("/about-us/", "About us"),
    ("/our-services/", "Our services"),
    ("/pricing-and-funding/", "Pricing and funding"),
    ("/referrals/", "Referrals"),
    ("/resources/", "Resources"),
    ("/contact-us/", "Contact us"),
]

def mailto(subject):
    return f"mailto:{EMAIL}?subject={subject.replace(' ', '%20')}"

def page(path, title, desc, body):
    nav_items = "\n".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a></li>'
        for href, label in NAV
    )
    html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0F6E56">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<!-- TODO: add og:image once photos are supplied (e.g. /assets/img/og.jpg) -->
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/styles.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <!-- TODO: swap text brand for logo image when supplied -->
    <a class="brand" href="/">Blossom<span>Therapy and Supports</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="main-nav" id="main-nav" aria-label="Main">
      <ul>
{nav_items}
        <li><a class="btn small" href="/#get-started">Get started</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h2>Blossom Therapy and Supports</h2>
        <p>Exercise physiology, physiotherapy and disability support. Home visits across the northern Gold Coast, plus telehealth.</p>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Gold Coast QLD, Australia</li>
          <li><a href="{FB}" rel="noopener">Facebook</a> &middot; <a href="{IG}" rel="noopener">Instagram</a></li>
        </ul>
      </div>
      <div>
        <h2>More</h2>
        <ul>
          <li><a href="/#get-started">Get started</a></li>
          <li><a href="/referrals/">GP and referrer form</a></li>
          <li><a href="/privacy/">Privacy policy</a></li>
          <li><a href="/accessibility/">Accessibility</a></li>
        </ul>
      </div>
    </div>
    <p class="copyright">&copy; 2026 Blossom Therapy and Supports. All rights reserved.</p>
  </div>
</footer>
</body>
</html>
"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)

def hero(h1, p):
    return f'<section class="page-hero"><div class="wrap"><h1>{h1}</h1><p>{p}</p></div></section>'

# ---------- Get started picker (Halaxy embed slots) ----------
def slot(form_name, intro, items, subject):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="halaxy-slot" data-halaxy-form="{form_name}">
  <!-- HALAXY EMBED: paste the "{form_name}" embed code here (Halaxy > Settings > General > Forms > ⋮ > Share settings > Embedded Form > Copy).
       Then delete the fallback content below. -->
  <p class="tag">Form coming soon</p>
  <p>{intro}</p>
  <ul>{lis}</ul>
  <a class="btn" href="{mailto(subject)}">Email us</a>
</div>"""

PICKER = f"""<section class="sec tint" id="get-started" aria-labelledby="gs-h">
  <div class="wrap">
    <span id="start-client"></span><span id="start-carer"></span><span id="start-referrer"></span>
    <h2 id="gs-h">Get started</h2>
    <p class="lead">Choose the option that fits you. We'll contact you within 1 business day.</p>
    <!-- CONFIRM: response time with Emma -->
    <div class="picker" role="tablist" aria-label="Who are you?">
      <button role="tab" id="tab-client" aria-controls="panel-client" aria-selected="true">I'm a client</button>
      <button role="tab" id="tab-carer" aria-controls="panel-carer" aria-selected="false" tabindex="-1">I'm a parent or carer</button>
      <button role="tab" id="tab-referrer" aria-controls="panel-referrer" aria-selected="false" tabindex="-1">I'm a GP or referrer</button>
    </div>
    <div class="panel" role="tabpanel" id="panel-client" aria-labelledby="tab-client">
      <h3>Tell us about you</h3>
      <p>One short form. You can fill it in on your phone.</p>
      {slot("Client intake", "Until our online form is ready, email us with:", ["Your name and phone number", "The service you're interested in", "Home visit or telehealth, and your suburb", "Funding (NDIS, private or other)", "Days and times that suit you"], "New client enquiry")}
    </div>
    <div class="panel" role="tabpanel" id="panel-carer" aria-labelledby="tab-carer" hidden>
      <h3>Tell us about the person you support</h3>
      <p>Your details, their details, and what support would help.</p>
      {slot("Carer intake", "Until our online form is ready, email us with:", ["Your name, phone number and relationship to the client", "The client's name and age", "The service you're interested in", "Home visit or telehealth, and suburb", "Funding (NDIS, private or other)", "Days and times that suit"], "Parent or carer enquiry")}
    </div>
    <div class="panel" role="tabpanel" id="panel-referrer" aria-labelledby="tab-referrer" hidden>
      <h3>Refer a client</h3>
      <p>Send us the referral and we'll contact your client directly.</p>
      {slot("Referrer form", "Until our online form is ready, email the referral to us with:", ["Client name, date of birth and phone number", "Reason for referral and relevant history", "Funding type (NDIS, Medicare CDM, private)", "Your name, practice and contact details"], "New referral")}
    </div>
  </div>
</section>"""

# ---------- Home ----------
home = f"""
<section class="hero">
  <div class="wrap">
    <h1>Shifting perspectives with movement, strength and meaningful support</h1>
    <p>Exercise physiology, physiotherapy and disability support. Home visits across the northern Gold Coast, plus telehealth.</p>
    <div class="btn-row">
      <a class="btn peach" href="#get-started">Get started</a>
      <a class="btn ghost" href="/#start-referrer">I'm a GP or referrer</a>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="what-h">
  <div class="wrap two-col">
    <div>
      <h2 id="what-h">What we do</h2>
      <p>We're a small team of exercise physiologists, a physiotherapist and disability support workers. We work with neurodivergent people, young women, and people living with invisible or fluctuating health conditions.</p>
      <p>Our approach is paced, collaborative and safety-focused. Support is built around you, not a generic program.</p>
      <a class="btn outline" href="/our-services/">Our services</a>
    </div>
    <div class="ph-box">Photo coming soon<!-- TODO: hero/feature photo --></div>
  </div>
</section>

<section class="sec tint" aria-labelledby="how-h">
  <div class="wrap">
    <h2 id="how-h">How it works</h2>
    <div class="grid">
      <div class="card"><span class="step-num">1</span><h3>Tell us who you are</h3><p>Pick the option that fits. It takes a few seconds.</p></div>
      <div class="card"><span class="step-num">2</span><h3>Fill in one short form</h3><p>Your details, funding and the times that suit you.</p></div>
      <div class="card"><span class="step-num">3</span><h3>We match and book</h3><p>We'll pair you with the right clinician and confirm a time with you.</p></div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="who-h">
  <div class="wrap">
    <h2 id="who-h">Who we support</h2>
    <div class="grid">
      <div class="card"><h3>Neurodiversity</h3><p>Neuro-affirming, paced support for autistic and ADHD people, focused on confidence and safety.</p></div>
      <div class="card"><h3>Women's health</h3><p>Support for endometriosis, pelvic pain and hormonal conditions, focused on movement and daily function.</p></div>
      <div class="card"><h3>Invisible illness</h3><p>Chronic pain, fatigue, POTS, MCAS, EDS and similar conditions, with pacing that adapts on the day.</p></div>
      <div class="card"><h3>Youth and teens</h3><p>Gentle, relationship-led support for young people who feel overwhelmed or misunderstood by traditional models.</p></div>
    </div>
  </div>
</section>

{PICKER}

<section class="sec" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h">Our services</h2>
    <div class="grid">
      <div class="card"><h3>Exercise physiology</h3><p>Home visits and telehealth, including women's health.</p></div>
      <div class="card"><h3>Physiotherapy</h3><p>Injury and pain care at home or online.</p></div>
      <div class="card peach"><h3>Disability support work</h3><p>Self-care, decision making and daily planning.</p></div>
      <div class="card peach"><h3>Girls' social groups</h3><p>Wattle Crew (school age) and Banksia Crew (post-school).</p></div>
    </div>
    <p style="margin-top:20px"><a class="btn outline" href="/our-services/">More about our services</a></p>
  </div>
</section>

<section class="sec tint" aria-labelledby="price-h">
  <div class="wrap">
    <h2 id="price-h">Prices at a glance</h2>
    <div class="grid">
      <div class="card"><h3>Home visits</h3><p>$175 per hour, private exercise physiology and physiotherapy.</p></div>
      <div class="card"><h3>Telehealth</h3><p>From $110 per session.</p></div>
      <div class="card"><h3>NDIS</h3><p>Charged in line with the NDIS Pricing Schedule.</p></div>
    </div>
    <p style="margin-top:20px"><a class="btn outline" href="/pricing-and-funding/">Full pricing and funding</a></p>
  </div>
</section>

<section class="sec" aria-labelledby="vision-h">
  <div class="wrap two-col">
    <div>
      <h2 id="vision-h">Our vision</h2>
      <p>Care that respects individuality, builds trust and supports growth without pressure or harm.</p>
      <a class="btn outline" href="/about-us/">About us</a>
    </div>
    <div>
      <h2>Free resources</h2>
      <p>Practitioner-developed resources from our training and clinical work, to support understanding, self-advocacy and gentle learning.</p>
      <a class="btn outline" href="/resources/">Browse resources</a>
    </div>
  </div>
</section>
<!-- TODO: "Some of our favourite moments" photo gallery, once photos are supplied -->
"""
page("/", "Blossom Therapy & Supports | Gold Coast and Telehealth",
     "Exercise physiology, physiotherapy and disability support on the northern Gold Coast and via telehealth. Neuro-affirming, paced and collaborative care.",
     home)

# ---------- About ----------
about = hero("About us", "A small team doing paced, collaborative, neuro-affirming care.") + """
<section class="sec">
  <div class="wrap two-col">
    <div class="prose">
      <!-- CONFIRM: the live About page couldn't be read during the build. Replace or extend this text with the current wording. -->
      <h2 style="margin-top:0">Our vision</h2>
      <p>A future where no one is made to feel broken for having a body or mind that works differently. Our care aims to honour individuality, build trust and support growth without pressure or harm.</p>
      <h2>How we work</h2>
      <ul class="tick">
        <li>Paced: we go at a speed that feels safe for you</li>
        <li>Collaborative: you, your family and your other supports are part of the plan</li>
        <li>Adaptive: sessions change on the day if your body or energy does</li>
        <li>In your space: home visits, or telehealth from wherever suits</li>
      </ul>
    </div>
    <div class="ph-box">Team photo coming soon</div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>Our team</h2>
    <p class="lead">Exercise physiologists, a physiotherapist and disability support workers.</p>
    <!-- TODO: one card per team member: photo, name, role, short bio, special interests -->
    <div class="grid">
      <div class="card"><div class="ph-box" style="min-height:140px;margin-bottom:12px">Photo</div><h3>Name</h3><p>Exercise physiologist</p></div>
      <div class="card"><div class="ph-box" style="min-height:140px;margin-bottom:12px">Photo</div><h3>Name</h3><p>Exercise physiologist</p></div>
      <div class="card"><div class="ph-box" style="min-height:140px;margin-bottom:12px">Photo</div><h3>Name</h3><p>Exercise physiologist (telehealth)</p></div>
      <div class="card"><div class="ph-box" style="min-height:140px;margin-bottom:12px">Photo</div><h3>Caite Brown</h3><p>Physiotherapist</p></div>
      <div class="card"><div class="ph-box" style="min-height:140px;margin-bottom:12px">Photo</div><h3>Name</h3><p>Disability support worker</p></div>
    </div>
  </div>
</section>
"""
page("/about-us/", "About us | Blossom Therapy & Supports",
     "Meet the Blossom team: exercise physiologists, a physiotherapist and disability support workers on the Gold Coast.", about)

# ---------- Services ----------
services = hero("Our services", "Home visits across the northern Gold Coast, and telehealth Australia-wide.") + f"""
<section class="sec">
  <div class="wrap">
    <div class="grid">
      <div class="card">
        <h3>Exercise physiology</h3>
        <p>Movement and strength programs built around your body, energy and goals. Includes women's health exercise physiology.</p>
        <p class="fine">Home visits and telehealth</p>
      </div>
      <div class="card">
        <h3>Physiotherapy</h3>
        <p>Assessment and treatment for injury, pain and movement problems, with the same paced, neuro-affirming approach.</p>
        <p class="fine">Home visits and telehealth</p>
      </div>
      <div class="card peach">
        <h3>Disability support work</h3>
        <p>Practical support with self-care, decision making and daily planning.</p>
        <p class="fine">NDIS. 3-hour minimum.</p>
      </div>
    </div>
  </div>
</section>
<section class="sec tint" id="groups">
  <div class="wrap">
    <h2>Girls' social groups</h2>
    <p class="lead">Small, supportive groups. Maximum 6 per group.</p>
    <div class="grid">
      <div class="card"><h3>Wattle Crew</h3><p>For school-aged girls. Fortnightly, Saturday afternoons.</p></div>
      <div class="card"><h3>Banksia Crew</h3><p>For girls who have left school or are homeschooled. Weekly, Thursday afternoons (occasionally Friday).</p></div>
    </div>
    <!-- TODO: Term calendars, session costs, duration and transport details (currently images on the old site) -->
    <div class="halaxy-slot" data-halaxy-form="Group waitlist">
      <!-- HALAXY EMBED: paste the "Group waitlist" form embed code here, then delete the fallback below. -->
      <p class="tag">Join the waitlist</p>
      <p>Email us with the participant's name and age, which group, and a contact number. We'll let you know when a spot opens.</p>
      <a class="btn" href="{mailto('Social group waitlist')}">Join the waitlist</a>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap two-col">
    <div>
      <h2>Where we visit</h2>
      <p>Home visits are based around Upper Coomera and Pimpama, and range out to Paradise Point. A travel fee applies for longer trips.</p>
      <!-- CONFIRM: full suburb list / travel zones -->
    </div>
    <div>
      <h2>Ready to start?</h2>
      <p>Tell us a little about you and we'll be in touch.</p>
      <a class="btn" href="/#get-started">Get started</a>
    </div>
  </div>
</section>
"""
page("/our-services/", "Our services | Blossom Therapy & Supports",
     "Exercise physiology, physiotherapy, NDIS disability support and girls' social groups on the northern Gold Coast and via telehealth.", services)

# ---------- Pricing ----------
def rows(items):
    return "".join(f'<div class="price-row"><span>{a}</span><strong>{b}</strong></div>' for a, b in items)

pricing = hero("Pricing and funding", "Clear prices, no surprises.") + f"""
<section class="sec">
  <div class="wrap">
    <h2>Private clients</h2>
    <p class="lead">Exercise physiology and physiotherapy are charged at the same rates.</p>
    <div class="grid">
      <div class="price-card">
        <h3>Home visits</h3>
        <p class="note">$175 per hour</p>
        {rows([("Initial assessment, 60 min", "$175"), ("Standard session, 45 min", "$131.25"), ("Extended session, 60 min", "$175")])}
        <p class="fine">Travel fee: $45 when travel is more than 30 minutes.</p>
        <!-- CONFIRM: 45-min rate is pro-rata of $175/hr. Travel fee trigger (each way? from the clinician's base?). -->
      </div>
      <div class="price-card">
        <h3>Telehealth</h3>
        <p class="note">Video sessions from home</p>
        {rows([("Initial assessment, 60 min", "$130"), ("Standard session, 30 min", "$110"), ("Extended session, 45 min", "$120")])}
        <!-- CONFIRM: telehealth durations; same rates for physio telehealth? -->
      </div>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>NDIS participants</h2>
    <p class="lead">We charge in line with the NDIS Pricing Schedule 2026–27.</p>
    <!-- CONFIRM: management types accepted (self, plan, agency) -->
    <div class="grid">
      <div class="price-card">
        <h3>Exercise physiology</h3>
        <p class="note">$161.99 per hour</p>
        {rows([("Initial assessment and report, 90 min", "$242.99"), ("Standard session, 60 min", "$161.99"), ("Short session, 30 min", "$81.00"), ("Review report", "$161.99–$323.98")])}
      </div>
      <div class="price-card">
        <h3>Physiotherapy</h3>
        <p class="note">Up to the NDIS price limit</p>
        {rows([("Hourly rate", "$183.99")])}
        <!-- CONFIRM: NDIS physio rate and session lengths -->
      </div>
      <div class="price-card">
        <h3>Support work</h3>
        <p class="note">3-hour minimum</p>
        {rows([("Per hour", "$73.58"), ("Travel", "$1 per km")])}
      </div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap prose">
    <h2 style="margin-top:0">Good to know</h2>
    <ul class="tick">
      <li>Not sure what your funding covers? <a href="/#get-started">Get in touch</a> and we'll talk it through.</li>
      <li>Social group costs are shared with families when you join the waitlist.</li>
    </ul>
    <!-- TODO: cancellation policy, payment methods, Medicare CDM (only if offered) -->
  </div>
</section>
"""
page("/pricing-and-funding/", "Pricing and funding | Blossom Therapy & Supports",
     "Prices for home visit and telehealth exercise physiology and physiotherapy, NDIS rates and support work.", pricing)

# ---------- Referrals ----------
referrals = hero("Referrals", "For GPs, specialists, support coordinators and other referrers.") + f"""
<section class="sec">
  <div class="wrap two-col">
    <div>
      <h2>Refer a client</h2>
      <p>Send us the referral and we'll contact your client directly, usually within 1 business day.</p>
      <div class="halaxy-slot" data-halaxy-form="Referrer form">
        <!-- HALAXY EMBED: paste the professional-contact (referrer) form embed code here, then delete the fallback below. -->
        <p class="tag">Online referral coming soon</p>
        <p>For now, download the referral form and email it to us, or email a referral letter.</p>
        <div class="btn-row">
          <a class="btn" href="https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/Client%20referral%20form.pdf">Download referral form (PDF)</a>
          <!-- TODO: copy this PDF into /assets/files/ before GoDaddy is cancelled -->
          <a class="btn outline" href="{mailto('New referral')}">Email a referral</a>
        </div>
      </div>
    </div>
    <div class="card">
      <h3>Please include</h3>
      <ul class="tick">
        <li>Client name, date of birth and phone number</li>
        <li>Reason for referral and relevant history</li>
        <li>Funding: NDIS, Medicare CDM or private</li>
        <li>Your name, practice and contact details</li>
      </ul>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>Who we see</h2>
    <p class="lead">Neurodivergent people, young women, people with invisible or fluctuating conditions, and young people who haven't clicked with traditional models. Home visits around Upper Coomera and Pimpama out to Paradise Point, and telehealth.</p>
  </div>
</section>
"""
page("/referrals/", "Referrals | Blossom Therapy & Supports",
     "Refer a client to Blossom Therapy & Supports for exercise physiology, physiotherapy or disability support.", referrals)

# ---------- Resources ----------
RES = [
    ("Menopause and its health implications: bone health and exercise as treatment", "Olivia Marshall-Baird",
     "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/5f660d03-8f82-487d-833b-ba0f0f75dc78/Blossom%20-%20Menopause%20and%20its%20Health%20Implication.pdf?ver=1791773321573"),
    ("Autism and allied health: professional development for practitioners", "Emma Norton",
     "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/780fc0e8-927c-4575-867b-f5f9be10c89a/Autism%20and%20Allied%20Health-2.pdf?ver=1791773321574"),
    ("Guide for parents of autistic teenage girls: transitioning to post-school education", "Emma Norton",
     "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/0d1753f9-fd61-4e9b-8b75-d5db86ac1559/7177%20Assessment%201.pdf?ver=1791773321574"),
    ("Cognitive differences in autism and learning: PD for physical therapists", "Emma Norton",
     "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/0009c1de-0d63-4556-9a68-aca5773b0f76/Cognitive%20Differences%20in%20Autism%20and%20Learning%E2%80%8B.pdf?ver=1791773321574"),
]
res_cards = "".join(
    f'<div class="card resource"><div><h3>{t}</h3><p class="fine">By {a} &middot; PDF</p></div><a class="btn small" href="{u}">Download</a></div>'
    for t, a, u in RES
)
resources = hero("Free resources", "Practitioner-developed materials to support understanding, self-advocacy and gentle learning.") + f"""
<section class="sec">
  <div class="wrap">
    <!-- TODO: copy these PDFs into /assets/files/ and update links before GoDaddy is cancelled -->
    <div class="grid" style="grid-template-columns:1fr">{res_cards}</div>
    <p class="fine" style="margin-top:24px;max-width:760px">These resources include previous academic assignments and materials developed during our training and professional development. They're for general information and education only, and don't replace individual assessment, advice or care. Please seek professional support where needed.</p>
  </div>
</section>
"""
page("/resources/", "Free resources | Blossom Therapy & Supports",
     "Free practitioner-developed resources on autism, menopause, women's health and more.", resources)

# ---------- Contact ----------
contact = hero("Contact us", "Want to see if we're right for you?") + f"""
<section class="sec">
  <div class="wrap two-col">
    <div>
      <h2>Free 30-minute chat</h2>
      <p>Talk to us about what you're looking for and see if we're a good fit. No pressure.</p>
      <div class="btn-row">
        <a class="btn" href="/#get-started">Get started</a>
        <a class="btn outline" href="{mailto('Free 30-minute chat')}">Email us</a>
      </div>
      <h2 style="margin-top:36px">Already a client?</h2>
      <p>Email us to book, change or cancel an appointment.</p>
      <!-- LATER: replace with Halaxy "Book a follow-up" link when online booking is switched on -->
    </div>
    <div class="card">
      <h3>Get in touch</h3>
      <ul class="tick">
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Gold Coast QLD, Australia</li>
        <li>Home visits: Upper Coomera and Pimpama out to Paradise Point</li>
        <li>Telehealth: Australia-wide</li>
        <li><a href="{FB}" rel="noopener">Facebook</a> and <a href="{IG}" rel="noopener">Instagram</a></li>
      </ul>
      <!-- TODO: phone number and office hours, if the team wants them published -->
    </div>
  </div>
</section>
"""
page("/contact-us/", "Contact us | Blossom Therapy & Supports",
     "Contact Blossom Therapy & Supports. Free 30-minute chat to see if we're the right fit.", contact)

# ---------- Privacy (draft) ----------
privacy = hero("Privacy policy", "How we collect, use and protect your information.") + f"""
<section class="sec">
  <div class="wrap prose">
    <!-- DRAFT for owner review. Not legal advice. Check against the OAIC guidance for health service providers before publishing. -->
    <p><strong>Last updated:</strong> [date]</p>
    <h2>Who we are</h2>
    <p>Blossom Therapy and Supports [ABN to add] provides exercise physiology, physiotherapy and disability support services. We are bound by the Privacy Act 1988 (Cth) and the Australian Privacy Principles.</p>
    <h2>What we collect</h2>
    <p>Contact details, date of birth, funding details (such as NDIS or Medicare), health information relevant to your care, referral information, and notes from your sessions.</p>
    <h2>How we collect it</h2>
    <p>From you or your carer through our online forms, email, phone or in person, and from your referrer or other health providers with your consent.</p>
    <h2>How we store it</h2>
    <p>Client records and online forms are held in Halaxy, our practice management system, which stores data in Australia. This website doesn't store health information.</p>
    <h2>How we use and share it</h2>
    <p>To provide and coordinate your care, to claim funding (for example, with the NDIS or your plan manager), and to communicate with your treating team with your consent, or where the law requires it.</p>
    <h2>Accessing or correcting your information</h2>
    <p>You can ask to see or correct your information at any time. Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Complaints</h2>
    <p>Contact us first at <a href="mailto:{EMAIL}">{EMAIL}</a>. If you're not satisfied, you can contact the Office of the Australian Information Commissioner (oaic.gov.au). NDIS participants can also contact the NDIS Quality and Safeguards Commission.</p>
    <h2>This website</h2>
    <p>This site doesn't use tracking or advertising cookies.</p>
  </div>
</section>
"""
page("/privacy/", "Privacy policy | Blossom Therapy & Supports", "How Blossom Therapy & Supports handles your personal and health information.", privacy)

# ---------- Accessibility ----------
access = hero("Accessibility", "We want this website to work for everyone.") + f"""
<section class="sec">
  <div class="wrap prose">
    <ul class="tick">
      <li>Plain language, with one main action per section</li>
      <li>No autoplay, pop-ups or flashing content</li>
      <li>Works with screen readers, keyboard navigation and text resizing</li>
      <li>Respects your device's "reduce motion" setting</li>
    </ul>
    <p>If something doesn't work for you, or you'd like information in another format, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>
"""
page("/accessibility/", "Accessibility | Blossom Therapy & Supports", "Accessibility at Blossom Therapy & Supports.", access)

# ---------- 404 ----------
nf = hero("Page not found", "Sorry, we couldn't find that page.") + '<section class="sec"><div class="wrap"><a class="btn" href="/">Go to the home page</a></div></section>'
page("/404/", "Page not found | Blossom Therapy & Supports", "Page not found.", nf)
os.replace(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html"))
os.rmdir(os.path.join(OUT, "404"))

print("built")
