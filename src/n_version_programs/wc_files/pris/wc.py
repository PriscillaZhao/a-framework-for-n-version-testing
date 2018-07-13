# -*- coding: utf-8 -*-
# Author: Qianyun Zhao

import sys
import argparse

total_lines,total_words,total_bytes,total_chars,longest_line = 0,0,0,0,0

def line_count(filepath):
    lines_n = 0
    content = open(filepath,encoding="ISO-8859-1")
    for i in content.readlines():
        lines_n = lines_n + 1
    content.close()
    return lines_n

def long_line(filepath):
    f = open(filepath, 'r',encoding="ISO-8859-1")
    longest = 0
    allLines = f.readlines()
    f.close()
    for line in allLines:
        linelen = len(line)
        if linelen > longest:
            longest = linelen
    return longest

def word_count(filepath):
    words_n = 0
    my_file = open(filepath,encoding="ISO-8859-1")
    for x in my_file.read().split():
        words_n += 1
    my_file.close()
    return words_n

def byte_count(filepath):
    my_file = open(filepath, 'r',encoding="ISO-8859-1")
    return len(my_file.read())

def char_count(filepath):
    my_file = open(filepath, 'r',encoding="ISO-8859-1")
    return len(my_file.read())

def count_statistic0(filepaths):
    global total_lines,total_words,total_bytes,total_chars,longest_line
    for filepath in filepaths:
        try:
            lines_number = line_count(filepath)
            total_lines = total_lines + lines_number
            words_number = word_count(filepath)
            total_words = total_words + words_number
            bytes_number = byte_count(filepath)
            total_bytes = total_bytes + bytes_number
            print(' %6d %6d %6d'%(lines_number,words_number,bytes_number),' ',filepath)
        except FileNotFoundError:
            print('wc: ',filepath,': No such file or directory')
    if len(filepaths) > 1:
        print(' %6d %6d %6d' % (total_lines, total_words, total_bytes),' ','total')


def count_statistic1(opts, filepaths):
    global total_lines, total_words, total_bytes,total_chars,longest_line
    all_line_len = []
    if opts == '-l':
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                print(' %6d'%(lines_number),' ',filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d'% (total_lines),' ','total')

    elif opts == '-w':
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words += words_number
                print(' %6d' % (words_number), ' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d' % (total_words),' ','total')

    elif opts == '-c':
        for filepath in filepaths:
            try:
                bytes_number = byte_count(filepath)
                total_bytes += bytes_number
                print(' %6d' % (bytes_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d' % (total_bytes),' ','total')

    elif opts == '-m':
        for filepath in filepaths:
            try:
                chars_number = char_count(filepath)
                total_chars += chars_number
                print(' %6d' % (chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d' % (total_chars),' ','total')

    elif opts == '-L':
        for filepath in filepaths:
            try:
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d' % (l_line), ' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d' % (longest_line),' ','total')

def count_statistic2(opts, filepaths):
    global total_lines, total_words, total_bytes,total_chars,longest_line
    all_line_len = []
    if opts == ['-l', '-c']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines += lines_number
                bytes_number = byte_count(filepath)
                total_bytes += bytes_number
                print(' %6d %6d' % (lines_number,bytes_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d' % (total_lines,total_bytes),' ','total')

    elif opts == ['-l', '-w']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines += lines_number
                words_number = word_count(filepath)
                total_words += words_number
                print(' %6d %6d' % (lines_number, words_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_lines, total_words),' ','total')

    elif opts == ['-l', '-m']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines += lines_number
                chars_number = char_count(filepath)
                total_chars += chars_number
                print(' %6d %6d' % (lines_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_lines, total_chars),' ','total')

    elif opts == ['-l', '-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines += lines_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d' % (lines_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_lines, longest_line),' ','total')

    elif opts == ['-w', '-c']:
        for filepath in filepaths:
            try:
                bytes_number = byte_count(filepath)
                total_bytes += bytes_number
                words_number = word_count(filepath)
                total_words += words_number
                print(' %6d %6d' % (words_number, bytes_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_words, total_bytes),' ','total')

    elif opts == ['-w', '-m']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words += words_number
                chars_number = char_count(filepath)
                total_chars += chars_number
                print(' %6d %6d' % (words_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_words, total_chars),' ','total')

    elif opts == ['-w', '-L']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words += words_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d' % (words_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_words, longest_line),' ','total')

    elif opts == ['-c', '-m']:
        for filepath in filepaths:
            try:
                bytes_number = byte_count(filepath)
                total_bytes += bytes_number
                chars_number = char_count(filepath)
                total_chars += chars_number
                print(' %6d %6d' % (bytes_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_bytes, total_chars),' ','total')

    elif opts == ['-c', '-L']:
        for filepath in filepaths:
            try:
                bytes_number = byte_count(filepath)
                total_bytes += bytes_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d' % (bytes_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_bytes, longest_line),' ','total')

    elif opts == ['-m', '-L']:
        for filepath in filepaths:
            try:
                chars_number = char_count(filepath)
                total_chars += chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d' % (chars_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
                print(' %6d %6d' % (total_chars, longest_line),' ','total')

def count_statistic3(opts, filepaths):
    global total_lines, total_words, total_bytes, total_chars,longest_line
    all_line_len = []
    if opts == ['-l','-w','-m']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                words_number = word_count(filepath)
                total_words = total_words + words_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                print(' %6d %6d %6d' % (lines_number, words_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_lines, total_words, total_chars),' ', 'total')

    elif opts == ['-l','-w','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                words_number = word_count(filepath)
                total_words = total_words + words_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (lines_number, words_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_lines, total_words, longest_line),' ', 'total')

    elif opts == ['-l','-c', '-m']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                print(' %6d %6d %6d' % (lines_number, bytes_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_lines, total_bytes, total_chars),' ', 'total')

    elif opts == ['-l','-c','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (lines_number, bytes_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_lines, total_bytes, longest_line),' ', 'total')

    elif opts == ['-l','-m','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (lines_number, chars_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_lines, total_chars, longest_line),' ', 'total')

    elif opts == ['-w','-c','-m']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                print(' %6d %6d %6d' % (words_number, bytes_number, chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_words, total_bytes, total_chars),' ', 'total')

    elif opts == ['-w', '-c', '-L']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (words_number, bytes_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_words, total_bytes, longest_line),' ', 'total')

    elif opts == ['-w', '-m', '-L']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words = total_words + words_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (words_number, chars_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_words, total_chars, longest_line),' ', 'total')

    elif opts == ['-c', '-m', '-L']:
        for filepath in filepaths:
            try:
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d' % (bytes_number, chars_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d' % (total_bytes, total_chars, longest_line),' ', 'total')

def count_statistic4(opts, filepaths):
    global total_lines, total_words, total_bytes, total_chars,longest_line
    all_line_len = []
    if opts == ['-l','-w','-c','-m']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                print(' %6d %6d %6d %6d' % (lines_number, words_number,bytes_number,chars_number),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d %6d' % (total_lines, total_words,total_bytes,total_chars),' ', 'total')

    elif opts == ['-l','-w','-c','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d %6d' % (lines_number, words_number,bytes_number,l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d %6d' % (total_lines, total_words,total_bytes,longest_line),' ', 'total')

    elif opts == ['-l','-c','-m','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d %6d' % (lines_number, bytes_number,chars_number,l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d %6d' % (total_lines,total_bytes,total_chars,longest_line),' ', 'total')

    elif opts == ['-w', '-c', '-m', '-L']:
        for filepath in filepaths:
            try:
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d %6d' % (words_number, bytes_number, chars_number, l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d %6d' % (total_words, total_bytes, total_chars, longest_line),' ', 'total')

def count_statistic5(opts, filepaths):
    global total_lines, total_words, total_bytes, total_chars,longest_line
    all_line_len = []
    if opts == ['-l', '-w', '-c', '-m','-L']:
        for filepath in filepaths:
            try:
                lines_number = line_count(filepath)
                total_lines = total_lines + lines_number
                words_number = word_count(filepath)
                total_words = total_words + words_number
                bytes_number = byte_count(filepath)
                total_bytes = total_bytes + bytes_number
                chars_number = char_count(filepath)
                total_chars = total_chars + chars_number
                l_line = long_line(filepath)
                all_line_len.append(l_line)
                longest_line = max(all_line_len)
                print(' %6d %6d %6d %6d %6d' % (lines_number, words_number, bytes_number, chars_number,l_line),' ', filepath)
            except FileNotFoundError:
                print('wc: ', filepath, ': No such file or directory')
        if len(filepaths) > 1:
            print(' %6d %6d %6d %6d %6d' % (total_lines, total_words, total_bytes, total_chars,longest_line),' ', 'total')

def get_version():
    print("""wc (GNU coreutils) 8.26
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Paul Rubin and David MacKenzie.""")

def get_help():
    print("""Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  With no FILE, or when FILE is -,
read standard input.  A word is a non-zero-length sequence of characters
delimited by white space.
The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the length of the longest line
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'wc invocation'""")

def get_files(path):
    try:
        my_file = open(path, encoding="ISO-8859-1")
        content = my_file.read().split('\x00')
    except FileNotFoundError:
        print('wc: ', path, ': No such file or directory')
        sys.exit()
    return content[:-1]

def get_stdin(filenames):
    filepath=[]
    for n in filenames:
        filepath.append(n)
    return filepath

if __name__ == '__main__':
    import unittest
    import doctest
    doctest.testmod()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-c','--bytes',action='store_true', help="print the byte counts")
    parser.add_argument('-m','--chars',action='store_true',help="print the character counts")
    parser.add_argument('-l','--lines',action='store_true',help="print the newline counts")
    parser.add_argument('--files0-from=', dest='files', action='store', help="read input from the files specified by NUL - terminated names in file F")
    parser.add_argument('-L','--max-line-length',dest='max',action='store_true', help="print the length of the longest line")
    parser.add_argument('-w','--words',action='store_true',help="print the word counts")
    parser.add_argument('--help', action='store_true', help="display this help and exit")
    parser.add_argument('--version',action='store_true',help="output version information and exit")
    parser.add_argument('file', nargs='*', help="Specify one or more file names")
    args = parser.parse_args()

    # no flag
    if not args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic0(args.file)

    # one flag
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic1('-l', args.file)
    elif not args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic1('-w', args.file)
    elif not args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic1('-c', args.file)
    elif not args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic1('-m', args.file)
    elif not args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files==None and not args.help:
        count_statistic1('-L', args.file)

    # two flags
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic2(['-l', '-w'], args.file)
    elif args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic2(['-l', '-c'], args.file)
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic2(['-l', '-m'], args.file)
    elif args.lines and not args.words and not args.bytes and not args.chars and args.max and not args.version and args.files==None and not args.help:
        count_statistic2(['-l','-L'], args.file)
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic2(['-w', '-c'], args.file)
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files==None and not args.help:
        count_statistic2(['-w', '-m'], args.file)
    elif not args.lines and args.words and not args.bytes and not args.chars and args.max and not args.version and args.files==None and not args.help:
        count_statistic2(['-w','-L'], args.file)
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and not args.max and args.files==None and not args.help :
        count_statistic2(['-c', '-m'], args.file)
    elif not args.lines and not args.words and args.bytes and not args.chars and args.max and not args.version and args.files==None and not args.help:
        count_statistic2(['-c','-L'], args.file)
    elif not args.lines and not args.words and not args.bytes and args.chars and args.max and not args.version and args.files==None and not args.help:
        count_statistic2(['-m','-L'], args.file)

    # Three flags
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files == None and not args.help:
        count_statistic0(args.file)
    elif args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files == None and not args.help:
        count_statistic3(['-l', '-w', '-m'], args.file)
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and args.max  and args.files == None and not args.help:
        count_statistic3(['-l', '-w', '-L'], args.file)
    elif args.lines and not args.words and args.bytes and args.chars and not args.version and not args.max and args.files == None and not args.help:
        count_statistic3(['-l', '-c', '-m'], args.file)
    elif args.lines and not args.words and args.bytes and not args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic3(['-l', '-c', '-L'], args.file)
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic3(['-l', '-m', '-L'], args.file)
    elif not args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files == None and not args.help:
        count_statistic3(['-w','-c','-m'], args.file)
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic3(['-w','-c','-L'], args.file)
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic3(['-w','-m','-L'], args.file)
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic3(['-c', '-m', '-L'], args.file)

    # Four flags
    elif args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files == None and not args.help:
        count_statistic4(['-l', '-w', '-c','-m'], args.file)
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic4(['-l', '-w', '-c','-L'], args.file)
    elif args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic4(['-l', '-c', '-m','-L'], args.file)
    elif not args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files == None and not args.help:
        count_statistic4(['-w', '-c', '-m','-L'], args.file)

    # Five flags
    elif args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files == None  and not args.help:
        count_statistic5(['-l', '-w', '-c', '-m','-L'], args.file)

    #--files0-from flag0
    elif not args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic0(get_files(args.files))
    elif not args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic0(filepath)

    # --files0-from flag1
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files!=None and args.files!='-' and not args.help:
        count_statistic1('-l',get_files(args.files))
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and not args.max  and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic1('-l',filepath)
    elif not args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files!=None and args.files!='-' and not args.help:
        count_statistic1('-w',get_files(args.files))
    elif not args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max  and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic1('-w',filepath)
    elif not args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic1('-c', get_files(args.files))
    elif not args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic1('-c', filepath)
    elif not args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files!=None and args.files!='-' and not args.help:
        count_statistic1('-m',get_files(args.files))
    elif not args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max  and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic1('-m',filepath)
    elif not args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files!=None and args.files!='-' and not args.help:
        count_statistic1('-L',get_files(args.files))
    elif not args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max  and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic1('-L',filepath)

    # --files0-from flag2
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-l', '-w'], get_files(args.files))
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-l', '-w'], filepath)
    elif args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-l', '-c'], get_files(args.files))
    elif args.lines and not args.words and args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-l', '-c'], filepath)
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-l', '-m'], get_files(args.files))
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-l', '-m'], filepath)
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-l', '-L'], get_files(args.files))
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-l', '-L'], filepath)
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-w', '-c'], get_files(args.files))
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-w', '-c'], filepath)
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-w', '-m'], get_files(args.files))
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-w', '-m'], filepath)
    elif not args.lines and args.words and not args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-w', '-L'], get_files(args.files))
    elif not args.lines and args.words and not args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-w', '-L'], filepath)
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-c', '-m'], get_files(args.files))
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-c', '-m'], filepath)
    elif not args.lines and not args.words and args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-c', '-L'], get_files(args.files))
    elif not args.lines and not args.words and args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-c', '-L'], filepath)
    elif not args.lines and not args.words and not args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic2(['-m', '-L'], get_files(args.files))
    elif not args.lines and not args.words and not args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic2(['-m', '-L'], filepath)

    # --files0-from flag3
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic0(get_files(args.files))
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic0(filepath)
    elif args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-l', '-w', '-m'], get_files(args.files))
    elif args.lines and args.words and not args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-l', '-w', '-m'], filepath)
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-l', '-w', '-L'], get_files(args.files))
    elif args.lines and args.words and not args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-l', '-w', '-L'], filepath)

    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-l', '-c', '-m'], get_files(args.files))
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-l', '-c', '-m'], filepath)
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-l', '-c', '-L'], get_files(args.files))
    elif args.lines and not args.words and not args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-l', '-c', '-L'], filepath)

    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-l', '-m', '-L'], get_files(args.files))
    elif args.lines and not args.words and not args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-l', '-m', '-L'], filepath)

    elif not args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-w', '-c', '-m'], get_files(args.files))
    elif not args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-w', '-c', '-m'], filepath)
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-w', '-c', '-L'], get_files(args.files))
    elif not args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-w', '-c', '-L'], filepath)
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-w', '-m', '-L'], get_files(args.files))
    elif not args.lines and args.words and not args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-w', '-m', '-L'], filepath)
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic3(['-c', '-m', '-L'], get_files(args.files))
    elif not args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic3(['-c', '-m', '-L'], filepath)

    # --files0-from flag4
    elif args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic4(['-l', '-w', '-c','-m'], get_files(args.files))
    elif args.lines and args.words and args.bytes and args.chars and not args.version and not args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic4(['-l', '-w', '-c','-m'], filepath)
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic4(['-l', '-w', '-c','-L'], get_files(args.files))
    elif args.lines and args.words and args.bytes and not args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic4(['-l', '-w', '-c','-L'], filepath)
    elif args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic4(['-l', '-c', '-m','-L'], get_files(args.files))
    elif args.lines and not args.words and args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic4(['-l', '-c', '-m','-L'], filepath)
    elif not args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic4(['-w', '-c', '-m','-L'], get_files(args.files))
    elif not args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic4(['-w', '-c', '-m','-L'], filepath)

    # --files0-from flag5
    elif args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files != None and args.files != '-' and not args.help:
        count_statistic5(['-l','-w', '-c', '-m', '-L'], get_files(args.files))
    elif args.lines and args.words and args.bytes and args.chars and not args.version and args.max and args.files == '-' and not args.help:
        content = input("")
        file_names = content.split()
        filepath = get_stdin(file_names)
        count_statistic5(['-l','-w', '-c', '-m', '-L'], filepath)

    # Other flags
    elif args.help and args.version:
        get_help()
    elif args.help and not args.version:
        get_help()
    elif not args.help and args.version:
        get_version()
    else:
        print("""
        wc: invalid option
        Try 'wc --help' for more information.""")