from typing import Union, Optional, Any, Dict, List


def func_1(line_str: Optional[str], world_list: List, aaa: Any, my_dict: Dict[int, str], bbb: Union[str, int]) -> dict:
    result = {}
    ...
    return result


def func_2(line_str: str | None, world_list: list[str | int,], aaa: Any, my_dict: dict[int, str], bbb: str | int) -> dict:
    result = {}
    ...
    return result
