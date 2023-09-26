from tokenz.tokens import get_id


def check(header):
    user_id = get_id(header)
    if not str(user_id).isdigit():
        return {"status": 0, "user_id": 0}
    else:
        return {"status": 1, "user_id": user_id}
