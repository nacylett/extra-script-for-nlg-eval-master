import os
import re
def drop():
    root_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    hyp_dir = os.path.join(root_dir, "examples", "hyp")
    ref_dir = os.path.join(root_dir, "examples", "ref")
    hyp_files = os.listdir(hyp_dir)
    ref_files = os.listdir(ref_dir)
    punctuation = r"~!@#$%^&*()_+`{}|\[\]\:\";\-\\\='<>?,./，。、《》？；：”‘“{【】}|、！@#￥%……&*（）——+=-"
    for file in hyp_files:
        file_path = os.path.join(hyp_dir, file)
        with open(file_path,"r", encoding="utf-8") as f1, open("%s.bak" % file_path, "w", encoding="utf-8") as f2:
            for lin in f1:
                lin = re.sub(r'[{}]+'.format(punctuation), '', lin)
                f2.write(lin)
        os.remove(file_path)
        os.rename("%s.bak" % file_path, file_path)
        f1.close()
        f2.close()
    for file in ref_files:
        file_path = os.path.join(ref_dir, file)
        with open(file_path,"r", encoding="utf-8") as f1, open("%s.bak" % file_path, "w", encoding="utf-8") as f2:
            for lin in f1:
                lin = re.sub(r'[{}]+'.format(punctuation), '', lin)
                f2.write(lin)
        os.remove(file_path)
        os.rename("%s.bak" % file_path, file_path)
        f1.close()
        f2.close()
if __name__ == '__main__':
    drop()



