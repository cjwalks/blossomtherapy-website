"""Enquiry forms (Netlify Forms). Submissions are emailed to the address set in
Netlify > Forms > Notifications. When the Halaxy forms are ready, these can be
swapped for the Halaxy embed codes (same spots, marked HALAXY EMBED).

Privacy: these forms ask for contact and booking details only, not health
information. Netlify stores submissions on its servers (outside Australia),
so keep clinical detail for Halaxy and phone calls.
"""

SERVICES = ["Exercise physiology", "Physiotherapy", "Disability support work", "Not sure yet"]
DELIVERY = ["Home visit", "Telehealth", "Either"]
FUNDING = ["NDIS: plan managed", "NDIS: self managed", "NDIS: agency managed",
           "Private", "Medicare (GP care plan)", "Other or not sure"]
TIMES = ["Weekday mornings", "Weekday afternoons", "After school", "Saturdays"]

PRIVACY_NOTE = ('<p class="fine form-note">Please don\'t include medical details here. '
                'We\'ll talk about those with you directly. See our <a href="/privacy/">privacy policy</a>.</p>')


def _id(form, name):
    return f"{form}-{name}"


def text(form, name, label, required=False, type_="text", autocomplete=None, hint=None):
    req = " required" if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    ac = f' autocomplete="{autocomplete}"' if autocomplete else ""
    hint_html = f'<span class="hint" id="{_id(form, name)}-hint">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{_id(form, name)}-hint"' if hint else ""
    return (f'<div class="field"><label for="{_id(form, name)}">{label}{star}</label>{hint_html}'
            f'<input id="{_id(form, name)}" name="{name}" type="{type_}"{ac}{req}{desc}></div>')


def textarea(form, name, label, hint=None, required=False):
    req = " required" if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    hint_html = f'<span class="hint" id="{_id(form, name)}-hint">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{_id(form, name)}-hint"' if hint else ""
    return (f'<div class="field full"><label for="{_id(form, name)}">{label}{star}</label>{hint_html}'
            f'<textarea id="{_id(form, name)}" name="{name}" rows="4"{req}{desc}></textarea></div>')


def select(form, name, label, options, required=False):
    req = " required" if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    opts = '<option value="">Choose one</option>' + "".join(f"<option>{o}</option>" for o in options)
    return (f'<div class="field"><label for="{_id(form, name)}">{label}{star}</label>'
            f'<select id="{_id(form, name)}" name="{name}"{req}>{opts}</select></div>')


def checks(form, name, legend, options):
    boxes = "".join(
        f'<label class="check"><input type="checkbox" name="{name}[]" value="{o}"> {o}</label>'
        for o in options
    )
    return f'<fieldset class="field full"><legend>{legend}</legend><div class="checks">{boxes}</div></fieldset>'


def consent(form, text_):
    return (f'<div class="field full"><label class="check"><input type="checkbox" name="consent" value="yes" required> '
            f'{text_} <span class="req" aria-hidden="true">*</span></label></div>')


def wrap(form, title_for_email, fields, button, enctype=False):
    enc = ' enctype="multipart/form-data"' if enctype else ""
    return f"""<form class="enquiry" name="{form}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company-website"{enc}>
  <input type="hidden" name="form-name" value="{form}">
  <input type="hidden" name="subject" value="{title_for_email}">
  <p class="hp"><label>Leave this empty: <input name="company-website" tabindex="-1" autocomplete="off"></label></p>
  <p class="fine">Fields marked <span class="req">*</span> are required.</p>
  <div class="fields">
    {fields}
  </div>
  {PRIVACY_NOTE}
  <button class="btn" type="submit">{button}</button>
</form>"""


def client_form():
    f = "client-enquiry"
    fields = "\n    ".join([
        text(f, "name", "Your name", True, autocomplete="name"),
        text(f, "phone", "Phone", True, "tel", "tel"),
        text(f, "email", "Email", True, "email", "email"),
        text(f, "suburb", "Suburb", True, autocomplete="address-level2"),
        select(f, "service", "Service you're interested in", SERVICES, True),
        select(f, "delivery", "Home visit or telehealth?", DELIVERY, True),
        select(f, "funding", "Funding", FUNDING, True),
        checks(f, "times", "Times that usually suit you", TIMES),
        textarea(f, "preferences", "Anything that would make first contact easier?",
                 "For example: text before calling, best time to call, or communication preferences."),
        consent(f, "I agree to Blossom contacting me about this enquiry."),
    ])
    return wrap(f, "New client enquiry", fields, "Send enquiry")


def carer_form():
    f = "carer-enquiry"
    fields = "\n    ".join([
        text(f, "name", "Your name", True, autocomplete="name"),
        text(f, "relationship", "Your relationship to the client", True, hint="For example: parent, carer, support coordinator."),
        text(f, "phone", "Phone", True, "tel", "tel"),
        text(f, "email", "Email", True, "email", "email"),
        text(f, "client-name", "Client's first name", True),
        text(f, "client-age", "Client's age"),
        text(f, "suburb", "Client's suburb", True),
        select(f, "service", "Service you're interested in", SERVICES, True),
        select(f, "delivery", "Home visit or telehealth?", DELIVERY, True),
        select(f, "funding", "Funding", FUNDING, True),
        checks(f, "times", "Times that usually suit", TIMES),
        textarea(f, "preferences", "Anything that would make first contact easier?",
                 "For example: who to contact first, communication or sensory preferences."),
        consent(f, "I agree to Blossom contacting me about this enquiry, and I have the client's permission to make it."),
    ])
    return wrap(f, "New parent or carer enquiry", fields, "Send enquiry")


def referral_form():
    f = "referral"
    fields = "\n    ".join([
        text(f, "referrer-name", "Your name", True, autocomplete="name"),
        text(f, "referrer-role", "Role and practice", True, hint="For example: GP, Smith Street Medical."),
        text(f, "referrer-phone", "Your phone", False, "tel", "tel"),
        text(f, "referrer-email", "Your email", True, "email", "email"),
        text(f, "client-name", "Client's full name", True),
        text(f, "client-dob", "Client's date of birth", False, "date"),
        text(f, "client-phone", "Client's (or carer's) phone", True, "tel"),
        text(f, "suburb", "Client's suburb", True),
        select(f, "service", "Service", SERVICES, True),
        select(f, "funding", "Funding", FUNDING, True),
        '<div class="field full"><label for="referral-letter">Referral letter (optional)</label>'
        '<span class="hint" id="referral-letter-hint">PDF or image, up to 8 MB. You can also email it to hello@blossomtherapy.au.</span>'
        '<input id="referral-letter" name="referral-letter" type="file" accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" aria-describedby="referral-letter-hint"></div>',
        consent(f, "The client (or their carer) has agreed to this referral."),
    ])
    return wrap(f, "New referral", fields, "Send referral", enctype=True).replace(
        PRIVACY_NOTE,
        '<p class="fine form-note">We\'ll contact your client directly. Clinical details are best included in the referral letter. '
        'See our <a href="/privacy/">privacy policy</a>.</p>')


def contact_form():
    f = "contact"
    fields = "\n    ".join([
        text(f, "name", "Name", True, autocomplete="name"),
        text(f, "email", "Email", True, "email", "email"),
        text(f, "phone", "Phone", False, "tel", "tel"),
        textarea(f, "message", "Message", required=True,
                 hint="Tell us what you're looking for, or ask about a free 30-minute chat."),
    ])
    return wrap(f, "Website enquiry", fields, "Send")
