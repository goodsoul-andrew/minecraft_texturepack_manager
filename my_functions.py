from io import BytesIO


def from_list_to_dict(lst, item):
    d = dict()
    for el in lst:
        d[el] = item
    return d


class TexturePackSettings:
    def __init__(self):

        def from_list_to_dict_bool(lst):
            return from_list_to_dict(lst, False)

        self.parameters = from_list_to_dict_bool(["name", "version", "description"])
        self.assets = from_list_to_dict_bool(["blockstates", "font", "lang", "models", "particles", "texts", "textures"])
        self.models = from_list_to_dict_bool(["block", "item"])
        temp = ["block", "colormap", "entity", "environment", "font", "environment", "gui",
                "item", "map", "misc", "mob_effect", "models", "painting", "particle"]
        self.textures = from_list_to_dict_bool(temp)
        self.texts = from_list_to_dict_bool(["credits", "end", "postcredits", "splashes"])



def create_pack_mcmeta(path, version, description):
    p = path + "/" + "pack.mcmeta"

    v = ['1.6.1 - 1.8.9', '1.9 - 1.10.2', '1.11 - 1.12.2', '1.13 - 1.14.4',
         '1.15 - 1.16.1', '1.16.2 - 1.16.5', '1.17 - 1.17.1', '1.18']
    pack_format = str(v.index(version) + 1)

    with open(p, "w") as pack_mcmeta:
        text = '{\n  "pack": {\n     "pack_format":'
        text += pack_format
        text += ',\n     "description": "'
        text += description
        text += '"\n  }\n}'
        #print(text)
        pack_mcmeta.write(text)


def copy_icon(path, new_path):
    with open(new_path, "wb") as new:
        with open(path, "rb") as old:
            temp = b""
            for b in old:
                temp += b
            new.write(BytesIO(temp).getbuffer())


