import os

if __name__ == "__main__":
    
    print(os.getcwd())
    
    if not os.path.exists(".\\ffmpeg.exe"):
        print("no ffmpeg.exe found, please copy ffmpeg.exe into this directory and retry")
        os.system("pause")
        exit()
    
    ffmpeg = os.getcwd() + "\\ffmpeg.exe"
    print("found ffmpeg: "+ffmpeg)

    file_path = input("please input the path contains .ts file: ")
    os.chdir(file_path) #修改当前工作目录

    print(os.getcwd()) #当前路径
    
    file_list = os.listdir('.')
    
    for file in file_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(file)[1] == '.ts':
            print(file)
            file_name_without_ext = os.path.splitext(file)[0]
            print(file_name_without_ext)
            ts2mp3_cmd = ffmpeg + ' -i "'+ file +'" -acodec copy "' +  file_name_without_ext + '.mp3"'
            print(ts2mp3_cmd)
            os.system(ts2mp3_cmd)
    os.system("pause")