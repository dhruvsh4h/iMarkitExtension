"""
Okanagan Pulse - Event Aggregator
iMarkit.com Community Intelligence Dashboard
Simulates scraping real Kelowna events for March 26-31, 2026.
"""

import json
import os

EVENTS = [
    {
        "id": 1,
        "title": "Tina Leon Live",
        "venue": "Rotary Centre for the Arts",
        "date": "2026-03-26",
        "time": "7:30 PM",
        "date_label": "Thu, Mar 26",
        "categories": ["Nightlife"],
        "is_featured": False,
        "is_free": False,
        "price": "$25",
        "hook": "Catch one of the Okanagan's most soulful voices light up the Rotary Centre stage in an intimate evening you won't forget.",
        "image_color": "#7B1D1D",
        "tags": ["Live Music", "Arts"],
        "source_url": "https://rotarycentreforthearts.com"
    },
    {
        "id": 2,
        "title": "Nate Haller at Red Bird Brewing",
        "venue": "Red Bird Brewing",
        "date": "2026-03-26",
        "time": "8:00 PM",
        "date_label": "Thu, Mar 26",
        "categories": ["Nightlife"],
        "is_featured": False,
        "is_free": False,
        "price": "No Cover",
        "hook": "Kick off the weekend with craft beer and live acoustic vibes — Nate Haller brings warm folk energy to Red Bird's taproom.",
        "image_color": "#8B4513",
        "tags": ["Live Music", "Nightlife", "Craft Beer"],
        "source_url": "https://redbirdbrewing.com"
    },
    {
        "id": 3,
        "title": "BC Interior Sportsman Show",
        "venue": "MNP Place",
        "date": "2026-03-27",
        "time": "10:00 AM",
        "date_label": "Fri, Mar 27",
        "categories": ["Family", "Business"],
        "is_featured": True,
        "is_free": False,
        "price": "$15 / Kids Free",
        "hook": "The region's premier outdoor expo — hunting, fishing, camping gear, and guided trip bookings all under one massive roof at MNP Place.",
        "image_color": "#2D5016",
        "tags": ["Outdoors", "Family", "Expo"],
        "source_url": "https://bcsportsmanshow.com"
    },
    {
        "id": 4,
        "title": "Comedy for a Cause",
        "venue": "Dakoda's",
        "date": "2026-03-27",
        "time": "7:00 PM",
        "date_label": "Fri, Mar 27",
        "categories": ["Nightlife"],
        "is_featured": False,
        "is_free": False,
        "price": "$20 (Charity)",
        "hook": "Laugh the night away for a good reason — local comedians take the Dakoda's stage to raise funds for a worthy Kelowna cause.",
        "image_color": "#4A1942",
        "tags": ["Comedy", "Charity", "Nightlife"],
        "source_url": "https://dakodaskelowna.com"
    },
    {
        "id": 5,
        "title": "Okanagan Screen Awards",
        "venue": "Landmark Cinemas",
        "date": "2026-03-28",
        "time": "6:00 PM",
        "date_label": "Sat, Mar 28",
        "categories": ["Business"],
        "is_featured": False,
        "is_free": False,
        "price": "$30",
        "hook": "Celebrate the Okanagan's best in film and media — an elegant awards gala honouring local storytellers on the big screen.",
        "image_color": "#1A1A2E",
        "tags": ["Film", "Awards", "Arts"],
        "source_url": "https://landmarkcinemas.com"
    },
    {
        "id": 6,
        "title": "Kelowna Farmers' & Crafters' Market",
        "venue": "Parkinson Recreation Centre",
        "date": "2026-03-28",
        "time": "8:00 AM",
        "date_label": "Sat, Mar 28",
        "categories": ["Family", "Free"],
        "is_featured": False,
        "is_free": True,
        "price": "Free Entry",
        "hook": "Stock up on fresh local produce, handmade goods, and community warmth at Kelowna's beloved Saturday morning tradition.",
        "image_color": "#B45309",
        "tags": ["Market", "Family", "Free"],
        "source_url": "https://kelownafarmersmarket.com"
    },
    {
        "id": 7,
        "title": "Punjabi Cultural Night — Vaisakhi Pre-Celebration",
        "venue": "Kelowna Community Theatre",
        "date": "2026-03-29",
        "time": "6:30 PM",
        "date_label": "Sun, Mar 29",
        "categories": ["Punjabi-Community", "Family"],
        "is_featured": False,
        "is_free": False,
        "price": "$10 / Kids Free",
        "hook": "A vibrant evening of bhangra, traditional food, and community spirit as Kelowna's Punjabi community gathers to welcome Vaisakhi season.",
        "image_color": "#D97706",
        "tags": ["Punjabi", "Cultural", "Family", "Dance"],
        "source_url": "#"
    },
    {
        "id": 8,
        "title": "Kelowna Business Networking Mixer",
        "venue": "Hotel Eldorado",
        "date": "2026-03-30",
        "time": "5:30 PM",
        "date_label": "Mon, Mar 30",
        "categories": ["Business"],
        "is_featured": False,
        "is_free": False,
        "price": "$15",
        "hook": "Grow your local network over craft cocktails and lakefront views — Kelowna's go-to Monday mixer for entrepreneurs and professionals.",
        "image_color": "#1E3A5F",
        "tags": ["Networking", "Business", "Professional"],
        "source_url": "#"
    },
    {
        "id": 9,
        "title": "Free Family Skate Night",
        "venue": "Rutland Arena",
        "date": "2026-03-30",
        "time": "7:00 PM",
        "date_label": "Mon, Mar 30",
        "categories": ["Family", "Free"],
        "is_featured": False,
        "is_free": True,
        "price": "Free",
        "hook": "Lace up and hit the ice — free public skating for the whole family at the Rutland Arena, skate rentals available on site.",
        "image_color": "#0E7490",
        "tags": ["Free", "Family", "Sports"],
        "source_url": "#"
    },
    {
        "id": 10,
        "title": "Open Mic Tuesday at BNA Brewing",
        "venue": "BNA Brewing",
        "date": "2026-03-31",
        "time": "8:00 PM",
        "date_label": "Tue, Mar 31",
        "categories": ["Nightlife", "Free"],
        "is_featured": False,
        "is_free": True,
        "price": "Free",
        "hook": "Close out March with raw, unfiltered talent — BNA's open mic night is where Kelowna's next big acts take their first stage.",
        "image_color": "#7C3AED",
        "tags": ["Open Mic", "Free", "Live Music"],
        "source_url": "https://bnabrewing.com"
    }
]

def main():
    output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "events.json")

    payload = {
        "generated_at": "2026-03-26T00:00:00",
        "region": "Kelowna, BC — Okanagan",
        "week": "March 26–31, 2026",
        "total_events": len(EVENTS),
        "events": EVENTS
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"[OK] Generated {len(EVENTS)} events → {output_path}")
    for e in EVENTS:
        cats = ", ".join(e["categories"])
        print(f"  • [{e['date_label']} {e['time']}] {e['title']} ({cats})")

if __name__ == "__main__":
    main()
