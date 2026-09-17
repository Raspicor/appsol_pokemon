# module.PetApp._rocket_battle_finish
# source line 14192
# Recovered from bytecode; default argument values are not shown.

def _rocket_battle_finish(self, gctx, won, conceded):
    flags = gctx['flags']
    if flags['ended']:
        return None
    flags['ended'] = None
    flags['locked'] = True
    win = gctx['win']

    try:
        win.destroy()
        if won:
            self.state['rocket_defeat_count'] = int(self.state.get('rocket_defeat_count', 0)) + 1
            gold = rocket_ambush_reward_gold(self.state['rocket_defeat_count'])
            title_msgs = self._earn_gold(gold, source = 'rocket')
            self.save_state()
            text = f'''🎉 로켓단을 격퇴했다! 💰{gold}골드 획득! (누적 격퇴 {self.state['rocket_defeat_count']}회)'''
            if title_msgs:
                text += '\n\n' + '\n'.join(title_msgs)
            None('PikaPet', text)
            return None
        if not None:
            None('PikaPet', '로켓단에게 당했다... 하지만 걱정 마세요, 아무 불이익도 없어요! 다음에 다시 도전해봐요.')
            return None
        return None
    except Exception:
        continue
