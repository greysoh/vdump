from os import listdir, mkdir, rename
import json

import yt_dlp

ydl_opts = {}

print("Loading ytmanifest.json...")
manifest_data = ""

with open("ytmanifest.json", "r", encoding="utf8") as f:
  manifest_data = f.read()

manifest = json.loads(manifest_data)

try:
  mkdir("out")
except FileExistsError:
  print("INFO: Ouput directory already exists!")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  for i, entry in enumerate(manifest):
    if entry["isDownloaded"]:
      continue

    info = ydl.extract_info(entry["url"], download=False)
    info_sanitized = ydl.sanitize_info(info)

    # Update the entry with the description -- Simple web parsing can't get us THAT far
    manifest[i]["description"] = info_sanitized["description"]

    # Let's download stuff.
    err = ydl.download(entry["url"])
    if err:
      raise Exception("YTDL error occurred!")
    
    # Move stuff because YoutubeDL is stupid.
    file_list = [f for f in listdir(".") if info_sanitized["id"] in f]
    if len(file_list) == 0:
      raise Exception("Could not find downloaded file.")
    
    file_name = file_list[0]
    rename(file_name, f"out/{i}.mp4")

    manifest[i]["isDownloaded"] = True

    # FIXME: This is quite expensive for computation...
    with open("ytmanifest.json", "w", encoding="utf8") as f:
      f.write(json.dumps(manifest))

print("All done! Goodbye.")
exit()