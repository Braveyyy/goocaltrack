from nicegui import ui

import create_study_event

# finish this / begin css work
class EventDropdown(ui.dropdown_button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with self:
            ui.item('Study', on_click=lambda: print('Study selected'))
            ui.item('Gym', on_click=lambda: print('Gym selected'))

class TimerButton(ui.button):
    def __init__(self, *args, **kwargs) -> None:
        self._state = False
        super().__init__(*args, **kwargs)
        self.on('click', self.toggle)
        self.props('size=xl round')
        self.style('width:120px; height:120px; font-size:22px;')

    def toggle(self) -> None:
        """Toggle the button state."""
        self._state = not self._state
        self.update()

    def update(self) -> None:
        with self.props.suspend_updates():
            self.props(f'color={"green" if self._state else "red"}')
        super().update()

TimerButton(icon='power_settings_new')
EventDropdown('Choose an Event', auto_close=True)

ui.run()

#create_study_event.main()
