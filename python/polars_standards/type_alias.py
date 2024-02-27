from __future__ import annotations
from typing import Literal
import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:  # 3.9, 3.8
    from typing_extensions import TypeAlias


# DetrendMethod: TypeAlias = Literal["linear", "mean"]