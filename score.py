# テキストの中のスコアの合計と平均、最低点と最高点を求める。


import tkinter as tk
import tkinter.filedialog as tf

root = tk.Tk()
root.minsize(400,300)

def file_open(event):
    filename = tf.askopenfilename()
    text_box.delete('1.0','end')
    with open(filename,'r')as f:
        score_list = []
        total = 0
        for line in f:
            temp = line.strip().split(',')
            # print(temp)
            score_list.append(temp)
            print(score_list)
            total += int(temp[1])
            # print(total)
        avg = total/len(score_list)
        score_list.sort(key=lambda x:int(x[1]))
        # print(score_list)
        text_box.insert(tk.END,f"最高点{score_list[0][0]}さんの{score_list[0][1]}点\n")
        text_box.insert(tk.END,f"最低点{score_list[-1][0]}さんの{score_list[-1][1]}点\n")
        text_box.insert(tk.END,f"平均点{avg}点")


btn = tk.Button(text='参照')
btn.bind('<1>',file_open)
btn.pack()

text_box = tk.Text(width=40,height=20)
text_box.pack()



root.mainloop()