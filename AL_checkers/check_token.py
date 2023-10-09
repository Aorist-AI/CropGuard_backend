from tokenz.tokenz import get_id


def check(header):
    users_id = get_id(header)
    if not str(users_id).isdigit():
        return {"status": 0, "users_id": 0}
    else:
        return {"status": 1, "users_id": users_id}
