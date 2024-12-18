from collections.abc import Mapping

PropValue = str | int | bool | None
Props = Mapping[str, PropValue | list[PropValue]]
