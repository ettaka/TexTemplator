import os 
import io

class TexTemplator:

    def __init__(self, path, template_path):
        self.report_path = path
        template_file = io.open(template_path, 'r', encoding='utf8', errors='ignore')
        self.template = template_file.read()
        self.texfile = io.open(self.report_path,'w')
        self.temp_image_paths = []

    def replace_doc_data(self, doc_data):
        for key in doc_data:
            self.template = self.template.replace(key, doc_data[key])

    def table(self, table, label, caption=None):
        head = '\\begin{table}\n'
        head += '  \\centering\n'
        head += '  \\caption{' + str(caption) + '}\n'
        table = head + table
        table += '\\end{table}\n'
        return table

    def figure(self, path, label, caption=None):
        figure_tex = '\\begin{figure}\n'
        figure_tex += '  \\includegraphics[width=\\textwidth]{' + path + '}\n'
        figure_tex += '  \\caption{' + str(caption) + '}\n'
        figure_tex += '  \\label{' + label + '}\n'
        figure_tex += '\\end{figure}\n'
        return figure_tex

    def write(self, doc_data):
        self.replace_doc_data(doc_data)
        self.texfile.write(self.template)

    def compile(self):
        cmd = 'pdflatex ' + self.report_path
        print("Compiling report with pdflatex: ", cmd)
        os.system(cmd)
        os.system(cmd)
        print("Removing all the temporary files.")
        #for temp_image_path in self.temp_image_paths:
            #os.remove(temp_image_path)
            
    def close(self):
        self.texfile.close()


