import os
import random
from .truce import SatelliteImageDownloader
from json import dumps


class AIModel:
    def __init__(self):
        self.name = "Model"

    def generate_images(self, coordinates, zoomLevel, coordinates_hash, starttime, endtime):
        # print("Method called")
        # # Usage
        # downloader = SatelliteImageDownloader("dd6c61a3-f396-4e05-87c0-bd0298d969e4")
        # coords = [85.3096, 23.3441, 85.3375, 23.3705]
        # downloader.download_image(coords, "2022-08-17", "ranchi_2022.png")
        # downloader.download_image(coords, "2023-08-17", "ranchi_2023.png")
        # print("Method ended")
        # processing here
        folder_path = "dist"
        file_list = os.listdir(folder_path)
        random_filename = random.choice(file_list)
        while random_filename == "assets" or random_filename == "index.html":
            random_filename = random.choice(file_list)
        print(random_filename)
        # filename must have coordinates attached when sending
        data = dumps(
            {
                "status": "image_generated",
                "type": [
                    {"Name": "Reference", "URL": random_filename, "IsCard": False},
                    {"Name": "Modified", "URL": random_filename, "IsCard": False},
                    {"Name": "Difference", "URL": random_filename, "IsCard": False},
                    {"Name": "Wildfire", "URL": random_filename, "IsCard": True},
                    {"Name": "Flood", "URL": random_filename, "IsCard": True},
                ],
                "data": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": 0,
                            "properties": {
                                "Code": "FRLA",
                                "Name": "Frederick Law Olmsted National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.13112956925647, 42.32550867371509],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 1,
                            "properties": {
                                "Code": "GLDE",
                                "Name": "Gloria Dei Church National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.14358360598474, 39.93437740957208],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 2,
                            "properties": {
                                "Code": "JOFI",
                                "Name": "John F Kennedy National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.12296449148327, 42.34659755450367],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 3,
                            "properties": {
                                "Code": "LONG",
                                "Name": "Longfellow House - Washington's Headquarters National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.12589617395572, 42.377018699780116],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 4,
                            "properties": {
                                "Code": "ROWI",
                                "Name": "Roger Williams National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.41080072906996, 41.82834611476998],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 5,
                            "properties": {
                                "Code": "WORI",
                                "Name": "Women's Rights National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.79059742893223, 42.91175340015097],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 6,
                            "properties": {
                                "Code": "TUPE",
                                "Name": "Tupelo National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-88.73708622728343, 34.255577049962426],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 7,
                            "properties": {
                                "Code": "BRCR",
                                "Name": "Brices Cross Roads National Battlefield Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-88.72889342660221, 34.50611958182276],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 8,
                            "properties": {
                                "Code": "CHRI",
                                "Name": "Christiansted National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-64.72987006544409, 17.737371115450806],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 9,
                            "properties": {
                                "Code": "BRVB",
                                "Name": "Brown v. Board Of Education National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-95.67614436611811, 39.03787664847986],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 10,
                            "properties": {
                                "Code": "HAGR",
                                "Name": "Hamilton Grange National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.9472712257268, 40.82128019145335],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 11,
                            "properties": {
                                "Code": "THRB",
                                "Name": "Theodore Roosevelt Birthplace National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.98875942305048, 40.738487824764015],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 12,
                            "properties": {
                                "Code": "ANJO",
                                "Name": "Andrew Johnson National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.83709021113485, 36.15624509030006],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 13,
                            "properties": {
                                "Code": "GEGR",
                                "Name": "General Grant National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.96285546338042, 40.81357110978011],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 14,
                            "properties": {
                                "Code": "SAPA",
                                "Name": "Saint Paul's Church National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.82577276392446, 40.89283511586187],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 15,
                            "properties": {
                                "Code": "FEHA",
                                "Name": "Federal Hall National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.01003101514203, 40.707225648244915],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 16,
                            "properties": {
                                "Code": "CACL",
                                "Name": "Castle Clinton National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.01680558080551, 40.70347795022505],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 17,
                            "properties": {
                                "Code": "ULSG",
                                "Name": "Ulysses S Grant National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.35169254931361, 38.55182373795377],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 18,
                            "properties": {
                                "Code": "AFBG",
                                "Name": "African Burial Ground National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.00432891216373, 40.7145494786104],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 19,
                            "properties": {
                                "Code": "CLBA",
                                "Name": "Clara Barton National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.1400968923483, 38.96762881961648],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 20,
                            "properties": {
                                "Code": "EDAL",
                                "Name": "Edgar Allan Poe National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.15000619734683, 39.961954818262406],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 21,
                            "properties": {
                                "Code": "BOAF",
                                "Name": "Boston African American National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.06764181118616, 42.35908295092028],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 22,
                            "properties": {
                                "Code": "NICO",
                                "Name": "Nicodemus National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-99.61691622083906, 39.39162299190838],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 23,
                            "properties": {
                                "Code": "SAMA",
                                "Name": "Salem Maritime National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-70.88640866812887, 42.52024529010838],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 24,
                            "properties": {
                                "Code": "FILA",
                                "Name": "First Ladies National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.37593264168406, 40.79662217354262],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 25,
                            "properties": {
                                "Code": "HSTR",
                                "Name": "Harry S Truman National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.51624880173956, 38.9271196803251],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 26,
                            "properties": {
                                "Code": "FOST",
                                "Name": "Fort Stanwix National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.45557625662032, 43.2105344060499],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 27,
                            "properties": {
                                "Code": "THKO",
                                "Name": "Thaddeus Kosciuszko National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.14732045203958, 39.94345312154055],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 28,
                            "properties": {
                                "Code": "WIHO",
                                "Name": "William Howard Taft National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.50758950892032, 39.11970352573182],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 29,
                            "properties": {
                                "Code": "JAGA",
                                "Name": "James A Garfield National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.35086557049902, 41.664865492500496],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 30,
                            "properties": {
                                "Code": "THRI",
                                "Name": "Theodore Roosevelt Inaugural National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.87242204965719, 42.90147672769445],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 31,
                            "properties": {
                                "Code": "GREG",
                                "Name": "Great Egg Harbor River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.64969520595511, 39.30421499367857],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 32,
                            "properties": {
                                "Code": "POCH",
                                "Name": "Port Chicago Naval Magazine National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.02968997340061, 38.05752521711916],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 33,
                            "properties": {
                                "Code": "RIGR",
                                "Name": "Rio Grande Wild & Scenic River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-97.14377094647499, 25.95204582086439],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 34,
                            "properties": {
                                "Code": "POHE",
                                "Name": "Potomac Heritage National Scenic Trail",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.36738194668293, 39.956988206785155],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 35,
                            "properties": {
                                "Code": "JAZZ",
                                "Name": "New Orleans Jazz National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.060953205562, 29.95859879628854],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 36,
                            "properties": {
                                "Code": "VALR",
                                "Name": "World War II Valor in the Pacific National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -157.94138288460783,
                                    21.366510151855085,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 37,
                            "properties": {
                                "Code": "CAWO",
                                "Name": "Carter G. Woodson Home National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02430875356602, 38.91088511316648],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 38,
                            "properties": {
                                "Code": "GERO",
                                "Name": "George Rogers Clark National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-87.53396434610524, 38.67813524569448],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 39,
                            "properties": {
                                "Code": "INDE",
                                "Name": "Independence National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.14692521397585, 39.9453737131525],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 40,
                            "properties": {
                                "Code": "JEFF",
                                "Name": "Jefferson National Expansion Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.18595301180287, 38.62254009262406],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 41,
                            "properties": {
                                "Code": "NEBE",
                                "Name": "New Bedford Whaling National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-70.92327477113328, 41.63460733723657],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 42,
                            "properties": {
                                "Code": "SACR",
                                "Name": "Saint Croix Island International Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-67.13350642097588, 45.12879056602938],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 43,
                            "properties": {
                                "Code": "SAIR",
                                "Name": "Saugus Iron Works National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.00724686413027, 42.468462996422964],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 44,
                            "properties": {
                                "Code": "STLI",
                                "Name": "Statue Of Liberty National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.04173576446185, 40.69826910022187],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 45,
                            "properties": {
                                "Code": "STEA",
                                "Name": "Steamtown National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.67022197795563, 41.40681280598398],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 46,
                            "properties": {
                                "Code": "TUIN",
                                "Name": "Tuskegee Institute National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.7046714781279, 32.43022512972665],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 47,
                            "properties": {
                                "Code": "WEFA",
                                "Name": "Weir Farm National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.45584614454683, 41.25743680098501],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 48,
                            "properties": {
                                "Code": "SAJU",
                                "Name": "San Juan National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-66.11587316023481, 18.468818521127695],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 49,
                            "properties": {
                                "Code": "MAWA",
                                "Name": "Maggie L Walker National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.43826064338633, 37.5480565790424],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 50,
                            "properties": {
                                "Code": "YUHO",
                                "Name": "Yucca House National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.68595484701112, 37.24895447871703],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 51,
                            "properties": {
                                "Code": "CASA",
                                "Name": "Castillo De San Marcos National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.31217173403155, 29.897857013631],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 52,
                            "properties": {
                                "Code": "ARHO",
                                "Name": "Arlington House, The Robert  E. Lee Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.07272691520815, 38.88326787598615],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 53,
                            "properties": {
                                "Code": "JICA",
                                "Name": "Jimmy Carter National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.43240803282944, 32.02631793559381],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 54,
                            "properties": {
                                "Code": "MALU",
                                "Name": "Martin Luther King Jr National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.37169330249506, 33.754920076352306],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 55,
                            "properties": {
                                "Code": "CHPI",
                                "Name": "Charles Pinckney National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.82487582157863, 32.845773923089936],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 56,
                            "properties": {
                                "Code": "FOSM",
                                "Name": "Fort Smith National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.43130218338237, 35.38837828221602],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 57,
                            "properties": {
                                "Code": "PISP",
                                "Name": "Pipe Spring National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.73985668087789, 36.86282666218236],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 58,
                            "properties": {
                                "Code": "GOIS",
                                "Name": "Governors Island National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.01689113495863, 40.691623778401286],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 59,
                            "properties": {
                                "Code": "LIHO",
                                "Name": "Lincoln Home National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-89.64513396957298, 39.79715642069349],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 60,
                            "properties": {
                                "Code": "DESO",
                                "Name": "De Soto National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.64335471685791, 27.52278352231193],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 61,
                            "properties": {
                                "Code": "EDIS",
                                "Name": "Thomas Edison National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.23982097063325, 40.785970757586604],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 62,
                            "properties": {
                                "Code": "HUTR",
                                "Name": "Hubbell Trading Post National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-109.56328115082408, 35.70546644096676],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 63,
                            "properties": {
                                "Code": "CHAM",
                                "Name": "Chamizal National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -106.45461592666625,
                                    31.767371101062324,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 64,
                            "properties": {
                                "Code": "MIMI",
                                "Name": "Minuteman Missile National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -101.96216064088252,
                                    43.877892008761144,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 65,
                            "properties": {
                                "Code": "TUAI",
                                "Name": "Tuskegee Airmen National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.67983321167087, 32.45538671570123],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 66,
                            "properties": {
                                "Code": "EUON",
                                "Name": "Eugene O'Neill National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.02666421306343, 37.82592473657651],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 67,
                            "properties": {
                                "Code": "BOST",
                                "Name": "Boston National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.05702448540092, 42.37348255493958],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 68,
                            "properties": {
                                "Code": "ADAM",
                                "Name": "Adams National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.0113517468376, 42.25647689490795],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 69,
                            "properties": {
                                "Code": "FOPO",
                                "Name": "Fort Point National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.47371724398397, 37.8084002052445],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 70,
                            "properties": {
                                "Code": "CHSC",
                                "Name": "Central High School National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-92.29983208314182, 34.736812622951405],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 71,
                            "properties": {
                                "Code": "FOLS",
                                "Name": "Fort Larned National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-99.21896096669342, 38.183842983218454],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 72,
                            "properties": {
                                "Code": "RORI",
                                "Name": "Rosie the Riveter WWII Home Front National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.36653505635901, 37.90866832535756],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 73,
                            "properties": {
                                "Code": "FOSC",
                                "Name": "Fort Scott National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.70454193262466, 37.84340286701331],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 74,
                            "properties": {
                                "Code": "PEVI",
                                "Name": "Perry's Victory & International Peace Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.81190442668668, 41.65379041897526],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 75,
                            "properties": {
                                "Code": "AMME",
                                "Name": "American Memorial Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [145.72035233007173, 15.213133853329555],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 76,
                            "properties": {
                                "Code": "ANDE",
                                "Name": "Andersonville National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.13093802586722, 32.197573362440366],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 77,
                            "properties": {
                                "Code": "FOCA",
                                "Name": "Fort Caroline National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.50049787820453, 30.38388966399186],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 78,
                            "properties": {
                                "Code": "FOMC",
                                "Name": "Fort McHenry National Monument and Historic Shrine",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.57912815313652, 39.26156739483277],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 79,
                            "properties": {
                                "Code": "FORA",
                                "Name": "Fort Raleigh National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.70938760851078, 35.93636834723129],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 80,
                            "properties": {
                                "Code": "HAMP",
                                "Name": "Hampton National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.5883223094582, 39.41447808416819],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 81,
                            "properties": {
                                "Code": "JOFL",
                                "Name": "Johnstown Flood National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.7769512565439, 40.34494335150366],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 82,
                            "properties": {
                                "Code": "LOWE",
                                "Name": "Lowell National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.31616921579818, 42.64610102507244],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 83,
                            "properties": {
                                "Code": "MIIN",
                                "Name": "Minidoka National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-114.2464059745946, 42.67801738147922],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 84,
                            "properties": {
                                "Code": "MUWO",
                                "Name": "Muir Woods National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -122.59219031030287,
                                    37.899655100144244,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 85,
                            "properties": {
                                "Code": "OCMU",
                                "Name": "Ocmulgee National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-83.6109676964351, 32.8367676509253],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 86,
                            "properties": {
                                "Code": "RUCA",
                                "Name": "Russell Cave National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.81868896360646, 34.97104302969246],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 87,
                            "properties": {
                                "Code": "SAHI",
                                "Name": "Sagamore Hill National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.49283525890276, 40.88534743664194],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 88,
                            "properties": {
                                "Code": "SAFR",
                                "Name": "San Francisco Maritime National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.42364633393989, 37.80857191826663],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 89,
                            "properties": {
                                "Code": "SPAR",
                                "Name": "Springfield Armory National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-72.58216842461714, 42.10797019704847],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 90,
                            "properties": {
                                "Code": "VAMA",
                                "Name": "Vanderbilt Mansion National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.94185751721938, 41.794398514930975],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 91,
                            "properties": {
                                "Code": "GICL",
                                "Name": "Gila Cliff Dwellings National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.27349674310848, 33.22759961571126],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 92,
                            "properties": {
                                "Code": "TUMA",
                                "Name": "Tumacacori National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.04776399422589, 31.57283093366739],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 93,
                            "properties": {
                                "Code": "TUZI",
                                "Name": "Tuzigoot National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.03199708944031, 34.77204934991178],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 94,
                            "properties": {
                                "Code": "WHMI",
                                "Name": "Whitman Mission National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-118.46293876096766, 46.04119285666407],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 95,
                            "properties": {
                                "Code": "HOME",
                                "Name": "Homestead National Monument of America",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-96.83748257566027, 40.2865160537571],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 96,
                            "properties": {
                                "Code": "WOTR",
                                "Name": "Wolf Trap National Park for the Performing Arts",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.26355410163892, 38.93793199647512],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 97,
                            "properties": {
                                "Code": "TICA",
                                "Name": "Timpanogos Cave National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.7093943699894, 40.44039718911578],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 98,
                            "properties": {
                                "Code": "THIS",
                                "Name": "Theodore Roosevelt Island Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.0624191798319, 38.89584162132938],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 99,
                            "properties": {
                                "Code": "LYBA",
                                "Name": "Lyndon Baines Johnson Memorial Grove on the Potomac",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.05331357204966, 38.880135753662984],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 100,
                            "properties": {
                                "Code": "FOSU",
                                "Name": "Fort Sumter National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.88296006189896, 32.75437787513024],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 101,
                            "properties": {
                                "Code": "CARL",
                                "Name": "Carl Sandburg Home National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.45244320103025, 35.266570200071854],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 102,
                            "properties": {
                                "Code": "TONT",
                                "Name": "Tonto National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.12005475098205, 33.64481517431764],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 103,
                            "properties": {
                                "Code": "IATR",
                                "Name": "Ice Age National Scenic Trail",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-89.61375420545654, 43.07682240928835],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 104,
                            "properties": {
                                "Code": "HEHO",
                                "Name": "Herbert Hoover National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.35508258374547, 41.66792352610145],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 105,
                            "properties": {
                                "Code": "LIBO",
                                "Name": "Lincoln Boyhood National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.99653930391227, 38.11817673689914],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 106,
                            "properties": {
                                "Code": "ABLI",
                                "Name": "Abraham Lincoln Birthplace National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.64442068791612, 37.611975893121695],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 107,
                            "properties": {
                                "Code": "MOCA",
                                "Name": "Montezuma Castle National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -111.83666585728099,
                                    34.611020730789164,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 108,
                            "properties": {
                                "Code": "FOFR",
                                "Name": "Fort Frederica National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.39589266381645, 31.22654266149378],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 109,
                            "properties": {
                                "Code": "GWCA",
                                "Name": "George Washington Carver National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.35522737178867, 36.98713219595603],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 110,
                            "properties": {
                                "Code": "PUHE",
                                "Name": "Puukohola Heiau National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-155.82116293422845, 20.02772186139583],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 111,
                            "properties": {
                                "Code": "CABR",
                                "Name": "Cabrillo National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-117.24147362061612, 32.67243113084509],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 112,
                            "properties": {
                                "Code": "NATC",
                                "Name": "Natchez National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.3821444417232, 31.54246933482903],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 113,
                            "properties": {
                                "Code": "LECL",
                                "Name": "Lewis & Clark National Historic Trail",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-95.83244756597631, 40.66418476574701],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 114,
                            "properties": {
                                "Code": "AZRU",
                                "Name": "Aztec Ruins National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-107.999927438689, 36.8368259123042],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 115,
                            "properties": {
                                "Code": "NAVA",
                                "Name": "Navajo National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-110.53625648955637, 36.68549126441223],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 116,
                            "properties": {
                                "Code": "CARI",
                                "Name": "Cane River Creole National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-93.0044493165306, 31.66537544033857],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 117,
                            "properties": {
                                "Code": "DAAV",
                                "Name": "Dayton Aviation Heritage National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.06594811912724, 39.802824220672655],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 118,
                            "properties": {
                                "Code": "SAGA",
                                "Name": "Saint-Gaudens National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-72.37403162934115, 43.50046886798249],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 119,
                            "properties": {
                                "Code": "MOCR",
                                "Name": "Moores Creek National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.11047702461649, 34.45834328420184],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 120,
                            "properties": {
                                "Code": "FOMA",
                                "Name": "Fort Matanzas National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.23844402184821, 29.711508408754753],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 121,
                            "properties": {
                                "Code": "MAVA",
                                "Name": "Martin Van Buren National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.70516992717663, 42.36995449266975],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 122,
                            "properties": {
                                "Code": "RABR",
                                "Name": "Rainbow Bridge National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-110.96550987139958, 37.0778877152767],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 123,
                            "properties": {
                                "Code": "PIPE",
                                "Name": "Pipestone National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-96.32475522881614, 44.013519580410964],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 124,
                            "properties": {
                                "Code": "FODA",
                                "Name": "Fort Davis National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -103.89612161564835,
                                    30.599341600425337,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 125,
                            "properties": {
                                "Code": "ORCA",
                                "Name": "Oregon Caves National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -123.40864092512629,
                                    42.095307455760924,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 126,
                            "properties": {
                                "Code": "SITK",
                                "Name": "Sitka National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -135.31536844280552,
                                    57.047011744724784,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 127,
                            "properties": {
                                "Code": "FOVA",
                                "Name": "Fort Vancouver National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -122.66164957809968,
                                    45.623571391754716,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 128,
                            "properties": {
                                "Code": "ALPO",
                                "Name": "Allegheny Portage Railroad National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.55634010413031, 40.45980275828842],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 129,
                            "properties": {
                                "Code": "BIHO",
                                "Name": "Big Hole National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-113.65014819078193, 45.64691889182957],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 130,
                            "properties": {
                                "Code": "FODO",
                                "Name": "Fort Donelson National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-87.86109759398028, 36.48701678405128],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 131,
                            "properties": {
                                "Code": "FRHI",
                                "Name": "Friendship Hill National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.92504168705825, 39.775434234452476],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 132,
                            "properties": {
                                "Code": "GEWA",
                                "Name": "George Washington Birthplace National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.92331590776256, 38.19300521035316],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 133,
                            "properties": {
                                "Code": "GUCO",
                                "Name": "Guilford Courthouse National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.84154206279355, 36.13298335000252],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 134,
                            "properties": {
                                "Code": "HOCU",
                                "Name": "Hopewell Culture National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.98813968868079, 39.38353207506073],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 135,
                            "properties": {
                                "Code": "HOFU",
                                "Name": "Hopewell Furnace National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.77141516182425, 40.2041277662195],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 136,
                            "properties": {
                                "Code": "LYJO",
                                "Name": "Lyndon B Johnson National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-98.61543901495575, 30.242295901244958],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 137,
                            "properties": {
                                "Code": "MABI",
                                "Name": "Marsh - Billings - Rockefeller National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-72.5350200015279, 43.63344940333467],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 138,
                            "properties": {
                                "Code": "POPO",
                                "Name": "Poverty Point National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.40874094165439, 32.63529881882212],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 139,
                            "properties": {
                                "Code": "SAPU",
                                "Name": "Salinas Pueblo Missions National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-106.09275782425358, 34.25991843407275],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 140,
                            "properties": {
                                "Code": "SAAN",
                                "Name": "San Antonio Missions National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-98.45424973424551, 29.33232954868117],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 141,
                            "properties": {
                                "Code": "STRI",
                                "Name": "Stones River National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.43408008802133, 35.87318787954412],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 142,
                            "properties": {
                                "Code": "VICK",
                                "Name": "Vicksburg National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.84309723806291, 32.36451191715054],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 143,
                            "properties": {
                                "Code": "WRBR",
                                "Name": "Wright Brothers National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.66793209638877, 36.01758408695178],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 144,
                            "properties": {
                                "Code": "NEPE",
                                "Name": "Nez Perce National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-116.27582196712781, 45.79613895035158],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 145,
                            "properties": {
                                "Code": "LIBI",
                                "Name": "Little Bighorn Battlefield National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-107.42190554309077, 45.56491080578535],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 146,
                            "properties": {
                                "Code": "CAVO",
                                "Name": "Capulin Volcano National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-103.97104269942275, 36.7817109582052],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 147,
                            "properties": {
                                "Code": "FOBO",
                                "Name": "Fort Bowie National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-109.45113196306811, 32.14925941858059],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 148,
                            "properties": {
                                "Code": "WABA",
                                "Name": "Washita Battlefield National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-99.70453743277493, 35.62079259893231],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 149,
                            "properties": {
                                "Code": "HOFR",
                                "Name": "Home Of Franklin D Roosevelt National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.92671769432188, 41.7680414283523],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 150,
                            "properties": {
                                "Code": "ELRO",
                                "Name": "Eleanor Roosevelt National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.9010718592605, 41.76343356410191],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 151,
                            "properties": {
                                "Code": "NISI",
                                "Name": "Ninety Six National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.01511067998587, 34.14365552969331],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 152,
                            "properties": {
                                "Code": "BOHA",
                                "Name": "Boston Harbor Islands National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-70.87208721135936, 42.2624095115165],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 153,
                            "properties": {
                                "Code": "WAPA",
                                "Name": "War In The Pacific National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [144.6539892933081, 13.39045706547521],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 154,
                            "properties": {
                                "Code": "EFMO",
                                "Name": "Effigy Mounds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.20777103539808, 43.09145864637621],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 155,
                            "properties": {
                                "Code": "HOVE",
                                "Name": "Hovenweep National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-109.07752895020165, 37.38537019570329],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 156,
                            "properties": {
                                "Code": "FOUN",
                                "Name": "Fort Union National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-105.0120173536709, 35.90737114509333],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 157,
                            "properties": {
                                "Code": "PUHO",
                                "Name": "Pu`uhonua O Honaunau National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-155.89230040633282, 19.40921108954358],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 158,
                            "properties": {
                                "Code": "DEPO",
                                "Name": "Devils Postpile National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-119.08739032309173, 37.61525639858674],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 159,
                            "properties": {
                                "Code": "FOUS",
                                "Name": "Fort Union Trading Post National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-104.03360076342334, 47.997814589583],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 160,
                            "properties": {
                                "Code": "COWP",
                                "Name": "Cowpens National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.80833974134818, 35.130562490759246],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 161,
                            "properties": {
                                "Code": "THST",
                                "Name": "Thomas Stone National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.03719868001934, 38.52888007863539],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 162,
                            "properties": {
                                "Code": "GRPO",
                                "Name": "Grand Portage National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-89.7606884993384, 47.99968200791734],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 163,
                            "properties": {
                                "Code": "HOBE",
                                "Name": "Horseshoe Bend National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.72305400404878, 32.98200764156868],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 164,
                            "properties": {
                                "Code": "BOWA",
                                "Name": "Booker T Washington National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.73357143276944, 37.11499541673693],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 165,
                            "properties": {
                                "Code": "JECA",
                                "Name": "Jewel Cave National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-103.82999400818576, 43.73102944966415],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 166,
                            "properties": {
                                "Code": "KAHO",
                                "Name": "Kaloko-Honokohau National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -156.03071958617622,
                                    19.680825527630716,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 167,
                            "properties": {
                                "Code": "CAGR",
                                "Name": "Casa Grande Ruins National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.53266082995748, 32.99694949335554],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 168,
                            "properties": {
                                "Code": "BEOL",
                                "Name": "Bent's Old Fort National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-103.42664991837817, 38.03977546256919],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 169,
                            "properties": {
                                "Code": "PIMA",
                                "Name": "Hohokam Pima National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.92473311289035, 33.1865785620018],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 170,
                            "properties": {
                                "Code": "MORU",
                                "Name": "Mount Rushmore National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -103.45251861171869,
                                    43.880370214419045,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 171,
                            "properties": {
                                "Code": "FONE",
                                "Name": "Fort Necessity National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-79.58831726514997, 39.81115857363511],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 172,
                            "properties": {
                                "Code": "JOMU",
                                "Name": "John Muir National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.13599464018154, 37.98259638345624],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 173,
                            "properties": {
                                "Code": "UPDE",
                                "Name": "Upper Delaware Scenic & Recreational River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.86871054034324, 41.44095255731114],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 174,
                            "properties": {
                                "Code": "CHAT",
                                "Name": "Chattahoochee River National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.26676470628281, 33.97241060914914],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 175,
                            "properties": {
                                "Code": "CHCH",
                                "Name": "Chickamauga & Chattanooga National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.25527973555432, 34.9191603279062],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 176,
                            "properties": {
                                "Code": "CORO",
                                "Name": "Coronado National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.24078388653147,
                                    31.350816813719984,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 177,
                            "properties": {
                                "Code": "FOPU",
                                "Name": "Fort Pulaski National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.93869700187282, 32.03125203517026],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 178,
                            "properties": {
                                "Code": "GOSP",
                                "Name": "Golden Spike National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.49490593840095, 41.63074261463882],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 179,
                            "properties": {
                                "Code": "KIMO",
                                "Name": "Kings Mountain National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.38979428477106, 35.14125664997549],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 180,
                            "properties": {
                                "Code": "MNRR",
                                "Name": "Missouri National Recreational River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-97.07068501568227, 42.76717228680925],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 181,
                            "properties": {
                                "Code": "MORR",
                                "Name": "Morristown National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.53797877461527, 40.76766922259114],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 182,
                            "properties": {
                                "Code": "NPSA",
                                "Name": "National Park of American Samoa",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -169.45380760526996,
                                    -14.239727732693918,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 183,
                            "properties": {
                                "Code": "PETR",
                                "Name": "Petroglyph National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-106.75778245199358, 35.12318884610665],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 184,
                            "properties": {
                                "Code": "PRSF",
                                "Name": "Presidio of San Francisco",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.46713073964011, 37.79654317448044],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 185,
                            "properties": {
                                "Code": "RICH",
                                "Name": "Richmond National Battlefield Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.25139965264403, 37.41785761698396],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 186,
                            "properties": {
                                "Code": "SARA",
                                "Name": "Saratoga National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.64405701265895, 42.9943032342173],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 187,
                            "properties": {
                                "Code": "LEWI",
                                "Name": "Lewis and Clark National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-124.06583125409449, 46.28745328712928],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 188,
                            "properties": {
                                "Code": "VIIS",
                                "Name": "Virgin Islands National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-64.77111048899694, 18.353798617233704],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 189,
                            "properties": {
                                "Code": "SCBL",
                                "Name": "Scotts Bluff National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-103.70713508742655, 41.83464192866749],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 190,
                            "properties": {
                                "Code": "GRKO",
                                "Name": "Grant-Kohrs Ranch National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.75655740295973, 46.4041525585678],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 191,
                            "properties": {
                                "Code": "MONO",
                                "Name": "Monocacy National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.40246951476036, 39.3576985239086],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 192,
                            "properties": {
                                "Code": "FLFO",
                                "Name": "Florissant Fossil Beds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-105.27884587582167, 38.91846111468554],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 193,
                            "properties": {
                                "Code": "DETO",
                                "Name": "Devils Tower National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -104.71559301356767,
                                    44.590555889322125,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 194,
                            "properties": {
                                "Code": "BUIS",
                                "Name": "Buck Island Reef National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-64.62221790245633, 17.81026717214854],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 195,
                            "properties": {
                                "Code": "HAFE",
                                "Name": "Harpers Ferry National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.72920504544601, 39.31756187483286],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 196,
                            "properties": {
                                "Code": "SUCR",
                                "Name": "Sunset Crater Volcano National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.51037604218448, 35.3711432259561],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 197,
                            "properties": {
                                "Code": "ELMO",
                                "Name": "El Morro National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.33755716279946, 35.03894415281187],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 198,
                            "properties": {
                                "Code": "KEWE",
                                "Name": "Keweenaw National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-88.56933502381558, 47.138999767529995],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 199,
                            "properties": {
                                "Code": "KNRI",
                                "Name": "Knife River Indian Villages National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-101.38400068375047, 47.35300212379206],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 200,
                            "properties": {
                                "Code": "MANZ",
                                "Name": "Manzanar National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-118.15471770065676, 36.72559195291623],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 201,
                            "properties": {
                                "Code": "KEMO",
                                "Name": "Kennesaw Mountain National Battlefield Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.57891655814971, 33.977290839811715],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 202,
                            "properties": {
                                "Code": "VICR",
                                "Name": "Virgin Islands Coral Reef National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-64.6961880374966, 18.278213954506434],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 203,
                            "properties": {
                                "Code": "VAFO",
                                "Name": "Valley Forge National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.45874838283551, 40.09676710215052],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 204,
                            "properties": {
                                "Code": "FOLA",
                                "Name": "Fort Laramie National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-104.54641519212936, 42.20428979438691],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 205,
                            "properties": {
                                "Code": "SARI",
                                "Name": "Salt River Bay National Historic Park and Ecological Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-64.7551934766009, 17.77908602227972],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 206,
                            "properties": {
                                "Code": "HOSP",
                                "Name": "Hot Springs National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-93.08972185108273, 34.51113822506357],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 207,
                            "properties": {
                                "Code": "FLNI",
                                "Name": "Flight 93 National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.89456904900808, 40.06061476060677],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 208,
                            "properties": {
                                "Code": "WICR",
                                "Name": "Wilson's Creek National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-93.40985162324179, 37.09999207803314],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 209,
                            "properties": {
                                "Code": "AGFO",
                                "Name": "Agate Fossil Beds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -103.74399899921055,
                                    42.421472450669654,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 210,
                            "properties": {
                                "Code": "PAAL",
                                "Name": "Palo Alto Battlefield National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-97.46272182869333, 26.024743571129836],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 211,
                            "properties": {
                                "Code": "WACA",
                                "Name": "Walnut Canyon National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.52001467316386, 35.16818671760679],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 212,
                            "properties": {
                                "Code": "APCO",
                                "Name": "Appomattox Court House National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.80089402128391, 37.382748231493544],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 213,
                            "properties": {
                                "Code": "MIMA",
                                "Name": "Minute Man National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-71.29604800703322, 42.45340079367497],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 214,
                            "properties": {
                                "Code": "ARPO",
                                "Name": "Arkansas Post National Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.34725180457292, 34.02089090945371],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 215,
                            "properties": {
                                "Code": "HAFO",
                                "Name": "Hagerman Fossil Beds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -114.95399890562766,
                                    42.775574955437094,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 216,
                            "properties": {
                                "Code": "PECO",
                                "Name": "Pecos National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-105.67489510930119, 35.53810317068588],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 217,
                            "properties": {
                                "Code": "PERI",
                                "Name": "Pea Ridge National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.03444497318469, 36.45478142493534],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 218,
                            "properties": {
                                "Code": "PETE",
                                "Name": "Petersburg National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.35477462919117, 37.23188607445225],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 219,
                            "properties": {
                                "Code": "CACO",
                                "Name": "Cape Cod National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-70.00526293681077, 41.95906033473802],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 220,
                            "properties": {
                                "Code": "CAHA",
                                "Name": "Cape Hatteras National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.60292836345364, 35.23684213001043],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 221,
                            "properties": {
                                "Code": "CALO",
                                "Name": "Cape Lookout National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.19003925692125, 34.95824468130278],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 222,
                            "properties": {
                                "Code": "CUIS",
                                "Name": "Cumberland Island National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.45252498127859, 30.858589807903808],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 223,
                            "properties": {
                                "Code": "DEWA",
                                "Name": "Delaware Water Gap National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-74.95693003838454, 41.10033238731896],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 224,
                            "properties": {
                                "Code": "FIIS",
                                "Name": "Fire Island National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.11493130493012, 40.656817817613984],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 225,
                            "properties": {
                                "Code": "GATE",
                                "Name": "Gateway National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-73.86126160474157, 40.602615522343235],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 226,
                            "properties": {
                                "Code": "JODA",
                                "Name": "John Day Fossil Beds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-119.63540858136547, 44.5431928610706],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 227,
                            "properties": {
                                "Code": "PRWI",
                                "Name": "Prince William Forest Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.38403576735115, 38.58819990832198],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 228,
                            "properties": {
                                "Code": "SAJH",
                                "Name": "San Juan Island National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-123.00646972800878, 48.46190942620296],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 229,
                            "properties": {
                                "Code": "SHIL",
                                "Name": "Shiloh National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-88.33949885076379, 35.143101616983735],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 230,
                            "properties": {
                                "Code": "CEBE",
                                "Name": "Cedar Creek & Belle Grove National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.31421463775484, 38.99372617682746],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 231,
                            "properties": {
                                "Code": "CHIR",
                                "Name": "Chiricahua National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -109.34145626519025,
                                    32.012170203508035,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 232,
                            "properties": {
                                "Code": "MANA",
                                "Name": "Manassas National Battlefield Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.53003887629056, 38.8207732144433],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 233,
                            "properties": {
                                "Code": "SAND",
                                "Name": "Sand Creek Massacre National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-102.54248629355702, 38.57376357895553],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 234,
                            "properties": {
                                "Code": "ANTI",
                                "Name": "Antietam National Battlefield",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.74907431595057, 39.48295017589319],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 235,
                            "properties": {
                                "Code": "CUGA",
                                "Name": "Cumberland Gap National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-83.6972737218358, 36.58215708927296],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 236,
                            "properties": {
                                "Code": "CEBR",
                                "Name": "Cedar Breaks National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.84526798850786, 37.63545562121178],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 237,
                            "properties": {
                                "Code": "CHIC",
                                "Name": "Chickasaw National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-97.0279155083743, 34.44175323997241],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 238,
                            "properties": {
                                "Code": "FOBU",
                                "Name": "Fossil Butte National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.76635347980823,
                                    41.856666705982775,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 239,
                            "properties": {
                                "Code": "KALA",
                                "Name": "Kalaupapa National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-156.9246498265113, 21.15464223113427],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 240,
                            "properties": {
                                "Code": "TAPR",
                                "Name": "Tallgrass Prairie National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-96.54985604955206, 38.41865705209544],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 241,
                            "properties": {
                                "Code": "INDU",
                                "Name": "Indiana Dunes National Lakeshore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-87.03241529098068, 41.661457848148025],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 242,
                            "properties": {
                                "Code": "JELA",
                                "Name": "Jean Lafitte National Historical Park and Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.14721503714877, 29.81917944805583],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 243,
                            "properties": {
                                "Code": "CATO",
                                "Name": "Catoctin Mountain Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.4612213279279, 39.64821331246887],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 244,
                            "properties": {
                                "Code": "NABR",
                                "Name": "Natural Bridges National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-110.00224358939779, 37.60453290516204],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 245,
                            "properties": {
                                "Code": "GETT",
                                "Name": "Gettysburg National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.23792628522821, 39.79931525936756],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 246,
                            "properties": {
                                "Code": "EISE",
                                "Name": "Eisenhower National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.26508101304417, 39.79577591523863],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 247,
                            "properties": {
                                "Code": "CIRO",
                                "Name": "City Of Rocks National Reserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-113.71240971986805, 42.06990240244938],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 248,
                            "properties": {
                                "Code": "KLGO",
                                "Name": "Klondike Gold Rush National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-135.25679581719572, 59.67538299804817],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 249,
                            "properties": {
                                "Code": "BAND",
                                "Name": "Bandelier National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -106.30481358808957,
                                    35.755866743179354,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 250,
                            "properties": {
                                "Code": "ACAD",
                                "Name": "Acadia National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-68.24411197733804, 44.350751388328206],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 251,
                            "properties": {
                                "Code": "AMIS",
                                "Name": "Amistad National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -101.08508073664261,
                                    29.484904505888327,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 252,
                            "properties": {
                                "Code": "ASIS",
                                "Name": "Assateague Island National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-75.33257321553181, 37.90756795438505],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 253,
                            "properties": {
                                "Code": "BITH",
                                "Name": "Big Thicket National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-94.43625085653211, 30.197215743080875],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 254,
                            "properties": {
                                "Code": "BLUE",
                                "Name": "Bluestone National Scenic River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.96082026944178, 37.58996437622538],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 255,
                            "properties": {
                                "Code": "COLO",
                                "Name": "Colonial National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.63422124246252, 37.28808974044507],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 256,
                            "properties": {
                                "Code": "CURE",
                                "Name": "Curecanti National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -107.16791467838674,
                                    38.462761028472045,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 257,
                            "properties": {
                                "Code": "FRSP",
                                "Name": "Fredericksburg & Spotsylvania National Military Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.74075317610887, 38.303092430017074],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 258,
                            "properties": {
                                "Code": "GARI",
                                "Name": "Gauley River National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.00420836253853, 38.20614946938015],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 259,
                            "properties": {"Code": "GRSP", "Name": "Green Springs"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.16731623763222, 38.0238746449461],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 260,
                            "properties": {
                                "Code": "HALE",
                                "Name": "Haleakala National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -156.14709314319208,
                                    20.704512129332194,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 261,
                            "properties": {
                                "Code": "LAMR",
                                "Name": "Lake Meredith National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-101.69709843061963, 35.5958605517495],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 262,
                            "properties": {
                                "Code": "LIRI",
                                "Name": "Little River Canyon National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-85.59478107090612, 34.44652300634574],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 263,
                            "properties": {
                                "Code": "NERI",
                                "Name": "New River Gorge National River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.9897043635666, 37.84026693367752],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 264,
                            "properties": {
                                "Code": "CONG",
                                "Name": "Congaree National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.81835232616444, 33.8062043146765],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 265,
                            "properties": {
                                "Code": "BLCA",
                                "Name": "Black Canyon Of The Gunnison National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -107.72398016641485,
                                    38.577392252894334,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 266,
                            "properties": {
                                "Code": "WUPA",
                                "Name": "Wupatki National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-111.33707369508468, 35.54673649570932],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 267,
                            "properties": {
                                "Code": "LABE",
                                "Name": "Lava Beds National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-121.5213368153262, 41.761497369483116],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 268,
                            "properties": {
                                "Code": "CUVA",
                                "Name": "Cuyahoga Valley National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.5690344075238, 41.26071335500069],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 269,
                            "properties": {
                                "Code": "CAVE",
                                "Name": "Carlsbad Caverns National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-104.52776563457927, 32.15234275399143],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 270,
                            "properties": {
                                "Code": "HAVO",
                                "Name": "Hawaii Volcanoes National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-155.2118228719388, 19.32614215615518],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 271,
                            "properties": {
                                "Code": "ALFL",
                                "Name": "Alibates Flint Quarries National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-101.67207841768075, 35.58307497951212],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 272,
                            "properties": {
                                "Code": "CANA",
                                "Name": "Canaveral National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.74777307769666, 28.778213207212296],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 273,
                            "properties": {
                                "Code": "BUFF",
                                "Name": "Buffalo National River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-92.9181061671278, 35.968644202183484],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 274,
                            "properties": {
                                "Code": "MACA",
                                "Name": "Mammoth Cave National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.13090198191068, 37.197604576779035],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 275,
                            "properties": {
                                "Code": "WHIS",
                                "Name": "Whiskeytown National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.60226571677792, 40.61359940526877],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 276,
                            "properties": {
                                "Code": "COLM",
                                "Name": "Colorado National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.69205501639672, 39.05042616102539],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 277,
                            "properties": {
                                "Code": "PINN",
                                "Name": "Pinnacles National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-121.18110088326603, 36.4901310064952],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 278,
                            "properties": {
                                "Code": "APIS",
                                "Name": "Apostle Islands National Lakeshore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-90.58034402114028, 46.93618142590913],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 279,
                            "properties": {
                                "Code": "BICY",
                                "Name": "Big Cypress National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.10503529985202, 25.98591492395742],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 280,
                            "properties": {
                                "Code": "BISO",
                                "Name": "Big South Fork National River & Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.66506686797332, 36.534838847833456],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 281,
                            "properties": {
                                "Code": "BICA",
                                "Name": "Bighorn Canyon National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.02711791308913, 45.2888706719196],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 282,
                            "properties": {
                                "Code": "BLRI",
                                "Name": "Blue Ridge Parkway",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.07056465618793, 36.436499472582476],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 283,
                            "properties": {
                                "Code": "CACH",
                                "Name": "Canyon De Chelly National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-109.34038567067785, 36.0942713524947],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 284,
                            "properties": {
                                "Code": "CRLA",
                                "Name": "Crater Lake National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.13525870459277, 42.94443605194011],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 285,
                            "properties": {
                                "Code": "DINO",
                                "Name": "Dinosaur National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.8396887082428, 40.47890301270882],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 286,
                            "properties": {
                                "Code": "EBLA",
                                "Name": "Ebey's Landing National Historical Reserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.68901426667851, 48.21350903766393],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 287,
                            "properties": {
                                "Code": "ELMA",
                                "Name": "El Malpais National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-107.89027837388127, 34.91493770120391],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 288,
                            "properties": {
                                "Code": "EVER",
                                "Name": "Everglades National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.95349638622787, 25.27225616404826],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 289,
                            "properties": {
                                "Code": "GLCA",
                                "Name": "Glen Canyon National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.80357960274928,
                                    37.397962595315896,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 290,
                            "properties": {
                                "Code": "GRCA",
                                "Name": "Grand Canyon National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -112.19586332050201,
                                    36.186683141213514,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 291,
                            "properties": {
                                "Code": "GRSM",
                                "Name": "Great Smoky Mountains National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-83.77104780772574, 35.53381126341195],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 292,
                            "properties": {
                                "Code": "ILMI",
                                "Name": "Illinois & Michigan Canal National Heritage Corridor",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-88.48014499043286, 41.330758674110314],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 293,
                            "properties": {
                                "Code": "ISRO",
                                "Name": "Isle Royale National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-89.10441847731086, 47.900839582369585],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 294,
                            "properties": {
                                "Code": "LACH",
                                "Name": "Lake Chelan National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -120.70061049014323,
                                    48.382371307707096,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 295,
                            "properties": {
                                "Code": "LARO",
                                "Name": "Lake Roosevelt National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -118.72140194449733,
                                    47.908992851618656,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 296,
                            "properties": {
                                "Code": "MISS",
                                "Name": "Mississippi National River & Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-93.12760188916005, 44.91461205863678],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 297,
                            "properties": {
                                "Code": "MORA",
                                "Name": "Mount Rainier National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-121.70574507946985, 46.86055919903173],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 298,
                            "properties": {
                                "Code": "NATR",
                                "Name": "Natchez Trace Parkway",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-89.6542135890102, 32.870039949616604],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 299,
                            "properties": {
                                "Code": "NOCA",
                                "Name": "North Cascades National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-121.34755778363238, 48.83303940981537],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 300,
                            "properties": {
                                "Code": "OLYM",
                                "Name": "Olympic National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-123.6194451629227, 47.79453520449651],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 301,
                            "properties": {
                                "Code": "ROMO",
                                "Name": "Rocky Mountain National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-105.69838532231373, 40.35579839722149],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 302,
                            "properties": {
                                "Code": "ROLA",
                                "Name": "Ross Lake National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -121.28431920356763,
                                    48.652216100873474,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 303,
                            "properties": {
                                "Code": "SAGU",
                                "Name": "Saguaro National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.60831406159426,
                                    32.178836085393556,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 304,
                            "properties": {
                                "Code": "SACN",
                                "Name": "Saint Croix National Scenic River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.57867725299548, 45.98016513150317],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 305,
                            "properties": {
                                "Code": "SHEN",
                                "Name": "Shenandoah National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.67619962877342, 38.28108210674896],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 306,
                            "properties": {
                                "Code": "TIMU",
                                "Name": "Timucuan Ecological & Historic Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-81.47140832455206, 30.43110956657626],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 307,
                            "properties": {
                                "Code": "GLAC",
                                "Name": "Glacier National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-113.80079159548487, 48.68426876066877],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 308,
                            "properties": {
                                "Code": "SLBE",
                                "Name": "Sleeping Bear Dunes National Lakeshore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.01522358560105, 45.111627318517684],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 309,
                            "properties": {
                                "Code": "OBED",
                                "Name": "Obed Wild & Scenic River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-84.72244777861376, 36.08458016746933],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 310,
                            "properties": {
                                "Code": "PIRO",
                                "Name": "Pictured Rocks National Lakeshore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.46694927014178, 46.513545397114434],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 311,
                            "properties": {
                                "Code": "OZAR",
                                "Name": "Ozark National Scenic Riverways",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-91.19602595696949, 37.14718713334885],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 312,
                            "properties": {
                                "Code": "PAIS",
                                "Name": "Padre Island National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-97.34068067534453, 26.70369447679065],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 313,
                            "properties": {
                                "Code": "ARCH",
                                "Name": "Arches National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -109.59545602760868,
                                    38.707917632251544,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 314,
                            "properties": {
                                "Code": "VOYA",
                                "Name": "Voyageurs National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-92.98057129969759, 48.51716932219992],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 315,
                            "properties": {
                                "Code": "THRO",
                                "Name": "Theodore Roosevelt National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -103.45925080636415,
                                    46.953620966658086,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 316,
                            "properties": {
                                "Code": "ORPI",
                                "Name": "Organ Pipe Cactus National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.96606947567764, 32.06300513238792],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 317,
                            "properties": {
                                "Code": "DRTO",
                                "Name": "Dry Tortugas National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-82.86655423155601, 24.654395618647623],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 318,
                            "properties": {
                                "Code": "WHSA",
                                "Name": "White Sands National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -106.33507223593554,
                                    32.779133376019175,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 319,
                            "properties": {
                                "Code": "BRCA",
                                "Name": "Bryce Canyon National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-112.18266888744083, 37.58399143875251],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 320,
                            "properties": {
                                "Code": "JODR",
                                "Name": "John D Rockefeller Jr Memorial Parkway",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.72504923859016,
                                    44.088146322936595,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 321,
                            "properties": {
                                "Code": "YELL",
                                "Name": "Yellowstone National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -110.49008302275851,
                                    44.583032217213656,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 322,
                            "properties": {
                                "Code": "NIOB",
                                "Name": "Niobrara National Scenic River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-99.9288902848823, 42.7689888618181],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 323,
                            "properties": {
                                "Code": "GRTE",
                                "Name": "Grand Teton National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-110.70546656038158, 43.81853565368195],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 324,
                            "properties": {
                                "Code": "CHCU",
                                "Name": "Chaco Culture National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -107.95869749995461,
                                    36.052810509413575,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 325,
                            "properties": {
                                "Code": "BADL",
                                "Name": "Badlands National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-102.39394509554067, 43.8340624087368],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 326,
                            "properties": {
                                "Code": "ZION",
                                "Name": "Zion National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -112.95443162869537,
                                    37.255709497131065,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 327,
                            "properties": {
                                "Code": "MEVE",
                                "Name": "Mesa Verde National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-108.50092888589481, 37.22351315320654],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 328,
                            "properties": {
                                "Code": "GRBA",
                                "Name": "Great Basin National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -114.25797817448695,
                                    38.946173783127065,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 329,
                            "properties": {
                                "Code": "CARE",
                                "Name": "Capitol Reef National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -111.00329294577273,
                                    37.795992535017426,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 330,
                            "properties": {
                                "Code": "CANY",
                                "Name": "Canyonlands National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -109.88314625527481,
                                    38.272072876214835,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 331,
                            "properties": {
                                "Code": "GRSA",
                                "Name": "Great Sand Dunes National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -105.57832630519154,
                                    37.759942701007226,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 332,
                            "properties": {
                                "Code": "LAVO",
                                "Name": "Lassen Volcanic National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-121.41212664904383, 40.48622026090819],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 333,
                            "properties": {
                                "Code": "GUIS",
                                "Name": "Gulf Islands National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-86.90996505020482, 30.37306477109711],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 334,
                            "properties": {
                                "Code": "PEFO",
                                "Name": "Petrified Forest National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-109.67471774572405, 34.98868180401879],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 335,
                            "properties": {
                                "Code": "BISC",
                                "Name": "Biscayne National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-80.21830159269447, 25.469689246647114],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 336,
                            "properties": {
                                "Code": "GUMO",
                                "Name": "Guadalupe Mountains National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -104.88434717034703,
                                    31.923384209391674,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 337,
                            "properties": {
                                "Code": "WICA",
                                "Name": "Wind Cave National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-103.42877641689412, 43.60787178123641],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 338,
                            "properties": {
                                "Code": "ALAG",
                                "Name": "Alagnak Wild River",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-155.87871917864993, 59.02764908262888],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 339,
                            "properties": {
                                "Code": "BIBE",
                                "Name": "Big Bend National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -103.22978967302261,
                                    29.298177668897967,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 340,
                            "properties": {
                                "Code": "CRMO",
                                "Name": "Craters Of The Moon National Monument & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-113.4416200510779, 43.28356162340532],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 341,
                            "properties": {
                                "Code": "DEVA",
                                "Name": "Death Valley National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-117.13511154435771, 36.48741910067162],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 342,
                            "properties": {
                                "Code": "REDW",
                                "Name": "Redwood National and State Parks",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-124.00482968014182, 41.27702956462916],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 343,
                            "properties": {
                                "Code": "GOGA",
                                "Name": "Golden Gate National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -122.55146603311029,
                                    37.862648681885084,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 344,
                            "properties": {
                                "Code": "YOSE",
                                "Name": "Yosemite National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-119.55600729459782, 37.84893656911814],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 345,
                            "properties": {
                                "Code": "SAMO",
                                "Name": "Santa Monica Mountains National Recreation Area",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-118.910464470296, 34.10214700522728],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 346,
                            "properties": {
                                "Code": "PORE",
                                "Name": "Point Reyes National Seashore",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-122.86492337132071, 38.05557132213282],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 347,
                            "properties": {
                                "Code": "KICA",
                                "Name": "Kings Canyon National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-118.59384064032848, 36.8749421087923],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 348,
                            "properties": {
                                "Code": "JOTR",
                                "Name": "Joshua Tree National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-116.15907084356105, 33.98096522850808],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 349,
                            "properties": {
                                "Code": "MOJA",
                                "Name": "Mojave National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-115.5570103212086, 35.10066435137423],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 350,
                            "properties": {
                                "Code": "SEKI",
                                "Name": "Sequoia & Kings Canyon National Parks",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-118.5752011004094, 36.50785282265928],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 351,
                            "properties": {
                                "Code": "CHIS",
                                "Name": "Channel Islands National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-119.7251698451474, 34.00392978229205],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 352,
                            "properties": {
                                "Code": "ANIA",
                                "Name": "Aniakchak National Monument & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-158.04745719101055, 56.84368466021347],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 353,
                            "properties": {
                                "Code": "BELA",
                                "Name": "Bering Land Bridge National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-164.4087917037424, 65.96080330575823],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 354,
                            "properties": {
                                "Code": "CAKR",
                                "Name": "Cape Krusenstern National Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-163.50428603026538, 67.41526306364067],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 355,
                            "properties": {
                                "Code": "DENA",
                                "Name": "Denali National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-151.05263550282112, 63.29777436004586],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 356,
                            "properties": {
                                "Code": "GAAR",
                                "Name": "Gates Of The Arctic National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-153.26413231698794, 67.9192854407937],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 357,
                            "properties": {
                                "Code": "GLBA",
                                "Name": "Glacier Bay National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-136.84071732838277, 58.80086474447531],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 358,
                            "properties": {
                                "Code": "KATM",
                                "Name": "Katmai National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -155.01341050350874,
                                    58.622573966764584,
                                ],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 359,
                            "properties": {
                                "Code": "KEFJ",
                                "Name": "Kenai Fjords National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-149.88152448868524, 59.95389688763184],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 360,
                            "properties": {
                                "Code": "KOVA",
                                "Name": "Kobuk Valley National Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-159.06308334658615, 67.28263652770183],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 361,
                            "properties": {
                                "Code": "LACL",
                                "Name": "Lake Clark National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-153.6018441528228, 60.64679690935658],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 362,
                            "properties": {
                                "Code": "NOAT",
                                "Name": "Noatak National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-161.1594590060686, 68.09280652513834],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 363,
                            "properties": {
                                "Code": "WRST",
                                "Name": "Wrangell - St Elias National Park & Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-142.60357111369407, 61.41843937955613],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 364,
                            "properties": {
                                "Code": "YUCH",
                                "Name": "Yukon - Charley Rivers National Preserve",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-142.79641659169639, 65.09350238346386],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 365,
                            "properties": {
                                "Code": "APPA",
                                "Name": "Appalachian National Scenic Trail",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-72.7402535097141, 43.691650670773555],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 366,
                            "properties": {
                                "Code": "MAMC",
                                "Name": "Mary McLeod Bethune Council House National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.03098188969467, 38.908022591832854],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 367,
                            "properties": {
                                "Code": "NACE",
                                "Name": "National Capital Parks-East",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.09410104237618, 38.67910430710282],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 368,
                            "properties": {"Code": "FODU", "Name": "Fort Dupont Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.94968629399797, 38.87819616831813],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 369,
                            "properties": {
                                "Code": "FRDO",
                                "Name": "Frederick Douglass National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.98510303343785, 38.862836277772715],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 370,
                            "properties": {
                                "Code": "GWMP",
                                "Name": "George Washington Memorial Parkway",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.05361153357251, 38.71381953074352],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 371,
                            "properties": {
                                "Code": "OXHI",
                                "Name": "Oxon Cove Park & Oxon Hill Farm",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.0230745539023, 38.79702173265857],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 372,
                            "properties": {"Code": "PISC", "Name": "Piscataway Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.06840167129472, 38.68456179269082],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 373,
                            "properties": {"Code": "GREE", "Name": "Greenbelt Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.90602165862857, 38.98055126072522],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 374,
                            "properties": {
                                "Code": "WHHO",
                                "Name": "President's Park (White House)",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.03656807555457, 38.895430023853166],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 375,
                            "properties": {
                                "Code": "KEAQ",
                                "Name": "Kenilworth Park & Aquatic Gardens",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.94934274387278, 38.912783049344085],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 376,
                            "properties": {"Code": "ROCR", "Name": "Rock Creek Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04621414691562, 38.96262227660261],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 377,
                            "properties": {
                                "Code": "MEHI",
                                "Name": "Meridian Hill Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.0357398248935, 38.92108758653459],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 378,
                            "properties": {
                                "Code": "OLST",
                                "Name": "The Old Stone House",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.06029340095944, 38.905699664469374],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 379,
                            "properties": {"Code": "LINC", "Name": "Lincoln Memorial"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04448622323585, 38.88852231375846],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 380,
                            "properties": {
                                "Code": "FOTH",
                                "Name": "Ford's Theatre National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02564352207143, 38.89669637068724],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 381,
                            "properties": {
                                "Code": "PAAV",
                                "Name": "Pennsylvania Avenue National Historic Site",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02127350293809, 38.89358295687963],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 382,
                            "properties": {
                                "Code": "WAMO",
                                "Name": "Washington Monument",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.03582078295108, 38.88858816206582],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 383,
                            "properties": {
                                "Code": "THJE",
                                "Name": "Thomas Jefferson Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.03632112651766, 38.88102284916951],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 384,
                            "properties": {"Code": "NAMA", "Name": "National Mall"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02924888507606, 38.874025510015194],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 385,
                            "properties": {
                                "Code": "NWWM",
                                "Name": "National World War II Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04040758984885, 38.88911940785463],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 386,
                            "properties": {
                                "Code": "VIVE",
                                "Name": "Vietnam Veterans Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04748475145276, 38.89080864030152],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 387,
                            "properties": {
                                "Code": "KOWA",
                                "Name": "Korean War Veterans Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04759263185332, 38.88781369849817],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 388,
                            "properties": {
                                "Code": "COGA",
                                "Name": "Constitution Gardens",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04450470809408, 38.89098652644936],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 389,
                            "properties": {
                                "Code": "FRDE",
                                "Name": "Franklin Delano Roosevelt Memorial",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.04296571547219, 38.883337520611825],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 390,
                            "properties": {"Code": "HAHA", "Name": "Harmony Hall"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.00377059837496, 38.74646346547231],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 391,
                            "properties": {"Code": "FOFO", "Name": "Fort Foote Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02771696848369, 38.767984867610295],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 392,
                            "properties": {"Code": "ANAC", "Name": "Anacostia Park"},
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.94197642918564, 38.91343719489454],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 393,
                            "properties": {
                                "Code": "BAWA",
                                "Name": "Baltimore-Washington Parkway",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-76.79491878920412, 39.101543051442995],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 394,
                            "properties": {
                                "Code": "CHOH",
                                "Name": "Chesapeake & Ohio Canal National Historical Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-78.00883124839731, 39.60727231050386],
                            },
                        },
                        {
                            "type": "Feature",
                            "id": 395,
                            "properties": {
                                "Code": "FOWA",
                                "Name": "Fort Washington Park",
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [-77.02875305317842, 38.712184675189576],
                            },
                        },
                    ],
                },
            }
        )
        self.image_generated(data)
