import sublime, sublime_plugin

class RepeaterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    clip = sublime.get_clipboard();
    self.view.window().show_input_panel("Paste how many times?", "", self.on_done, None, None)

  def on_done(self, user_input):
    pasteCount = int(float(user_input))
    clip = sublime.get_clipboard();
    text = '';

    for x in range(0,pasteCount):
        text += clip

    sublime.set_clipboard(text);
    self.view.run_command('paste');
    sublime.set_clipboard(clip);
