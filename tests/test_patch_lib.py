from patch_lib import patch_document


def test_not_modified_document():
    document = patch_document({"test": "test"}, [])
    assert document == {"test": "test"}


def test_add():
    document = patch_document({"test": "test"}, [
        {"op": "add",
         "path": "/test2",
         "value": "test2"}
    ])
    assert document == {"test": "test", "test2": "test2"}


def test_remove():
    document = patch_document({"test": "test"}, [
        {"op": "remove",
         "path": "/test"}
    ])
    assert document == {}


def test_replace():
    document = patch_document({"test": "test"}, [
        {"op": "replace",
         "path": "/test",
         "value": "test2"}
    ])
    assert document == {"test": "test2"}


def test_copy():
    document = patch_document({"test": "test"}, [
        {"op": "copy",
         "path": "/test2",
         "from": "/test"}
    ])
    assert document == {"test": "test", "test2": "test"}


def test_move():
    document = patch_document({"test": "test"}, [
        {"op": "move",
         "path": "/test2",
         "from": "/test"}
    ])
    assert document == {"test2": "test"}

###


def test_add2():
    document = patch_document({"test": "test"}, [
        {"op": "add",
         "path": "/test2/test2",
         "value": "test2"}
    ])
    assert document == {"test": "test", "test2/test2": "test2"}


def test_remove2():
    document = patch_document({"test/test": "test"}, [
        {"op": "remove",
         "path": "/test/test"}
    ])
    assert document == {}


def test_replace2():
    document = patch_document({"test/test": "test"}, [
        {"op": "replace",
         "path": "/test/test",
         "value": "test2"}
    ])
    assert document == {"test/test": "test2"}


def test_copy2():
    document = patch_document({"test": "test"}, [
        {"op": "copy",
         "path": "/test2/test2",
         "from": "/test"}
    ])
    assert document == {"test": "test", "test2/test2": "test"}


def test_move2():
    document = patch_document({"test/test": "test"}, [
        {"op": "move",
         "path": "/test2/test2",
         "from": "/test/test"}
    ])
    assert document == {"test2/test2": "test"}
