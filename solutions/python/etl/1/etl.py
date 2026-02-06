def transform(legacy_data):
    new_data = {}
    for key in legacy_data:
        for letter in legacy_data[key]:
            new_data.setdefault(letter.lower(), key)
    return new_data