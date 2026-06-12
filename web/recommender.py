import math

# ── Full datasets ─────────────────────────────────────────────────────────────

MOVIES = [
  { "id":1,  "title":"The Dark Knight",                   "tags":["Action","Crime","Drama"],          "year":2008, "emoji":"🦇", "subtitle":"Christopher Nolan",         "image":"" },
  { "id":2,  "title":"Inception",                         "tags":["Action","Sci-Fi","Thriller"],      "year":2010, "emoji":"🌀", "subtitle":"Christopher Nolan",         "image":"" },
  { "id":3,  "title":"The Godfather",                     "tags":["Crime","Drama","Classic"],         "year":1972, "emoji":"🤌", "subtitle":"Francis Ford Coppola",      "image":"" },
  { "id":4,  "title":"Pulp Fiction",                      "tags":["Crime","Drama","Thriller"],        "year":1994, "emoji":"💼", "subtitle":"Quentin Tarantino",         "image":"" },
  { "id":5,  "title":"Interstellar",                      "tags":["Sci-Fi","Drama","Adventure"],      "year":2014, "emoji":"🚀", "subtitle":"Christopher Nolan",         "image":"" },
  { "id":6,  "title":"The Matrix",                        "tags":["Sci-Fi","Action","Thriller"],      "year":1999, "emoji":"💊", "subtitle":"The Wachowskis",            "image":"" },
  { "id":7,  "title":"Goodfellas",                        "tags":["Crime","Drama","Biography"],       "year":1990, "emoji":"🔫", "subtitle":"Martin Scorsese",           "image":"" },
  { "id":8,  "title":"Parasite",                          "tags":["Thriller","Drama","Comedy"],       "year":2019, "emoji":"🏠", "subtitle":"Bong Joon-ho",              "image":"" },
  { "id":9,  "title":"Avengers: Endgame",                 "tags":["Action","Sci-Fi","Adventure"],     "year":2019, "emoji":"⚡", "subtitle":"Russo Brothers",            "image":"" },
  { "id":10, "title":"The Grand Budapest Hotel",          "tags":["Comedy","Drama","Adventure"],      "year":2014, "emoji":"🏨", "subtitle":"Wes Anderson",              "image":"" },
  { "id":11, "title":"La La Land",                        "tags":["Drama","Romance","Musical"],       "year":2016, "emoji":"🎵", "subtitle":"Damien Chazelle",           "image":"" },
  { "id":12, "title":"Mad Max: Fury Road",                "tags":["Action","Adventure","Sci-Fi"],     "year":2015, "emoji":"🔥", "subtitle":"George Miller",             "image":"" },
  { "id":13, "title":"Forrest Gump",                      "tags":["Drama","Romance","Comedy"],        "year":1994, "emoji":"🏃", "subtitle":"Robert Zemeckis",           "image":"" },
  { "id":14, "title":"Get Out",                           "tags":["Horror","Thriller","Mystery"],     "year":2017, "emoji":"😨", "subtitle":"Jordan Peele",              "image":"" },
  { "id":15, "title":"Whiplash",                          "tags":["Drama","Music"],                   "year":2014, "emoji":"🥁", "subtitle":"Damien Chazelle",           "image":"" },
  { "id":16, "title":"The Shawshank Redemption",          "tags":["Drama","Crime","Classic"],         "year":1994, "emoji":"🔓", "subtitle":"Frank Darabont",            "image":"" },
  { "id":17, "title":"Spirited Away",                     "tags":["Animation","Fantasy","Adventure"], "year":2001, "emoji":"🐉", "subtitle":"Hayao Miyazaki",            "image":"" },
  { "id":18, "title":"No Country for Old Men",            "tags":["Crime","Drama","Thriller"],        "year":2007, "emoji":"🪙", "subtitle":"Coen Brothers",             "image":"" },
  { "id":19, "title":"Her",                               "tags":["Sci-Fi","Drama","Romance"],        "year":2013, "emoji":"🤖", "subtitle":"Spike Jonze",               "image":"" },
  { "id":20, "title":"The Social Network",                "tags":["Drama","Biography"],               "year":2010, "emoji":"💻", "subtitle":"David Fincher",             "image":"" },
  { "id":21, "title":"Dune",                              "tags":["Sci-Fi","Adventure","Drama"],      "year":2021, "emoji":"🏜️", "subtitle":"Denis Villeneuve",           "image":"" },
  { "id":22, "title":"Everything Everywhere All at Once", "tags":["Sci-Fi","Comedy","Drama"],         "year":2022, "emoji":"🥟", "subtitle":"Daniels",                   "image":"" },
  { "id":23, "title":"The Silence of the Lambs",          "tags":["Thriller","Crime","Horror"],       "year":1991, "emoji":"🦋", "subtitle":"Jonathan Demme",            "image":"" },
  { "id":24, "title":"Schindler's List",                  "tags":["Drama","Biography","History"],     "year":1993, "emoji":"🕯️", "subtitle":"Steven Spielberg",           "image":"" },
  { "id":25, "title":"Blade Runner 2049",                 "tags":["Sci-Fi","Drama","Mystery"],        "year":2017, "emoji":"🌆", "subtitle":"Denis Villeneuve",           "image":"" },
  { "id":26, "title":"Fight Club",                        "tags":["Drama","Thriller","Mystery"],      "year":1999, "emoji":"🥊", "subtitle":"David Fincher",             "image":"" },
  { "id":27, "title":"The Lion King",                     "tags":["Animation","Adventure","Musical"], "year":1994, "emoji":"🦁", "subtitle":"Disney",                    "image":"" },
  { "id":28, "title":"Titanic",                           "tags":["Romance","Drama","History"],       "year":1997, "emoji":"🚢", "subtitle":"James Cameron",             "image":"" },
  { "id":29, "title":"Avatar",                            "tags":["Sci-Fi","Adventure","Action"],     "year":2009, "emoji":"💙", "subtitle":"James Cameron",             "image":"" },
  { "id":30, "title":"Black Panther",                     "tags":["Action","Sci-Fi","Adventure"],     "year":2018, "emoji":"🐾", "subtitle":"Ryan Coogler",              "image":"" },
  { "id":31, "title":"Coco",                              "tags":["Animation","Adventure","Musical"], "year":2017, "emoji":"💀", "subtitle":"Pixar",                     "image":"" },
  { "id":32, "title":"A Beautiful Mind",                  "tags":["Drama","Biography","Mystery"],     "year":2001, "emoji":"🧩", "subtitle":"Ron Howard",                "image":"" },
  { "id":33, "title":"The Departed",                      "tags":["Crime","Drama","Thriller"],        "year":2006, "emoji":"🔐", "subtitle":"Martin Scorsese",           "image":"" },
  { "id":34, "title":"Oppenheimer",                       "tags":["Drama","Biography","History"],     "year":2023, "emoji":"☢️", "subtitle":"Christopher Nolan",         "image":"" },
  { "id":35, "title":"Barbie",                            "tags":["Comedy","Fantasy","Adventure"],    "year":2023, "emoji":"👱", "subtitle":"Greta Gerwig",              "image":"" },
  { "id":36, "title":"Top Gun: Maverick",                 "tags":["Action","Drama","Adventure"],      "year":2022, "emoji":"✈️", "subtitle":"Joseph Kosinski",            "image":"" },
  { "id":37, "title":"The Revenant",                      "tags":["Adventure","Drama","Thriller"],    "year":2015, "emoji":"🐻", "subtitle":"Alejandro G. Iñárritu",      "image":"" },
  { "id":38, "title":"12 Angry Men",                      "tags":["Drama","Crime","Classic"],         "year":1957, "emoji":"⚖️", "subtitle":"Sidney Lumet",              "image":"" },
  { "id":39, "title":"Princess Mononoke",                 "tags":["Animation","Fantasy","Adventure"], "year":1997, "emoji":"🌲", "subtitle":"Hayao Miyazaki",            "image":"" },
  { "id":40, "title":"Eternal Sunshine of the Spotless Mind", "tags":["Romance","Sci-Fi","Drama"],   "year":2004, "emoji":"☀️", "subtitle":"Michel Gondry",             "image":"" },
  { "id":41, "title":"The Truman Show",                   "tags":["Drama","Comedy","Sci-Fi"],         "year":1998, "emoji":"📺", "subtitle":"Peter Weir",                "image":"" },
  { "id":42, "title":"Gladiator",                         "tags":["Action","Drama","History"],        "year":2000, "emoji":"🗡️", "subtitle":"Ridley Scott",               "image":"" },
  { "id":43, "title":"Joker",                             "tags":["Crime","Drama","Thriller"],        "year":2019, "emoji":"🃏", "subtitle":"Todd Phillips",             "image":"" },
  { "id":44, "title":"Us",                                "tags":["Horror","Thriller","Mystery"],     "year":2019, "emoji":"✂️", "subtitle":"Jordan Peele",              "image":"" },
  { "id":45, "title":"Knives Out",                        "tags":["Mystery","Comedy","Thriller"],     "year":2019, "emoji":"🔪", "subtitle":"Rian Johnson",              "image":"" },
  { "id":46, "title":"1917",                              "tags":["Drama","History","Action"],        "year":2019, "emoji":"🪖", "subtitle":"Sam Mendes",                "image":"" },
  { "id":47, "title":"The Wolf of Wall Street",           "tags":["Biography","Crime","Comedy"],      "year":2013, "emoji":"💰", "subtitle":"Martin Scorsese",           "image":"" },
  { "id":48, "title":"Hereditary",                        "tags":["Horror","Drama","Mystery"],        "year":2018, "emoji":"👁️", "subtitle":"Ari Aster",                  "image":"" },
  { "id":49, "title":"Midsommar",                         "tags":["Horror","Mystery","Drama"],        "year":2019, "emoji":"🌸", "subtitle":"Ari Aster",                 "image":"" },
  { "id":50, "title":"Arrival",                           "tags":["Sci-Fi","Drama","Mystery"],        "year":2016, "emoji":"🛸", "subtitle":"Denis Villeneuve",           "image":"" },
  { "id":51, "title":"The Prestige",                      "tags":["Drama","Mystery","Thriller"],      "year":2006, "emoji":"🎩", "subtitle":"Christopher Nolan",         "image":"" },
  { "id":52, "title":"Gone with the Wind",                "tags":["Romance","Drama","History"],       "year":1939, "emoji":"🌪️", "subtitle":"Victor Fleming",             "image":"" },
  { "id":53, "title":"WALL·E",                            "tags":["Animation","Sci-Fi","Romance"],    "year":2008, "emoji":"🤖", "subtitle":"Pixar",                     "image":"" },
  { "id":54, "title":"Amélie",                            "tags":["Romance","Comedy","Drama"],        "year":2001, "emoji":"🎠", "subtitle":"Jean-Pierre Jeunet",        "image":"" },
  { "id":55, "title":"Oldboy",                            "tags":["Mystery","Thriller","Drama"],      "year":2003, "emoji":"🐙", "subtitle":"Park Chan-wook",            "image":"" },
  { "id":56, "title":"The Lighthouse",                    "tags":["Horror","Drama","Mystery"],        "year":2019, "emoji":"⚓", "subtitle":"Robert Eggers",             "image":"" },
  { "id":57, "title":"Moonlight",                         "tags":["Drama","Romance"],                 "year":2016, "emoji":"🌙", "subtitle":"Barry Jenkins",             "image":"" },
  { "id":58, "title":"Birdman",                           "tags":["Drama","Comedy","Mystery"],        "year":2014, "emoji":"🦅", "subtitle":"Alejandro G. Iñárritu",      "image":"" },
]

BOOKS = [
  { "id":1,  "title":"1984",                        "tags":["Dystopian","Sci-Fi","Classic"],        "year":1949, "emoji":"📖", "subtitle":"George Orwell",           "image":"" },
  { "id":2,  "title":"Harry Potter (Series)",       "tags":["Fantasy","Adventure","Classic"],       "year":1997, "emoji":"⚡", "subtitle":"J.K. Rowling",            "image":"" },
  { "id":3,  "title":"Dune",                        "tags":["Sci-Fi","Adventure","Fantasy"],        "year":1965, "emoji":"🏜️", "subtitle":"Frank Herbert",            "image":"" },
  { "id":4,  "title":"The Hitchhiker's Guide",      "tags":["Sci-Fi","Comedy","Adventure"],         "year":1979, "emoji":"🌌", "subtitle":"Douglas Adams",            "image":"" },
  { "id":5,  "title":"Sapiens",                     "tags":["Non-Fiction","History","Science"],     "year":2011, "emoji":"🧠", "subtitle":"Yuval Noah Harari",        "image":"" },
  { "id":6,  "title":"To Kill a Mockingbird",       "tags":["Fiction","Drama","Classic"],           "year":1960, "emoji":"🐦", "subtitle":"Harper Lee",               "image":"" },
  { "id":7,  "title":"The Great Gatsby",            "tags":["Fiction","Romance","Classic"],         "year":1925, "emoji":"🥂", "subtitle":"F. Scott Fitzgerald",      "image":"" },
  { "id":8,  "title":"Pride and Prejudice",         "tags":["Romance","Classic","Fiction"],         "year":1813, "emoji":"💌", "subtitle":"Jane Austen",              "image":"" },
  { "id":9,  "title":"The Alchemist",               "tags":["Adventure","Fiction","Philosophy"],    "year":1988, "emoji":"⚗️", "subtitle":"Paulo Coelho",             "image":"" },
  { "id":10, "title":"Gone Girl",                   "tags":["Mystery","Thriller","Fiction"],        "year":2012, "emoji":"🔍", "subtitle":"Gillian Flynn",            "image":"" },
  { "id":11, "title":"The Hunger Games",            "tags":["Dystopian","Adventure","Sci-Fi"],      "year":2008, "emoji":"🏹", "subtitle":"Suzanne Collins",          "image":"" },
  { "id":12, "title":"A Brief History of Time",     "tags":["Non-Fiction","Science","Physics"],     "year":1988, "emoji":"🪐", "subtitle":"Stephen Hawking",          "image":"" },
  { "id":13, "title":"The Da Vinci Code",           "tags":["Mystery","Thriller","Adventure"],      "year":2003, "emoji":"🗝️", "subtitle":"Dan Brown",                "image":"" },
  { "id":14, "title":"Lord of the Rings",           "tags":["Fantasy","Adventure","Epic"],          "year":1954, "emoji":"💍", "subtitle":"J.R.R. Tolkien",           "image":"" },
  { "id":15, "title":"Crime and Punishment",        "tags":["Classic","Crime","Drama"],             "year":1866, "emoji":"⚖️", "subtitle":"Fyodor Dostoevsky",        "image":"" },
  { "id":16, "title":"Brave New World",             "tags":["Dystopian","Sci-Fi","Classic"],        "year":1932, "emoji":"🧬", "subtitle":"Aldous Huxley",            "image":"" },
  { "id":17, "title":"Atomic Habits",               "tags":["Non-Fiction","Self-Help","Psychology"],"year":2018, "emoji":"⚛️", "subtitle":"James Clear",              "image":"" },
  { "id":18, "title":"The Fault in Our Stars",      "tags":["Romance","Drama","Fiction"],           "year":2012, "emoji":"⭐", "subtitle":"John Green",               "image":"" },
  { "id":19, "title":"Educated",                    "tags":["Biography","Non-Fiction","Drama"],     "year":2018, "emoji":"🎓", "subtitle":"Tara Westover",            "image":"" },
  { "id":20, "title":"Sherlock Holmes",             "tags":["Mystery","Crime","Classic"],           "year":1887, "emoji":"🔎", "subtitle":"Arthur Conan Doyle",       "image":"" },
  { "id":21, "title":"The Name of the Wind",        "tags":["Fantasy","Adventure","Epic"],          "year":2007, "emoji":"🌬️", "subtitle":"Patrick Rothfuss",          "image":"" },
  { "id":22, "title":"Ender's Game",                "tags":["Sci-Fi","Adventure","Classic"],        "year":1985, "emoji":"🎮", "subtitle":"Orson Scott Card",         "image":"" },
  { "id":23, "title":"The Midnight Library",        "tags":["Fiction","Philosophy","Romance"],      "year":2020, "emoji":"📚", "subtitle":"Matt Haig",                "image":"" },
  { "id":24, "title":"Project Hail Mary",           "tags":["Sci-Fi","Adventure","Science"],        "year":2021, "emoji":"🧫", "subtitle":"Andy Weir",                "image":"" },
  { "id":25, "title":"The Martian",                 "tags":["Sci-Fi","Adventure","Comedy"],         "year":2011, "emoji":"👨‍🚀", "subtitle":"Andy Weir",                "image":"" },
  { "id":26, "title":"Normal People",               "tags":["Romance","Drama","Fiction"],           "year":2018, "emoji":"💛", "subtitle":"Sally Rooney",             "image":"" },
  { "id":27, "title":"Circe",                       "tags":["Fantasy","Mythology","Fiction"],       "year":2018, "emoji":"🧙", "subtitle":"Madeline Miller",          "image":"" },
  { "id":28, "title":"The Girl with the Dragon Tattoo", "tags":["Mystery","Thriller","Crime"],      "year":2005, "emoji":"🐉", "subtitle":"Stieg Larsson",            "image":"" },
  { "id":29, "title":"Thinking, Fast and Slow",     "tags":["Non-Fiction","Psychology","Science"],  "year":2011, "emoji":"🧠", "subtitle":"Daniel Kahneman",          "image":"" },
  { "id":30, "title":"The Subtle Art of Not Giving a F*ck", "tags":["Non-Fiction","Self-Help","Philosophy"], "year":2016, "emoji":"🖕", "subtitle":"Mark Manson",    "image":"" },
  { "id":31, "title":"Frankenstein",                "tags":["Classic","Sci-Fi","Horror"],           "year":1818, "emoji":"⚡", "subtitle":"Mary Shelley",             "image":"" },
  { "id":32, "title":"Dracula",                     "tags":["Classic","Horror","Mystery"],          "year":1897, "emoji":"🧛", "subtitle":"Bram Stoker",              "image":"" },
  { "id":33, "title":"The Catcher in the Rye",      "tags":["Classic","Fiction","Drama"],           "year":1951, "emoji":"🧢", "subtitle":"J.D. Salinger",            "image":"" },
  { "id":34, "title":"Of Mice and Men",             "tags":["Classic","Drama","Fiction"],           "year":1937, "emoji":"🐭", "subtitle":"John Steinbeck",           "image":"" },
  { "id":35, "title":"The Handmaid's Tale",         "tags":["Dystopian","Sci-Fi","Drama"],          "year":1985, "emoji":"🔴", "subtitle":"Margaret Atwood",          "image":"" },
  { "id":36, "title":"Foundation",                  "tags":["Sci-Fi","Classic","Epic"],             "year":1951, "emoji":"🌐", "subtitle":"Isaac Asimov",             "image":"" },
  { "id":37, "title":"The Power of Now",            "tags":["Non-Fiction","Philosophy","Self-Help"],"year":1997, "emoji":"🕰️", "subtitle":"Eckhart Tolle",             "image":"" },
  { "id":38, "title":"It Ends with Us",             "tags":["Romance","Drama","Fiction"],           "year":2016, "emoji":"🌸", "subtitle":"Colleen Hoover",           "image":"" },
  { "id":39, "title":"A Court of Thorns and Roses", "tags":["Fantasy","Romance","Adventure"],       "year":2015, "emoji":"🌹", "subtitle":"Sarah J. Maas",            "image":"" },
  { "id":40, "title":"Becoming",                    "tags":["Biography","Non-Fiction","History"],   "year":2018, "emoji":"🌟", "subtitle":"Michelle Obama",           "image":"" },
  { "id":41, "title":"The Body Keeps the Score",    "tags":["Non-Fiction","Psychology","Science"],  "year":2014, "emoji":"🧬", "subtitle":"Bessel van der Kolk",      "image":"" },
  { "id":42, "title":"The Seven Husbands of Evelyn Hugo", "tags":["Romance","Drama","Mystery"],     "year":2017, "emoji":"💄", "subtitle":"Taylor Jenkins Reid",      "image":"" },
  { "id":43, "title":"Where the Crawdads Sing",     "tags":["Mystery","Romance","Drama"],           "year":2018, "emoji":"🦆", "subtitle":"Delia Owens",              "image":"" },
  { "id":44, "title":"Recursion",                   "tags":["Sci-Fi","Thriller","Mystery"],         "year":2019, "emoji":"🔁", "subtitle":"Blake Crouch",             "image":"" },
  { "id":45, "title":"Dark Matter",                 "tags":["Sci-Fi","Thriller","Mystery"],         "year":2016, "emoji":"🌌", "subtitle":"Blake Crouch",             "image":"" },
  { "id":46, "title":"Animal Farm",                 "tags":["Classic","Dystopian","Fiction"],       "year":1945, "emoji":"🐷", "subtitle":"George Orwell",            "image":"" },
  { "id":47, "title":"The Road",                    "tags":["Drama","Dystopian","Adventure"],       "year":2006, "emoji":"🛣️", "subtitle":"Cormac McCarthy",           "image":"" },
  { "id":48, "title":"The Three-Body Problem",      "tags":["Sci-Fi","Mystery","Epic"],             "year":2008, "emoji":"🔭", "subtitle":"Liu Cixin",                "image":"" },
  { "id":49, "title":"Eleanor Oliphant Is Completely Fine", "tags":["Fiction","Drama","Romance"],   "year":2017, "emoji":"🌷", "subtitle":"Gail Honeyman",           "image":"" },
  { "id":50, "title":"Animal Farm",                 "tags":["Classic","Dystopian","Fiction"],       "year":1945, "emoji":"🐷", "subtitle":"George Orwell (alt ed.)", "image":"" },
]

PRODUCTS = [
  { "id":1,  "title":"AirPods Pro",                   "tags":["Electronics","Audio","Wireless"],      "year":2023, "emoji":"🎧", "subtitle":"Apple",              "image":"" },
  { "id":2,  "title":"Running Shoes",                 "tags":["Sports","Footwear","Fitness"],         "year":2023, "emoji":"👟", "subtitle":"Nike / Adidas",      "image":"" },
  { "id":3,  "title":"Coffee Maker",                  "tags":["Kitchen","Appliance","Home"],          "year":2023, "emoji":"☕", "subtitle":"Breville",            "image":"" },
  { "id":4,  "title":"Gaming Chair",                  "tags":["Gaming","Furniture","Home"],           "year":2023, "emoji":"🪑", "subtitle":"Secretlab",           "image":"" },
  { "id":5,  "title":"Yoga Mat",                      "tags":["Sports","Fitness","Wellness"],         "year":2023, "emoji":"🧘", "subtitle":"Lululemon",           "image":"" },
  { "id":6,  "title":"Smart Watch",                   "tags":["Electronics","Fitness","Wearable"],    "year":2023, "emoji":"⌚", "subtitle":"Apple / Samsung",    "image":"" },
  { "id":7,  "title":"Mechanical Keyboard",           "tags":["Electronics","Gaming","Computer"],     "year":2023, "emoji":"⌨️", "subtitle":"Keychron",            "image":"" },
  { "id":8,  "title":"Travel Backpack",               "tags":["Travel","Fashion","Outdoor"],          "year":2023, "emoji":"🎒", "subtitle":"Osprey",              "image":"" },
  { "id":9,  "title":"Electric Kettle",               "tags":["Kitchen","Appliance","Home"],          "year":2023, "emoji":"🫖", "subtitle":"Cuisinart",           "image":"" },
  { "id":10, "title":"Noise-Cancelling Headphones",   "tags":["Electronics","Audio","Travel"],        "year":2023, "emoji":"🎵", "subtitle":"Sony WH-1000XM5",    "image":"" },
  { "id":11, "title":"Standing Desk",                 "tags":["Home","Office","Furniture"],           "year":2023, "emoji":"🖥️", "subtitle":"Flexispot",           "image":"" },
  { "id":12, "title":"Protein Powder",                "tags":["Fitness","Health","Sports"],           "year":2023, "emoji":"💪", "subtitle":"Optimum Nutrition",   "image":"" },
  { "id":13, "title":"Indoor Plant Set",              "tags":["Home","Decor","Wellness"],             "year":2023, "emoji":"🌿", "subtitle":"The Sill",            "image":"" },
  { "id":14, "title":"Cookware Set",                  "tags":["Kitchen","Home","Cooking"],            "year":2023, "emoji":"🍳", "subtitle":"All-Clad",            "image":"" },
  { "id":15, "title":"Wireless Charger",              "tags":["Electronics","Gadget","Wireless"],     "year":2023, "emoji":"🔋", "subtitle":"Anker",               "image":"" },
  { "id":16, "title":"Hiking Boots",                  "tags":["Outdoor","Sports","Footwear"],         "year":2023, "emoji":"🥾", "subtitle":"Salomon",             "image":"" },
  { "id":17, "title":"Air Purifier",                  "tags":["Home","Health","Appliance"],           "year":2023, "emoji":"💨", "subtitle":"Dyson",               "image":"" },
  { "id":18, "title":"Portable Speaker",              "tags":["Electronics","Audio","Outdoor"],       "year":2023, "emoji":"🔊", "subtitle":"JBL Charge 5",        "image":"" },
  { "id":19, "title":"Skincare Set",                  "tags":["Beauty","Wellness","Health"],          "year":2023, "emoji":"✨", "subtitle":"The Ordinary",         "image":"" },
  { "id":20, "title":"E-Reader",                      "tags":["Electronics","Reading","Gadget"],      "year":2023, "emoji":"📱", "subtitle":"Kindle Paperwhite",   "image":"" },
  { "id":21, "title":"4K Monitor",                    "tags":["Electronics","Computer","Office"],     "year":2023, "emoji":"🖥️", "subtitle":"LG UltraWide",        "image":"" },
  { "id":22, "title":"Espresso Machine",              "tags":["Kitchen","Appliance","Cooking"],       "year":2023, "emoji":"☕", "subtitle":"De'Longhi",           "image":"" },
  { "id":23, "title":"Resistance Bands Set",          "tags":["Fitness","Sports","Wellness"],         "year":2023, "emoji":"🏋️", "subtitle":"Fit Simplify",        "image":"" },
  { "id":24, "title":"Gaming Mouse",                  "tags":["Electronics","Gaming","Computer"],     "year":2023, "emoji":"🖱️", "subtitle":"Logitech G Pro",       "image":"" },
  { "id":25, "title":"Sunglasses",                    "tags":["Fashion","Outdoor","Accessories"],     "year":2023, "emoji":"🕶️", "subtitle":"Ray-Ban",              "image":"" },
  { "id":26, "title":"Camping Tent",                  "tags":["Outdoor","Travel","Sports"],           "year":2023, "emoji":"⛺", "subtitle":"REI Co-op",           "image":"" },
  { "id":27, "title":"Blender",                       "tags":["Kitchen","Appliance","Health"],        "year":2023, "emoji":"🥤", "subtitle":"Vitamix",             "image":"" },
  { "id":28, "title":"Desk Lamp",                     "tags":["Office","Home","Decor"],               "year":2023, "emoji":"💡", "subtitle":"BenQ",                "image":"" },
  { "id":29, "title":"Perfume",                       "tags":["Beauty","Fashion","Accessories"],      "year":2023, "emoji":"🌺", "subtitle":"Chanel / YSL",        "image":"" },
  { "id":30, "title":"Smart Home Hub",                "tags":["Electronics","Gadget","Home"],         "year":2023, "emoji":"🏠", "subtitle":"Amazon Echo",         "image":"" },
  { "id":31, "title":"Dumbbell Set",                  "tags":["Fitness","Sports","Home"],             "year":2023, "emoji":"🏋️", "subtitle":"Bowflex",             "image":"" },
  { "id":32, "title":"Winter Jacket",                 "tags":["Fashion","Outdoor","Travel"],          "year":2023, "emoji":"🧥", "subtitle":"Patagonia",           "image":"" },
  { "id":33, "title":"Instant Pot",                   "tags":["Kitchen","Appliance","Cooking"],       "year":2023, "emoji":"🍲", "subtitle":"Instant Pot",         "image":"" },
  { "id":34, "title":"Webcam",                        "tags":["Electronics","Computer","Office"],     "year":2023, "emoji":"📷", "subtitle":"Logitech C920",       "image":"" },
  { "id":35, "title":"Running Headband",              "tags":["Sports","Fitness","Fashion"],          "year":2023, "emoji":"🎽", "subtitle":"Nike",                "image":"" },
  { "id":36, "title":"Mattress",                      "tags":["Home","Wellness","Furniture"],         "year":2023, "emoji":"🛏️", "subtitle":"Casper / Purple",      "image":"" },
  { "id":37, "title":"Vinyl Record Player",           "tags":["Audio","Home","Decor"],                "year":2023, "emoji":"🎶", "subtitle":"Pro-Ject",            "image":"" },
  { "id":38, "title":"Action Camera",                 "tags":["Electronics","Outdoor","Travel"],      "year":2023, "emoji":"🎥", "subtitle":"GoPro Hero 12",       "image":"" },
  { "id":39, "title":"Electric Toothbrush",           "tags":["Health","Wellness","Beauty"],          "year":2023, "emoji":"🦷", "subtitle":"Oral-B",              "image":"" },
  { "id":40, "title":"Notebook / Journal",            "tags":["Office","Reading","Decor"],            "year":2023, "emoji":"📓", "subtitle":"Leuchtturm1917",      "image":"" },
  { "id":41, "title":"Tennis Racket",                 "tags":["Sports","Outdoor","Fitness"],          "year":2023, "emoji":"🎾", "subtitle":"Wilson",              "image":"" },
  { "id":42, "title":"Drone",                         "tags":["Electronics","Outdoor","Gadget"],      "year":2023, "emoji":"🚁", "subtitle":"DJI Mini 4 Pro",      "image":"" },
  { "id":43, "title":"Swim Goggles",                  "tags":["Sports","Fitness","Outdoor"],          "year":2023, "emoji":"🥽", "subtitle":"Speedo",              "image":"" },
  { "id":44, "title":"Candle Set",                    "tags":["Home","Decor","Wellness"],             "year":2023, "emoji":"🕯️", "subtitle":"Diptyque",             "image":"" },
  { "id":45, "title":"Noise Machine",                 "tags":["Wellness","Home","Health"],            "year":2023, "emoji":"😴", "subtitle":"LectroFan",           "image":"" },
  { "id":46, "title":"Portable Monitor",              "tags":["Electronics","Computer","Travel"],     "year":2023, "emoji":"💻", "subtitle":"ASUS ZenScreen",      "image":"" },
  { "id":47, "title":"Leather Wallet",                "tags":["Fashion","Accessories","Travel"],      "year":2023, "emoji":"👛", "subtitle":"Bellroy",             "image":"" },
  { "id":48, "title":"Cycling Helmet",                "tags":["Sports","Outdoor","Safety"],           "year":2023, "emoji":"🚴", "subtitle":"Giro",                "image":"" },
  { "id":49, "title":"Smart Scale",                   "tags":["Health","Fitness","Gadget"],           "year":2023, "emoji":"⚖️", "subtitle":"Withings",            "image":"" },
  { "id":50, "title":"Board Game",                    "tags":["Gaming","Home","Entertainment"],       "year":2023, "emoji":"🎲", "subtitle":"Settlers of Catan",   "image":"" },
]

DATASETS = {
    "movies": MOVIES,
    "books": BOOKS,
    "products": PRODUCTS,
}

COLLAB_USERS = {
  "movies": [
    {1:5,2:4,5:5,6:4,12:3,21:5,25:4,50:5,51:4},
    {3:5,4:5,7:5,16:5,18:4,23:4,24:5,34:4,47:3},
    {8:5,10:4,11:3,13:4,17:5,22:4,35:4,54:5},
    {2:5,6:5,9:4,12:5,21:4,25:5,19:3,29:4,36:5},
    {1:4,4:4,14:5,23:5,18:5,8:4,44:5,48:4,49:3},
    {5:5,11:4,13:5,15:4,17:4,19:5,24:3,53:5,57:4},
    {3:4,7:5,16:5,20:4,24:5,15:3,34:5,46:4},
    {2:4,6:5,9:5,12:4,22:5,25:3,21:4,29:5,37:4},
    {8:5,10:5,11:5,13:4,17:5,22:3,39:4,54:5,40:4},
    {1:5,14:4,18:5,23:5,4:4,16:4,43:5,44:4},
    {26:5,27:5,30:4,33:4,42:4,51:5,58:4},
    {28:5,31:4,32:5,38:4,52:3,55:5},
    {34:5,46:5,50:4,47:4,20:5,24:4},
    {35:5,10:4,13:4,41:5,45:4,22:5,8:3},
    {36:5,37:4,29:4,9:5,12:5,6:4,26:3},
  ],
  "books": [
    {1:5,3:4,4:5,11:4,16:5,22:4,36:5,49:4},
    {2:5,9:4,14:5,3:4,11:4,21:5,39:4,27:3},
    {5:5,12:5,17:5,19:4,29:5,42:4,41:3},
    {7:5,8:5,18:5,6:4,23:4,26:5,43:4,50:3},
    {10:5,13:5,15:4,20:5,28:5,32:4,45:3},
    {1:4,3:5,16:4,11:5,47:5,35:4,22:3},
    {2:5,14:5,9:4,17:3,19:4,24:5,25:4,40:3},
    {6:5,7:4,8:5,18:4,5:3,30:5,37:4,44:5},
    {10:4,13:5,20:5,15:5,28:4,46:5,31:3},
    {5:5,12:4,17:5,19:5,2:4,33:5,38:4,48:3},
    {1:4,4:3,36:5,22:5,3:4,16:4,49:5},
    {14:5,21:4,27:5,39:4,8:5,18:3},
    {25:5,24:4,45:5,46:4,3:5,11:3},
    {30:5,17:4,37:5,42:4,5:5,12:3},
    {43:5,50:4,26:5,18:4,7:5,8:3},
  ],
  "products": [
    {1:5,6:5,7:4,10:5,15:4,20:5,34:4,42:3},
    {2:5,5:5,12:4,16:5,8:3,23:5,31:4,41:5},
    {3:5,9:5,14:4,17:3,13:4,22:5,27:4,33:3},
    {4:5,7:5,11:4,6:4,15:3,21:5,24:5,28:4},
    {1:4,10:5,18:5,6:4,20:4,37:5,38:3,46:4},
    {2:4,5:5,8:4,16:5,12:5,26:5,32:4,48:3},
    {3:4,9:4,13:5,17:5,14:3,36:5,44:4,45:5},
    {4:4,7:4,11:5,6:5,1:3,21:4,34:5,40:3},
    {1:5,10:4,18:4,20:5,15:5,29:4,47:5,49:3},
    {2:5,5:4,12:5,16:4,8:5,23:4,43:5,35:3},
    {6:5,19:5,39:4,45:4,49:5,1:3,17:4},
    {7:5,24:5,21:4,34:4,11:5,4:3},
    {3:5,22:5,27:4,33:5,9:4,14:3},
    {26:5,32:4,8:5,16:5,41:4,2:3},
    {37:5,38:4,42:5,18:4,10:5,46:3},
  ],
}

# ── Helpers and algorithms ────────────────────────────────────────────────────

def cosine_sim(a, b):
    dot = sum(a[i] * b[i] for i in range(len(a)))
    ma = math.sqrt(sum(x * x for x in a))
    mb = math.sqrt(sum(x * x for x in b))
    return dot / (ma * mb) if ma and mb else 0.0



def item_vector(item, all_tags):
    tags = set(item["tags"])
    return [1.0 if t in tags else 0.0 for t in all_tags]
def content_based(category, ratings_dict, top_n=6):
    # make sure we have a real Python dict
    ratings_dict = dict(ratings_dict)

    items = DATASETS[category]
    if not ratings_dict:
        return []

    all_tags = sorted({tag for it in items for tag in it["tags"]})
    rated_ids = set(ratings_dict.keys())
    unrated = [it for it in items if it["id"] not in rated_ids]
    if not unrated:
        unrated = [it for it in items if ratings_dict.get(it["id"], 0) >= 4]
        if not unrated:
            unrated = items[:]

    profile = [0.0] * len(all_tags)
    total_w = 0.0

    for it in items:
        mid = it["id"]
        if mid in ratings_dict:
            w = float(ratings_dict[mid])
            vec = item_vector(it, all_tags)
            for i in range(len(all_tags)):
                profile[i] += vec[i] * w
            total_w += w

    if not total_w:
        return []

    profile = [x / total_w for x in profile]

    liked_tags = set()
    for it in items:
        mid = it["id"]
        if mid in ratings_dict and float(ratings_dict[mid]) >= 4.0:
            liked_tags.update(it["tags"])

    results = []
    for it in unrated:
        vec = item_vector(it, all_tags)
        sim = cosine_sim(profile, vec)
        matched = [t for t in it["tags"] if t in liked_tags]
        reason = "matches " + ", ".join(matched) if matched else "similar overall taste"
        enriched = dict(it)
        enriched["score"] = round(sim * 100.0, 1)
        enriched["reason"] = reason
        results.append(enriched)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]


def debug_content(category, ratings_dict):
    ratings_dict = dict(ratings_dict)  # convert proxy → dict

    items = DATASETS[category]
    rated_ids = set(ratings_dict.keys())
    unrated = [it for it in items if it["id"] not in rated_ids]
    return {
        "num_ratings": len(ratings_dict),
        "rated_ids": list(rated_ids),
        "num_items": len(items),
        "num_unrated": len(unrated),
    }
def collaborative(category, ratings_dict, top_n=6):
    ratings_dict = dict(ratings_dict)
    items = DATASETS[category]
    users = COLLAB_USERS.get(category, [])
    if not ratings_dict:
        return []
    rated_ids = set(ratings_dict.keys())
    sims = []

    for u in users:
        common = rated_ids & set(u.keys())
        if not common:
            sims.append(0.0)
            continue
        a = [ratings_dict[iid] for iid in common]
        b = [u[iid] for iid in common]
        sims.append(cosine_sim(a, b))

    item_scores = {}
    item_count = {}

    for u, sim in zip(users, sims):
        if sim <= 0:
            continue
        for iid, r in u.items():
            if iid in rated_ids:
                continue
            item_scores[iid] = item_scores.get(iid, 0.0) + sim * r
            item_count[iid] = item_count.get(iid, 0.0) + sim

    if not item_scores:
        return []

    id_map = {it["id"]: it for it in items}
    results = []

    best_sim_val = max(sims) if sims else 0.0
    best_sim_pct = best_sim_val * 100.0 if best_sim_val > 0 else 0.0

    for iid, score_sum in item_scores.items():
        if iid not in id_map:
            continue
        it = dict(id_map[iid])
        norm = score_sum / item_count[iid]
        it["score"] = round(norm / 5.0 * 100.0, 1)
        it["reason"] = f"{round(best_sim_pct, 0):.0f}% match with users like you"
        results.append(it)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]
def get_items(category):
    return DATASETS.get(category, [])

def get_users(category):
    return COLLAB_USERS.get(category, [])

def recommend_content(category, ratings_dict, top_n=6):
    items = DATASETS.get(category, [])
    return content_based(category, ratings_dict, top_n)

def recommend_collaborative(category, ratings_dict, top_n=6):
    items = DATASETS.get(category, [])
    users = COLLAB_USERS.get(category, [])
    return collaborative(category, ratings_dict, top_n)
