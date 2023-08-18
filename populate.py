from pymongo import MongoClient
from bs4 import BeautifulSoup

# MongoDB Connection
password = "admin123"  # replace this with the actual password
client = MongoClient(f"mongodb+srv://admin123:{password}@iiith-silverjubliee.a497uaa.mongodb.net/?retryWrites=true&w=majority")
db = client["iiith_events"]
collection = db["schedule"]

# Given HTML
html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Events Schedule</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .container {
            display: flex;
            justify-content: space-around;
            padding: 20px;
            flex-wrap: wrap;
            margin: 0 auto;
            max-width: 1200px;
        }

        .day {
            width: 100%;
            border: 1px solid #ddd;
            padding: 15px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            background-color: #fff;
        }

        h1 {
            color: #444;
            text-align: center;
        }

        h2 {
            color: #555;
            border-bottom: 2px solid #f2f2f2;
            padding-bottom: 5px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            padding: 10px;
            text-align: left;
        }

        tr:nth-child(even) {
            background-color: #f6f6f6;
        }

        tr:hover {
            background-color: #f0f0f0;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        th {
            background-color: #001cf2;
            color: white;
        }

        /* Tablet view */
        @media screen and (min-width: 600px) {
            .day {
                width: 48%; /* slightly less than 50% to account for potential margins and padding */
            }
        }

        /* Desktop view */
        @media screen and (min-width: 992px) {
            .day {
                width: 30%;
            }
        }
    </style>
</head>

<body>
    <!-- ... rest of your HTML ... -->
</body>

</html>

</head>

<body>
    <h1>Event Schedule </h1>
    <div class="container">
        <!-- Sept 1 -->
        <div class="day">
            <h2>SEPT 1 - PROF RAJ REDDY DAY</h2>
            <table>
                <tr>
                    <th>Time</th>
                    <th>Events</th>
                </tr>
                <tr>
                    <td>3:00 PM to 5:00 PM</td>
                    <td>Alumni Registration</td>
                </tr>
                <tr>
                    <td>4:00 PM to 5:00 PM</td>
                    <td>HI TEA @ Block D</td>
                </tr>
                <tr>
                    <td>5:00 PM to 6:00 PM</td>
                    <td>Unveil the Art installation: The One near Thub and Humble Entry</td>
                </tr>
                <tr>
                    <td>5:00 PM to 6:00 PM</td>
                    <td>GC meeting (GC proceeds to venue after Unveiling)</td>
                </tr>
                <tr>
                    <td></td>
                    <td>IIITH 25 special performance by Dance Crew club</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Announce Winners of Creatives Contest</td>
                </tr>
                <tr>
                    <td>6:00 pm to 8:00 pm</td>
                    <td>Networking & Cultural Events</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Faculty, students & alum- mingle</td>
                </tr>
                <tr>
                    <td></td>
                    <td>1. Saakshatkaar- Realization of the timeless knowledge by Dr Saroja and Mr Jaychandran (6.00
                        pm-7.30 pm)</td>
                </tr>
                <tr>
                    <td></td>
                    <td>2. Amrit Dhara Music Concert by Mr. Devi Prasad (7.30 pm-8 pm)</td>
                </tr>
                <tr>
                    <td></td>
                    <td>3. Students event</td>
                </tr>
                <tr>
                    <td>8:00 PM to 10:00 PM</td>
                    <td>DINNER</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Gala Dinner - RR Honor</td>
                </tr>
                <tr>
                    <td>8:00 PM to 10:00 PM</td>
                    <td>FUN AFTER</td>
                </tr>
                <tr>
                    <td></td>
                    <td>DJ Night</td>
                </tr>
            </table>
        </div>
        <!-- Sept 2 -->
        <div class="day">
            <h2>SEPT 2 - FOUNDATION DAY</h2>
            <table>
                <tr>
                    <th>Time</th>
                    <th>Events</th>
                </tr>
                <tr>
                    <td>10:30 AM am to 1:00 pm</td>
                    <td>Curated Demo videos in exhibition halls (unmanned walk around @ exhibition hall)</td>
                </tr>
                <tr>
                    <td>11:30 AM to 12:30 pm</td>
                    <td>Students and Alumni Interactions - Career Guidance</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Reflections of RR Video Screening in Exhibition Hall</td>
                </tr>
                <tr>
                    <td>1:00 PM to 1:30 PM</td>
                    <td>Unveil the Hall of fame: Star & Digi WALL - 10 mins</td>
                </tr>
                <tr>
                    <td>1:30 PM to 2:30 PM</td>
                    <td>Grand Lunch</td>
                </tr>
                <tr>
                    <td>2:30 PM to 4:00 PM</td>
                    <td>HELLO ALUM</td>
                </tr>
                <tr>
                    <td>2:30 to 3:00 PM</td>
                    <td>Alum panel (seniors from corp) Theme: 'AI for Society') - 30 mins</td>
                </tr>
                <tr>
                    <td>3:00 to 3:30 PM</td>
                    <td>Alum panel (seniors from Academia) Theme: 'Vision for 2050') - 30 mins</td>
                </tr>
                <tr>
                    <td>3:30 to 3:45 PM</td>
                    <td>Unviel TimeCapsule - IIIT Next 25 yrs (Video of The 2018 box) & create capsule for next 10 years
                        - 15 mins</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Ramesh version of Low tea</td>
                </tr>
                <tr>
                    <td>4:00 PM to 6:00 PM</td>
                    <td>Next 25</td>
                </tr>
                <tr>
                    <td>4 to 4:30</td>
                    <td>Talks: PJN Address (past 25); board member talk (next 25), Prof Raj Reddy - 30 mins</td>
                </tr>
                <tr>
                    <td>4:30 to 4:45</td>
                    <td>Keynotes: Satya Nadella Address and others video messages - 15 mins</td>
                </tr>
                <tr>
                    <td>4:45 to 5:30</td>
                    <td>Prof Raj Reddy Foundation Day Lecture Series - First talk by Prof Vint Cerf - 30 mins+15 mins
                    </td>
                </tr>
                <tr>
                    <td>5:30 to 5:40</td>
                    <td>Formal Recognitions</td>
                </tr>
                <tr>
                    <td>5:40 to 5:50</td>
                    <td>Address By New Chairman</td>
                </tr>
                <tr>
                    <td></td>
                    <td>RR Reflections Video</td>
                </tr>
                <tr>
                    <td>5:50 to 6:00</td>
                    <td>Thanks Giving: PJN interacts with senior leaders in the room (Open Mic)</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Play new facilities video as backdrop in conclusion</td>
                </tr>
                <tr>
                    <td>6:00 to 6:30 pm</td>
                    <td>HI TEA @ Cultural events Venue</td>
                </tr>
                <tr>
                    <td>6:30 to 8:00 pm</td>
                    <td>Launch of IIITH anthem/Movie by Music/Decore club - 15 mins</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Cultural Program - Falak Chayya & Alumni Band - 90 mins</td>
                </tr>
            </table>
        </div>
        <!-- Sept 3 -->
        <div class="day">
            <h2>SEPT 3 - ALUM <br>DAY</h2>
            <table>
                <tr>
                    <th>Time</th>
                    <th>Events</th>
                </tr>
                <tr>
                    <td>10:30 to 11:30 AM</td>
                    <td>Mock class by Prof. Kaul</td>
                </tr>
                <tr>
                    <td>11:30 to 12:30</td>
                    <td>Fireside chat: alum civil service officers/ /w Jayesh Ranjan</td>
                </tr>
                <tr>
                    <td>12:30 to 1:00 PM</td>
                    <td>1. Announce/Create IIITH Alumni Association India Chapter/batch reps for each batch</td>
                </tr>
                <tr>
                    <td></td>
                    <td>2. Alumni Felicitation</td>
                </tr>
                <tr>
                    <td>1:00 PM to 2:00 PM</td>
                    <td>LUNCH</td>
                </tr>
                <tr>
                    <td></td>
                    <td>Student Club Events</td>
                </tr>
                <tr>
                    <td>10:00 AM to 1:00 PM</td>
                    <td>Resin Art Workshop Session 1</td>
                </tr>
                <tr>
                    <td>10:00 AM to 12:00 PM</td>
                    <td>Minecraft Build Battle</td>
                </tr>
                <tr>
                    <td>2:00 PM to 5:00 PM</td>
                    <td>Resin Art Workshop Session 2</td>
                </tr>
                <tr>
                    <td>2:00 PM to 4:00 PM</td>
                    <td>Minecraft BedWars Competition</td>
                </tr>
                <tr>
                    <td>4:00 PM to 6:00 PM</td>
                    <td>CineDanceCon Dance Event</td>
                </tr>
                <tr>
                    <td>All day</td>
                    <td>Exoplanet Hunt</td>
                </tr>
            </table>
        </div>
    </div>
</body>

</html>
"""

soup = BeautifulSoup(html, 'html.parser')

days = soup.find_all(class_='day')
data = []

for day in days:
    title = day.h2.text
    events = []
    rows = day.table.find_all('tr')[1:]  # Skipping header row
    for row in rows:
        cols = row.find_all('td')
        time = cols[0].text if cols else ''
        description = cols[1].text if len(cols) > 1 else ''
        events.append({
            "time": time.strip(),
            "description": description.strip()
        })
    data.append({
        "title": title,
        "events": events
    })

# Insert data into MongoDB
collection.insert_many(data)

print("Data populated into MongoDB successfully!")
