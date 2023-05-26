import os
import shutil


def copy_files(origin, destin):
    count = 0
    for root, _, files in os.walk(origin):
        for nom_arxiu in files:
            ruta_arxiu = os.path.join(root,nom_arxiu)
            ruta_arxiu_dest = os.path.join(destin,nom_arxiu)
            #print(ruta_arxiu)
            if os.path.exists(ruta_arxiu_dest):
                os.remove(ruta_arxiu_dest)

            if os.path.isfile(ruta_arxiu) and not nom_arxiu.endswith((".json",".JSON")):
                shutil.move(ruta_arxiu, destin)
                print(ruta_arxiu)
                count+=1           
            elif os.path.isfile(ruta_arxiu) and nom_arxiu.endswith((".json",".JSON")):
                os.remove(ruta_arxiu)

    print("Copia finalitzada " + "Cantitat de arxius = ", count)

origin_directory = "/home/Benny/Downloads/Fotos test/"
# destination_directory = "/home/Benny/Downloads/Temp/"
destination_directory = "/home/Benny/Downloads/Fotos temp/"
copy_files(origin_directory,destination_directory)