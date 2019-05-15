from win32com import client as wc
 
word = wc.Dispatch('Word.Application')
 
doc = word.Documents.Open('c:/test')
 
doc.SaveAs('c:/test.text', 2)
 
doc.Close()
 
word.Quit()