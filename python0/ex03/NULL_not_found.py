from typing import Any


def NULL_not_found(object: Any) -> int:
    obj_type = type(object)

    # is はメモリ上の同じ実体かどうかを判定(シングルトン定数)
    if object is None:  # None == NULL(Clang)
        print(f"Nothing: {object} {obj_type}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {obj_type}")
    elif object is False:  # bool は int の子クラスのため is で判断
        print(f"Fake: {object} {obj_type}")
    elif object == 0 and obj_type is int:  # type(x) is int(class)
        print(f"Zero: {object} {obj_type}")
    elif object == "" and obj_type is str:
        print(f"Empty: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1

    return 0
