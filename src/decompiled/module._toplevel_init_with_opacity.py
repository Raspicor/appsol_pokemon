# module._toplevel_init_with_opacity
# source line 4479
# Recovered from bytecode; default argument values are not shown.

def _toplevel_init_with_opacity(self, *args, **kwargs):
    _ORIGINAL_TOPLEVEL_INIT(*{
        **kwargs })

    try:
        _ALL_OPEN_TOPLEVELS.append(self)
        if _APP_INSTANCE is not None:
            alpha = _APP_INSTANCE.state.get('window_opacity', 1)
            if alpha < 0.999:
                self.attributes('-alpha', alpha)
                return None
            return None
        return None
    except Exception:
        return None
