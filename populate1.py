from bs4 import BeautifulSoup
import pymongo

# Your HTML content
html_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Calendar</title>
    <style>
        .calendar {
            border: 3px solid #ccc;
            border-radius: 10px;
            padding: 8px;
            background: #240047;
            display: grid;
            grid-template-rows: repeat(3, auto);
            grid-gap: 0px;
            overflow: hidden;
            max-width: 95%;
            margin: 0 auto;
        }

        .row {
            display: grid;
            grid-gap: 10px;
            align-items: start;
            padding: 5px;
        }

        .row1 {
            grid-template-columns: 1fr repeat(3, minmax(150px, 1fr));
        }

        .row2 {
            grid-template-columns: repeat(6, minmax(150px, 1fr));
        }

        .row3 {
            grid-template-columns: repeat(3, 2fr) repeat(2, 1fr);
        }

        .header {
            padding: 20px;
            color: #fff;
            font-weight: bold;
            border-radius: 5px;
            overflow: hidden;
            text-align: center;
            font-size: 2.5rem;
            font-family: Brush Script MT, Brush Script Std, cursive;
        }

        .event {
            perspective: 1000px;
            height: 150px;
            transition: all 0.3s;
            cursor: pointer;
            overflow: hidden;
        }

        .event-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transform-style: preserve-3d;
            transition: all 0.5s;
        }

        .event-front,
        .event-back {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 10px;
            backface-visibility: hidden;
            display: grid;
            grid-template-rows: auto 1fr;
            align-items: center;
        }

        .event-front {
            background: #79cbc5;
            color: #fff;
        }

        .event:nth-child(even) .event-front {
            background: #7374b7;
            color: #fff;
        }

        .event.today .event-front {
            background: #09e178;
            color: #fff;
        }

        .event.main-event .event-front {
            background: #b97b36;
            color: #fff;
        }

        .event-back {
            transform: rotateY(180deg);
            background: #f4f4f4;
            color: #000;
            text-align: center;
            display: flex;
            justify-content: center;
            padding: 0px;
            font-size: 1rem;
            border-radius: 10px;
        }

        .event:hover .event-inner {
            transform: rotateY(180deg);
        }

        .date-container {
            display: flex;
            align-items: center;
            padding: 15px;
        }

        .month {
            writing-mode: vertical-rl;
            text-align: center;
            font-weight: bold;
            transform: rotate(180deg);
            line-height: 1.2;
        }

        .date {
            font-size: 2.2rem;
            font-weight: bold;
            margin-left: 5px;
        }

        .description {
            text-align: center;
            font-size: 1 rem;
            overflow-wrap: break-word;
            padding: 5px;
            font-weight: bold;
        }

        .description a {
            color: inherit;
            text-decoration: none;
        }

        @media screen and (max-width: 768px) {
            .calendar {
                grid-template-columns: repeat(1, 1fr);
            }

            .row {
                grid-template-columns: repeat(1, 1fr);
            }

            .header {
                font-size: 2rem;
            }

            .event {
                margin-bottom: 0px;
            }
        }
    </style>
</head>

<body>
    <div class="calendar">
        <div class="row row1">
            <div class="header">Silver Jubilee<p style="font-size: 1.2rem; font-family:Georgia, serif;"> EVENTS CALENDAR
                </p>
            </div> <!-- Event 1 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-09">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">09</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=GEN+AI+SUMMIT&dates=20230809/20230809"
                                target="_blank">GEN AI SUMMIT</a></div>
                    </div>
                    <div class="event-back">in collaboration with Telangana Goverment</div>
                </div>
            </div>
            <!-- Event 2 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-12">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">12</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=THE+OTHER+KOHINOORS&dates=20230812/20230812"
                                target="_blank">THE OTHER KOHINOORS</a></div>
                    </div>
                    <div class="event-back">Movie Screening and interaction With Director</div>
                </div>
            </div>
            <!-- Event 3 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-13">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">13</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=JOYODHONI&dates=20230813/20230813"
                                target="_blank">JOYODHONI</a></div>
                    </div>
                    <div class="event-back">an entertaining evening of music, dance, poetry and art</div>
                </div>
            </div>
        </div>
        <div class="row row2">
            <!-- Event 4 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-14">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">14</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=JEE+JAISII+AAPKI+MARZI&dates=20230814/20230814"
                                target="_blank">JEE JAISII AAPKI MARZI</a></div>
                    </div>
                    <div class="event-back">a theatre play by
                        Aakanksha Sansthan
                        Jodhpur</div>
                </div>
            </div>
            <!-- Event 5 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-17">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">17</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=DISTINGUISHED+LECTURE&dates=20230817/20230817"
                                target="_blank">DISTINGUISHED LECTURE</a></div>
                    </div>
                    <div class="event-back">by Mr. V K Saraswat</div>
                </div>
            </div>
            <!-- Event 6 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-19">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">19</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=FALLING+WALLS&dates=20230819/20230819"
                                target="_blank">FALLING WALLS</a></div>
                    </div>
                    <div class="event-back">3-minute science idea pitch competition</div>
                </div>
            </div>
            <!-- Event 7 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-21">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">21</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=YC@CIE15&dates=20230821/20230821"
                                target="_blank">YC@CIE15</a></div>
                    </div>
                    <div class="event-back">Celebrating IITH alum VC startups</div>
                </div>
            </div>
            <!-- Event 8 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-23">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">23</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=FIRESIDE+CHAT+with+Sri+N+Chandrababu+Naidu&dates=20230823/20230823"
                                target="_blank">FIRESIDE CHAT</a></div>
                    </div>
                    <div class="event-back">with
                        Sri N Chandrababu
                        Naidu</div>
                </div>
            </div>
            <!-- Event 9 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-08-31">
                        <div class="date-container">
                            <div class="month">AUG</div>
                            <div class="date">31</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=MICROSOFT+DAY@IITH+Celebrating+25+years+of+research+partnership&dates=20230831/20230831"
                                target="_blank">MICROSOFT DAY@IITH </a></div>
                    </div>
                    <div class="event-back">Celebrating 25 years of research partnership</div>
                </div>
            </div>
        </div>
        <div class="row row3">
            <!-- Event 10 -->
            <div class="event main-event">
                <div class="event-inner">
                    <div class="event-front" id="2023-09-01">
                        <div class="date-container">
                            <div class="month">SEP</div>
                            <div class="date">01</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=CELEBRATING+PROF+RAJ+REDDY&dates=20230901/20230901"
                                target="_blank">CELEBRATING PROF RAJ REDDY</a></div>
                    </div>
                    <div class="event-back">CELEBRATING PROF RAJ REDDY</div>
                </div>
            </div>
            <!-- Event 11 -->
            <div class="event main-event">
                <div class="event-inner">
                    <div class="event-front" id="2023-09-02">
                        <div class="date-container">
                            <div class="month">SEP</div>
                            <div class="date">02</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=lITH+FOUNDATION+DAY+CELEBRATIONS&dates=20230902/20230902"
                                target="_blank">IIITH FOUNDATION DAY CELEBRATIONS</a></div>
                    </div>
                    <div class="event-back">Prof Raj Reddy Lecture series' talk
                        Policy roundtable
                        Launch of Wall of fame</div>
                </div>
            </div>
            <!-- Event 12 -->
            <div class="event main-event">
                <div class="event-inner">
                    <div class="event-front" id="2023-09-03">
                        <div class="date-container">
                            <div class="month">SEP</div>
                            <div class="date">03</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=ALUMNI+DAY&dates=20230903/20230903"
                                target="_blank">ALUMNI DAY</a></div>
                    </div>
                    <div class="event-back">Fireside chat with IIITH alumni
                        civil service officers and Mr Jayesh Ranjan;
                        alumni awards: fun events</div>
                </div>
            </div>
            <!-- Event 13 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-09-22">
                        <div class="date-container">
                            <div class="month">SEP</div>
                            <div class="date">22</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=QUALCOMM+DAY&dates=20230922/20230922"
                                target="_blank">QUALCOMM DAY</a></div>
                    </div>
                    <div class="event-back">Celebrating research and technology collaboration</div>
                </div>
            </div>
            <!-- Event 14 -->
            <div class="event">
                <div class="event-inner">
                    <div class="event-front" id="2023-09-30">
                        <div class="date-container">
                            <div class="month">SEP</div>
                            <div class="date">30</div>
                        </div>
                        <div class="description"><a
                                href="https://www.google.com/calendar/render?action=TEMPLATE&text=CINEMA+WORKSHOP&dates=20230930/20230930"
                                target="_blank">CINEMA WORKSHOP</a></div>
                    </div>
                    <div class="event-back">CINEMA WORKSHOP</div>
                </div>
            </div>
        </div>
    </div>
    <script>
        // Check today's date and add 'today' class if it matches an event date
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
        var yyyy = today.getFullYear();

        var todayId = yyyy + '-' + mm + '-' + dd;

        var eventElement = document.getElementById(todayId);
        if (eventElement) {
            eventElement.classList.add('today');
        }
    </script>
</body>

</html>'''

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all event elements
event_elements = soup.select(".event .event-front")

events_data = []
for event in event_elements:
    event_data = {
        "id": event["id"],
        "month": event.select_one(".month").text.strip(),
        "date": event.select_one(".date").text.strip(),
        "description": event.select_one(".description a").text.strip(),
        "link": event.select_one(".description a")["href"].strip(),
        "event_back": event.find_next_sibling(class_="event-back").text.strip()
    }
    events_data.append(event_data)

# MongoDB connection string
connection_string = "mongodb+srv://admin123:admin123@iiith-silverjubliee.a497uaa.mongodb.net/?retryWrites=true&w=majority"

# Connect to the MongoDB server
client = pymongo.MongoClient(connection_string)
db = client["event_calendar_db"]  # Create or use an existing database named "event_calendar_db"
events_collection = db["events"]  # Create or use an existing collection named "events"

# Insert the events data into the MongoDB collection
events_collection.insert_many(events_data)

print("Events data populated in MongoDB!")
