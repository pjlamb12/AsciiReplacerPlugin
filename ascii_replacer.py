import sublime, sublime_plugin, string

class AsciiReplacerCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		for r in reversed(self.view.sel()):
			for line_r in reversed(self.view.lines(r)):
				text = self.view.substr(line_r)
				print(text)
				text = text.replace('& ', '&amp; ')
				text = text.replace("‘", "'")
				text = text.replace("’", "'")
				text = text.replace('“', '"')
				text = text.replace('”', '"')
				text = text.replace('% ', '&#37; ')
				text = text.replace('…', '&#8230;')
				self.view.replace(edit, line_r, text)
		self.view.erase_status('ascii_replacer')
		sublime.status_message('Ascii Replacer is finished running!')
