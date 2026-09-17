# module.PetApp._code_build_ui._refresh_ult
# source line 13062
# Recovered from bytecode; default argument values are not shown.

def _refresh_ult():
    if ult_btn is None:
        return None
    used = None['p_active'] in gctx['p_ult_used']
    limit = gctx.get('ult_limit', 0)

    try:
        if limit:
        
            try:
                left = max(0, limit - gctx.get('ult_use_count', 0))
                if left <= 0:
                    ok = False
                    text = '✨ 필살기(다 씀)'
                else:
                    ok = not gctx['flags']['locked']
                    text = f'''✨ 필살기 ({left}/{limit})'''
                ult_btn.configure(text = text, state = 'normal' if ok else 'disabled')
                return None
            
                try:
                    if used:
                    
                        try:
                            pass
                        if not used:
                        
                            try:
                                if gctx['flags']['locked']:
                                
                                    try:
                                        pass
                                    return None
                                    except Exception:
                                        ult_btn.configure
                                        return None
