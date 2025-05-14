def filter_dict(user_dict):
    filtered_dict = {}
    for key, value in user_dict.items():
        if value:
            filtered_dict[key] = value
    return filtered_dict