# This file is part of stable-diffusion-webui (https://github.com/sd-webui/stable-diffusion-webui/).

# Copyright 2022 sd-webui team.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
# base webui import and utils.
from scripts.sd_utils import *
# from scripts.modeldnld import Models
# streamlit imports


#other imports
import pandas as pd
from io import StringIO

# Temp imports 


# end of imports
#---------------------------------------------------------------------------------------------------------------

def layout():
    #search = st.text_input(label="Search", placeholder="Type the name of the model you want to search for.", help="")

    csvString = f"""
                    ,Stable Diffusion v1.4            , ./models/ldm/stable-diffusion-v1               , https://huggingface.co/CompVis/stable-diffusion-v-1-4-original                  
                    ,GFPGAN v1.4                      , ./models/gfpgan                                , https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth
                    ,RealESRGAN_x4plus                , ./models/realesrgan                            , https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth            
                    ,RealESRGAN_x4plus_anime_6B       , ./models/realesrgan                            , https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth 
                    ,Waifu Diffusion v1.2             , ./models/custom                                , https://huggingface.co/hakurei/waifu-diffusion
                    ,Waifu Diffusion v1.2 Pruned      , ./models/custom                                , https://huggingface.co/crumb/pruned-waifu-diffusion
                    ,TrinArt Stable Diffusion v2      , ./models/custom                                , https://huggingface.co/naclbit/trinart_stable_diffusion_v2
                    ,Stable Diffusion Concept Library , ./models/custom/sd-concepts-library            , https://github.com/sd-webui/sd-concepts-library
                    ,Blip Model                       , ./models/blip                                  , https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model*_base_caption.pth
                    """
    colms = st.columns((1, 3, 5, 5))
    columns = ["№",'Model Name','Save Location','Download Link']

    # Convert String into StringIO
    csvStringIO = StringIO(csvString)
    df = pd.read_csv(csvStringIO, sep=",", header=None, names=columns)		

    for col, field_name in zip(colms, columns):
        # table header
        col.write(field_name)

    for x, model_name in enumerate(df["Model Name"]):
        col1, col2, col3, col4 = st.columns((1, 3, 4, 6))
        col1.write(x)  # index
        col2.write(df['Model Name'][x])
        col3.write(df['Save Location'][x])
        col4.write(df['Download Link'][x])    

    # mdldnld.st_ui()

    # if st.button("Stable Diffusion"):
    #     Models.modelSD()

    # if st.button("RealESRGAN"):
    #     Models.realESRGAN()

    # if st.button("GFPGAN"):
    #     Models.GFPGAN()

    # if st.button("Latent Diffusion"):
    #     Models.modelLD()

    # if st.button("SD Concept Lib"):
    #     Models.SD_conLib()

    # if st.button("Blip"):
    #     Models.modelBlip()

    # if st.button("Waifu Diffusion"):
    #     Models.modelWD()

    # if st.button("Waifu Pruned"):
    #     Models.modelWDP()

    # if st.button("TrinArt SD"):
    #     Models.modelTSD()