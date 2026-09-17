# module.PetApp.open_pvp_battle._end_battle
# source line 18100
# Recovered from bytecode; default argument values are not shown.

def _end_battle(won, reason):
    if b['ended']:
        return None
    b['ended'] = None

    try:
        atk_btn.configure(state = 'disabled')
        give_btn.configure(state = 'disabled')
        if won is True:
            None('승리')
            if not b.get('opp_name'):
                b.get('opp_name')
            None('PikaPet', f'''🎉 승리! {'상대'}를 이겼어요!''' + f'''\n{reason}''' if reason else '')
            return None
        if None is False:
            None('패배')
            if not b.get('opp_name'):
                b.get('opp_name')
            None('PikaPet', f'''😢 패배... {'상대'}에게 졌어요.''' + f'''\n{reason}''' if reason else '')
            return None
        if not reason:
            reason
        None('PikaPet', '대결이 중단됐어요.')
        return None
    except Exception:
        continue
