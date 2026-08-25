import PyPDF2
if __name__ == '__main__':


    file = open("D:/BaiduNetdiskDownload/Gitee 代码与版本管理规范.pdf", "rb")  # 注意用 "rb" 二进制模式
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())
    file.close()