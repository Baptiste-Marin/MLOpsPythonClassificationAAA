import argparse
import asyncio
from pathlib import Path
import shutil

import json
import os

# from ecotag_sdk.ecotag import (
#     ApiInformation,
#     download_annotations,
#     get_access_token,
# )


parser = argparse.ArgumentParser("download_labels")
parser.add_argument("--access_token", type=str, default="")
parser.add_argument("--project_name", type=str, default="triple-a-project")
parser.add_argument("--local_json_path", type=str, default="inputs/movie-trailer-annotations.json")
# parser.add_argument(
#     "--api_url",
#     type=str,
#     default="https://axaguildev-ecotag.azurewebsites.net/api/server",
# )
# parser.add_argument(
#     "--token_endpoint",
#     type=str,
#     default="https://demo.duendesoftware.com/connect/token",
# )
# parser.add_argument("--client_id", type=str, default="m2m")
# parser.add_argument("--client_secret", type=str, default="secret")
args = parser.parse_args()

#access_token = args.access_token
project_name = args.project_name
local_json_path = args.local_json_path
print("args json path -- ", args.local_json_path)
#api_url = args.api_url
# token_endpoint = args.token_endpoint
# client_id = args.client_id
# client_secret = args.client_secret

# if access_token == "":
#     access_token = get_access_token(token_endpoint, client_id, client_secret)


# async def main():
#     base_path = Path(__file__).resolve().parent
#     dataset_path = base_path / "labels"
#     filename = "movie-trailer-annotations.json"
#     dataset_path.mkdir(exist_ok=True)

#     api_information = ApiInformation(api_url=api_url, access_token=access_token)
#     await download_annotations(
#         api_information, project_name, str(dataset_path), filename
#     )

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

print("[DEBUG] Un chemin local pour le json a été spécifié : ", local_json_path)
print("[DEBUG] Chemin actuel : ", os.getcwd())
print("[DEBUG] Répertoire inputs existant : ", os.path.exists("inputs"))
print("[DEBUG] Répertoire inputs : ", os.listdir("inputs"))
print("[DEBUG] Fichier local existant sans ./: ", os.path.exists(local_json_path))
print("[DEBUG] Fichier local existant avec ./ : ", os.path.exists("./" + local_json_path))

if local_json_path and os.path.exists("./" + local_json_path):
    print("[DEBUG] Le chemin local pour le json est valide.")
    base_path = Path(__file__).resolve().parent
    dataset_path = base_path / "labels"
    dataset_path.mkdir(exist_ok=True)

    destination_file = dataset_path / "movie-trailer-annotations.json"
    shutil.move("./" + local_json_path, destination_file)
    

    print("[DEBUG] Le fichier a été déplacé dans le répertoire de travail.")
else: 
    print("marche pas frr")
