def are_required_filled(args: dict, params: dict) -> bool:
    for k in params.keys():
        if params[k]["required"] and str(args[k]) == "<class 'inspect._empty'>":
            return False

    return True

