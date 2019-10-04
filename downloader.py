#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import appscript, argparse, io, os, pytube, subprocess, sys, time
import tkinter as tk
from tkinter import ttk

##修改測試
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
        self.tar = []
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

        self.frm3 = tk.LabelFrame(self.root, bg="gray",
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
                value=txt_res.get(key), variable=self.res,
                relief="solid", width=8)
            # btn1.grid(column=i, row=0)
            btn1.pack(side="left", padx=5, anchor="center")
            btn1.bind("<Button-1>", self.Select)

        self.btn2 = ttk.Button(self.frm2, text='Download', command=self.Download)
        self.btn2.pack(side="left")


        self.log = tk.Message(self.frm3, bg="white", text='test', \
        font=fnt_s, width=frm3_width-20)
        self.log.pack(padx=2, side="top")




    # def yt(self, url):
    #     yt = pytube.YouTube(url)
    #     self.filter = yt.streams.filter()
    #     return yt


    def Select(self, event):
        value = event.widget["text"]
        print(value, txt_res.get(value))
        for key in txt_res:
            if value == key:
                self.var = value
                self.res = txt_res.get(value)
        
        self.log.config(text=f'Press {value} get{self.res}')
        print(f'Press {value} get{self.res}')



    def Download(self):
        url = self.frm_entry.get()            

        if not url:
            value = 'None url'
            print(value)
            self.log.config(text=value)

        else:
            print('pass url')
            try:
                yt = pytube.YouTube(
                    url, on_progress_callback=self.onProgress)

                if self.var == list( txt_res.keys() )[-1]:
                    self.type = 'audio'
                    print(self.var)
                    self.tar = yt.streams.filter(only_audio=True).all()
                    print(" it's music ", self.tar)
                
                else:
                    self.type = 'vedio'
                    self.tar = yt.streams.filter(
                        file_extension="mp4", res=self.res).all()

                print(self.tar)

            except:
                # print('yt error')
                value = 'Error: yt'
                print(value)
            
            if self.tar:
                subprocess.Popen( self.tar[0].download(path), shell=True )
                # self.tar[0].download(path)
                # value = f'Download...: {self.percent:05.2f}%\r'
                # print(value)
                # self.log.config(text=value)
                if self.type == 'audio':
                    os.system("/usr/local/Cellar/ffmpeg/ffmpeg -i -vn -ab 320k 'test.mp3' ")
                    
            else:
                value = 'None tar'
                print(value)


            # print(yt.title)
            # print(tar)

            # appscript.app("Terminal").do_script(\
            #     f"tar[0].download(path)"
            #     )

            # tar[0].download(output_path=path)

            # subprocess.Popen( tar[0].download(path) )

        
    def onProgress(self, stream, chunk, handle, remaining):
        total = stream.filesize
        self.percent = (total - remaining) / total*100
        msg = f'Download...: {self.percent:05.2f}%\r'
        self.log.config(text=msg)
        print(msg)
        self.log.after(33)

        

if __name__ == "__main__":    
    Base = tk.Tk()
    Base.geometry(f"{win_width}x{win_height}")
    Base.title(title_en)

    App(Base)

    Base.mainloop()
