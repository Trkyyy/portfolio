import PyPDF2
r=PyPDF2.PdfReader('assets/Luke_McGarvey_06_01.pdf')
text='\n\n'.join((p.extract_text() or '') for p in r.pages)
open('assets/cv_text.txt','w',encoding='utf-8').write(text)
print('Wrote', len(text), 'chars to assets/cv_text.txt')
