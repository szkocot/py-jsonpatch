class PatchError(Exception):
    pass


class DictQuery(dict):
    def get(self, path, default=None):
        keys = path.split("/")
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)

            if not val:
                break

        return val


def patch_document(document, commands):

    document = DictQuery(document)

    for command in commands:

        location = command["path"][1:]

        if command["op"] is "add":
            document[location] = command["value"]
        elif command["op"] is "remove":
            del document[location]
        elif command["op"] is "replace":
            document[location] = command["value"]
        elif command["op"] is "copy":
            location_from = command["from"][1:]
            document[location] = document[location_from]
        elif command["op"] is "move":
            location_from = command["from"][1:]
            document[location] = document[location_from]
            del document[location_from]
    return document
