import sublime, sublime_plugin, string

class AsciiReplacerCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		for r in reversed(self.view.sel()):
			for line_r in reversed(self.view.lines(r)):
				text = self.view.substr(line_r)
				print(text)
				text = text.replace('& ', '&amp; ')
				text = text.replace('©', '&copy;')
				text = text.replace("‘", "'")
				text = text.replace("’", "'")
				text = text.replace('“', '"')
				text = text.replace('”', '"')
				text = text.replace('% ', '&#37; ')
				text = text.replace('…', '&#8230;')
				text = text.replace(' ', ' ')
				text = text.replace('', '')
				text = text.replace('Á', '&#193;')
				text = text.replace('á', '&#225;')
				text = text.replace('É', '&#201;')
				text = text.replace('é', '&#233;')
				text = text.replace('Í', '&#205;')
				text = text.replace('í', '&#237;')
				text = text.replace('Ó', '&#211;')
				text = text.replace('ó', '&#243;')
				text = text.replace('Ú', '&#218;')
				text = text.replace('ú', '&#250;')
				self.view.replace(edit, line_r, text)
		self.view.erase_status('ascii_replacer')
		sublime.status_message('Ascii Replacer is finished running!')
