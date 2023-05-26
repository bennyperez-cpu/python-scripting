import os
import shutil

origin_directory = "/home/Benny/Downloads/Fotos Google Drive/"
# destination_directory = "/home/Benny/Downloads/Temp/"
destination_directory = "/media/Benny/TOSHIBA EXT/7.-Fotos/Fotos_26May23_GoogleFotos/"
count = 0

for nom_dir_prin in os.listdir(origin_directory):
    ruta_dir_1 = os.path.join(origin_directory,nom_dir_prin) + "/Takeout/Google Fotos/"
    # print(ruta_dir_1)
    for nom_dir_sec in os.listdir(ruta_dir_1):
       ruta_dir_2 = os.path.join(ruta_dir_1,nom_dir_sec) 
    #    print(ruta_dir_2)
       if os.path.isdir(ruta_dir_2):
            for nom_arxiu in os.listdir(ruta_dir_2): 
                ruta_arxiu = os.path.join(ruta_dir_2,nom_arxiu)
                ruta_arxiu_dest = os.path.join(destination_directory,nom_arxiu)
                #print(ruta_arxiu)
                if os.path.exists(ruta_arxiu_dest):
                    os.remove(ruta_arxiu_dest)

                if os.path.isfile(ruta_arxiu) and not nom_arxiu.endswith((".json",".JSON")):
                    shutil.move(ruta_arxiu, destination_directory)
                    print(ruta_arxiu)
                    count+=1           
                elif os.path.isfile(ruta_arxiu) and nom_arxiu.endswith((".json",".JSON")):
                    os.remove(ruta_arxiu)

print("Move Completed", count)