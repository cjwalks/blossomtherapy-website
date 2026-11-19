"""Booking workflow page (/book/): three step-by-step forms (client, parent/carer,
GP/referrer) on Netlify Forms. Health detail is limited to "how can we help".
Without JavaScript every step shows at once, so the page still works.
"""
from forms import text, textarea, select

SERVICES = ["Exercise physiology", "Physiotherapy", "Disability support work", "Not sure yet"]
DELIVERY = ["Home visit", "Telehealth", "Either"]
FUNDING = ["NDIS", "Medicare (GP care plan)", "Private", "Not sure"]
NDIS_MGMT = ["Plan managed", "Self managed", "Agency (NDIA) managed"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
TIMES = ["Morning (8am to 12pm)", "Afternoon (12pm to 3pm)", "After school (3pm to 6pm)"]
START = ["As soon as possible", "Within 2 weeks", "Within a month", "Just enquiring for now"]
CONTACT = ["Phone call", "Text message", "Email"]
HEARD = ["GP or health professional", "Support coordinator", "Friend or family", "Instagram or Facebook", "Google", "Other"]


def cards(form, name, legend, options, required=False, kind="radio", reveal=None):
    """Big tap-friendly option cards. reveal={option: section_id} shows a section when chosen."""
    req = " required" if (required and kind == "radio") else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    nm = name if kind == "radio" else f"{name}[]"
    items = []
    for o in options:
        data = f' data-reveal="{reveal[o]}"' if reveal and o in reveal else ""
        items.append(f'<label class="opt"><input type="{kind}" name="{nm}" value="{o}"{req}{data}><span>{o}</span></label>')
    return f'<fieldset class="field full"><legend>{legend}{star}</legend><div class="opts">{"".join(items)}</div></fieldset>'


def reveal_block(id_, inner):
    return f'<div class="reveal field full" id="{id_}" hidden><div class="fields">{inner}</div></div>'


def step(title, intro, fields):
    p = f'<p class="step-intro">{intro}</p>' if intro else ""
    return f'<fieldset class="step"><legend class="step-title">{title}</legend>{p}<div class="fields">{fields}</div></fieldset>'


def funding_step(f, who="you"):
    ndis = reveal_block(f"{f}-ndis", "".join([
        cards(f, "ndis-management", "How is the NDIS plan managed?", NDIS_MGMT),
        text(f, "plan-manager", "Plan manager or support coordinator (name and email)",
             hint="Optional. Helps us send service agreements and invoices to the right place."),
        text(f, "plan-end", "Plan end date", type_="date"),
    ]))
    medicare = reveal_block(f"{f}-medicare", cards(
        f, "gp-plan", "Is there a GP referral on a care plan?", ["Yes", "No", "Not sure"]))
    private = reveal_block(f"{f}-private", cards(
        f, "health-fund", "Private health insurance with extras cover?", ["Yes", "No", "Not sure"]))
    return step("Funding", "This helps us check what's covered before we call.", "".join([
        cards(f, "funding", "How will sessions be funded?", FUNDING, True,
              reveal={"NDIS": f"{f}-ndis", "Medicare (GP care plan)": f"{f}-medicare", "Private": f"{f}-private"}),
        ndis, medicare, private,
    ]))


def service_step(f, about="you"):
    return step("What are you looking for?", "", "".join([
        cards(f, "service", "Which service?", SERVICES, True),
        cards(f, "delivery", "Home visit or telehealth?", DELIVERY, True),
    ]))


def help_step(f, who="you"):
    return step("How can we help?", "A sentence or two is plenty. We'll talk through the details with you.", "".join([
        textarea(f, "how-can-we-help", f"What would {who} like help with?",
                 "For example: the condition, injury or concern you're seeking support for.", required=True),
        textarea(f, "goals", f"What would {who} like to be able to do?",
                 "Optional. For example: walk to the beach, get back to netball, manage daily tasks with less fatigue."),
        cards(f, "referred", "Has a GP or another provider referred " + ("you" if who == "you" else "them") + "?", ["Yes", "No"]),
    ]))


def when_step(f):
    return step("When suits?", "Tick everything that could work. We'll find the best match.", "".join([
        cards(f, "days", "Days", DAYS, kind="checkbox"),
        cards(f, "times", "Times", TIMES, kind="checkbox"),
        cards(f, "start", "How soon would you like to start?", START, True),
        text(f, "clinician-preference", "Anyone you'd like to see?", hint="Optional. Leave blank if you have no preference."),
    ]))


def contact_prefs(f):
    return "".join([
        cards(f, "contact-method", "Best way to contact you", CONTACT, True),
        text(f, "contact-time", "Best time to reach you", hint="Optional. For example: after 3pm, or weekday mornings."),
        textarea(f, "first-contact", "Anything that would make first contact easier?",
                 "Optional. For example: text before calling, or communication and sensory preferences."),
        select(f, "heard-about", "How did you hear about us?", HEARD),
    ])


def review_step(f, consent_text):
    return f"""<fieldset class="step step-review"><legend class="step-title">Check and send</legend>
<p class="step-intro">Check your answers below. Use Back to change anything.</p>
<dl class="summary" aria-live="polite"></dl>
<div class="fields"><div class="field full"><label class="check"><input type="checkbox" name="consent" value="yes" required> {consent_text} <span class="req" aria-hidden="true">*</span></label></div></div>
<p class="fine">Your details go to the Blossom team only. See our <a href="/privacy/">privacy policy</a>.</p>
</fieldset>"""


def shell(f, subject, steps, submit, enctype=False):
    enc = ' enctype="multipart/form-data"' if enctype else ""
    return f"""<form class="booking-form" id="form-{f}" name="{f}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company-website"{enc}>
  <input type="hidden" name="form-name" value="{f}">
  <input type="hidden" name="subject" value="{subject}">
  <p class="hp"><label>Leave this empty: <input name="company-website" tabindex="-1" autocomplete="off"></label></p>
  <div class="progress" aria-hidden="true"><span></span></div>
  <p class="step-count" aria-live="polite"></p>
  {steps}
  <div class="step-nav">
    <button type="button" class="btn outline js-back">Back</button>
    <button type="button" class="btn js-next">Next</button>
    <button type="submit" class="btn js-submit">{submit}</button>
  </div>
</form>"""


def client_form():
    f = "booking-client"
    details = step("Your details", "", "".join([
        text(f, "first-name", "First name", True, autocomplete="given-name"),
        text(f, "last-name", "Last name", True, autocomplete="family-name"),
        text(f, "dob", "Date of birth", type_="date", hint="Optional. Saves time at your first visit."),
        text(f, "phone", "Phone", True, "tel", "tel"),
        text(f, "email", "Email", True, "email", "email"),
        text(f, "suburb", "Suburb", True, autocomplete="address-level2"),
        contact_prefs(f),
    ]))
    steps = "".join([service_step(f), help_step(f), funding_step(f), when_step(f), details,
                     review_step(f, "I agree to Blossom contacting me about this booking request.")])
    return shell(f, "New booking request: client", steps, "Send booking request")


def carer_form():
    f = "booking-carer"
    about = step("About the person you support", "", "".join([
        text(f, "client-first-name", "Their first name", True),
        text(f, "client-age", "Their age", True),
        text(f, "suburb", "Their suburb", True),
        cards(f, "contact-who", "Who should we contact to book?", ["Me", "Them", "Either of us"], True),
    ]))
    details = step("Your details", "", "".join([
        text(f, "name", "Your name", True, autocomplete="name"),
        text(f, "relationship", "Your relationship to them", True, hint="For example: parent, carer, support coordinator."),
        text(f, "phone", "Phone", True, "tel", "tel"),
        text(f, "email", "Email", True, "email", "email"),
        contact_prefs(f),
    ]))
    steps = "".join([service_step(f), help_step(f, "they"), about, funding_step(f), when_step(f), details,
                     review_step(f, "I agree to Blossom contacting me about this booking request, and the person I support has agreed to it (or I'm their guardian).")])
    return shell(f, "New booking request: parent or carer", steps, "Send booking request")


def referral_form():
    f = "booking-referral"
    you = step("Your details", "", "".join([
        text(f, "referrer-name", "Your name", True, autocomplete="name"),
        text(f, "referrer-role", "Your role", True, hint="For example: GP, psychologist, support coordinator."),
        text(f, "practice", "Practice or organisation", True, autocomplete="organization"),
        text(f, "referrer-phone", "Phone", False, "tel", "tel"),
        text(f, "referrer-email", "Email", True, "email", "email"),
    ]))
    client = step("Client details", "", "".join([
        text(f, "client-name", "Client's full name", True),
        text(f, "client-dob", "Date of birth", type_="date"),
        text(f, "client-phone", "Client's phone", True, "tel"),
        text(f, "client-email", "Client's email", type_="email"),
        text(f, "suburb", "Suburb", True),
        text(f, "carer-contact", "Parent, carer or guardian to contact", hint="Optional. Name and phone."),
    ]))
    referral = step("Referral", "", "".join([
        cards(f, "service", "Service", SERVICES, True),
        cards(f, "delivery", "Home visit or telehealth?", DELIVERY, True),
        textarea(f, "how-can-we-help", "Reason for referral", "The condition or concern, and what you'd like us to help with.", required=True),
        cards(f, "urgency", "How soon should we see them?", ["Routine", "Within 2 weeks", "Urgent"], True),
        '<div class="field full"><label for="booking-referral-letter">Referral letter or care plan (optional)</label>'
        '<span class="hint" id="booking-referral-letter-hint">PDF, Word or image, up to 8 MB.</span>'
        '<input id="booking-referral-letter" name="referral-letter" type="file" accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" aria-describedby="booking-referral-letter-hint"></div>',
    ]))
    steps = "".join([you, client, referral, funding_step(f),
                     review_step(f, "The client (or their parent, carer or guardian) has agreed to this referral.")])
    return shell(f, "New referral", steps, "Send referral", enctype=True)


PATHS = [
    ("client", "I'm booking for myself", "Book exercise physiology, physiotherapy or support work for you.", client_form),
    ("carer", "I'm a parent or carer", "Book for someone you support, like your child or a family member.", carer_form),
    ("referrer", "I'm a GP or referrer", "Refer a client and we'll contact them directly.", referral_form),
]


def booking_page_body():
    chooser = "".join(
        f'<a class="path-card" href="?for={k}" data-path="{k}"><span class="path-title">{t}</span><span>{d}</span></a>'
        for k, t, d, _ in PATHS
    )
    panels = "".join(
        f'<section class="path-panel" id="path-{k}" data-panel="{k}"><h2>{t}</h2>'
        f'<p class="fine"><a href="/book/" class="js-change-path">&larr; Choose a different option</a></p>{fn()}</section>'
        for k, t, d, fn in PATHS
    )
    return f"""
<section class="book-hero">
  <div class="wrap">
    <h1>Book with Blossom</h1>
    <p>A few short steps, about 3 minutes. We'll be in touch within 1 business day to confirm a time with you.</p>
  </div>
</section>
<section class="sec book-body">
  <div class="wrap book-wrap">
    <div class="chooser" id="chooser">
      <h2>Who is this booking for?</h2>
      <div class="path-grid">{chooser}</div>
      <p class="fine">Just have a question? <a href="/contact-us/#contact-form">Send us a message</a> instead.</p>
    </div>
    {panels}
  </div>
</section>
"""
