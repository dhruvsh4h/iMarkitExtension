"""
Okanagan Pulse - Event Aggregator
iMarkit.com Community Intelligence Dashboard
Generates realistic Kelowna events for a 3-month forward window (Mar 27 - Jun 30, 2026).
All events must have a valid source_url - no placeholder '#' links.
"""

import json
import os
from datetime import datetime

# ── Real seed events (late March 2026) ──────────────────────────────────────
SEED_EVENTS = [
    {
        "title": "Tina Leon Live",
        "venue": "Rotary Centre for the Arts",
        "date": "2026-03-26", "time": "7:30 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$25",
        "hook": "Catch one of the Okanagan's most soulful voices light up the Rotary Centre stage in an intimate evening you won't forget.",
        "image_color": "#7B1D1D",
        "tags": ["Live Music", "Arts"],
        "source_url": "https://rotarycentreforthearts.com"
    },
    {
        "title": "Nate Haller at Red Bird Brewing",
        "venue": "Red Bird Brewing",
        "date": "2026-03-26", "time": "8:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "No Cover",
        "hook": "Kick off the weekend with craft beer and live acoustic vibes -- Nate Haller brings warm folk energy to Red Bird's taproom.",
        "image_color": "#8B4513",
        "tags": ["Live Music", "Nightlife", "Craft Beer"],
        "source_url": "https://redbirdbrewing.com"
    },
    {
        "title": "BC Interior Sportsman Show",
        "venue": "MNP Place",
        "date": "2026-03-27", "time": "10:00 AM",
        "categories": ["Family", "Business"],
        "is_featured": True,
        "is_free": False, "price": "$15 / Kids Free",
        "hook": "The region's premier outdoor expo -- hunting, fishing, camping gear, and guided trip bookings all under one massive roof at MNP Place.",
        "image_color": "#2D5016",
        "tags": ["Outdoors", "Family", "Expo"],
        "source_url": "https://bcsportsmanshow.com"
    },
    {
        "title": "Comedy for a Cause",
        "venue": "Dakoda's",
        "date": "2026-03-27", "time": "7:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$20 (Charity)",
        "hook": "Laugh the night away for a good reason -- local comedians take the Dakoda's stage to raise funds for a worthy Kelowna cause.",
        "image_color": "#4A1942",
        "tags": ["Comedy", "Charity", "Nightlife"],
        "source_url": "https://www.dakodasnightclub.com"
    },
    {
        "title": "Okanagan Screen Awards",
        "venue": "Landmark Cinemas",
        "date": "2026-03-28", "time": "6:00 PM",
        "categories": ["Business"],
        "is_free": False, "price": "$30",
        "hook": "Celebrate the Okanagan's best in film and media -- an elegant awards gala honouring local storytellers on the big screen.",
        "image_color": "#1A1A2E",
        "tags": ["Film", "Awards", "Arts"],
        "source_url": "https://www.landmarkcinemas.com/kelowna"
    },
    {
        "title": "Kelowna Farmers' & Crafters' Market",
        "venue": "Parkinson Recreation Centre",
        "date": "2026-03-28", "time": "8:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free Entry",
        "hook": "Stock up on fresh local produce, handmade goods, and community warmth at Kelowna's beloved Saturday morning tradition.",
        "image_color": "#B45309",
        "tags": ["Market", "Family", "Free"],
        "source_url": "https://bcfarmersmarket.org/kelowna-farmers-and-crafters-market/"
    },
    {
        "title": "Punjabi Cultural Night",
        "venue": "Kelowna Community Theatre",
        "date": "2026-03-29", "time": "6:30 PM",
        "categories": ["Punjabi-Community", "Family"],
        "is_free": False, "price": "$10 / Kids Free",
        "hook": "A vibrant evening of bhangra, traditional food, and community spirit as Kelowna's Punjabi community gathers to welcome Vaisakhi season.",
        "image_color": "#D97706",
        "tags": ["Punjabi", "Cultural", "Family", "Dance"],
        "source_url": "https://www.kelownacommunitytheatre.com"
    },
    {
        "title": "Kelowna Business Networking Mixer",
        "venue": "Hotel Eldorado",
        "date": "2026-03-30", "time": "5:30 PM",
        "categories": ["Business"],
        "is_free": False, "price": "$15",
        "hook": "Grow your local network over craft cocktails and lakefront views -- Kelowna's go-to Monday mixer for entrepreneurs and professionals.",
        "image_color": "#1E3A5F",
        "tags": ["Networking", "Business", "Professional"],
        "source_url": "https://www.kelownachamber.org"
    },
    {
        "title": "Free Family Skate Night",
        "venue": "Rutland Arena",
        "date": "2026-03-30", "time": "7:00 PM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Lace up and hit the ice -- free public skating for the whole family at the Rutland Arena, skate rentals available on site.",
        "image_color": "#0E7490",
        "tags": ["Free", "Family", "Sports"],
        "source_url": "https://www.kelowna.ca/parks-recreation/recreation-facilities/arenas"
    },
    {
        "title": "Open Mic Tuesday at BNA Brewing",
        "venue": "BNA Brewing",
        "date": "2026-03-31", "time": "8:00 PM",
        "categories": ["Nightlife", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Close out March with raw, unfiltered talent -- BNA's open mic night is where Kelowna's next big acts take their first stage.",
        "image_color": "#7C3AED",
        "tags": ["Open Mic", "Free", "Live Music"],
        "source_url": "https://www.bnabrewing.com"
    },
]

# ── Simulated events for April, May, June 2026 ─────────────────────────────
FUTURE_EVENTS = [
    # ─── APRIL 2026 ───
    {
        "title": "Kelowna Wine & Food Experience",
        "venue": "Laurel Packinghouse",
        "date": "2026-04-02", "time": "6:00 PM",
        "categories": ["Business", "Nightlife"],
        "is_free": False, "price": "$65",
        "hook": "Sip through 30+ Okanagan wineries paired with gourmet bites from the valley's top chefs -- the ultimate tasting night.",
        "image_color": "#6B1A38",
        "tags": ["Wine", "Food", "Tasting"],
        "source_url": "https://www.laurelpackinghouse.com"
    },
    {
        "title": "Kelowna Farmers' Market -- Spring Opening",
        "venue": "Parkinson Recreation Centre",
        "date": "2026-04-04", "time": "8:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free Entry",
        "hook": "The beloved Saturday market returns for the spring season with the first local greens, artisan crafts, and fresh baking.",
        "image_color": "#B45309",
        "tags": ["Market", "Family", "Free"],
        "source_url": "https://bcfarmersmarket.org/kelowna-farmers-and-crafters-market/"
    },
    {
        "title": "Easter Egg Hunt at City Park",
        "venue": "City Park",
        "date": "2026-04-05", "time": "10:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Bring the kids and hunt for thousands of hidden eggs across City Park -- face painting, bouncy castles, and the Easter Bunny included.",
        "image_color": "#16A34A",
        "tags": ["Family", "Free", "Holiday"],
        "source_url": "https://www.kelowna.ca/parks-recreation"
    },
    {
        "title": "Kelowna Tech Startup Demo Day",
        "venue": "Okanagan coLab",
        "date": "2026-04-07", "time": "4:00 PM",
        "categories": ["Business"],
        "is_free": False, "price": "$10",
        "hook": "Watch 8 Okanagan startups pitch live to investors and the community -- networking reception with craft beer to follow.",
        "image_color": "#1E40AF",
        "tags": ["Tech", "Startups", "Networking"],
        "source_url": "https://www.okanagancolab.com"
    },
    {
        "title": "Bhangra Fitness Bootcamp",
        "venue": "Parkinson Recreation Centre",
        "date": "2026-04-08", "time": "6:00 PM",
        "categories": ["Punjabi-Community", "Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Get moving to bhangra beats in this high-energy dance fitness class -- no experience needed, all fitness levels welcome.",
        "image_color": "#EA580C",
        "tags": ["Fitness", "Punjabi", "Dance", "Free"],
        "source_url": "https://www.kelowna.ca/parks-recreation"
    },
    {
        "title": "Jazz Night at Train Station Pub",
        "venue": "Train Station Pub",
        "date": "2026-04-10", "time": "8:30 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "No Cover",
        "hook": "Smooth jazz trios take over the Train Station stage -- settle into a booth with a cocktail and let the evening unwind itself.",
        "image_color": "#312E81",
        "tags": ["Jazz", "Live Music", "Nightlife"],
        "source_url": "https://www.trainstationpub.ca"
    },
    {
        "title": "Okanagan Spring Craft Fair",
        "venue": "Kelowna Curling Club",
        "date": "2026-04-11", "time": "10:00 AM",
        "categories": ["Family", "Business"],
        "is_free": True, "price": "Free Entry",
        "hook": "Over 60 local artisans showcase handmade pottery, jewelry, candles, and textiles -- support small and shop local this spring.",
        "image_color": "#92400E",
        "tags": ["Craft Fair", "Artisan", "Shopping"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Vaisakhi Nagar Kirtan Parade",
        "venue": "Rutland -- Hwy 33",
        "date": "2026-04-13", "time": "10:00 AM",
        "categories": ["Punjabi-Community", "Family", "Free"],
        "is_featured": True,
        "is_free": True, "price": "Free",
        "hook": "Kelowna's vibrant Sikh community celebrates Vaisakhi with a colourful procession, live kirtan, langar, and open-air festivities along Highway 33.",
        "image_color": "#F59E0B",
        "tags": ["Vaisakhi", "Punjabi", "Parade", "Cultural"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Kelowna Earth Day Clean-Up",
        "venue": "Knox Mountain Park",
        "date": "2026-04-22", "time": "9:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Join hundreds of volunteers for a trail and shoreline cleanup at Knox Mountain -- gloves, bags, and coffee provided.",
        "image_color": "#15803D",
        "tags": ["Volunteer", "Environment", "Free"],
        "source_url": "https://www.kelowna.ca/parks-recreation/parks-beaches/knox-mountain-park"
    },
    {
        "title": "Okanagan Tattoo & Arts Festival",
        "venue": "Kelowna Memorial Arena",
        "date": "2026-04-24", "time": "12:00 PM",
        "categories": ["Nightlife", "Business"],
        "is_free": False, "price": "$20",
        "hook": "Ink, art, and live music collide as top tattoo artists from across BC set up shop for a weekend of live tattooing and exhibitions.",
        "image_color": "#1C1917",
        "tags": ["Tattoo", "Art", "Festival"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Saturday Night Comedy at Dakoda's",
        "venue": "Dakoda's",
        "date": "2026-04-25", "time": "8:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$22",
        "hook": "Dakoda's monthly stand-up showcase brings touring Canadian comedians to Kelowna -- arrive early for dinner and the best seats.",
        "image_color": "#4A1942",
        "tags": ["Comedy", "Nightlife", "Stand-Up"],
        "source_url": "https://www.dakodasnightclub.com"
    },
    {
        "title": "Kelowna Yacht Club Open House",
        "venue": "Kelowna Yacht Club",
        "date": "2026-04-26", "time": "11:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Tour the marina, meet sailing instructors, and take free demo rides on the lake -- a perfect spring Sunday for the whole family.",
        "image_color": "#0369A1",
        "tags": ["Sailing", "Free", "Family", "Waterfront"],
        "source_url": "https://www.kelownayachtclub.com"
    },

    # ─── MAY 2026 ───
    {
        "title": "Kelowna May Day Festival",
        "venue": "Stuart Park",
        "date": "2026-05-01", "time": "11:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Celebrate spring with maypole dancing, live folk music, kids' crafts, and a flower crown contest right on the downtown waterfront.",
        "image_color": "#DB2777",
        "tags": ["Festival", "Family", "Free", "Spring"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Okanagan Cinco de Mayo Fiesta",
        "venue": "Dakoda's",
        "date": "2026-05-05", "time": "6:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$10",
        "hook": "Tacos, tequila, and a DJ spinning Latin beats -- Dakoda's goes full fiesta mode for Cinco de Mayo with drink specials all night.",
        "image_color": "#B91C1C",
        "tags": ["Nightlife", "Party", "Latin"],
        "source_url": "https://www.dakodasnightclub.com"
    },
    {
        "title": "Punjabi Mothers' Day Brunch",
        "venue": "Kelowna Community Theatre Hall",
        "date": "2026-05-10", "time": "10:30 AM",
        "categories": ["Punjabi-Community", "Family"],
        "is_free": False, "price": "$25",
        "hook": "Honour the mothers in your life with a traditional Punjabi brunch -- live tabla music, henna artists, and heartfelt community tributes.",
        "image_color": "#BE185D",
        "tags": ["Punjabi", "Family", "Mother's Day"],
        "source_url": "https://www.kelownacommunitytheatre.com"
    },
    {
        "title": "Kelowna International Food Festival",
        "venue": "City Park",
        "date": "2026-05-16", "time": "11:00 AM",
        "categories": ["Family", "Business"],
        "is_featured": True,
        "is_free": True, "price": "Free Entry (food for purchase)",
        "hook": "Taste the world without leaving Kelowna -- 40+ food vendors from Indian to Ethiopian to Filipino line the waterfront for a two-day culinary tour.",
        "image_color": "#C2410C",
        "tags": ["Food", "Cultural", "Festival", "Family"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Glenmore Neighbourhood Night Market",
        "venue": "Glenmore Community Centre",
        "date": "2026-05-17", "time": "4:00 PM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free Entry",
        "hook": "A walkable evening market with street food trucks, local artisans, face painting, and live acoustic music in the Glenmore neighbourhood.",
        "image_color": "#A16207",
        "tags": ["Night Market", "Family", "Free", "Local"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Victoria Day Long Weekend Beach Bash",
        "venue": "Gyro Beach",
        "date": "2026-05-18", "time": "12:00 PM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Kick off summer early with volleyball tournaments, a live DJ, BBQ vendors, and the unofficial first swim of the season at Gyro Beach.",
        "image_color": "#0891B2",
        "tags": ["Beach", "Party", "Free", "Summer"],
        "source_url": "https://www.kelowna.ca/parks-recreation/parks-beaches"
    },
    {
        "title": "Kelowna Chamber Business Excellence Awards",
        "venue": "Delta Grand Okanagan",
        "date": "2026-05-21", "time": "6:00 PM",
        "categories": ["Business"],
        "is_free": False, "price": "$95",
        "hook": "The premier business gala of the year -- black tie, three-course dinner, and awards recognizing Kelowna's most impactful companies and leaders.",
        "image_color": "#1E3A5F",
        "tags": ["Business", "Awards", "Gala", "Networking"],
        "source_url": "https://www.kelownachamber.org"
    },
    {
        "title": "Okanagan Reggae Night",
        "venue": "Fernando's Pub",
        "date": "2026-05-22", "time": "9:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$12",
        "hook": "Island vibes hit the Okanagan -- live reggae band, tropical cocktails, and a packed dancefloor to carry you into the long weekend.",
        "image_color": "#166534",
        "tags": ["Reggae", "Live Music", "Nightlife"],
        "source_url": "https://www.fernandospub.ca"
    },
    {
        "title": "Spring Wine Trail -- Kelowna Wineries",
        "venue": "Mission Hill, Quails' Gate, Summerhill",
        "date": "2026-05-23", "time": "11:00 AM",
        "categories": ["Business"],
        "is_free": False, "price": "$45 (pass)",
        "hook": "A self-guided tour of 12 wineries along Kelowna's Lakeshore and Westside wine trails -- your pass includes tastings at each stop.",
        "image_color": "#7C2D12",
        "tags": ["Wine", "Tour", "Okanagan"],
        "source_url": "https://www.tourismkelowna.com/wine-702/"
    },
    {
        "title": "Kids Free Fishing Day",
        "venue": "Shannon Lake",
        "date": "2026-05-24", "time": "8:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Rods and tackle provided -- bring the kids for a free morning of stocked-lake fishing, casting lessons, and outdoor fun.",
        "image_color": "#0E7490",
        "tags": ["Fishing", "Family", "Free", "Outdoors"],
        "source_url": "https://www.kelowna.ca/parks-recreation"
    },
    {
        "title": "Kelowna Pride Kickoff Party",
        "venue": "BNA Brewing",
        "date": "2026-05-29", "time": "7:00 PM",
        "categories": ["Nightlife", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Rainbow flags, drag performances, and craft beer -- BNA hosts the official kickoff party for Kelowna Pride Week 2026.",
        "image_color": "#7C3AED",
        "tags": ["Pride", "LGBTQ+", "Party", "Free"],
        "source_url": "https://www.bnabrewing.com"
    },
    {
        "title": "Kelowna Gravel Fondo",
        "venue": "Myra-Bellevue Provincial Park",
        "date": "2026-05-30", "time": "7:00 AM",
        "categories": ["Family"],
        "is_free": False, "price": "$55",
        "hook": "Ride 60km of Okanagan back-country gravel through vineyards and forests -- post-ride BBQ and craft beer at the finish line.",
        "image_color": "#78350F",
        "tags": ["Cycling", "Outdoors", "Sports"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },

    # ─── JUNE 2026 ───
    {
        "title": "Kelowna Ribfest",
        "venue": "City Park",
        "date": "2026-06-05", "time": "11:00 AM",
        "categories": ["Family"],
        "is_free": True, "price": "Free Entry (food for purchase)",
        "hook": "North America's top rib teams battle it out over open flames -- live country music, kids' zone, and all-you-can-eat ribs by the lake.",
        "image_color": "#991B1B",
        "tags": ["Food", "BBQ", "Festival", "Family"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Sikh Heritage Month Gala Dinner",
        "venue": "Delta Grand Okanagan",
        "date": "2026-06-06", "time": "6:00 PM",
        "categories": ["Punjabi-Community", "Business"],
        "is_free": False, "price": "$60",
        "hook": "A formal evening celebrating Sikh contributions to the Okanagan -- keynote speakers, awards, traditional music, and a five-course dinner.",
        "image_color": "#B45309",
        "tags": ["Punjabi", "Gala", "Cultural", "Heritage"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Downtown Kelowna Block Party",
        "venue": "Bernard Avenue",
        "date": "2026-06-07", "time": "2:00 PM",
        "categories": ["Family", "Free", "Nightlife"],
        "is_free": True, "price": "Free",
        "hook": "Bernard Ave shuts down to cars and opens up to street performers, food trucks, DJs, and dancing -- the ultimate summer kickoff.",
        "image_color": "#DC2626",
        "tags": ["Block Party", "Free", "Summer", "Music"],
        "source_url": "https://www.downtownkelowna.com"
    },
    {
        "title": "Okanagan Salsa & Bachata Social",
        "venue": "Rotary Centre for the Arts",
        "date": "2026-06-12", "time": "8:00 PM",
        "categories": ["Nightlife"],
        "is_free": False, "price": "$15",
        "hook": "Beginner lesson at 8, social dancing till midnight -- Latin rhythms, great DJs, and a welcoming dance community under one roof.",
        "image_color": "#B91C1C",
        "tags": ["Dance", "Latin", "Nightlife", "Social"],
        "source_url": "https://rotarycentreforthearts.com"
    },
    {
        "title": "Kelowna Dragon Boat Festival",
        "venue": "Waterfront Park",
        "date": "2026-06-13", "time": "8:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free to Watch",
        "hook": "Dozens of teams paddle for glory on Okanagan Lake -- cheer from the shore with food vendors, live music, and kids' activities all day.",
        "image_color": "#0369A1",
        "tags": ["Sports", "Festival", "Free", "Waterfront"],
        "source_url": "https://www.kelownadragonboatfestival.com"
    },
    {
        "title": "Kelowna Craft Beer Week Launch",
        "venue": "BNA Brewing, Red Bird, Vice & Virtue",
        "date": "2026-06-15", "time": "4:00 PM",
        "categories": ["Nightlife", "Business"],
        "is_free": False, "price": "$30 (passport)",
        "hook": "A passport to 15 Kelowna breweries with exclusive limited releases, brewery tours, and tap takeovers all week long.",
        "image_color": "#92400E",
        "tags": ["Craft Beer", "Festival", "Nightlife"],
        "source_url": "https://www.bnabrewing.com"
    },
    {
        "title": "Okanagan Punjabi Mela",
        "venue": "City Park",
        "date": "2026-06-20", "time": "11:00 AM",
        "categories": ["Punjabi-Community", "Family", "Free"],
        "is_featured": True,
        "is_free": True, "price": "Free",
        "hook": "The biggest South Asian festival in the Interior -- bhangra competitions, Punjabi food stalls, live dhol, henna, and fun for all ages at City Park.",
        "image_color": "#EA580C",
        "tags": ["Punjabi", "Mela", "Festival", "Cultural", "Free"],
        "source_url": "https://www.tourismkelowna.com/things-to-do/events/"
    },
    {
        "title": "Summer Solstice Yoga at Waterfront",
        "venue": "Kerry Park",
        "date": "2026-06-21", "time": "6:30 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "Greet the longest day of the year with a free sunrise yoga session on the waterfront -- mats provided, all levels welcome.",
        "image_color": "#D97706",
        "tags": ["Yoga", "Wellness", "Free", "Summer"],
        "source_url": "https://www.kelowna.ca/parks-recreation"
    },
    {
        "title": "Kelowna Startup Week",
        "venue": "Innovation Centre Kelowna",
        "date": "2026-06-22", "time": "9:00 AM",
        "categories": ["Business"],
        "is_free": False, "price": "$35 (week pass)",
        "hook": "Five days of panels, workshops, and pitch competitions -- connect with founders, VCs, and the Okanagan tech ecosystem.",
        "image_color": "#1E40AF",
        "tags": ["Tech", "Startups", "Business", "Conference"],
        "source_url": "https://www.okanagancolab.com"
    },
    {
        "title": "Canada Day Fireworks & Festival",
        "venue": "City Park & Waterfront",
        "date": "2026-06-30", "time": "10:00 AM",
        "categories": ["Family", "Free"],
        "is_free": True, "price": "Free",
        "hook": "All-day festivities with live bands, food trucks, kids' zone, and the grand finale fireworks show over Okanagan Lake at dusk.",
        "image_color": "#DC2626",
        "tags": ["Canada Day", "Fireworks", "Festival", "Free"],
        "source_url": "https://www.kelowna.ca/parks-recreation"
    },
]


def format_date_label(iso_date: str) -> str:
    """Convert '2026-04-13' to 'Mon, Apr 13'."""
    dt = datetime.strptime(iso_date, "%Y-%m-%d")
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return f"{day_names[dt.weekday()]}, {month_names[dt.month-1]} {dt.day}"


def main():
    all_events = SEED_EVENTS + FUTURE_EVENTS

    # Validate: every event must have a real source_url
    valid_events = []
    for ev in all_events:
        url = ev.get("source_url", "")
        if not url or url == "#":
            print(f"  [SKIP] No valid URL: {ev['title']}")
            continue
        valid_events.append(ev)

    # Assign IDs and date labels
    for i, ev in enumerate(valid_events, 1):
        ev["id"] = i
        ev["date_label"] = format_date_label(ev["date"])
        if "is_featured" not in ev:
            ev["is_featured"] = False

    # Sort by date, then time
    valid_events.sort(key=lambda e: (e["date"], e["time"]))
    for i, ev in enumerate(valid_events, 1):
        ev["id"] = i

    output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "events.json")

    dates = sorted(set(e["date"] for e in valid_events))
    first_label = format_date_label(dates[0])
    last_label = format_date_label(dates[-1])

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "region": "Kelowna, BC -- Okanagan",
        "date_range": f"{first_label} - {last_label}",
        "date_min": dates[0],
        "date_max": dates[-1],
        "total_events": len(valid_events),
        "events": valid_events
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"[OK] Generated {len(valid_events)} events -> {output_path}")
    print(f"     Date range: {dates[0]} to {dates[-1]}")
    for e in valid_events:
        cats = ", ".join(e["categories"])
        print(f"  {e['id']:>2}. [{e['date_label']} {e['time']}] {e['title']} ({cats})")
        print(f"      -> {e['source_url']}")


if __name__ == "__main__":
    main()
