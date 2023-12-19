from sentinelhub import (
    SHConfig,
    SentinelHubRequest,
    MimeType,
    CRS,
    BBox,
    SentinelHubDownloadClient,
    DataCollection,
    bbox_to_dimensions,
)
from datetime import datetime
from PIL import Image
import numpy as np


class SatelliteImageDownloader:
    def __init__(self, instance_id):
        self.config = SHConfig()
        self.config.instance_id = instance_id
        self.config.sh_client_id = "fc4293da-06a0-4895-b365-ce968c93286c"
        self.config.sh_client_secret = "KC3BFLK1sJowjUQr4g5gif003yXtYhlN"

    def download_image(self, coords, date, file_path):
        bbox = BBox(bbox=coords, crs=CRS.WGS84)
        size = bbox_to_dimensions(bbox, resolution=10)
    
        request = SentinelHubRequest(
            evalscript="""
                //VERSION=3
                function setup() {
                    return {
                        input: ["B02", "B03", "B04"],
                        output: { bands: 3 }
                    };
                }
    
                function evaluatePixel(sample) {
                    return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
                }
            """,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L2A,
                    time_interval=(date, date),
                )
            ],
            responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
            bbox=bbox,
            size=size,
            config=self.config,
        )
    
        image = request.get_data()[0]
        im = Image.fromarray(np.uint8(image))
        im.save(file_path)
