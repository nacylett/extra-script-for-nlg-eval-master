import os
from nlgeval import compute_metrics
import csv
import os
import datetime

root_dir = os.path.join(os.path.dirname(__file__), '..', '..')
hyp_dir = os.path.join(root_dir,"examples","hyp")
ref_dir = os.path.join(root_dir, "examples", "ref")
csv_path = os.path.join(root_dir, "examples", "csv", datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".csv")
def loop():
    hyp_files = os.listdir(hyp_dir)
    ref_files = os.listdir(ref_dir)
    references = []
    f = open(csv_path, "w",newline="")
    writer = csv.writer(f)
    head = [""]
    lines = [["Bleu_1"], ["Bleu_2"], ["Bleu_3"], ["Bleu_4"], ["METEOR"], ["ROUGE_L"], ["CIDEr"]]
    for file in ref_files:
        references.append(os.path.join(ref_dir,file))
    for file in hyp_files:
        try:
            print("============================")
            print(file, "结果")
            head.append(file)
            metrics_dict = compute_metrics(os.path.join(hyp_dir, file),
                                       references=references,csv_lines = lines)


        except Exception as e:
            print(e)
            pass
    writer.writerow(head)
    writer.writerows(lines)
    f.close()



if __name__ == '__main__':
    loop()
    # compute_metrics(os.path.join(hyp_dir, "MT1.txt"),
    #                 references=os.path.join(ref_dir,"Model1.txt"))
