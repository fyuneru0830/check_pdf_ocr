# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

################################################################
# need file "pdf2txt.py"
# need module "pip install pdfminer.six"

# will search the pdf file in the ./pdf and output the how many char in the pdf file
################################################################
def get_pdf_list():
    file_list = []
    import os

    directory = './pdf'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.pdf'):
            file_list.append(f)
    return file_list


def pdf2txt(filepath):
    import subprocess
    try:
        # res = subprocess.check_output('python ./pdf2txt.py \'pdf/iPhoneで電子工作_OCR.pdf\'')
        res = subprocess.run(['python', './pdf2txt.py', filepath], capture_output=True,
                             text=True).stdout
        return res
    except:
        print("error")


def check_size(txt):
    return len(txt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ファイルリストを配列に出力
    filelist = get_pdf_list()
    # ファイルリストをプリント
    print(filelist)
    # ファイルリストを元にテキスト化を行う
    f = open('str_list.txt', 'w')
    for filepath in filelist:
        txt = pdf2txt(filepath)
        f.write(filepath + "," + str(len(txt))+'\n')
    f.close()

