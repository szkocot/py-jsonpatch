class PatchError(Exception):
    pass


def patch_document(document, commands):

    for command in commands:

        location = command["path"].split("/")[1]

        if command["op"] is "add":
            document[location] = command["value"]
        elif command["op"] is "remove":
            del document[location]
        elif command["op"] is "replace":
            document[location] = command["value"]
        elif command["op"] is "copy":
            location_from = command["from"].split("/")[1]
            document[location] = document[location_from]
        elif command["op"] is "move":
            location_from = command["from"].split("/")[1]
            document[location] = document[location_from]
            del document[location_from]
    return document
