# module.PetApp.open_todo._delete_item
# source line 18652
# Recovered from bytecode; default argument values are not shown.

def _delete_item(item):
    todos = self._todo_list()

    try:
        todos.remove(item)
        self.save_state()
        None()
        return None
    except ValueError:
        continue
