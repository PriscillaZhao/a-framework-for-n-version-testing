#!/usr/bin/python3
#-*-coding:utf-8-*-
#import os.path
import sys

def all_count(content_):
    for line in text_read.readlines():
        words=line.split()
        wordcount=wordcount+len(words)

def word_count(sysargv):
    wordcount=0
    try:
        text_read=open(sysargv,"r")
    except IOError:
        return 0
    else:
        for line in text_read.readlines():
            words=line.split()
            wordcount=wordcount+len(words)
        return wordcount

def line_count(sysargv):
    try:
        text=open(sysargv,"r").read()
    except IOError:
        return 0
    else:
        linecount=text.count("\n")
        return linecount

def byte_count(sysargv):
    try:
        text=open(sysargv,"r").read()
    except IOError:
        return 0
    else:
        byte=bytes(text,encoding='utf-8')
        bytecount=len(byte)
        return bytecount

def char_count(sysargv):
    try:
        text=open(sysargv,"r").read()
    except IOError:
        return 0
    else:
        char=bytes(text,encoding='utf-8')
        charcount=len(char)
        return charcount

def long_count(sysargv):
    try:
        text=open(sysargv,"r")
    except IOError:
        return 0
    else:
        lines=[line.strip() for line in text]
        longest=0
        long_line=""
        for line in lines:
            linelen=len(line)
            if linelen>longest:
                longest=linelen
                long_line=line
        return longest

def get_file_name(sysargv): return sysargv

def file_handling(list):
    global file_result
    file_result=[]
    if len(list)>1:
        line_total=word_total=byte_total=char_total=long_total=0
        for i in list:
            line_total+=line_count(i)
            word_total+=word_count(i)
            byte_total+=byte_count(i)
            char_total+=char_count(i)
            long_total+=long_count(i)
            file_output=[line_count(i),word_count(i),byte_count(i),char_count(i),long_count(i),i]
            file_result.append(file_output)
        file_result.append([line_total,word_total,byte_total,char_total,long_total,"total"])
    else:
        file_output=[line_count(file_list[0]),word_count(file_list[0]),byte_count(file_list[0]),char_count(file_list[0]),long_count(file_list[0]),file_list[0]]
        file_result.append(file_output)

def new_print(list,l,w,c,m,L):
    if len(list)==1:
        try:
            open(list[0][5],"r")
        except IOError:
            print('\t'+list[0][5]+" : No such file or directory")
        else:
            if l or w or c or m or L:
                if l: print('\t'+repr(list[0][0]), end='')
                if w: print('\t'+repr(list[0][1]), end='')
                if c: print('\t'+repr(list[0][2]), end='')
                if m: print('\t'+repr(list[0][3]), end='')
                if L: print('\t'+repr(list[0][4]), end='')
                print('\t'+list[0][5])
            else:
                for i in range(3):
                    print('\t'+repr(list[0][i]), end='')
                print('\t'+repr(list[0][5]))
    else:
        for i in range(len(list)):
            if i==len(list)-1:
                if print_line or print_word or print_byte or print_char or print_long:
                        if l: print('\t'+repr(list[i][0]).rjust(len(str(list[len(list)-1][0]))), end='')
                        if w: print('\t'+repr(list[i][1]).rjust(len(str(list[len(list)-1][1]))), end='')
                        if c: print('\t'+repr(list[i][2]).rjust(len(str(list[len(list)-1][2]))), end='')
                        if m: print('\t'+repr(list[i][3]).rjust(len(str(list[len(list)-1][3]))), end='')
                        if L: print('\t'+repr(list[i][4]).rjust(len(str(list[len(list)-1][4]))), end='')
                        print('\t'+list[i][5])
                else:
                    print('\t'+repr(list[i][0]).rjust(len(str(list[len(list)-1][0]))), end='')
                    print('\t'+repr(list[i][1]).rjust(len(str(list[len(list)-1][1]))), end='')
                    print('\t'+repr(list[i][2]).rjust(len(str(list[len(list)-1][2]))), end='')
                    print('\t'+list[i][5])
            else:
                try:
                    open(list[i][5],"r")
                except IOError:
                    print('\t'+list[i][5]+" : No such file or directory")
                else:
                    if print_line or print_word or print_byte or print_char or print_long:
                        if l: print('\t'+repr(list[i][0]).rjust(len(str(list[len(list)-1][0]))), end='')
                        if w: print('\t'+repr(list[i][1]).rjust(len(str(list[len(list)-1][1]))), end='')
                        if c: print('\t'+repr(list[i][2]).rjust(len(str(list[len(list)-1][2]))), end='')
                        if m: print('\t'+repr(list[i][3]).rjust(len(str(list[len(list)-1][3]))), end='')
                        if L: print('\t'+repr(list[i][4]).rjust(len(str(list[len(list)-1][4]))), end='')
                        print('\t'+list[i][5])
                    else:
                        print('\t'+repr(list[i][0]).rjust(len(str(list[len(list)-1][0]))), end='')
                        print('\t'+repr(list[i][1]).rjust(len(str(list[len(list)-1][1]))), end='')
                        print('\t'+repr(list[i][2]).rjust(len(str(list[len(list)-1][2]))), end='')
                        print('\t'+list[i][5])

def std_handling(num):
    if num==0:
        f=sys.stdin.read()
        content=f.split('\n')
        #print(content)
        content_list=[len(content)-1,0,len(content)-1]
        for i in content:
            content_list[1]+=len(i.split())
            content_list[2]+=len(bytes(i,encoding='utf-8'))

        flag_list=[print_line,print_long,print_byte]
        for i in range(3):
            if flag_list[i]:
                print('\t'+repr(content_list[i]), end='')
        print()
        exit()

def arg_handling(com):
    global print_line,print_word,print_byte,print_long,print_char
    print_line=print_word=print_byte=print_long=print_char=False
    global file_list
    file_list=[]
    global file_num
    file_num=0

    for i in com:
        if i=="-l" or i=="--line" or i=="--lines":
            print_line=True
        elif i=="-w" or i=="--word" or i=="--words":
            print_word=True
        elif i=="-L" or i=="--max-line-length":
            print_long=True
        elif i=="-m" or i=="--char" or i=="--chars":
            print_char=True
        elif i=="-c" or i=="--byte" or i=="--bytes":
            print_byte=True
        elif i=="-h" or i=="--help":
            print("-c, --bytes            print the byte counts")
            print("-m, --chars            print the character counts")
            print("-l, --lines            print the newline counts")
            print("    --files0-from=F    read input from the files specified by\n\t\t\tNUL-terminated names in file F;\n\t\t\tIf F is - then read names from standard input")
            print("-L, --max-line-length  print the length of the longest line")
            print("-w, --words            print the word counts")
            print("    --help     \t       display this help and exit")
            exit()
        elif i=="-v" or i=="--version":
            print("")
            exit()
        elif i[0:14]=="--files0-from=":
            if len(i[14:])==1 and i[14:]=="-":
                std_handling(0)
            else:
                try:
                    open(i[14:],"r")
                except IOError:
                    print("cannot open '" + i[14:] + "' for reading: No such file or directory")
                    exit()
                else:
                    f=open(i[14:])
                    li=f.read().splitlines()
                    for i in li:
                        i.replace("\n",'').replace("\t",'')
                        print(i)
                    exit()
        elif len(i)>=2 and i[0]=="-":
            print ("invalid option -- '" + i +"'")
            exit()
        else:
            file_num+=1
            file_list.append(i)
    #print(file_list)


command=sys.argv[1:]
arg_handling(command)
std_handling(file_num)
file_handling(file_list)
new_print(file_result,print_line,print_word,print_byte,print_char,print_long)