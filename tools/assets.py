"""Image and file list from the old GoDaddy site.

Every image is referenced by file name. If the file exists in site/assets/img/,
the site uses the local copy. If not, it falls back to the old GoDaddy CDN URL,
which stops working once GoDaddy is cancelled. Upload every file below into
site/assets/img/ (same names) before cancelling.
"""

GODADDY = "https://img1.wsimg.com/isteam/ip/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/"

IMAGES = {
    # name: where it's used / what it is
    "blob-d2ed51b.png": "Logo (header)",
    "IMG_8906.jpeg": "Home hero: team photo by the water",
    "RGB_BT_SM_Icon01.png": "Who we support icon (pink circle)",
    "RGB_BT_SM_Icon03.png": "Who we support icon (orange flower, peach circle)",
    "RGB_BT_SM_Icon04.png": "Who we support icon (blue circle)",
    "RGB_BT_Logo_Icon.png": "Who we support icon (teal flower, peach circle)",
    "IMG_8922.jpeg": "About: Our Why photo",
    "IMG_8918.jpeg": "About: Emma",
    "IMG_8915.jpeg": "About: Olivia",
    "IMG_8920.jpeg": "About: Michaela",
    "IMG_8729.jpeg": "Services: exercise physiology",
    "IMG_8512.jpeg": "Services / gallery",
    "IMG_8857.jpeg": "Gallery",
    "IMG_8715.jpeg": "Gallery",
    "IMG_8900.jpeg": "Gallery",
    "2.png": "Wattle Crew Term 1 2026 calendar (not shown: out of date)",
    "3.png": "Banksia Crew Term 1 2026 calendar p1 (not shown: out of date)",
    "4.png": "Banksia Crew Term 1 2026 calendar p2 (not shown: out of date)",
    "5.png": "Groups additional details (not shown; text copied into page)",
    "6.png": "Groups: meet the leaders (not shown; text copied into page)",
}

FILES = {
    "Client-referral-form.pdf": "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/Client%20referral%20form.pdf",
    "Menopause-and-its-health-implications.pdf": "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/5f660d03-8f82-487d-833b-ba0f0f75dc78/Blossom%20-%20Menopause%20and%20its%20Health%20Implication.pdf?ver=1791773321573",
    "Autism-and-allied-health.pdf": "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/780fc0e8-927c-4575-867b-f5f9be10c89a/Autism%20and%20Allied%20Health-2.pdf?ver=1791773321574",
    "Guide-for-parents-of-autistic-teenage-girls.pdf": "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/0d1753f9-fd61-4e9b-8b75-d5db86ac1559/7177%20Assessment%201.pdf?ver=1791773321574",
    "Cognitive-differences-in-autism-and-learning.pdf": "https://img1.wsimg.com/blobby/go/fc922215-55f7-48fb-bc5a-a0bc6ec97e0e/downloads/0009c1de-0d63-4556-9a68-aca5773b0f76/Cognitive%20Differences%20in%20Autism%20and%20Learning%E2%80%8B.pdf?ver=1791773321574",
}

# Local name -> file name on the GoDaddy CDN, where they differ.
# Gallery photos were uploaded to GoDaddy as screenshots; save them locally as gallery-01.png etc.
REMOTE = {
    "gallery-01.png": "Screenshot%202025-10-21%20at%207.38.21%E2%80%AFam.png",
    "gallery-02.png": "Screenshot%202025-10-21%20at%207.39.29%E2%80%AFam.png",
    "gallery-03.png": "Screenshot%202025-10-21%20at%207.39.44%E2%80%AFam.png",
    "gallery-04.png": "Screenshot%202025-10-21%20at%207.49.27%E2%80%AFam.png",
    "gallery-05.png": "Screenshot%202025-10-21%20at%207.49.46%E2%80%AFam.png",
    "gallery-06.png": "Screenshot%202025-10-21%20at%207.50.14%E2%80%AFam.png",
    "gallery-07.png": "Screenshot%202025-10-21%20at%207.50.26%E2%80%AFam.png",
    "gallery-08.png": "Screenshot%202025-10-21%20at%207.50.39%E2%80%AFam.png",
    "gallery-09.png": "Screenshot%202025-10-21%20at%207.50.53%E2%80%AFam.png",
    "gallery-10.png": "Screenshot%202025-10-21%20at%207.55.35%E2%80%AFam.png",
    "gallery-11.png": "Screenshot%202025-10-21%20at%208.21.13%E2%80%AFam.png",
}
GALLERY = ["IMG_8512.jpeg", "IMG_8857.jpeg", "IMG_8715.jpeg", "IMG_8900.jpeg"] + [f"gallery-{i:02d}.png" for i in range(1, 12)]
