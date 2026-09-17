# module.PetApp._check_gen_master_titles
# source line 14888
# Recovered from bytecode; default argument values are not shown.

def _check_gen_master_titles(self):
    msgs = []
    gen_names = {
        9: '9세대',
        8: '8세대',
        7: '7세대',
        6: '6세대',
        5: '5세대',
        4: '4세대(신오)',
        3: '3세대(호연)',
        2: '2세대(성도)',
        1: '1세대(관동)' }
    best = self.state.get('inf_meter_best', { })
    for mode in INF_METER_MODES:
        for gen in range(1, 10):
            tid = master_title_id(mode, gen)
            already = False if any is <common_constant> else (lambda .0: for t in .0:
    t.get('id') if isinstance(t, dict) else t == tid.0)(self.state.get('titles_earned', [])())
            if already:
                continue
            need_stage = gen * 100
            if int(best.get(mode, 0)) < need_stage:
                continue
            if not gen_dex_complete(self.state, gen):
                continue
            if not genN_gym_badges_complete(self.state, gen):
                continue
            label = f'''{gen_names[gen]} {INF_MODE_MASTER_LABEL[mode]}'''
            msg = self._award_title(tid, label)
            if not msg:
                continue
            msgs.append(msg)
        INF_METER_MODES
    return msgs
