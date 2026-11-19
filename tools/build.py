"""Build the Blossom site into ../site.  Run from repo root:  python3 tools/build.py

Content comes from the original GoDaddy site (pulled 19 Nov 2026), with
physiotherapy (Caite Brown) added. Markers in the HTML:
  HALAXY EMBED  paste Halaxy form embed code here
  CONFIRM       fact to check before launch
  TODO          waiting on photos / info
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from assets import GODADDY, FILES, REMOTE, GALLERY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
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


def img(name, w=1200):
    """Local copy if uploaded to site/assets/img, else the old GoDaddy CDN."""
    if os.path.exists(os.path.join(OUT, "assets", "img", name)):
        return f"/assets/img/{name}"
    return f"{GODADDY}{REMOTE.get(name, name)}/:/rs=w:{w},cg:true,m"


def file_url(name):
    if os.path.exists(os.path.join(OUT, "assets", "files", name)):
        return f"/assets/files/{name}"
    return FILES[name]


def mailto(subject):
    return f"mailto:{EMAIL}?subject={subject.replace(' ', '%20')}"


FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21h2.9z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3a4.7 4.7 0 100 9.4 4.7 4.7 0 000-9.4zm0 7.7a3 3 0 110-6 3 3 0 010 6zm6-7.9a1.1 1.1 0 11-2.2 0 1.1 1.1 0 012.2 0zM21 8c-.1-1.5-.4-2.8-1.5-3.9S17 2.7 15.5 2.6C14 2.5 10 2.5 8.5 2.6 7 2.7 5.7 3 4.6 4.1S3.1 6.5 3 8c-.1 1.5-.1 6.5 0 8 .1 1.5.4 2.8 1.5 3.9S7 21.3 8.5 21.4c1.5.1 5.5.1 7 0 1.5-.1 2.8-.4 3.9-1.5s1.4-2.4 1.5-3.9c.1-1.5.1-6.5 0-8zm-2 9.7a3 3 0 01-1.7 1.7c-1.2.5-4 .4-5.3.4s-4.1.1-5.3-.4a3 3 0 01-1.7-1.7c-.5-1.2-.4-4-.4-5.3s-.1-4.1.4-5.3A3 3 0 016.7 5c1.2-.5 4-.4 5.3-.4s4.1-.1 5.3.4A3 3 0 0119 6.7c.5 1.2.4 4 .4 5.3s.1 4.1-.4 5.3z"/></svg>'


def page(path, title, desc, body):
    nav_items = "\n".join(
        '<li><a href="%s"%s>%s</a></li>' % (href, ' aria-current="page"' if href == path else "", label)
        for href, label in NAV
    )
    html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#DCFADC">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{img('IMG_8906.jpeg', 1200)}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Quicksand:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/"><img src="{img('blob-d2ed51b.png', 400)}" alt="Blossom Therapy and Supports" width="200" height="105"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="main-nav" id="main-nav" aria-label="Main">
      <ul>
{nav_items}
        <li><a class="btn small" href="/#get-started">Work With Us</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="social">
      <a href="{FB}" rel="noopener" aria-label="Blossom on Facebook">{FB_SVG}</a>
      <a href="{IG}" rel="noopener" aria-label="Blossom on Instagram">{IG_SVG}</a>
    </div>
    <p class="name">Blossom Therapy and Supports</p>
    <p>Gold Coast QLD, Australia &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <ul class="footer-links">
      <li><a href="/#get-started">Get started</a></li>
      <li><a href="/referrals/">Referrals</a></li>
      <li><a href="/privacy/">Privacy policy</a></li>
      <li><a href="/accessibility/">Accessibility</a></li>
    </ul>
    <p class="copyright">Copyright &copy; 2026 Blossom Therapy and Supports. All rights reserved.</p>
  </div>
</footer>
</body>
</html>
"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)


def page_hero(h1, p=""):
    para = f"<p>{p}</p>" if p else ""
    return f'<section class="page-hero"><div class="wrap"><h1>{h1}</h1>{para}</div></section>'


# ---------------- Get started picker ----------------
def slot(form_name, intro, items, subject):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="halaxy-slot" data-halaxy-form="{form_name}">
  <!-- HALAXY EMBED: paste the "{form_name}" embed code here (Halaxy > Settings > General > Forms > ⋮ > Share settings > Embedded Form > Copy).
       Then delete the fallback content below. -->
  <p class="tag">Online form coming soon</p>
  <p>{intro}</p>
  <ul>{lis}</ul>
  <a class="btn" href="{mailto(subject)}">Email us</a>
</div>"""


PICKER = f"""<section class="sec white" id="get-started" aria-labelledby="gs-h">
  <div class="wrap">
    <span id="start-client"></span><span id="start-carer"></span><span id="start-referrer"></span>
    <h2 id="gs-h">Work with us</h2>
    <p class="lead">Choose the option that fits you. We'll be in touch within 1 business day.</p>
    <!-- CONFIRM: response time with Emma -->
    <div class="picker" role="tablist" aria-label="Who are you?">
      <button role="tab" id="tab-client" aria-controls="panel-client" aria-selected="true">I'm a client</button>
      <button role="tab" id="tab-carer" aria-controls="panel-carer" aria-selected="false" tabindex="-1">I'm a parent or carer</button>
      <button role="tab" id="tab-referrer" aria-controls="panel-referrer" aria-selected="false" tabindex="-1">I'm a GP or referrer</button>
    </div>
    <div class="panel" role="tabpanel" id="panel-client" aria-labelledby="tab-client">
      <h3>Tell us about you</h3>
      <p>One short form that you can fill in on your phone.</p>
      {slot("Client intake", "Until our online form is ready, email us with:", ["Your name and phone number", "The service you're interested in (exercise physiology, physiotherapy, support work or social groups)", "Home visit or telehealth, and your suburb", "Funding (NDIS, private or other)", "Days and times that suit you"], "New client enquiry")}
    </div>
    <div class="panel" role="tabpanel" id="panel-carer" aria-labelledby="tab-carer" hidden>
      <h3>Tell us about the person you support</h3>
      <p>Your details, their details, and what support would help.</p>
      {slot("Carer intake", "Until our online form is ready, email us with:", ["Your name, phone number and relationship to the client", "The client's name and age", "The service you're interested in", "Home visit or telehealth, and suburb", "Funding (NDIS, private or other)", "Days and times that suit"], "Parent or carer enquiry")}
    </div>
    <div class="panel" role="tabpanel" id="panel-referrer" aria-labelledby="tab-referrer" hidden>
      <h3>Refer a client</h3>
      <p>Send us the referral and we'll contact your client directly.</p>
      {slot("Referrer form", "Until our online form is ready, download our referral form or email a referral with:", ["Client name, date of birth and phone number", "Reason for referral and relevant history", "Funding type (NDIS, Medicare CDM or private)", "Your name, practice and contact details"], "New referral")}
      <p style="margin-top:14px"><a href="{file_url('Client-referral-form.pdf')}">Download the referral form (PDF)</a></p>
    </div>
  </div>
</section>"""

# ---------------- Home ----------------
GALLERY_HTML = "\n      ".join(f'<img src="{img(g, 800)}" alt="A Blossom moment" loading="lazy">' for g in GALLERY)

home = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-card">
      <img src="{img('IMG_8906.jpeg', 1600)}" alt="The Blossom team smiling together by the water">
      <div class="hero-text">
        <h1>Blossom Therapy &amp; Supports</h1>
        <p>Shifting perspectives with movement, strength and meaningful support</p>
        <div class="btn-row">
          <a class="btn light" href="#get-started">Work With Us</a>
          <a class="btn outline" style="color:#fff;border-color:#fff" href="/#start-referrer">I'm a GP or referrer</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec peach">
  <div class="wrap three">
    <div>
      <h3>What Do We Do?</h3>
      <p>We are a small team of Exercise Physiologists, a Physiotherapist and Disability Support Workers. We specialise in supporting neurodivergent individuals, young women, and people living with invisible or fluctuating health conditions.</p>
      <p>Our approach is paced, collaborative, and grounded in safety: meeting each person where they are, not where a generic program says they should be.</p>
      <a class="btn" href="/our-services/">Learn More</a>
    </div>
    <div>
      <h3>Our Vision</h3>
      <p>We envision a future where no one is made to feel broken for having a body or mind that works differently.</p>
      <p>At Blossom, our vision is to create care that honours individuality, builds trust, and supports growth without pressure or harm.</p>
      <a class="btn" href="/about-us/">Discover More</a>
    </div>
    <div>
      <h3>Our Resources</h3>
      <p>Our resources are practitioner-developed materials, including previous assignments and tools we've created through our training and clinical experience. They're designed to support understanding, self-advocacy, and gentle learning for neurodivergent individuals and those living with complex or invisible health conditions.</p>
      <a class="btn" href="/resources/">Browse Resources</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>Who Do We Support?</h2>
    <hr class="rule">
    <div class="icons">
      <div><img src="{img('RGB_BT_SM_Icon01.png', 400)}" alt=""><h3>Neurodiversity</h3><p>We support neurodivergent individuals, including autistic and ADHD people, with care that is neuro-affirming, paced, and respectful of sensory and nervous-system needs. Our focus is on building confidence, safety, and sustainable engagement, not forcing compliance.</p></div>
      <div><img src="{img('RGB_BT_SM_Icon04.png', 400)}" alt=""><h3>Women's Health</h3><p>We work with individuals living with women's health conditions such as endometriosis, pelvic pain, and hormonal conditions. Our approach acknowledges pain, fatigue, and fluctuation, supporting movement and daily function without minimising lived experience.</p></div>
      <div><img src="{img('RGB_BT_SM_Icon03.png', 400)}" alt=""><h3>Invisible Illness</h3><p>We support people with invisible and fluctuating health conditions, including chronic pain, fatigue, POTS, MCAS, EDS, and related presentations. Care is adapted in real time, with pacing and flexibility prioritised to reduce flare-ups and build long-term trust in movement.</p></div>
      <div><img src="{img('RGB_BT_Logo_Icon.png', 400)}" alt=""><h3>Youth/Teens</h3><p>We support children, adolescents, and young people who may feel overwhelmed, disengaged, or misunderstood by traditional exercise and support models. Our work is gentle, relationship-led, and developmentally appropriate, supporting confidence, autonomy, and participation at each individual's pace.</p></div>
    </div>
  </div>
</section>

<section class="sec peach">
  <div class="wrap">
    <h2>How it works</h2>
    <div class="grid">
      <div class="card"><span class="step-num">1</span><h3>Tell us who you are</h3><p>Pick the option that fits. It only takes a few seconds.</p></div>
      <div class="card"><span class="step-num">2</span><h3>Fill in one short form</h3><p>Your details, your funding and the times that suit you.</p></div>
      <div class="card"><span class="step-num">3</span><h3>We match and book</h3><p>We'll pair you with the right clinician and confirm a time with you.</p></div>
    </div>
  </div>
</section>

{PICKER}

<section class="sec teal">
  <div class="wrap">
    <h2>Some of our favourite moments...</h2>
    <div class="gallery">
      {GALLERY_HTML}
    </div>
    <!-- TODO: better alt text describing each photo -->
  </div>
</section>
"""
page("/", "Blossom Therapy & Supports | Gold Coast and Telehealth",
     "Exercise physiology, physiotherapy and disability support on the Gold Coast and via telehealth. Neuro-affirming, paced and collaborative care.",
     home)

# ---------------- About ----------------
def member(photo, name, role, bio):
    pic = f'<img src="{img(photo, 600)}" alt="{name.split(" ")[0]}">' if photo else '<div class="ph-box">Photo coming soon</div>'
    return f'<div class="member">{pic}<div><h3>{name}</h3><p class="role">{role}</p>{bio}</div></div>'

about = f"""
<section class="sec">
  <div class="wrap split">
    <div>
      <h2>Our Why</h2>
      <p>Blossom Therapy &amp; Supports was created for people who are often told they are “too complex,” “too sensitive,” or “not progressing as expected.”</p>
      <p>Again and again, we saw individuals, particularly neurodivergent young women and people living with invisible or fluctuating health conditions, disengage from exercise, therapy, and support after feeling misunderstood, pushed, or blamed for bodies that did not respond predictably.</p>
      <p>Blossom exists to do things differently.</p>
      <p>We believe that when people feel safe, believed, and met where they are, progress becomes possible. Not through force or compliance, but through trust, understanding, and collaboration.</p>
    </div>
    <img src="{img('IMG_8922.jpeg', 1000)}" alt="The Blossom team">
  </div>
</section>

<section class="sec peach">
  <div class="wrap">
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:40px">
      <div>
        <h2>Our Philosophy</h2>
        <p>At the heart of Blossom Therapy &amp; Supports is a simple belief:</p>
        <p><strong>You are not broken. Your body and nervous system are doing their best to protect you.</strong></p>
        <p>Rather than trying to “fix” people or push them toward arbitrary benchmarks, we work alongside each individual to understand their body, capacity, and lived experience. From there, we build support that is sustainable, respectful, and meaningful.</p>
        <p>We value progress that lasts, not progress that comes at the cost of burnout, flare-ups, or disengagement.</p>
      </div>
      <div>
        <h2>Our Commitment</h2>
        <p>We are committed to providing care that:</p>
        <ul class="tick">
          <li>Is neuro-affirming and trauma-informed</li>
          <li>Respects autonomy and consent</li>
          <li>Acknowledges the emotional impact of long-term health challenges</li>
          <li>Supports independence without abandoning support</li>
        </ul>
        <p>Above all, we aim to help people rebuild trust: in their bodies, in movement, and in support systems that may have failed them before.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>Meet the Team!</h2>
    <hr class="rule">
    <div class="team">
      {member("IMG_8918.jpeg", "Emma", "Founder, Accredited Exercise Physiologist &amp; Support Worker",
        "<p>Emma also holds a Graduate Diploma in Autism Studies and is passionate about disability support work for girls and young women who are neurodiverse and/or have invisible illnesses such as EDS, POTS and MCAS, as well as mental health challenges. Emma enjoys helping her clients improve their wellbeing, build confidence, and gain independence through Exercise Physiology and meaningful support.</p>")}
      {member("IMG_8915.jpeg", "Olivia", "Accredited Exercise Physiologist &amp; Support Worker",
        "<p>With a Master's in Women's Health Medicine, Olivia brings specialised knowledge and experience. She is particularly passionate about helping those with invisible illnesses like hEDS, POTS, CFS/ME and Fibromyalgia, as well as supporting individuals facing long covid and cancer. Her dedication extends to empowering women to understand their bodies, manage their health confidently, and feel strong through movement and education, emphasising the importance of movement in healing.</p>")}
      {member(None, "Caite", "Physiotherapist",
        "<!-- CONFIRM: Caite to review and edit this bio, and add a photo (assets/img/caite.jpg) -->"
        "<p>Caite is a physiotherapist who is currently completing a Master of Sport and Exercise Physiotherapy at The University of Queensland. She delivers Blossom's physiotherapy service, with home visits and telehealth, bringing the same paced, collaborative and neuro-affirming approach to injury, pain and movement.</p>")}
      {member("IMG_8920.jpeg", "Michaela", "Support Worker",
        "<p>Currently studying Paramedicine, Michaela brings a calm, patient, and nurturing energy to her work. Her gentle presence helps clients, including those managing invisible illnesses and neurodiversity, feel supported, safe, and understood as they build confidence and independence in daily life.</p>")}
    </div>
    <!-- CONFIRM: any other team members (e.g. the telehealth-only EP) -->
  </div>
</section>
"""
page("/about-us/", "About Us | Blossom Therapy & Supports",
     "Neurodivergent support at Blossom Therapy & Supports. Our why, our philosophy, and the team of exercise physiologists, a physiotherapist and support workers.", about)

# ---------------- Services ----------------
services = page_hero("Our Services", "We are a small team of Exercise Physiologists, a Physiotherapist and Disability Support Workers on the Gold Coast. We specialise in supporting neurodivergent individuals, young women, and people living with invisible or fluctuating health conditions.") + f"""
<section class="sec">
  <div class="wrap split">
    <img src="{img('IMG_8729.jpeg', 1000)}" alt="Exercise physiology session">
    <div>
      <h2>Exercise Physiology</h2>
      <p>Movement and strength support built around your body, capacity and goals, delivered by Accredited Exercise Physiologists in your home, in the community, or via telehealth.</p>
      <p>We believe everyone should have access to specialised and individualised Exercise Physiology. This is why we provide Telehealth services for people all over Australia.</p>
      <a class="btn" href="/#get-started">Work With Us</a>
    </div>
  </div>
</section>

<section class="sec peach">
  <div class="wrap split flip">
    <img src="{img('IMG_8512.jpeg', 1000)}" alt="Blossom women's health session">
    <div>
      <h2>Women's Health Exercise Physiology</h2>
      <p>We work with individuals living with women's health conditions such as endometriosis, pelvic pain, and hormonal conditions. Our approach acknowledges pain, fatigue, and fluctuation, supporting movement and daily function without minimising lived experience.</p>
      <p>Our women's health care is led by Olivia, who holds a Master's in Women's Health Medicine.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="ph-box">Physio photo coming soon<!-- TODO: assets/img/physio.jpg --></div>
    <div>
      <h2>Physiotherapy</h2>
      <p class="fine" style="color:var(--orange);font-weight:700;margin-top:-4px">New at Blossom</p>
      <p>Physiotherapy is now part of the Blossom team, delivered by Caite. Caite assesses and treats injury, pain and movement problems with the same paced, collaborative and neuro-affirming approach as the rest of the team.</p>
      <p>Home visits on the Gold Coast, and telehealth.</p>
      <!-- CONFIRM: any areas of focus Caite wants listed (e.g. hypermobility, persistent pain, return to sport) -->
      <a class="btn" href="/#get-started">Work With Us</a>
    </div>
  </div>
</section>

<section class="sec peach">
  <div class="wrap">
    <h2>Disability Support Work</h2>
    <p class="lead">Practical, gentle support from disability support workers with all relevant checks, helping clients build confidence and independence in daily life.</p>
    <div class="grid">
      <div class="card"><h3>Assistance with Self-Care Activities</h3><p>Core supports for everyday living.</p></div>
      <div class="card"><h3>Assistance with Decision Making, Daily Planning and Budgeting</h3><p>Capacity building supports.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="groups">
  <div class="wrap">
    <h2>Girls Social Support Groups</h2>
    <hr class="rule">
    <div class="grid">
      <div class="card"><h3>Wattle Crew</h3><p>Fortnightly sessions on Saturday afternoons for school aged girls looking for socialising and engaging in wholesome activities!</p><p><strong>Max. 6 girls</strong></p></div>
      <div class="card"><h3>Banksia Crew</h3><p>Weekly sessions on Thursday afternoons for girls who have just left school or who are homeschooled!</p><p><strong>Max. 6 girls</strong></p><p class="fine">*Please note some weeks the session will run on a Friday due to staff being away.</p></div>
      <div class="card peach">
        <h3>Details</h3>
        <ul class="tick">
          <li>Cost: $150 per session</li>
          <li>Duration: 3 hours (usually 1pm to 4pm)</li>
          <li>Activities include beach walks, botanical gardens, crafts, baking, gentle yoga and outings</li>
          <li>Need help with transport to or from the meeting location? Reach out and we may be able to assist.</li>
        </ul>
      </div>
    </div>
    <h3 style="color:var(--teal);margin-top:36px">Meet your support group leaders</h3>
    <p><strong>Olivia</strong> (Liv) is an Accredited Exercise Physiologist with a Master's in Women's Health and a passionate Disability Support Worker. She is passionate about creating a space for like-minded girls to come together, participate in wholesome activities, find meaningful hobbies and build independence. These groups are Liv's babies, and she is your go-to if you need any assistance.</p>
    <p><strong>Emma</strong> is the founder of Blossom Therapy &amp; Supports. You may see Emma filling in for Liv while she is away, or you may chat to her when enquiring about the sessions.</p>
    <!-- TODO: current term calendar images (the Term 1 2026 ones on the old site are out of date). Upload as assets/img/wattle-calendar.png and banksia-calendar.png -->
    <div class="halaxy-slot" data-halaxy-form="Group waitlist">
      <!-- HALAXY EMBED: paste the "Group waitlist" form embed code here, then delete the fallback below. -->
      <p class="tag">Join the list</p>
      <p>Email us with the participant's name and age, which group, and a contact number. We'll send you the current term calendar and let you know when a spot is available.</p>
      <a class="btn" href="{mailto('Social group enquiry')}">Enquire about groups</a>
    </div>
  </div>
</section>
"""
page("/our-services/", "Exercise Physiology, Physiotherapy & Disability Support Services | Blossom",
     "Exercise physiology, women's health exercise physiology, physiotherapy, NDIS disability support work and girls' social groups on the Gold Coast and via telehealth.", services)

# ---------------- Pricing ----------------
def prow(name, price, detail=""):
    d = f'<span class="detail">{detail}</span>' if detail else ""
    return f'<div class="price-row"><span class="name">{name}</span><strong>{price}</strong>{d}</div>'

pricing = page_hero("Service Prices", "Clear prices, so there are no surprises.") + f"""
<section class="sec">
  <div class="wrap" style="max-width:860px">
    <div class="price-group">
      <h3>Exercise Physiology and Physiotherapy: Home Visit</h3>
      <p class="note">Provided by an Accredited Exercise Physiologist or Physiotherapist in your home or community. Travel is included within a 30-minute drive. $175 per hour.</p>
      {prow("Initial Appointment", "$175", "60 minutes")}
      {prow("Standard Appointment", "$131.25", "45 minutes")}
      {prow("Extended Appointment", "$175", "60 minutes")}
      {prow("Travel Fee", "$45", "For travel beyond 30 minutes")}
      <!-- CONFIRM: 45-min price is pro rata of $175/hr. Change if a fixed price is preferred. -->
    </div>
    <div class="price-group">
      <h3>Exercise Physiology and Physiotherapy: Telehealth</h3>
      <p class="note">Provided by an Accredited Exercise Physiologist or Physiotherapist via Zoom.</p>
      {prow("Initial Appointment", "$130", "60 minutes")}
      {prow("Standard Appointment", "$110", "30 minutes")}
      {prow("Extended Appointment", "$120", "45 minutes")}
      <!-- CONFIRM: physio telehealth at the same rates as EP -->
    </div>
    <div class="price-group">
      <h3>Exercise Physiology: NDIS</h3>
      <p class="note">Provided by an Accredited Exercise Physiologist in your home or in the community.</p>
      {prow("Initial Appointment", "$242.99", "60-minute appointment + Initial Assessment report")}
      {prow("Standard Appointment", "$161.99", "60 minutes")}
      {prow("Short Appointment", "$81.00", "30 minutes")}
      {prow("NDIS Review Report", "$161.99 – $323.98", "Based on level of depth required and time to complete")}
    </div>
    <div class="price-group">
      <h3>Physiotherapy: NDIS</h3>
      <p class="note">Provided by a Physiotherapist in your home or in the community.</p>
      {prow("Hourly rate", "Up to $183.99", "Billed in line with the NDIS Pricing Schedule 2026–27")}
      <!-- CONFIRM: NDIS physio items, session lengths and report pricing -->
    </div>
    <div class="price-group">
      <h3>Support Work Services</h3>
      <p class="note">Provided by a disability support worker with all relevant checks.</p>
      {prow("Assistance with Self-Care Activities (Core)", "$73.58/hr*", "Minimum 3 hours")}
      {prow("Assistance with Decision Making, Daily Planning, Budgeting (CB)", "$73.58/hr*", "Minimum 3 hours")}
      {prow("Travel", "$1/km", "Travel done within the session, in the support worker's car")}
      <p class="fine" style="margin-top:14px">*Prices shown are representative of weekday, daytime prices. For weekend or public holiday prices please refer to the NDIS table of costs or email us for assistance. We bill in line with the NDIS Price Guide and are happy to liaise with support coordinators regarding budgets.</p>
    </div>
    <div class="price-group">
      <h3>Girls Social Support Groups</h3>
      {prow("Wattle Crew or Banksia Crew", "$150", "Per session, 3 hours")}
    </div>
    <p class="center"><a class="btn" href="/#get-started">Work With Us</a></p>
    <!-- TODO: cancellation policy and payment methods, if the team wants them listed -->
  </div>
</section>
"""
page("/pricing-and-funding/", "Pricing & Funding | Blossom Therapy & Supports",
     "Prices for home visit and telehealth exercise physiology and physiotherapy, NDIS rates, support work and social groups.", pricing)

# ---------------- Referrals ----------------
referrals = page_hero("Referral Form", "New clients and referrers: send us a referral and we will contact you once we receive it.") + f"""
<section class="sec">
  <div class="wrap split" style="align-items:start">
    <div>
      <h2>Refer a client</h2>
      <div class="halaxy-slot" data-halaxy-form="Referrer form">
        <!-- HALAXY EMBED: paste the professional-contact (referrer) form embed code here, then delete the fallback below. -->
        <p class="tag">Online referral coming soon</p>
        <p>For now, please complete the referral form and email it to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <div class="btn-row">
          <a class="btn" href="{file_url('Client-referral-form.pdf')}">Download PDF</a>
          <a class="btn outline" href="{mailto('New referral')}">Email a referral</a>
        </div>
      </div>
    </div>
    <div class="card" style="background:var(--peach)">
      <h3 style="color:var(--orange)">Please include</h3>
      <ul class="tick">
        <li>Client name, date of birth and phone number</li>
        <li>Reason for referral and relevant history</li>
        <li>Service: exercise physiology, physiotherapy, support work or social groups</li>
        <li>Funding: NDIS, Medicare CDM or private</li>
        <li>Your name, practice and contact details</li>
      </ul>
    </div>
  </div>
</section>
"""
page("/referrals/", "Client Referral Form | Blossom Therapy",
     "Refer a client to Blossom Therapy & Supports for exercise physiology, physiotherapy, disability support or social groups.", referrals)

# ---------------- Resources ----------------
RES = [
    ("Menopause &amp; its Health Implications: Bone Health &amp; Exercise as Treatment", "Olivia Marshall-Baird", "Menopause-and-its-health-implications.pdf"),
    ("Autism and Allied Health: Professional Development for Practitioners", "Emma Norton", "Autism-and-allied-health.pdf"),
    ("Guide for parents of autistic teenage girls: Transitioning to Post-School Education", "Emma Norton", "Guide-for-parents-of-autistic-teenage-girls.pdf"),
    ("Cognitive Differences in Autism and Learning: PD for Physical Therapists", "Emma Norton", "Cognitive-differences-in-autism-and-learning.pdf"),
]
res_cards = "".join(
    f'<div class="card resource"><div><h3>{t}</h3><p class="fine">By {a} &middot; PDF</p></div><a class="btn small" href="{file_url(f)}">Download</a></div>'
    for t, a, f in RES
)
resources = page_hero("Free Resources") + f"""
<section class="sec">
  <div class="wrap">
    <div class="card peach" style="margin-bottom:24px">
      <h3>Resource Disclaimer</h3>
      <p>The free resources shared on this website include previous academic assignments and practitioner-developed materials created during our training and professional development. They are provided for general information and education only and are not intended to replace individualised assessment, advice, or care. Readers are encouraged to use discretion and seek appropriate professional support where needed.</p>
    </div>
    <div class="grid" style="grid-template-columns:1fr">{res_cards}</div>
  </div>
</section>
"""
page("/resources/", "Free Resources | Blossom Therapy & Supports",
     "Free practitioner-developed resources on autism, menopause, women's health and more.", resources)

# ---------------- Contact ----------------
contact = page_hero("Contact Us") + f"""
<section class="sec">
  <div class="wrap split" style="align-items:start">
    <div>
      <h2>Want to see if we are right for you?</h2>
      <p>We understand that every person and every journey is unique, especially when it comes to disability support work or navigating an invisible illness. That's why we offer a free 30-minute chat: to connect, have an honest conversation about what you're seeking, and explore if we're the right team to support you. Whether you're interested in exercise physiology, physiotherapy, neurodiversity, or women's health, there's no pressure, just an opportunity to see if it feels right.</p>
      <div class="btn-row">
        <a class="btn" href="/#get-started">Work With Us</a>
        <a class="btn outline" href="{mailto('Free 30-minute chat')}">Book a free chat</a>
      </div>
      <h2 style="margin-top:40px;font-size:28px">Already a client?</h2>
      <p>Email us to book, change or cancel an appointment.</p>
      <!-- LATER: Halaxy "Book a follow-up" link when online booking is switched on -->
    </div>
    <div class="card">
      <h3>Get in touch</h3>
      <ul class="tick">
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Gold Coast QLD, Australia</li>
        <li>Home visits across the Gold Coast</li>
        <li>Telehealth Australia-wide</li>
        <li><a href="{FB}" rel="noopener">Facebook</a> and <a href="{IG}" rel="noopener">Instagram</a></li>
      </ul>
      <!-- TODO: phone number and hours, if the team wants them published -->
    </div>
  </div>
</section>
"""
page("/contact-us/", "Contact Us | Blossom Therapy and Supports",
     "Contact Blossom Therapy & Supports. Book a free 30-minute chat to see if we're the right team for you.", contact)

# ---------------- Privacy (draft) ----------------
privacy = page_hero("Privacy Policy", "How we collect, use and protect your information.") + f"""
<section class="sec">
  <div class="wrap prose">
    <!-- DRAFT for owner review. Not legal advice. Check against the OAIC guidance for health service providers before relying on it. -->
    <p><strong>Last updated:</strong> [date]</p>
    <h2>Who we are</h2>
    <p>Blossom Therapy and Supports [ABN to add] provides exercise physiology, physiotherapy and disability support services. We are bound by the Privacy Act 1988 (Cth) and the Australian Privacy Principles.</p>
    <h2>What we collect</h2>
    <p>Contact details, date of birth, funding details (such as NDIS or Medicare), health information relevant to your care, referral information, and notes from your sessions.</p>
    <h2>How we collect it</h2>
    <p>From you or your carer through our online forms, email, phone or in person, and from your referrer or other health providers with your consent.</p>
    <h2>How we store it</h2>
    <p>Client records and online forms are held in Halaxy, our practice management system, which stores data in Australia. This website does not store health information.</p>
    <h2>How we use and share it</h2>
    <p>To provide and coordinate your care, to claim funding (for example with the NDIS or your plan manager), and to communicate with your treating team with your consent, or where the law requires it.</p>
    <h2>Accessing or correcting your information</h2>
    <p>You can ask to see or correct your information at any time. Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Complaints</h2>
    <p>Contact us first at <a href="mailto:{EMAIL}">{EMAIL}</a>. If you're not satisfied, you can contact the Office of the Australian Information Commissioner (oaic.gov.au). NDIS participants can also contact the NDIS Quality and Safeguards Commission.</p>
    <h2>This website</h2>
    <p>This site does not use tracking or advertising cookies.</p>
  </div>
</section>
"""
page("/privacy/", "Privacy Policy | Blossom Therapy & Supports", "How Blossom Therapy & Supports handles your personal and health information.", privacy)

# ---------------- Accessibility ----------------
access = page_hero("Accessibility", "We want this website to work for everyone.") + f"""
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

# ---------------- 404 ----------------
nf = page_hero("Page not found", "Sorry, we couldn't find that page.") + '<section class="sec"><div class="wrap"><a class="btn" href="/">Go to the home page</a></div></section>'
page("/404/", "Page not found | Blossom Therapy & Supports", "Page not found.", nf)
os.replace(os.path.join(OUT, "404", "index.html"), os.path.join(OUT, "404.html"))
os.rmdir(os.path.join(OUT, "404"))

print("built", OUT)
