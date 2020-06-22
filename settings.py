from typing import Dict, List, Optional, Union
from flags import FLAGS


class Settings:

  def __init__(self,
               mode: str = 'full',
               debug_mode: bool = False,
               custom_flags: Optional[Dict[str, bool]] = None) -> None:
    self._mode = mode
    self._debug_mode = debug_mode
    self._custom_flags: Dict[str, bool] = {}
    if custom_flags is not None:
      self._custom_flags.update(custom_flags)
    for flag in FLAGS:
      # If we're in full randomize mode, override all the flags to on.
      if mode == 'full':
        self._custom_flags[flag[0]] = True
      else:
        self._custom_flags.setdefault(flag[0], False)
      self._custom_flags.setdefault(flag[0], True)

  def custom_flags_to_json(self) -> List[bool]:
    """Return JSON serialization of custom flags."""
    return [self._custom_flags[flag[0]] for flag in FLAGS]

  @property
  def mode(self) -> str:
    return self._mode

  @property
  def debug_mode(self) -> bool:
    return self._debug_mode

  def get_flag(self, flag: str) -> Union[str, bool]:
    """Get a specific custom flag."""
    return self._custom_flags.get(flag, True)

  def __getattr__(self, item: str) -> bool:
    """Fall-back to get the custom flags as if they were class attributes."""
    if self._mode == 'full':
      return True
    if item in self._custom_flags:
      return self._custom_flags[item]
    raise AttributeError(item)
