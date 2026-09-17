# module.PetApp.reset_pet
# source line 18916
# Recovered from bytecode; default argument values are not shown.

def reset_pet(self):
    if not None('처음부터 다시 키우기', '정말 처음부터 다시 시작할까요?\n지금 포켓몬과 도감 정보는 모두 사라져요.'):
        return None
    fresh = messagebox.askyesno(DEFAULT_STATE)
    fresh['element_train'] = dict(DEFAULT_STATE['element_train'])
    fresh['daily_action_count'] = dict(DEFAULT_STATE['daily_action_count'])
    fresh['train_sessions'] = dict(DEFAULT_STATE['train_sessions'])
    fresh['dex'] = { }
    fresh['caught'] = { }
    fresh['missed'] = { }
    fresh['party'] = []
    fresh['catch_counts'] = dict(DEFAULT_STATE['catch_counts'])
    fresh['todos'] = []
    fresh['sacrificed'] = []
    fresh['party_hidden'] = []
    fresh['battle_code_log'] = []
    fresh['mega_evolved'] = False
    fresh['keyboard_control'] = False
    fresh['nickname'] = ''
    fresh['second_body_dex'] = None
    fresh['body1_visible'] = True
    fresh['body2_visible'] = True
    fresh['minigame_atk_bonus_pct'] = 0
    fresh['minigame_daily'] = dict(DEFAULT_STATE['minigame_daily'])
    fresh['omok_history'] = []
    fresh['gym_badges'] = []
    fresh['shiny_caught'] = { }
    fresh['mine_sessions'] = dict(DEFAULT_STATE['mine_sessions'])
    fresh['gacha_sessions'] = dict(DEFAULT_STATE['gacha_sessions'])
    fresh['food_sessions'] = dict(DEFAULT_STATE['food_sessions'])
    fresh['coin_gacha_pool'] = None
    fresh['coin_wallet'] = 0
    fresh['single_monitor_mode'] = self.state.get('single_monitor_mode', False)
    fresh['secondary_monitor_mode'] = self.state.get('secondary_monitor_mode', False)
    fresh['infinite_stone_damage'] = self.state.get('infinite_stone_damage', 0)
    fresh['infinite_stone_broken'] = self.state.get('infinite_stone_broken', False)
    fresh['infinite_stone_size'] = self.state.get('infinite_stone_size', DEFAULT_STATE.get('infinite_stone_size', 130))
    save_state_to_disk(fresh)
    self.restart_requested = True
    self.quit_app()
