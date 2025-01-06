# sudo apt-get install sox libsox-fmt-mp3

import requests
import json
import os



def tts_eo(path, name, text):
    source      = "temp.mp3"
    destination = f"{path}/{name}"

    payload = {
        "text": text,
        "voice": "female",
        "rules": json.dumps({
            "letters": {
                "a": "a",
                "b": "b",
                "c": "ts",
                "ĉ": "cz",
                "d": "d",
                "e": "e",
                "f": "f",
                "g": "g",
                "ĝ": "dż",
                "h": "h",
                "ĥ": "ch",
                "i": "ij",
                "j": "y",
                "ĵ": "rz",
                "k": "k",
                "l": "l",
                "m": "m",
                "n": "n",
                "o": "o",
                "p": "p",
                "r": "r",
                "s": "s",
                "ŝ": "sz",
                "t": "t",
                "u": "u",
                "ŭ": "ł",
                "v": "w",
                "z": "z"
            },
            "fragments": [
                { "match": "tsx", "replace": "cz" },
                { "match": "gx", "replace": "dż" },
                { "match": "hx", "replace": "ch" },
                { "match": "yx", "replace": "rz" },
                { "match": "sx", "replace": "sz" },
                { "match": "ux", "replace": "ł" },
                { "match": "atsij", "replace": "atssij" },
                { "match": "ide\b", "replace": "ijde" },
                { "match": "io\b", "replace": "ijo" },
                { "match": "ioy\b", "replace": "ijoj" },
                { "match": "ioyn\b", "replace": "ijojn" },
                { "match": "feyo\b", "replace": "fejo" },
                { "match": "feyoy\b", "replace": "feyoj" },
                { "match": "feyoyn\b", "replace": "feyoj" },
                { "match": "^ekzij", "replace": "ekzji" },
                { "match": "tssijl", "replace": "tssil" },
                { "match": "ijuy", "replace": "iuyy" },
                { "match": "ijeh", "replace": "ije" },
                { "match": "sijlo", "replace": "ssilo" },
                { "match": "^sij", "replace": "syy" },
                { "match": "tsij", "replace": "tssij" },
                { "match": "sij", "replace": "ssij" },
                { "match": "sssij", "replace": "ssij" },
                { "match": "rijpozij", "replace": "ryypozyj" },
                { "match": "zijs", "replace": "zyjs" }
            ],
            "overrides": [
                { "eo": "ok", "pl": "ohk" },
                { "eo": "s-ro", "pl": "sjijnjoro" },
                { "eo": "s-ino", "pl": "sjijnjorijno" },
                { "eo": "ktp", "pl": "ko-to-po" },
                { "eo": "k.t.p", "pl": "ko-to-po" },
                { "eo": "atm", "pl": "antałtagmeze" },
                { "eo": "ptm", "pl": "posttagmeze" },
                { "eo": "bv", "pl": "bonvolu" }
            ],
            "numbers": {
                "0": "nulo",
                "1": "unu",
                "2": "du",
                "3": "trij",
                "4": "kvar",
                "5": "kvijn",
                "6": "ses",
                "7": "sep",
                "8": "ohk",
                "9": "nał",
                "10": "dek",
                "100": "tsent",
                "1000": "mijl",
                "1000000": "mijlijono"
            }
        })
    }

    response = requests.post('https://api.parol.martinrue.com/speak', data=json.dumps(payload))
    url = json.loads(response.text)["url"]
    headers = {
        "Accept": "audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5",
        "Range": "bytes=0-",
        "Referer": "https://parol.martinrue.com/"
    }

    response = requests.get(url, headers=headers)
    with open(source, "wb") as file:
        file.write(response.content)

    # convert from mp3 @ 22050 kHz to wav @ 32000 kHz (required by EdgeTX)
    print(f'sox {source} -r 32000 {destination}')
    os.system(f'sox {source} -r 32000 {destination}')



with open("eo-EO.csv") as file:
    lines = file.readlines()

for line in lines[1:]:
    string_id, source_text, translation, context, path, filename = [field.replace('"', '') for field in line.split(',')]
    path = "SOUNDS/en/" + path
    print(f'Generating {path}/{filename}...')
    tts_eo(path, filename, translation)

os.system("rm temp.mp3")
