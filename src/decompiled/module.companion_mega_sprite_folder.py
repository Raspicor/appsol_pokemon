# module.companion_mega_sprite_folder
# source line 529
# Recovered from bytecode; default argument values are not shown.

def companion_mega_sprite_folder(entry):
    if not entry:
        return None
    base = None.get('en')
    if not base:
        return None
    for suffix in None:
        candidate = base + suffix
        for search_base in SPRITE_SEARCH_DIRS:
            if os.path.isdir(os.path.join(search_base, candidate)):
            
            
                return None, SPRITE_SEARCH_DIRS, candidate
    return None
    except Exception:
        continue
