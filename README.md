# Youtube-with-Python
Python code to download videos from youtube.
This project aims on downloading videos from youtube using Python and Youtube_dl module 

## Prerequisites
You will be required to download the Youtube_dl module. This can be easily done using the **pip** command.
```
pip install youtube_dl
```
### Tweaks in YoutubeDL.py
Some changes have been mase inside the YoutubeDL.py file that you can find in your python folder. Specific path is as follows:
 ```
 Python\Lib\site-packages\youtube_dl\YoutubeDL.py
 ```
 Inside this file the following modificaton has been made in the list_formats() method :
 #### Original 
 ```
         formats = info_dict.get('formats', [info_dict])
        table = [
            [f['format_id'], f['ext'], self.format_resolution(f), self._format_note(f)]
            for f in formats
            if f.get('preference') is None or f['preference'] >= -1000]
        if len(formats) > 1:
            table[-1][-1] += (' ' if table[-1][-1] else '') + '(best)'

        header_line = ['format code', 'extension', 'resolution', 'note']
        self.to_screen(
            '[info] Available formats for %s:\n%s' %
            (info_dict['id'], render_table(header_line, table)))
  ```
  
  #### Modified
  ```
  		formats = info_dict.get('formats', [info_dict])
		table = [
			[f['format_id'], f['ext'], self.format_resolution(f), self._format_note(f)]
			for f in formats
			if f.get('preference') is None or f['preference'] >= -1000]
		if len(formats) > 1:
			table[-1][-1] += (' ' if table[-1][-1] else '') + '(best)'

		#header_line = ['format code', 'extension', 'resolution', 'note']
		#self.to_screen(
		#    '[info] Available formats for %s:\n%s' %
		#    (info_dict['id'], render_table(header_line, table)))
			file = open('ret.txt','wb')
			for s in range(0,len(table)):
				file.write(str(table[s]))
			file.close()
 ```
 
 ### About the files
 **youtube_gui.py** : Is the core program that runs the gui (made using tkinter)
 
 **youtube1.py** : Is responsible for retriving video content from youtube
 
