#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import appscript, argparse, io, os, pytube, subprocess, sys, time
import tkinter as tk
from tkinter import ttk


###文字
title_en, title_ch = 'YouTube Downloader', 'Youtube下載器',
# txt_res = 'SD', 'HD', 'FHD', 'Audio'
# txt_res1 = '480p', '720p', '1080p'
txt_res = {'SD':'480p', 'HD':'720p', 'FHD':'1080p', 'Audio':None}


###尺寸
win_width, win_height = 500, 500
title_width, title_height = win_width, 40
# log_width, log_height = win_width, 100
frm1_width, frm1_height = win_width, 35
frm2_width, frm2_height = win_width, 35
frm3_width, frm3_height= win_width, win_height-title_height-frm1_height - frm2_height
entry_width, entry_height = win_width, 30
btn1_width, btn1_height = 5, 20 

fnt_l, fnt_m, fnt_s = ("Arial", 30), ("Arial", 20), ("Arial", 10)

###其他
path="/Users/KirkShu/"
url = \
    "https://www.youtube.com/watch?v=5yv9zLChuuE"

# yt = pytube.YouTube(url)
class App(object):
    def __init__(self, master=object):
        self.root = master
        self.url, self.res = tk.StringVar(), tk.StringVar()
        # self.ArgParser()
        self.Frame()


    def Frame(self):
        self.frm_title = tk.LabelFrame(self.root, text=title_ch, font=fnt_l, \
            bg="lightblue", width=title_width, height=title_height)
        self.frm_title.pack_propagate(0)
        self.frm_title.pack(side="top", expand="false")

        self.frm1 = tk.LabelFrame(self.root, bg="gray", \
            width=frm1_width, height=frm1_height)
        self.frm1.pack_propagate(0)
        self.frm1.pack()

        self.frm2 = tk.LabelFrame(self.root, bg="lightblue",
                                  width=frm2_width, height=frm2_height)
        self.frm2.pack_propagate(0)
        self.frm2.pack()

        self.frm3 = tk.LabelFrame(self.root, bg="white",
                                  width=frm3_width, height=frm3_height)
        self.frm3.pack_propagate(0)
        self.frm3.pack()

        self.lab1 = tk.Label(self.frm1, text='網址：')
        self.lab1.grid(column=0, row=0, padx=5)
        self.frm_entry = tk.Entry(self.frm1, font=fnt_m, \
            width=entry_width)
        # self.frm_entry.pack(side="top")
        self.frm_entry.grid(column=1, row=0, padx=10)

        # self.cbox = ttk.Radiobutton(self.frm2, values=self.res, font=fnt_m)
        # self.cbox.grid(column=0, row=0, padx=5)
        # self.cbox.currxent(0)
        
        for key in txt_res:
            btn1 = tk.Radiobutton(self.frm2, text=key, \
                variable=self.res, value=txt_res.get(key), \
                relief="solid", width=8)
            # btn1.grid(column=i, row=0)
            btn1.pack(side="left", padx=5, anchor="center")
            btn1.bind("<Button-1>", self.Select)

        self.btn2 = ttk.Button(self.frm2, text='Download')
        self.btn2.pack(side="left")


        self.log = tk.Message(self.frm3, bg="gray", text='test', \
        font=fnt_s, width=frm3_width-20)
        self.log.pack(padx=2, side="top")




    # def yt(self, url):
    #     yt = pytube.YouTube(url)
    #     self.filter = yt.streams.filter()
    #     return yt


    def Select(self, event):
        value = event.widget["text"]
        print(value, self.res.get())
        url = f"{self.frm_entry.get()}"
        # url = "https://www.youtube.com/watch?v=5yv9zLChuuE"

        if url:
            print('pass url')
            try:
                yt = pytube.YouTube( \
                    url, on_progress_callback=self.onProgress)
            except:
                print('yt error')
            for j in txt_res:
                if value == txt_res[-1]:
                    self.tar = yt.streams.filter(only_audio=True).all()
                    print(f'res:{j}')
                else:
                    self.tar = yt.streams.filter(file_extension="mp4", res="480p").all()

                if value == txt_btn1[0]:
                    print('btn1', url)
                    tar = yt.streams.filter(file_extension="mp4", res="480p").all()
                elif value == txt_btn1[1]:
                    print('btn2', url)
                    tar = yt.streams.filter(file_extension="mp4", res="720p").all()
                elif value == txt_btn1[2]:
                    print('btn3', url)
                    tar = yt.streams.filter(file_extension="mp4", res="720p").all()
                elif value == txt_btn1[3]:
                    print('btn4', url)
                    tar = yt.streams.filter(only_audio=True).all()

                # print(yt.title)
                # print(tar)
                # os.system(" gnome-terminal -e ' call rosservice /Run ' ")
                
                # appscript.app("Terminal").do_script(\
                #     f"tar[0].download(path)"
                #     )

                # tar[0].download(output_path=path)
                
                subprocess.Popen( tar[0].download(path) )
        else:
            value  = 'None URL' 
                      
        self.log.config(text=f'{value}')


    def ArgParser(self):
        # parser = argparse.ArgumentParser()
        # args = parser.parse_args()
        # parser.add_argument("url", help='url for youtube')
        # parser.add_argument("-fhd", action="store_true", help='1080畫質')
        # parser.add_argument("-hd", action="store_true", help='720畫質')
        # parser.add_argument("-sd", action="store_true", help='480畫質')
        # parser.add_argument("-aud", action="store_true", help='下載mp3')
        # yt = pytube.YouTube(args.url, on_pregress_callback=self.onProgress)
        pass
    
        
    def onProgress(self, stream, chunk, handle, remaining):
        total = stream.filesize
        percent = (total - remaining) / total*100
        print(f'Download... : {percent:05.2f}%\r')
        # self.CreateLog(txt=f'Download... : {percent:05.2f}%\r')
        
        pass

    def CreateLog(self, txt):
        for info in self.frm3.winfo_children():
            info.destroy()
        log = tk.Message(self.frm3, bg="gray", text=txt, \
            font=fnt_s, width=frm3_width-20)
        log.pack(padx=2, side="top")


if __name__ == "__main__":    
    Base = tk.Tk()
    Base.geometry(f"{win_width}x{win_height}")
    Base.title(title_en)

    App(Base)

    Base.mainloop()
