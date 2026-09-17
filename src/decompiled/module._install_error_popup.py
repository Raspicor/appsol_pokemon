# module._install_error_popup
# source line 18999
# Recovered from bytecode; default argument values are not shown.

def _install_error_popup(root):
    import traceback as _tb
    _err_state = {
        'showing': False }

    def _handler(exc, val, tb):
        ''
    
        try:
            msg = ''.join(_tb.format_exception(exc, val, tb))
            if 'invalid command name' in str(val):
                return None
            if None['showing']:
                return None
            _err_state['showing'] = None
        
            try:
                None('PikaPet 오류', '방금 누른 동작에서 오류가 발생했어요.\n이 내용을 스크린샷으로 캡처해서 알려주시면 바로 고칠 수 있어요:\n\n' + msg[-1500:])
                _err_state['showing'] = False
                return None
                except Exception:
                    msg = f'''{exc}: {val}'''
                    continue
            except Exception:
            
                try:
                    continue
                
                    try:
                        pass
                    except:
                        _err_state['showing'] = False






    try:
        root.report_callback_exception = _handler
        return None
    except Exception:
        return None
