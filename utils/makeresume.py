import sys
from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=1)
pdf.add_section(Section(open(sys.argv[1], encoding='utf-8').read()))
pdf.meta["title"] = "Curriculum Vitae"
pdf.meta["author"] = "Leonardo Silva Amaral"
pdf.meta["creator"] = "CI/CD Pipeline"
pdf.save(sys.argv[2])
